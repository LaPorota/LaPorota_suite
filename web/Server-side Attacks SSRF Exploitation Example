### Info

Podemos encontrar una ssrf cuando una funcionalidad realiza una llamada a una ip o url ajena al sitio.

podríamos cambiar entonces una llamada a una api por una llamada al localhost con el fin de acceder a aplicaciones no expuestas
debido a su "trust relationship".

Tambien podemos obtener accesos a secciones del sitio que no nos son permitidas, como el admin.

### control bypass:

Algunas apps tienen restricciones o validaciones para que un atacante no pueda acceder a servicios externos o a directorios sensibles
como "/admin".Para evadirlos podemos:

1. Usar representaciones alternativas de la ip 127.0.0.1, como 2130706433, 017700000001, o 127.1
2. Crear nuestro propio dominio que apunte a 127.0.0.1 (se puede hacer con spoofed.burpcollaborator.net)
3. Usar URL encode

Deberemos probar una conjunción de las mismas para pasar todos los métodos de validación.



