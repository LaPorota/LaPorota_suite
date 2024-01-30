Previo a enumerar más profundamente, necesitamos tener un conocimiento de la situación de los activos que intervienen en el pentest.

### 1)Ver las interfaces disponibles para conocer redes internas(si las hay)
    ipconfig /all

### 2)Routing table
    route print

### 3)Enumerar el estado del defender

    Get-MpComputerStatus

### 4) Listar applicaciones bloqueadas

    Get-AppLockerPolicy -Effective | select -ExpandProperty RuleCollections

#### Podemos testear la política de bloqueo con una aplicación puntual

    Get-AppLockerPolicy -Local | Test-AppLockerPolicy -path C:\Windows\System32\cmd.exe -User Everyone

    
