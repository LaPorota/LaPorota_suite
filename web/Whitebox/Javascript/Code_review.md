## Casos de ofuscación

### Packer

- Es una técnica muy comun de ofuscación en JS.
- Podemos reconocerla por encontrarnos una función eval que llama luego a otra función con 6 parámetros.

    eval(function (p, a, c, k, e, d) {

Una función tipo PACKER guarda todos los strings que hacen a una variable o función en un diccionario y separa cada palabra con **|** 
