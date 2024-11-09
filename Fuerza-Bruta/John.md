
##### Single crack mode:
###### John va a buscar romper el hash con una lista que tiene por defecto
      john --format=<hash_type> <hash or hash_file>

###### Se le puede agregar una o más(separárndolas por comas) listas con el comando --wordlist
      john --format=<hash_type> <hash or hash_file> --wordlist=<word_list>

### Reglas

Agrega algunas reglas, muchas vienen por default con llamar al comando. Estas reglas consisten en capitalizar letras, etc.

      --rules

Podemos crear reglas como si fueran para hashcat agregando un titulo a la regla:

      [List.Rules:<nombre>]
      c $1 $3 $7 $!
      c $1 $3 $7 $@
      c $1 $3 $7 $#

Luego deberemos copiar esta regla al config de john para que funcione:

      sudo sh -c 'cat /home/kali/passwordattacks/rule >> /etc/john/john.conf'

Para correr la regla la llamamos por su nombre

      john --wordlist=<dictio> --rules=<name> <file_a_crackear>

##### Cracking files:
John trae muchas herramientas para crackear archivos específicos. Estas transforman la encriptación del archivo puntual en hashes con los que John puede trabajar
Ejemplo:

       **<tool> <file_to_crack> > file.hash**

 
      pdf2john server_doc.pdf > server_doc.hash

luego podemos crackear el hash resultante con john.


para encontrar estas herramientas: 

      locate *2john*

### Crack keepass

      keepass2john Database.kdbx > keepass.hash

##### Hashcat mode 13400 (si nos da un error de salt, eliminar lo anterior al $keepass)

### Crack RSA

      ssh2john id_rsa > ssh.hash

##### Hashcat mode 22921 

Puede ser que en algunos casos donde los algoritmos sean modernos hashcat no pueda trabajar con el hash. 
