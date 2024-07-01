### Pagina donde manipular JWTs

https://jwt.io

### Missing signature verification

En algunos casos las aplicaciones no validan la signature, con lo cual podremos modificar el token sin problema.


### None Algorithm Attack

Cuando usamos como algoritmo "none" la firma no es computada debido a la falta de algoritmo. Podríamos crear un nuevo token con CyberChef

##### 1) vamos a cyberchef

  https://gchq.github.io/CyberChef/
##### 2) Elegimos JWT sign y en signing algorithm elegimos none (borramos el secretkey)
##### 3) Copiamos el payload en texto plano en el input, manipulamos y en el output nos generará un token.
