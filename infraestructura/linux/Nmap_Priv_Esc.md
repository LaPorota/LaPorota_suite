#### Escalar privilegios con nmap (en la pc victima)
si soporta el modo interactivo:
    nmap --interactive
    !sh

/usr/share/nmap/scripts
escaneo avanzado con evasión:

(para el lab: correr snort: powershell : .\snort.exe -i 5 -A console -c C:\Snort\etc\snort.conf )

Reconocimiento de hosts:
metodo para usar el ARP constatando si efectivamente hay un nodo del otro lado
sudo nmap -sn -n -PS rango de ip

sudo nmap -Pn -S ip_a_spoofear -e interfaz ip_victima