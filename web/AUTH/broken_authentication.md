SIEMPRE BUSCAR EL ROBOTS.txt EN BUSQUEDA DE SUBDIRECTORIOS IMPORTANTES!!!

LEER BIEN EL Código tanto html como js para buscar links a subdirectorios no adivinables!

### User enum:
hacer fuerza bruta al login de las siguientes formas:

1)Probar con el login por carteles como "invalid user"

2)Probar si al poner el user y una contraseña erronea el user sigue apareciendo en el form.

3)Comprobar el tiempo de respuesta al momento de intentar los logueos:

Ejemplo de tiempo de respuesta con burp spoofeando la ip para baypassear restricciones:

https://portswigger.net/web-security/authentication/password-based/lab-username-enumeration-via-response-timing

4)Hacer fuerza bruta en el formulario de registro buscando en las respuestas los users que ya están registrados.

Fuerza Bruta sobre ip blockeada:

https://portswigger.net/web-security/authentication/password-based/lab-broken-bruteforce-protection-ip-block

### Bypass MF2

En muchas páginas al momento de introducir bien las credenciales uno ya se encuentra "logueado realmente", al pedirnos el segundo
factor de autenticación podríamos probar saltearlo redirigiendonos a una página posterior al login como el perfil.

### Buscar entrar a un sitio por confianza en la ip:

Agregando la cabecera "X-Forwarded-For" y una ip de confianza como "127.0.0.1"


### Token de reseteo predecible:

wfuzz -z range,00000-99999 --ss "Valid" "https://brokenauthentication.hackthebox.eu/token.php?user=admin&token=FUZZ"

Crear una cuenta, generar un token de restauración de password, intentar un refresh de pass de la cuenta de la victima y utilizar el token generado para nuestra cuenta.


#### Lista para probar políticas de contraseñas:
qwerty						

Qwerty	

Qwerty1		

Qwertyu1		

Qwert1!		

Qwerty1!			

QWERTY1				

QWERT1!				

QWERTY1!				

Qwerty!		

Qwertyuiop12345!@#$%


### Modficar la contraseña de un tercer usuario:

Ir al formulario de reseteo de password y agregar en los campos enviados (con un proxy) campos como "username" o "userid" con el nombre del usuario a cambiar

### Comprobar tokens con decodify:
https://github.com/s0md3v/Decodify

### BF una cookie de sesión con John
john --incremental=LowerNum --min-length=6 --max-length=6 --stdout| wfuzz -z stdin -b HTBSESS=FUZZ --ss "Welcome" -u https://brokenauthentication.hackthebox.eu/profile.php 

--incremental= tipo de caracteres que podemos observar en la cookie

-- min and max-lenght= el minimo y máximo de caracteres en la cookie.

con esto alimentamos a wfuzz para hacer fuzzing en la coockie.









