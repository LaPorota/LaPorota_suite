#### Buscar archivos de configuración:
      for l in $(echo ".conf .config .cnf");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "lib\|fonts\|share\|core" ;done

#### Buscar passwords en un archivo con una extención puntual:
      for i in $(find / -name *.cnf 2>/dev/null | grep -v "doc\|lib");do echo -e "\nFile: " $i; grep "user\|password\|pass" $i 2>/dev/null | grep -v "\#";done

#### Buscar dbs:
      for l in $(echo ".sql .db .*db .db*");do echo -e "\nDB File extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share\|man";done

#### Buscar contraseñas en archivos de configuración de WP

      cat wp-config.php | grep 'DB_USER\|DB_PASSWORD'

#### Buscar notas:
      find /home/* -type f -name "*.txt" -o ! -name "*.*"

#### Buscar scripts:
      for l in $(echo ".py .pyc .pl .go .jar .c .sh");do echo -e "\nFile extension: " $l; find / -name *$l 2>/dev/null | grep -v "doc\|lib\|headers\|share";done

#### Buscar ssh private keys:
      grep -rnw "PRIVATE KEY" /home/* 2>/dev/null | grep ":1"

#### Buscar ssh-rsa:
      grep -rnw "ssh-rsa" /home/* 2>/dev/null | grep ":1"

#### Listar las carpetas .ssh
Al listar la carpeta si hay un file KNOWN_HOSTS, este contiene public keys para todos los hosts a los que el usuario se conectó.
            ls ~/.ssh

#### Ver el bash history:
      tail -n5 /home/*/.bash*

#### Buscar contenidos interesantes en logs:
      for i in $(ls /var/log/* 2>/dev/null);do GREP=$(grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null); if [[ $GREP ]];then echo -e "\n#### Log file: " $i; grep "accepted\|session opened\|session closed\|failure\|failed\|ssh\|password changed\|new user\|delete user\|sudo\|COMMAND\=\|logs" $i 2>/dev/null;fi;done

#### Buscar credenciales en mozilla:

      ls -l .mozilla/firefox/ | grep default 
      
Luego:

      cat .mozilla/firefox/<log>/logins.json | jq .

##### Podemos desencriptar contraseñas y usuarios guardados en firefox con:
      git clone https://github.com/unode/firefox_decrypt.git

      python3.9 firefox_decrypt.py

#### Obtener credenciales de AWS

Cuando realizamos una autenticación en AWS utilizando el cli o el sdk se genera un conjunto de credenciales que incluyen un Access Key Id y un Secret Access Key. Suele guardarse en:

##### Root:
    /root/.aws/credentials

##### User:

      /home/NombreDeUsuario/.aws/credentials

