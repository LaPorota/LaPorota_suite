
### Sed
#### Sufijo
    sed 's/$/sufijo/' diccionario.txt > diccionario_modificado.txt

#### Prefijo
    sed 's/^/prefijo/' diccionario.txt > diccionario_modificado.txt

#### Duplicar las palabras de la lista y volver a la segunda upper

    sed 's/\(.*\)/\1\n\U\1/' input.txt > dictio.txt



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

### Crear listas mediante script bash
Agregar bucle for por cada nuevo "index" de caracteres a agregar"

    #!/bin/bash

    palabra="palabra"
    caracteres_a_agregar=("q" "w" "e" "r" "t" "y" "u" "i" "o" "p" "a" "s" "d" "f" "g" "h" "j" "k" "l" "z" "x" "c" "v" "b" "n" "m" "1" "2" "3" "4" "5" "6" "7" "8" "9" "0" "!" "?" "-" "_" "@" "Q" "W" "E" "R" "T" "Y" "U" "I" "O" "P" "A" "S" ">

    # Crear o sobrescribir el archivo lista.txt
    > lista.txt

    # Bucle para agregar caracteres a la palabra y escribir en el archivo
    for char in "${caracteres_a_agregar[@]}"; do
        for char2 in "${caracteres_a_agregar[@]}"; do
                echo "${palabra}${char}${char2}" >> lista.txt
    done
    done

