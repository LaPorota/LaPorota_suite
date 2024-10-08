# Estructura

- El AD tiene una estructura jerarquica teniendo como mayor "escalafón" un Forest.
- Cada bosque puede tener uno o varios dominios
- Cada dominio puede tener subdominios
- Cada dominio es una estructura que posee objetos(Usuarios, equipos y grupos). Estos objetos se llaman **Organizational Units(OU)**

Por medio de esta organización podemos tener una estructura clara y coherente. Esto se vuelve especialmente importante al momento de agregar **GPOs(Group Policy Objects)**.

---

# Criterio de enumeración

Cuando ganamos acceso a un entorno de AD deberíamos comenzar buscando mucha información incluyendo:

- Nivel funcional del dominio
- Password Policy del dominio
- Inventario de los usuarios de AD
- Inventario de las computadoras del AD
- Inventario de grupos y memberships
- Relaciones de confianza del dominio
- ACL's de los objetos
- GPOs
- Privilegios de accesos remotos.

Con esta información podemos tener una buena idea de los "quick wins".

Recuerden que la enumeración es de caracter iterativa. Cada vez que logremos llegar a un nuevo host o usuario dentro de un dominio tendremos que realizar nuevas enumeraciones.

---

# Permisos y privilegios



El AD tiene muchos grupos que dan privilegios elevados a sus miembros. 

| Grupo | Desc |
|---|---|
|Default administrators | Administradores de dominios y entrerprise admins |
|Server Operators | Pueden modificar servicios, acceder a carpetas SMB y backapear archivos |
|Backup operators | Deben ser considerados como Domain Admins. Pueden acceder al DC de manera local. Pueden hacer shadow copies de SAM y NTDS, leer el registro remotamente y acceder a los archivos de systema del DC desde un SMB.|
|Print operators | Miembros que están permitidos a loguearse en el DC de manera local y que pueden engañar a windows para cargar un driver malicioso |
| Hyper-V Administrators | Si hay DCs virtuales en el entorno, deben ser conciderados como Domain Admins.|
| Account Operators | Pueden modificar cuentas y grupos no protegidos en el AD |
|Remote Desktop Users | No suelen tener permisos elevados, pero pueden loguearse por medio de Remote desktop y moverse lateralmente usando RDP |
| Remote Management Users | Pueden loguearse en el DC mediante PSRemoting) |
| Group Policy Creator Owners | Pueden crear nuevas GPOs pero necesitan permisos adicionales para linkearlos a un objeto |
| Schema Admins | Pueden modificar el esquema estructural del AD y pueden crear un Backdoor en cualquier grupo que se vaya a crear agregando una cuenta comprometida al Default Object ACL |
|DNS Admins | Tienen permisos para cargar una DLL en un DC pero no tienen permisos necesarios para resetear el servidor DNS. Con lo cual pueden cargar una DLL maliciosa y esperar a un reboot como mecanismo de persistencia|

---

# ACLs

- Listas que definen qué usuario tiene privilegios sobre un objeto y el nivel de los mismos.
- Las settings de estas se llaman **ACE**.

### Tipos de ACLs:
Hay dos tipos de ACLs: **DACL** y **SACL**

##### DACL  
Define los principios de seguridad que se dan a un objeto. Si no hay un DACL aplicado a un objeto, todos los que quieran acceder a él van a tener full rights. Si hay DACL pero no tiene ninguna ACE agregada, entonces nadie podrá acceder al archivo.
##### SACL 
Permite a los administradores a loguear los intentos de acceder a objetos seguros.

### ACEs. 
Hay tres tipos de ACE:

##### Access denied  
Muestran si un user o grupo tiene el acceso explicitamente denegado a un objeto.
##### Access allowed  
Muestran si un ""  "" "   """"""""""" Permitido a un objeto
##### System audit  
Auditan si un user o grupo intentó acceder a un objeto brindando información de si se dio el acceso o no y de qué forma.

Los ACE están conformados por 4 componentes:

1) SID del user o grupo que tiene acceso al objeto
2) La flag del tipo de ACE (denegado, allowed, sistem audit)
3) Flags que especifican si un objeto hijo  puede o no heredar los permisos de acceso del objeto padre.
4) Una marca de acceso(valor de 32bits que define los permisos otorgados sobre el objeto)

Los ACEs son importantes porque podemos abusar de ellos y usualmente, en empresas de grandes tamaños, son difíciles de manejar. Sus fallas de configuración tampoco saltan en scanners.
  
