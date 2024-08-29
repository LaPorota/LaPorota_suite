# Info

Un EC2 es un servidor virtual dentro de AWS.

# AMI

La AMI(Amazon Machine Image) son plantillas preconfiguradas que contienen el sistema operativo y la configuración de software necesaria para lanzar una instancia EC2

# Grupos de seguridad

- Funcionan como firewalls virtuales.
- Controlan el tráfico desde(egress) y hacia(ingress) la EC2
- Permite especificar reglas basadas en IP, Protocolos y puertos.

---

# Networking en EC2

El networking en Amazon EC2 brinda la arquitectura necesaria para conectar las instancias EC2 con el internet, otros servicios de AWS y con componentes dentro de una red interna.

### Amazon Virtual Private Cloud (VPC)

- Red virtual privada dentro de la infraestructura de AWS
- Permite crear subredes para generar bloques aislados unos de otros.
- Posee tablas de ruteo que determinan cómo el tráfico es dirigido entre las subredes, internet y otros servicios de AWS.
- IGW (internet gateway) permite la comunicación entre instancias de la VPC e internet
- Nat Gateway permite que las instancias en una subred privada accedan a servicios en internet u otros servicios de AWS mientras se mantienen inaccesibles desde internet.

---

# IMDS

El instance metadata service gestiona los metadatos de una instancia. Estos metadatos son un conjunto crucial de información sobre la instancia. Se utiliza para gestionar y adaptar el comportamiento de la instancia.

Los metadatos de una EC2 tienen detalles como: 

- Nombre del Host
- IP
- Grupos de seguridad asignados
- Credenciales temporales de IAM
- Configuración del balanceador de carga.

#### Accediendo a los metadatos

Los metadatos son accedidos mediante una URL específica. Esta dirección ip es accesible únicamente desde la instancia.

    http://169.254.169.254/latest/meta-data/

#### Listado de roles asociados a la instancia

    http://169.254.169.254/latest/meta-data/iam/security-credentials/

#### Obtener credenciales de un rol IAM Asignado

    http://169.254.169.254/latest/meta-data/iam/security-credentials/<rol>
    

#### Veriones y seguridad

Actualmente IMDS tiene dos versiones: v1 y v2.

|versión | diferencias | Vulnerabilidad |
|---|--|---|
|V1 | No posee medidas de seguridad más que la imposibilidad de acceder a los datos fuera de la instancia.| Puede ser consultado si la aplicación servida en la instancia es vulnerable a ssrf|
|v2 | Posee tokens de sesión conseguidos mediante un método put desde la instancia, tiene métodos http restringidos a PUT y GET y los tokens tienen una vida útil de 6hs| Solamente es vulnerable en el caso de que esté sirviendo una app vulnerable a SSRF en un formulario que se envíe por método PUT (casi imposible) y otro por método get. |
