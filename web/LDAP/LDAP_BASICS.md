# INFO
Las aplicaciones web usan el LDAP para integrarse con el AD u otro servicio de directorio para autenticacion.

## Terminología

- Directory server (DS): es la entidad que guarda datos(no es un database server)
- LDAP ENTRY: guarda datos de una entidad y tiene 3 componentes principales:
    - Distinguished Name (DN): es un identificador único que consiste en multiples RELATIVE DISTINGUISHED NAMES (RDNs), Cada RDN consiste en un par de clave-valor (ej: **iud=admin,dc=dominio,dc=com**)
    - TIenen multiples atributos que guardan datos. Cada atributo consisten en un tipo de atributo y un valor seteado.
    - Tienen o pueden tener multiples object classes que consisten en tipos de atributos relacionados a un tipo particular de objeto, instancia, persona o grupo.
- LDAP define "Operations"(acciones que un cliente puede iniciar)
    - Bind Operation: Autenticación del cliente en el server
    - Unbind Operation: Cerrar la conexión del cliente con el servidor
    - Add Operation: Crear una nueva entry
    - Delete operation: Eliminar una entry
    - Modify Operation: Modificar una entry
    - Search operation: Buscar entries que matcheen con una query

## LDAP Search filter syntax
Todos los search filters deben estar encerrados en paréntesis. Cada componente debe consistir de atributo, operador y valor.
#### Operadores básicos

- "=" : igual que
- ">=" : mayor o igual que
- "<=" : Menor o igual que
- "~=" : Aproximadamente

#### Concatenadores:
- "(&()())" : AND. ejemplo:  "(&(name=Kaylie)(title=Manager))"
- "(|()())" : OR. ejemplo: "(|(name=Kaylie)(title=Manager))"
- "(!())" : NOT. ejemplo: "(!(name=Kaylie))"

#### Wildcards
- (name=*) matchea todas las entries que tengan un atributo "name"
- (name=k*) matchea todas las entries que tengan un atriburo "name" y cuyo valor inicie con k
- (name=\*a\*) matchea todas las entries con atributo name y que dentro de su valor tenga una letra a
