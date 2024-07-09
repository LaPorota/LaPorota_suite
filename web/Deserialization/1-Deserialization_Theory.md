### INFO

- La serialización es el proceso de tomar un objeto de la memoria y convertirlo en bytes para ser almacenado o enviado a travez de la red.
- La deserialización toma el dato serializado y lo convierte en el objeto original en la memoria.
- La mayoría de los lenguajes de programación orientados a objetos soportan la serialización de manera nativa.

   
### Serialización en PHP

    $original_data = array("HTB", 123, 7.77);
    $serialized_data = serialize($original_data);

#### Objeto serializado:

    a:3:{i:0;s:3:"HTB";i:1;i:123;i:2;d:7.77;}

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
