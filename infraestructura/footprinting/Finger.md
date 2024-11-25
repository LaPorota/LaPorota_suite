### Tool

    https://github.com/pentestmonkey/finger-user-enum
    
### Enumeración de usuarios

perl finger-user-enum.pl -U users.txt -t 10.0.0.1 | grep --invert-match 'is not known'


### Datos de un usuario

perl finger-user-enum.pl -u <user> -t 10.0.0.1

