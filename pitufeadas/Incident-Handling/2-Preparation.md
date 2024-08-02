### Intro

La etapa de preparación tiene dos objetivos:

1) Establecimiento de la capacidad de respuesta a incidentes dentro de la organización.
2) La habilidad de proteger y prevenir incidentes de seguridad implementando medidas de protección.

### Pre requisitos

- Miembros del equipo con skills en respuesta a incidentes
- Fuerza de trabajo entrenada
- Políticas claras y documentadas
- Herramientas

---

### Políticas claras y Documentadas

Las políticas deben contener:

- Información de contacto y roles de los miembros del equipo de respuesta a incidentes
- Información de contacto de los departamentos de legales y compliance, management teams, soporte IT, comunicaciones, ISP, facility management y equipo externo de respuesta a incidentes.
- Políticas, plan y procedimientos de respuesta a incidentes.
- Políticas y procedimientos para compartir información sobre el incidente.
- Lineamientos de los sistemas y redes, aparte de una golden image y un entorno en clean state
- Dieagramas de redes
- Base de datos de gestión de activos de toda la organización
- Listado de cuentas con privilegios excesivos que pueden ser usadas de ser necesario por el equipo. (Estos usuarios son habilitados durante la etapa de investigación de un incidente y son deshabilitados luego. Es obligatorio que se le reseteen los passwords luego de ser deshabilitados)
- Capacidad de adquirir hardware, software o recurso externo sin un proceso de adquisición completo.
- Un cheatsheet de forense/investigaciones

---

### Medidas de protección más importantes

#### DMARC

Protección de email contra phishing.

La idea de DMARC es rechazar los emails que "pretenden" originarse en la organización. 

Aunque es muy eficiente para bloquear phishing, requiere mucho testeo y fortaleciemiento de las reglas antes de llevarlo a un ambiente productivo debido a que puede muy fácilmente bloquear mails legítimos. Tiene muchos falsos positivos.

#### Endpoint Hardening

Hay algunos standars muy reconocidos de endpoint hardening:

- Deshabilitar LLMNR/NetBIOS
- Implementado de LAPS (sistema que gestiona la rotación de la contraseña del administrador para que no sea la misma en todos los dispositivos) y remover privilegios de administración de los usuarios regulares.
- Setear powershell en "ConstrainedLanguage" mode. (Modo que limita en gran proporción los comandos que pueden ser ejecutados en powershell).
- Habilitar ASR (Attack Surface Reduction) si se está usando MS Defender.
- Bloquear la ejecución desde las carpetas writeables por el usuario. 
- Bloquear la ejecución de scripts como: .hta, .vbs, .cmd, .bat, .js o similares.
- Utilizar host-based Firewalls con el fin de hacer bloqueos de endpoint a endpoint
- Implementar un EDR.

#### Network Protection


- Segmentación de red. Es importante para impedir que una brecha de seguridad se expanda por toda la red.
- Los sistemas críticos deben estar aislados.
- Los sistemas internos no deben estar expuestos a internet.
- Implemantación de IDS/IPS.
- Asegurar que solo los dispositivos aprobados por la organización puedan conectarse a la red.

#### IAM, MFA y PASSWORDS

- Usar contraseñas fuertes (fuertes y complejas no son lo mismo)
- Implementar identity managers para gestionar la identidad y los privilegios de los usuarios
- Implementar MFA para prevenir los accesos en caso de robo de credenciales.



