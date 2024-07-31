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

Lo más importante de la función packer es el "return". Ahí es donde la función va a devolver el código original luego de restorearlo. Lo único que debemos hacer es encontrar esta parte, reemplasar el return por un console.log para imprimir la función original en la consola.
            
    console.log(p);

Para hacer todo esto de manera más cómoda podemos usar Prettier para presentar mejór el texto y jsconsole para correrlo.

###### Prettier
    https://prettier.io/playground/

###### JSConsole

    https://jsconsole.com/

#### Recursive packing

Vamos a encontrar que muchas veces se hacen varios empaquetados sobre un código. Primero se empaquetan funciones específicas y luego se empaqueta todo el código. Tendremos que realizar los pasos anteriores sobre el codigo general y luego sobre las funciones propias hasta obtener un código limpio.

---

### Dead code

Son variables o funciones que están guardadas dentro de un JS que no son usadas o referenciadas en ningun lado. Es código no necesario que se utiliza para engordar el script y volver más complicada la lectura por un humano o un antivirus ya que se hace más dificil discernir cuál códogo está en uso y cuál no.
También, podemos encontrar variables y funciones de Dead Code que son llamadas por funciones que tampoco son usadas. Esto se vuelve más complicado cuando nos encontramos que tenemos varios archivos JS y que una función que parece no utilizada es referenciada desde otro script.

Para buscar estas líneas de código y quitarlas del script de manera sencilla podemos usar vscode, cargar el código y luego en cada variable o funcion:

click derecho > find all references.
