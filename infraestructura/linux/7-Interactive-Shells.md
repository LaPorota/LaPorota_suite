### Perl

    perl -e 'exec "/bin/bash";'

### Ruby

    ruby -e 'exec "/bin/bash"'

### PHP

    php -r 'system("/bin/bash");'

### Bash 

    /bin/bash -i

Si no nos despliega una bash interactiva, debemos verificar que la misma esté asociada a un tty. En este caso podemos forzarla con el siguiente comando:

    script -qc /bin/bash /dev/null

### Python

    python -c 'import pty; pty.spawn("/bin/bash")'
