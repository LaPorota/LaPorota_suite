# Info

Powerview tiene dos presentaciones: Su homonimo en script de powershell y SharpView. 

SharpView es una versiónm recreada en .Net de manera portable, tiene como beneficio una transacción de información menos transparente, lo cual la vuelve más útil al momento de atacar entornos reales sin que podamos ser agarrados infraganti por los pitufos.

Ambos usan los mismos argumentos y funciones. Puede variar la presentación del resultado.


Tabla de funciones para reconocimiento:

    https://powersploit.readthedocs.io/en/latest/Recon/

A cada función podemos agregarle el **-Help** para que nos muestre todos los parámetros aceptados

---

# Funciones básicas

## Referidas al dominio 

#### Obtener información de un dominio

    .\SharpView.exe Get-Domain
##### Enumerar las OUs del dominio

    .\SharpView.exe Get-DomainOU | findstr /b "name"


#### Enumerar usuarios que no necesiten kerberos preauth

    .\SharpView.exe Get-DomainUser -KerberosPreauthNotRequired

##### Enumerar computadoras dentro del dominio

    Get-DomainComputer | select dnshostname, useraccountcontrol  

##### Enumerar GPOs

    .\SharpView.exe Get-DomainGPO | findstr displayname

##### Enumerar relaciones de confianza

    Get-DomainTrust



---

## Referido a los grupos

##### Obtener grupos de un dominio

    Get-DomainGroup -Properties Name

##### Buscar protected groups

    .\SharpView.exe Get-DomainGroup -AdminCount

##### Buscar miembros de un grupo

    .\SharpView.exe Get-DomainGroupMember -Identity 'Help Desk'

##### Buscar managed security groups

    Find-ManagedSecurityGroups | select GroupName

##### Buscar managers de los security groups

    Get-DomainManagedSecurityGroup

Luego podemos ver qué permisos tiene el manager sobre el grupo

    $sid = ConvertTo-SID joe.evans
    Get-DomainObjectAcl -Identity 'Security Operations' | ?{ $_.SecurityIdentifier -eq $sid}


##### Listar grupos locales de un host

    .\SharpView.exe Get-NetLocalGroupMember -ComputerName WS01

---

## Referido a los usuarios


##### Enumerar cantidad de usuarios en un dominio

    (Get-DomainUser).count
    
##### Convertir name a SID

    .\SharpView.exe ConvertTo-SID -Name sally.jones

##### Convertir Sid a Name

    .\SharpView.exe Convert-ADName -ObjectName S-1-5-21-2974783224-3764228556-2640795941-1724

##### Conseguir la información más importante de un user

    Get-DomainUser -Identity harry.jones -Domain inlanefreight.local | Select-Object -Property name,samaccountname,description,memberof,whencreated,pwdlastset,lastlogontimestamp,accountexpires,admincount,userprincipalname,serviceprincipalname,mail,useraccountcontrol

##### Conseguir la información más útil de todos los usuarios del dominio

    Get-DomainUser * -Domain inlanefreight.local | Select-Object -Property name,samaccountname,description,memberof,whencreated,pwdlastset,lastlogontimestamp,accountexpires,admincount,userprincipalname,serviceprincipalname,mail,useraccountcontrol | Export-Csv .\inlanefreight_users.csv -NoTypeInformation

##### Listar UACs de un user

    Get-DomainUser harry.jones  | ConvertFrom-UACValue -showall

##### Ver en qué computadoras los usuarios están logueados

    Find-DomainUserLocation

    
##### Conseguir todos los users ASREPRoasteables

    .\SharpView.exe Get-DomainUser -KerberosPreauthNotRequired -Properties samaccountname,useraccountcontrol,memberof

##### Conseguir todos los usuarios kerberosteables

    .\SharpView.exe Get-DomainUser -SPN -Properties samaccountname,memberof,serviceprincipalname

##### Buscar usuarios para ver si en su descripción tienen el password

    Get-DomainUser -Properties samaccountname,description | Where {$_.description -ne $null}


##### Buscar usuarios con kerberos constrained delegation

    .\SharpView.exe Get-DomainUser -TrustedToAuth -Properties samaccountname,useraccountcontrol,memberof

##### Encontrar usuarios foraneos en grupos del dominio

    Find-ForeignGroup

Si luego convertimos el SID to Name, vamos a poder saber de qué dominio es nativo el user

Luego podremos buscar usuarios kerberosteables de ese dominio externo.

    Get-DomainUser -SPN -Domain freightlogistics.local | select samaccountname,memberof,serviceprincipalname | fl

---

## Referidas a las computadoras


##### Enumerar computadoras de un dominio

    .\SharpView.exe Get-DomainComputer -Properties dnshostname,operatingsystem,lastlogontimestamp,useraccountcontrol

##### Enumerar computadoras con constrained delegation

    Get-DomainComputer -TrustedToAuth | select -Property dnshostname,useraccountcontrol

##### Enumerar qué GPOs se linkean a una computadora

    Get-DomainGPO -ComputerIdentity WS01 | select displayname
##### Ver si nuestro user tiene permisos de administrador en otro host

    Test-AdminAccess -ComputerName SQL01
##### Ver si un host tiene SMB shares

    .\SharpView.exe Get-NetShare -ComputerName DC01

---

## Referidas a los ACLs

##### Listar ACLs de un user

    Get-DomainObjectAcl -Identity harry.jones -Domain inlanefreight.local -ResolveGUIDs

##### Listar ACLs interesantes de un dominio
    
    Find-InterestingDomainAcl -Domain inlanefreight.local -ResolveGUIDs

##### Buscar users con permisos de DCSync

    $dcsync = Get-ObjectACL "DC=inlanefreight,DC=local" -ResolveGUIDs | ? { ($_.ObjectAceType -match 'Replication-Get')} | Select-Object -ExpandProperty SecurityIdentifier | Select -ExpandProperty value

Luego

    Convert-SidToName $dcsync
##### Ver quienes tienen GenericALL sobre un usuario específico

    Get-ObjectAcl -SamAccountName "joe.evans" -ResolveGUIDs | Where-Object { $_.ActiveDirectoryRights -match "GenericAll" } | ForEach-Object {
        $sid = $_.SecurityIdentifier
        $name = (Get-ADUser -Filter {SID -eq $sid} -ErrorAction SilentlyContinue).SamAccountName
        if (-not $name) {
            $name = (Get-ADGroup -Filter {SID -eq $sid} -ErrorAction SilentlyContinue).SamAccountName
        }
        [PSCustomObject]@{
            IdentityReference = $name
            ActiveDirectoryRights = $_.ActiveDirectoryRights
        }
    }

## Referidas a las relaciones de confianza

##### Listar relaciones de confianza

    Get-DomainTrust

##### Listar relaciones de nuestro dominio y dominios alcanzables

    Get-DomainTrustMapping
