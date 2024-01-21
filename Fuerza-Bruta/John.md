
##### Single crack mode:
###### John va a buscar romper el hash con una lista que tiene por defecto
      john --format=<hash_type> <hash or hash_file>

###### Se le puede agregar una o más(separárndolas por comas) listas con el comando --wordlist
      john --format=<hash_type> <hash or hash_file> --wordlist=<word_list>

--rules:
Agrega algunas reglas, muchas vienen por default con llamar al comando. Estas reglas consisten en capitalizar letras, etc.

###### cracking files:
John trae muchas herramientas para crackear archivos específicos. Estas transforman la encriptación del archivo puntual en hashes con los que John puede trabajar
Ejemplo:

 <tool> <file_to_crack> > file.hash
  pdf2john server_doc.pdf > server_doc.hash

luego podemos crackear el hash resultante con john.
para encontrar estas herramientas: locate *2john*
