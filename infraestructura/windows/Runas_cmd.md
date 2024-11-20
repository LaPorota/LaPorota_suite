SI tenemos acceso solo por consola y tenemos otro usuario podemos usar **Invoke-RunasCs.ps1" para correr un comando. 


Lo importamos en powershell y luego lo llamamos con el usuario.

    Invoke-RunasCs -Username svc_mssql -Password trustno1 -Command "whoami"
