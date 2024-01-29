#### Suele usar los puertos
- 80	HTTP	Used for non-secure HTTP communication between the web server and web browser.
- 443	HTTPS	Used for secure HTTP communication between the web server and web browser. Encrypts the communication between the web server and web browser.
-1935	RPC	Used for client-server communication. Remote Procedure Call (RPC) protocol allows a program to request information from another program on a different network device.
- 25	SMTP	Simple Mail Transfer Protocol (SMTP) is used for sending email messages.
- 8500	SSL	Used for server communication via Secure Socket Layer (SSL). (a este llamamos cuando vamos a buscar el servicio en el browser)
- 5500	Server Monitor	Used for remote administration of the ColdFusion server.

### Enumeration
- Las páginas de ColdFusion suelen ser .cfm o .cfc
- En los http headers suele avisarlo en "server" o en "x-powered-by"
- Sus archivos por default son:
  - admin.cfm
  - CFIDE/administrator/index.cfm
 
Suele disponibilizar dos carpetas importantes:
- CFIDE ( El path al login del admin se encuentra dentro de esta carpeta /CFIDE/administrator)
- cfdocs
