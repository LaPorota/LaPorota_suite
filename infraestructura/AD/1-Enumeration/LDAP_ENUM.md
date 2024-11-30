# Intro
Para relacionarnos mediante ldap podemos usar ldeep

# instalación

### 1) Creamos un entorno virtual

    python -m venv ldeep

### 2) entramos al entorno virtual

    source ldeep/bin/activate

### 3) Instalamos ldeep

    python -m pip install ldeep

# Enumeración

### ver opciones de enumeración

    ldeep ldap -h
En la práctica:

    ldeep ldap -u <user> -p '<pass>' -d <domain> -s ldap://<domain> <opcion>

### Enumerar todo el AD
Enumerar todo el AD con el comando all. Esto nos va a generar muchos archivos, si podemos es mejor enumerar con bloodhound y luego extraer los datos necesarios para el abuso
    
    ldeep ldap -u <user> -p '<pass>' -d <domain> -s ldap://<domain> all output

# ABUSO

### agregarnos a un grupo


    ldeep ldap -u <user> -p '<pass>' -d <domain> -s ldap://<domain> add_to_group "<distinguishedName_del_user>" "<distinguishedName_del_grupo"


Ejemplo aplicado

    ldeep ldap -u fulano -p 'mengano' -d dominio.local -s ldap://dominio.local add_to_group "CN=Fulano Flores,OU=STAFF,DC=dominio,DC=local" "CN=remote access,OU=remote,DC=dominio,DC=local"
