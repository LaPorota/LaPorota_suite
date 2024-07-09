### INFO

- La serialización es el proceso de tomar un objeto de la memoria y convertirlo en bytes para ser almacenado o enviado a travez de la red.
- La deserialización toma el dato serializado y lo convierte en el objeto original en la memoria.
- La mayoría de los lenguajes de programación orientados a objetos soportan la serialización de manera nativa.

   
### Serialización en PHP

    $original_data = array("HTB", 123, 7.77);
    $serialized_data = serialize($original_data);

#### Objeto serializado:

    a:3:{i:0;s:3:"HTB";i:1;i:123;i:2;d:7.77;}
##### Descomposición del objeto serializado

      a:3:{ \\ (a)rray de (3) items
      
      i:0;s:3: "HTB"  \\ (i)ndex 0 del array; (s)tring de (3) caracteres con valor "HTB"
      
      i:1;i:123; \\ (i)ndex (1) del array; dato tipo (i)nteger conm valor de (123)
      
      i:2;d:7.77; \\ (i)ndex (2) del array; dato tipo (d)ouble con valor de (7.77)
      }

#### Objeto reconstruido:
$reconstructed_data = unserialize($serialized_data);

var_dump($reconstructed_data);

    array(3) {
      [0]=>
      string(3) "HTB"
      [1]=>
      int(123)
      [2]=>
      float(7.77)
    }
---

### Serialización en python

Las librerías más comunes de serialización de datos en python son: PyYAML, JSONpickle y Pickle.

      import pickle
      original_data = ["HTB", 123, 7.77]
      serialized_data = pickle.dumps(original_data)

#### Objeto serializado:

      b'\x80\x04\x95\x16\x00\x00\x00\x00\x00\x00\x00]\x94(\x8c\x03HTB\x94K{G@\x1f\x14z\xe1G\xae\x14e.'
### ATENCIÓN!!

**Pickle usa varios protocolos y el resultado es muy distinto según cual se use:**

Usando el mismo array pero con el protocolo 0 el objeto serializado da:

      b'(lp0\nVHTB\np1\naI123\naF7.77\na.'

Documentación sobre cómo trabajar los protocolos:

      https://docs.python.org/3/library/pickle.html#pickle.dump
