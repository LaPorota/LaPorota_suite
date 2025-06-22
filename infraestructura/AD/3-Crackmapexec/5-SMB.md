# Enumeración 

## Enumerar si un user tiene accesos a carpetas compartidas

    crackmapexec smb 10.129.203.121 -u grace -p Inlanefreight01! --shares


## Listar todos los archivos dentro de una carpeta

    crackmapexec smb 10.129.204.177 -u grace -p Inlanefreight01! --spider <carpeta> --regex .

## Listar archivos con una extensión dentro de una carpeta


    crackmapexec smb 10.129.203.121 -u grace -p Inlanefreight01! --spider <carpeta> --pattern <extensión>

## Listar los archivos de una carpeta que tengan una palabra en su contenido

    crackmapexec smb 10.129.204.177 -u grace -p Inlanefreight01! --spider <carpeta> --content --regex <palabra>


# Gestión de archivos

## Descargar un archivo

    crackmapexec smb 10.129.203.121 -u grace -p Inlanefreight01! --share <carpeta> --get-file <file_smb> <file_final>

## Subir un archivo

    crackmapexec smb 10.129.203.121 -u grace -p Inlanefreight01! --share <share> --put-file <path_to_file> <file_final>

