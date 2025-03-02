# Info

Airgraph nos permite generar mapas de redes en formato imagen a partir de una captura en formato CSV de airodump.


Los access points son coloreados según el tipo de encripción:

- verde: WPA
- Amarillo: WEP
- Rojo: Red abierta
- Negro: Encriptación no conocida.


      sudo airgraph-ng -i <csv> -g CAPR -o <imagen>.png
