
### Sed
#### Sufijo
    sed 's/$/sufijo/' diccionario.txt > diccionario_modificado.txt

#### Prefijo
    sed 's/^/prefijo/' diccionario.txt > diccionario_modificado.txt


### Crear listas personalizadas de password:

#### 1)usar cupp para generar el diccionario
#### 2)Limpiar el diccionario en base a las politicas de contraseñas del sitio:

    sed -ri '/^.{,7}$/d' diccionario           # remove shorter than 8
    sed -ri '/[!-/:-@\[-`\{-~]+/!d' diccionario # remove no special chars
    sed -ri '/[0-9]+/!d' diccionario           # remove no numbers
    sed -i '/[A-Z]/!d' diccionario             # remueve las palabras sin mayusculas
    sed -i 's/\b[a-z][a-zA-Z0-9]*\b//g' diccionario #remueve todas las palabras que no inicien con mayuscula

    


### Crear listas personalizadas de users:

    git clone https://github.com/urbanadventurer/username-anarchy.git
    ./username-anarchy nombre_apellido > diccionario donde almacernar los resultados

podemos modificar listas con hashcat aplicandole reglas para que estas sean modificadas en base a las mismas:

    hashcat --force password.list -r custom.rule --stdout | sort -u > mut_password.list

Hashcat trae una serie de reglas por defecto dentro de la carpeta:
    /usr/share/hashcat/rules/