# Info

Es un web proxy. Nos permite pivotear de diferentes formas a servicios internos.

# Enumeración

El mejor recurso es spose
    
    https://github.com/aancw/spose

Luego lo corremos

    python spose.py --proxy http://10.10.11.131:3128 --target 10.10.11.131

Spose hará una revisión interna y verá qué servicios hay expuestos

# Uso/abuso

### Proxychains

Podemos utilizarlo luego como proxy http en proxychains agregando al file:

    http 10.10.10.10 3128

Si el servicio requiere de usuario y contraseña, se agregan luego del puerto en la misma línea y separados.

    http 10.10.10.10 3128 username passw0rd

### Navegador

Podemos también agregarlo como proxy al navegador para acceder desde el mismo a servicios web internos.


