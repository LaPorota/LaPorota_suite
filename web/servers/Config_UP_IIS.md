### INFO

- IIS viene por default en windows pero usualmente no viene activado.


### Activar IIS

ir a "activar o desactivar las características de windows".

Una vez allí activar las siguientes features dentro de  Internet information services:

1) web manaegment tools > IIS Management Console
2) word wide web services > Application Development Features > ASP.NET 4.8
3) Word wide web services > Common HTTP Features > Static content

Una vez hecho esto, windows va a descargar e instalar automáticamente todas las dependencias necesarias.

La carpeta webRoot va a estar en C:\inetpub\wwwroot

Una vez copiados todos los archivos del servicio web en la webRoot:

En inicio buscamos :

1) Internet Information Services (IIS) Manager
2) Dentro damos click derecho y seleccionamos "ver sitios"
3) Luego agregar sitio
4) Agregamos nombre del sitio, en aplication pool .net v4.5, configuramos el path a la carpeta del servicio y le proporcionamos un puerto.


Si debemos hacer debug recordar dar permisos de escritura a la carpeta del servicio web para IIS 
