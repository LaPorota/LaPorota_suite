### rdp
    Set-ItemProperty -Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server' -name "fDenyTSConnections" -value 0

Luego:

      New-NetFirewallRule -Displayname "Remote Desktop" -Direction Inbound -Action Allow -Protocol TCP -LocalPort 3389



        reg add HKLM\System\CurrentControlSet\Control\Lsa /t REG_DWORD /v DisableRestrictedAdmin /d 0x0 /f

### WINrm

        sc config WinRM start= auto
        net start WinRM
