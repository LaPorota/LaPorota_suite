# Info

Windows Management Instrumentation (WMI) es una funcionalidad de windows que estandariza la forma de interacción con SMI, dispositivos, aplicaciones y entornos de red.

Puede ser usado para hacer queries sobre información de los sistemas, configurarlos y realizar tareas administrativas en máquinas remotas.

Por default usa el puerto 135 y una serie de puertos dinámicos entre el 48152 y el 65535.

# Enumeración

##### Nmap

    nmap -p135,49152-65535 10.129.229.244 -sV

Los servicios van a aparecer como **RCP**

##### NetExec

    netexec wmi 10.129.229.244 -u helen -p RedRiot88
