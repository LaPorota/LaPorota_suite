Los siguientes códigos son snipets en JS para insertar como scripts al momento de hacer un Hook a una función.

    frida -U -f com.mobilehackinglab.fridaone -l scrpt.js


### Ver el valor traido por un método

Supongamos que necesitamos interceptar un método que trae un valor, podríamos interceptarlo cuando está pasando y de esta manera obtener el mismo.

    Java.perform(function() {
        var Function = Java.use("<package.class>");
    
        Function.<method_to_hook>.implementation = function() {
            console.log("This method is hooked");
            var ret_val = this.<method_to_hook>();
            console.log("The return value is " + ret_val);
            return ret_val; // Ensure we return the original value
        }
    });

### Reemplazar un valor on the fly

Supongamos que necesitamos poner un Pin que no tenemos, podemos llamar a la validación del mismo en la APK para interceptar y generar nuestro propio Pin y que a la app le parezca válido

    Java.perform(function() {
      var Function = Java.use("<package>.<class>");
      Function.<method_to_hook>.implementation = function() {
        console.log("Intercepted the generateRandomNumber method.");
        console.log("Returning 5");
        return 5;
      };
    });

### Invocar a un método

Ir jugando con el timeout, si intenta ejectar el script para crrer la función antes de que la app sea cargada, dará error.

    Java.perform(function() {
        setTimeout(function() {
        var <class_reference> = Java.use("<package_name>.<class>");
        <class_reference>.<static_method>();
      }, 2000); // Retrasa la ejecución 2 segundos
    });

### Cambiar el valor de una variable estática

Supongams que tenemos una variable que es estática y necesitamos cambiarle el valor para forzar una ejecución o obtener un resultado sobre el cual pondera, podemos cambiarlo con el siguiente snippet

    Java.perform(function (){
         setTimeout(function() {
        var <class_reference> = Java.use("<package_name>.<class>");
        <class_reference>.<variable>.value = <value>;
        }, 2000); // Retrasa la ejecución 2 segundos
    });
