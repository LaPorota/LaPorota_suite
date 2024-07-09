### INFO

- Php tiene un total de 17 magic methods
- Son métodos que reescriben el comportamiento de los objetos cuando son llamados
- Inician con "__"

| Método   | Desc. |
|----------|------|
| __construct    | Método constructor de una clase  |
| __toString    | Define cómo un objeto reacciona al ser trabajado como un string   |
| __call  | Usado cuando se trata de llamar un metodo inaccesible dentro del contexto de un objeto   |
| __get     | CUando tratamos de leer propiedades inaccesibles   |
| __set    | Llamado cuando tratamos de escribir propiedades inaccesibles   |
| __clone    | Cuando tratamos de clonar un objeto   |
| __destruct     | Cuando necesitamos destruir un objeto   |
| __isset    | Cuando tratamos de llamar un isset() o un isempty() en propiedades inaccessibles   |
| __invoke    | Cuando tratamos de invocar un objeto como función   |
| __sleep     | **Llamada cuando se necesita serializar un objeto**. Si __serialize y __sleep están definidas la segunda es ignorada   |
| __wakeup    | **Llamada cuando se deserializa un objeto**. Si __unserialize y __wakeup están definidas, la segunra es ignorada   |
| __unset    | Llamada cuando se tratamos de hacer un unset sobre una propiedad inaccesible   |
| __callStatic    | Llamada cuando necesitamos acceder a un metodo inaccesible en un contexto estático  |
| __set_state    | Llamado cuando var_export es llamado sobre un objeto   |
| __debuginfo    | Llamado cuando var_dump es llamado sobre un objeto   |
| __unserialize     |  Llamado cuando necesitamos un deserializar un objeto  |
| __serialize    | Llamado cuando necesitamos serializar un objeto   |
