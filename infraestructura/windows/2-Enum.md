walkthroughts:
https://tryhackme.com/room/windows10privesc


#### TOOLS:

- Seatbelt: 	C# project for performing a wide variety of local privilege escalation checks
- winPEAS: 	WinPEAS is a script that searches for possible paths to escalate privileges on Windows hosts. All of the checks are explained here
- PowerUp: 	PowerShell script for finding common Windows privilege escalation vectors that rely on misconfigurations. It can also be used to exploit some of the issues found
- SharpUp: 	C# version of PowerUp
- JAWS: 	PowerShell script for enumerating privilege escalation vectors written in PowerShell 2.0
- SessionGopher: 	SessionGopher is a PowerShell tool that finds and decrypts saved session information for remote access tools. It extracts PuTTY, WinSCP, SuperPuTTY, FileZilla, and RDP saved session information
- Watson: 	Watson is a .NET tool designed to enumerate missing KBs and suggest exploits for Privilege Escalation vulnerabilities.
- LaZagne: 	Tool used for retrieving passwords stored on a local machine from web browsers, chat tools, databases, Git, email, memory dumps, PHP, sysadmin tools, wireless network configurations, internal Windows password storage mechanisms, and more
- Windows Exploit Suggester - Next Generation: 	WES-NG is a tool based on the output of Windows' systeminfo utility which provides the list of vulnerabilities the OS is vulnerable to, including any exploits for these vulnerabilities. Every Windows OS between Windows XP and Windows 10, including their Windows Server counterparts, is supported
- Sysinternals Suite: 	We will use several tools from Sysinternals in our enumeration including AccessChk, PipeList, and PsService.

Carpeta TMP:
C:\Windows\Temp


## Sobre los usuarios

#### privilegios de nuestro user:
    whoami /priv

#### conocer los grupos a los que pertenece el user:
    whoami /groups

#### Listar grupos en el sistema:
    net localgroup
##### Desde powershell
    Get-LocalGroup

#### ver miembros de un grupo:
    net localgroup <GRUPO>
##### Desde Powershell
    Get-LocalGroupMember <grupo>

#### LISTAR USUARIOS  
    net user
##### desde powershell

    Get-LocalUser
#### ver los usuarios logueados y datos de sus sessiones:
    query user


## Sobre el sistema

#### Conocer las apps/binarios bloqueados en el sistema:
    GetAppLockerPolicy == https://docs.microsoft.com/en-us/powershell/module/applocker/get-applockerpolicy?view=windowsserver2019-ps

#### ver información del sistema: 
    systeminfo

En este apartado podremos ver cosas interesantes como la versión del sistema, si es una maquina física o una VM y la última vez que fue encendida (system boot time). Esto
último nos da una idea de si ha recibido parches recientemente (una computadora que fue prendida hace 6 meses muy posiblemente no haya recibido parches de actualizaciones en
ese tiempo)

#### Listar procesos:
    tasklist /svc
##### desde powershell
    Get-Process
#### Ver variables de entorno:
    set

#### Ver los hot-fixes del sistema

##### cmd
    wmic qfe
##### powershell 
    Get-HotFix | ft -AustoSize

##### Ver los programas instalados:
###### cmd
    wmic product get name
###### powershell
    $INSTALLED = Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Uninstall\* |  Select-Object DisplayName, DisplayVersion, InstallLocation
    $INSTALLED += Get-ItemProperty HKLM:\Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\* | Select-Object DisplayName, DisplayVersion, InstallLocation
    $INSTALLED | ?{ $_.DisplayName -ne $null } | sort-object -Property DisplayName -Unique | Format-Table -AutoSize

### Ver las conexiones TCP y UDP en la pc:
    
    netstat -ano


las conexiones al local host (127.0.0.1 o ::1) son de procesos que corren solamente dentro del sistema, son propensas entonces a ser menos seguras por no estar en expuestas. 



#### ver la política de passwords y otras informaciones de cuenta:
    net accounts



  
