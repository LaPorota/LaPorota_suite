## Casos de ofuscación

### Packer

- Es una técnica muy comun de ofuscación en JS.
- Podemos reconocerla por encontrarnos una función eval que llama luego a otra función con 6 parámetros.

    eval(function (p, a, c, k, e, d) {

Una función tipo PACKER guarda todos los strings que hacen a una variable o función en un diccionario y separa cada palabra con **|**. Luego la función splitea esta variable con ".split('|')" con el fin de obtener todos los strings originales separados y utiliza una función predefinida para restaurar todo a su versión original (de esto se encarga eval)

##### Unpacking

Las funciones packer usualmente inician con unas pocas funciones que decodean el código y termina con un String largo que lleva el contenido del código ofuscado.


                function (p, a, c, k, e, d) {
            e = function (c) {
                ...SNIP...
            };
        
            if (!"".replace(/^/, String)) {
                  ...SNIP...
            }
        
            while (c--) {
                ...SNIP...
            }
        
            return p;
        })(
            'dh dl=di' ...SNIP... ''
        )
