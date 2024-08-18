### Intro

- Al igual que cualquier otra interconexión, burpSuite puede inspeccionar y manipular los datos enviados mediante websockets.
- Podemos encontrar estos envíos en la solapa WebSockets History dentro del plugin **Proxy**
- Podemos también enviar esto a repeater para hacer pruebas.

### Dentro de repeater

Podemos aquí hacer envíos hacia el server y el cliente impersonando a ambos mediante el selector que se encuentra al lado del boton de send.

##### Cortar conexión

Podemos cortar la conexión con el websocket server mediante el botón "deslizable" al lado del lápiz.

##### Manipular el Handshake

Podemos manipular el handshake(la request de conexión) clonando la conexión websocket. Para esto vamos al lápiz:

1. Seleccionamos la conexión que queremos clonar
2. Tocamos el boton de Clone.
3. Modificamos la request del handshake
4. Tocamos el botón connect.

De esta manera tendremos una nueva conexión con el servidor de websockets, ahora podremos enviar y recibir mensajes mediante el repeater.

### Nueva conexión

Podemos crear una nueva conexión a otro server WS usando la opción del lápiz y seleccionando **New WebSocket** y creando una nueva request.
