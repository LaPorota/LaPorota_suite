# Enumerar AD sin credenciales:

## Kerbrute
##### Instalación
     git clone https://github.com/ropnop/kerbrute.git
     cd kerbrute
     make all
     cd dist
     sudo mv kerbrute_linux_amd64 /usr/local/bin/kerbrute 

##### USO
     kerbrute userenum -d INLANEFREIGHT.LOCAL --dc <ip_domain_controller> <diccionario_de_users> -o valid_ad_users


## ENUM4LINUX:
     enum4linux -U 172.16.5.5  

##### Enumerar usuarios

     | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"
     
## RPCCLIENT :
     rpcclient -U "" -N 172.16.5.5

##### Enumerar usuarios
     --- enumdomusers
     
##### Obtener info del dominio

     --querydominfo
##### Obtener info de las politicas de pass

     --getdompwinfo
##### Obtener info de los usuarios

     | grep "user:" | cut -f2 -d"[" | cut -f1 -d"]"


## CRACKMAPEXEC:
     crackmapexec smb 172.16.5.5 --users


## LDAPSEARCH:

##### Listar Usuarios
     ldapsearch -H ldap://172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"  | grep sAMAccountName: | cut -f2 -d" "
     
##### Listar usuarios con información 

     ldapsearch -H ldap://172.16.5.5 -x -b "DC=INLANEFREIGHT,DC=LOCAL" -s sub "(&(objectclass=user))"
## LdapSearch-ad

#### Información del Ad
     python3 ldapsearch-ad.py -l 10.129.1.207 -t info


## WINDAPSEARCH:

##### Listar Usuarios
     ./windapsearch.py --dc-ip 172.16.5.5 -u "" -U
##### Listar Computadoras

    python3 windapsearch.py --dc-ip 10.129.1.207 -u "" -C

---

# ENUMERAR AD CON CREDENCIALES:
## Crackmapexec

##### Enumerar users
sudo crackmapexec smb 172.16.5.5 -u htb-student -p Academy_student_AD! --users

## ldapsearch-ad

##### Enumerar políticas de contraseña

     python3 ldapsearch-ad.py -l 10.129.1.207 -d inlanefreight -u james.cross -p Summer2020 -t pass-pols

##### Enumerar usuarios kerberosteables

     python3 ldapsearch-ad.py -l 10.129.1.207 -d inlanefreight -u james.cross -p Summer2020 -t kerberoast | grep servicePrincipalName:
##### Enumerar usuarios ASREPRoadteables

     python3 ldapsearch-ad.py -l 10.129.1.207 -d inlanefreight -u james.cross -p Summer2020 -t asreproast
