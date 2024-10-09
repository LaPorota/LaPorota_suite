# Enumerar AD sin credenciales:

### Kerbrute
##### Instalación
     git clone https://github.com/ropnop/kerbrute.git
     cd kerbrute
     make all
     cd dist
     sudo mv kerbrute_linux_amd64 /usr/local/bin/kerbrute 

##### USO
     kerbrute userenum -d INLANEFREIGHT.LOCAL --dc <ip_domain_controller> <diccionario_de_users> -o valid_ad_users


### ENUM4LINUX:
     enum4linux -U 172.16.5.5  | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"

### RPCCLIENT :
     rpcclient -U "" -N 172.16.5.5
     --- enumdomusers

### CRACKMAPEXEC:
     crackmapexec smb 172.16.5.5 --users

### LDAPSEARCH:
     ldapsearch -H ldap://172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "

### WINDAPSEARCH:

##### Listar Usuarios
     ./windapsearch.py --dc-ip 172.16.5.5 -u "" -U
##### Listar Computadoras

    python3 windapsearch.py --dc-ip 10.129.1.207 -u "" -C
