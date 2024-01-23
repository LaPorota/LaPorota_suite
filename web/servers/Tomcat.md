#### Info
- Soporta aplicaciones en JAVA.
- Soporta JSP
- Utilizado por frameworks como Spring

#### Discovery
##### Versiones:
Si el server trabaja detrás de un reverse proxy podemos impulsar un error 404. Si la página está por defecto entonces nos dirá la versión

    http://app-dev.inlanefreight.local:8080/invalid

Otra forma es revisando el /docs:

        curl -s http://app-dev.inlanefreight.local:8080/docs/ | grep Tomcat 


