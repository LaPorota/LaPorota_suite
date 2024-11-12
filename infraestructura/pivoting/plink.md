### Dinamic remote port forwarding
Nos conectamos a nuestra maquina atacante mediante ssh y redireccionamos el tráfico a un puerto de una pc inaccesible a un puerto de nuestra máquinola atacante

    plink.exe -ssh -l kali -pw <YOUR PASSWORD HERE> -R 127.0.0.1:<puerto_a_abrir_en_attacker>:<ip_destino>:<puerto> <ip_attacker>
