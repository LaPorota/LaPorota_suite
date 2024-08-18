### Info

Los WebSockets son un protocolo de la capa de aplicación que permite la comunicación en dos vias: Cliente y Servidor.

Originalmente las aplicaciones(los browsers) se conectaban con el servidor usando HTTP mediante las request y responses. Una característica del protocolo HTTP/2 llamada **Server Push** permite a los servidores enviar
recursos de manera proactiva sin necesidad de que el cliente envíe una request.

Las conexiones a websockets se manteienen abiertas de manera más extensiva y transfieren data en cualquier dirección y en cualquier momento.

Son muy útiles en aplicaciones en tiempo real como un **chat**. De no ser por los web sockets, los usuarios deberían refrescar la página(GET request) todo el tiempo para ver si hay nuevos mensajes. Los websockets, en este caso, permiten que de manera instantanea los mensajes vayan y vengan sin request de por medio.


Los WebSockets pueden reconocerse por **ws://** y **wss://**:

ws:// = Mensajes por protocolo HTTP

wss:// = Mensajes por el protocolo HTTPS


### Conexión a un websocket mediante JS



    const socket = new WebSocket('ws://websockets.com/echo');

### WebSocket handshake
#### Request
    GET /echo HTTP/1.1
    Host: websockets.htb
    Connection: Upgrade
    Upgrade: websocket
    Sec-WebSocket-Version: 13
    Sec-WebSocket-Key: 7QpTshdCiQfiv3tH7myJ1g==
    Origin: http://websockets.htb

##### Headers

| header | Value | desc |
|---|---|---|
|Connection y Upgrade | Upgrade y Websocket | indican que el cliente quiere establecer una conexión mediante websockets |
|Sec-WebSocket-version | 13 | Muesta la versión del protocolo websocket elegida por el cliente |
|Sec-WebSocket-Key | \<key\> | Contiene un valor único que confirma que el cliente quiere establecer una conexión. No aporta ninuna seuridad. |
|Origin | \<origen\> | Contiene el origen de la request como en todo HTTP |


#### Response

    HTTP/1.1 101 Switching Protocols
    Connection: Upgrade
    Upgrade: websocket
    Sec-WebSocket-Accept: QU/gD/2y41z9ygrOaGWgaC+Pm2M=

##### Headers

| header | value | desc |
|---|---|---|
|Http 101 | X | El status 101 indica que se completó la conexión entre websockets |
|Sec-WebSocket-Accept | \<key\> | contiene un valor deliverado salido del valor enviado por el cliente en la sec-websocket-key y confirma que el server quiere establecer la conexión |


#### Websockets Handbook:

    https://pages.ably.com/hubfs/the-websocket-handbook.pdf
