### FUZZING

Podemos fuzzear valores mediante diccionarios:

#### Listas:
seclist/fuzzing/databases/nosql.txt

https://github.com/cr0hn/nosqlinjection_wordlists/blob/master/mongodb_nosqli.txt

#### ejemplo con wfuzz:

    wfuzz -z file,/usr/share/seclists/Fuzzing/Databases/NoSQL.txt -u http://127.0.0.1/index.php -d '{"trackingNum": FUZZ}'

