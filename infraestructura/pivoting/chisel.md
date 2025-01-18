# Info

Chisel usa un criterio cliente servidor. El **server** es la máquina que recibirá el forwardeo de puertos, el **client** es quien hará el forwardeo.
Esto quiere decir que si quisieramos forwardear un puerto desde una máquina que estamos atacando, el cliente irá en ella y el server en la máquina atacante o pivot.


# Server
Debemos configurarlo como server, que espere una conexión reversa y el puerto por el cual va a recibir los datos

    chisel server --reverse -p 1234

# Client
comando explicado

    chisel client <ip_server>:<puerto> R:<puerto_que_se_abrirá_en_la_máquina_atacante>:<ip(localhost o ip de otra máquina a la que llegar>:<puerto_a_alcanzar>

Ejemplo:

    chisel client 192.168.0.3:1234 R:3000:127.0.0.1:8080
