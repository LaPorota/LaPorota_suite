## Linux
Para extraer datos de una app que se conecta a un servicio podemos usar en linux "gdb".

    gdb ./app_a_reversear

#### 1)Luego insertamos:

    set disassembly-flavor intel

#### 2) disas main

    disas main
    
#### 3)buscamos dentro de los registros que encontró el llamado a alguna app que nos sirva.

#### 4)Insertamos un breakpoint para que nos dumpee el contenido de la memoria en esa instancia.

    b *<espacio_de_memoria>

#### 5) corremos el proceso
    run

### Si la dirección de memoria es muy corta, nos va a dar un error. tendremos que volver a repetir el paso 1 y 2 anotar la dirección correspondiente, cerrar el debuger y repetir todo el proceso pero con la dirección de memoria correspondiente


## En windows podemos usar DnSpy
https://github.com/dnSpy/dnSpy
