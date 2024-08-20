### Info

Podemos encontrar una ssrf cuando una funcionalidad realiza una llamada a una ip o url ajena al sitio.

podríamos cambiar entonces una llamada a una api por una llamada al localhost con el fin de acceder a aplicaciones no expuestas
debido a su "trust relationship".

Tambien podemos obtener accesos a secciones del sitio que no nos son permitidas, como el admin.

### control bypass:

Algunas apps tienen restricciones o validaciones para que un atacante no pueda acceder a servicios externos o a directorios sensibles
como "/admin".Para evadirlos podemos:

1. Usar representaciones alternativas de la ip 127.0.0.1:

- 127.0.0.0 - 127.255.255.255
- 127.1
- 127.000000000000000.1
- 0.0.0.0
- 0
- 2130706433
- 0177.0000.0000.0001
- 0x7f000001
- 0\:0\:0\:0\:0\:0\:0:1 - ::1
- :\:ffff:127.0.0.1
  
2. Crear nuestro propio dominio que apunte a la dirección interna **127.0.0.1**

Existen sitios que permiten hacer esto. Entre ellos:
- spoofed.burpcollaborator.net
- localtest.me


Otra Opción es crear un servidor en php


    <?php header('Location: http://127.0.0.1/<sección a llamar>'); ?>

3. Usar URL encode

Deberemos probar una conjunción de las mismas para pasar todos los métodos de validación.



