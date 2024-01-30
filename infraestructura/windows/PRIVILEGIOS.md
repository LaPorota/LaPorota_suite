##### SeNetworkLogonRight	
Access this computer from the network	

Administrators, Authenticated Users	

Determines which users can connect to the device from the network. This is required by network protocols such as SMB, NetBIOS, CIFS, and COM+.
##### SeRemoteInteractiveLogonRight	
Allow log on through Remote Desktop Services	

Administrators, Remote Desktop Users	

This policy setting determines which users or groups can access the login screen of a remote device through a Remote Desktop Services connection. A user can establish a Remote Desktop Services connection to a particular server but not be able to log on to the console of that same server.
##### SeBackupPrivilege	
Back up files and directories	

Administrators	

This user right determines which users can bypass file and directory, registry, and other persistent object permissions for the purposes of backing up the system.
##### SeSecurityPrivilege	
Manage auditing and security log	

Administrators	

This policy setting determines which users can specify object access audit options for individual resources such as files, Active Directory objects, and registry keys. These objects specify their system access control lists (SACL). A user assigned this user right can also view and clear the Security log in Event Viewer.
##### SeTakeOwnershipPrivilege	
Take ownership of files or other objects	

Administrators	

This policy setting determines which users can take ownership of any securable object in the device, including Active Directory objects, NTFS files and folders, printers, registry keys, services, processes, and threads.
##### SeDebugPrivilege	
Debug programs	

Administrators	

This policy setting determines which users can attach to or open any process, even a process they do not own. Developers who are debugging their applications do not need this user right. Developers who are debugging new system components need this user right. This user right provides access to sensitive and critical operating system components.
##### SeImpersonatePrivilege	
Impersonate a client after authentication	

Administrators, Local Service, Network Service, Service

This policy setting determines which programs are allowed to impersonate a user or another specified account and act on behalf of the user.
##### SeLoadDriverPrivilege	
Load and unload device drivers	

Administrators	

This policy setting determines which users can dynamically load and unload device drivers. This user right is not required if a signed driver for the new hardware already exists in the driver.cab file on the device. Device drivers run as highly privileged code.
##### SeRestorePrivilege	
Restore files and directories	

Administrators	

This security setting determines which users can bypass file, directory, registry, and other persistent object permissions when they restore backed up files and directories. It determines which users can set valid security principals as the owner of an object.
