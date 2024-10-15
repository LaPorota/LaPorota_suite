# Info

- Distributed Component Object Model
- Extiende el Component Object Model
- Opera en el RPC
- Utiliza el puerto 135 y una serie de puertos dinámicos que van desde el 49512-65535

La información sobre la identidad, implementación y configuración de cada objeto DCOM está guardado en el registro linkeado por varias keys:

| Key | desc |
|---|---|
|CLSID(class identifier) | Una GUID única para una clase COM que apunta a su implementación en el registro mediante InProcServer32 o LocalServer32. |
|ProgId (Programmatic Identifier) | Un nombre user-friendly para la clase COM (opcional como alternativa al CLSID) |
|AppID (Application Identifier) | Especifica los detalles de configuración de uno o mas objetos COM |


# Enumeration

### Nmap

    nmap -p135,49152-65535 10.129.229.244 -sCV -Pn
