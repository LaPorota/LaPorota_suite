# BF

Hay 3 formas de probar autenticarse contra MSSQL:

1) Con usuario de dominio (por defecto)
2) Con usuario local
3) COn usuario de MSSQL

### Con usuario de dominio 
Hacemos la llamada con CME como viene

### Con usuario local

agregamos como domionio el "."

    crackmapexec mssql 10.129.203.121 -u julio grace -p Inlanefreight01! -d .

### Con usuario de MSSQL
Agregamos la flag: --local-auth

    crackmapexec mssql 10.129.203.121 -u julio grace  -p Inlanefreight01! --local-auth

## ¡¡Si el usuario dice pwnd! quiere decir que es DBA!!

# Footprinting

### Obtener DBs
    crackmapexec mssql 10.129.203.121 -u grace -p Inlanefreight01! -q "SELECT name FROM master.dbo.sysdatabases"

### Obtener nombres de las tablas

    crackmapexec mssql 10.129.203.121 -u nicole -p Inlanefreight02! --local-auth -q "SELECT table_name from <db>.INFORMATION_SCHEMA.TABLES"

### Dumpear una tabla

    crackmapexec mssql 10.129.203.121 -u nicole -p Inlanefreight02! --local-auth -q "SELECT * from [db].[dbo].<tabla>" 

### Ejecutar comandos de windows


