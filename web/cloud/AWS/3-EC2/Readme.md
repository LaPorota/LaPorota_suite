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
