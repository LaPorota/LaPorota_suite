### Intro

La data exfiltration funciona como las inyecciones SQL o el XSS en sus versiones avanzadas. Debemos intentar entender la query que se está haciendo al XML (en base al comportamiento) para inyectar código.

### Confirmando el Xpath injection

Podemos intentar una inyección booleana para determinar si la misma existe:

    SOMETHINGINVALID') or ('1'='1

