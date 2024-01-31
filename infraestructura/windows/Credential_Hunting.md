Como primer herramienta podemos buscar (si estamos por rdp) podemos usar el buscador de windows con las siguientes palabras, talvez aparezcan ficheros con contraseñas guardadas:

- Passwords	
- Passphrases	
- Keys
- Username	
- User account	
- Creds
- Users	
- Passkeys	
- Passphrases
- configuration	
- dbcredential	
- dbpassword
- pwd	
- Login	
- Credentials

Lo siguiente que podemos hacer es unsar lazagne 

https://github.com/AlessandroZ/LaZagne/releases/

Una vez que lo metimos en la pc victima lo corremos con:

    start lazagne.exe all

también podemos usar el findr por cmd:

    findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml *.git *.ps1 *.yml

También traer contraseñas de chrome:

    gc 'C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Custom Dictionary.txt' | Select-String password

Powershell History

    gc (Get-PSReadLineOption).HistorySavePath

Podemos también en un oneliner recorrer todos los archivos historicos de powershell a los que tenemos acceso

    foreach($user in ((ls C:\users).fullname)){cat "$user\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt" -ErrorAction SilentlyContinue}

El archivo unnatend.xml puede tener contraseñas también


