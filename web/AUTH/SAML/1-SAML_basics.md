### INFO

- Es un XML-Based standard
- Permite la autenticación, autorización y puede ser usado para implementar SSO.
- Los datos son intercambiados mediante XMLs firmados digitalmente para asegurar su integridad.

---

### Componentes

| Componente | Desc |
|-----------|-----------|
| Identiti provider (**idP**)    | La entidad que autentica usuarios. Provee información de la identidad a otros componentes y genera **SAML assertions**    | 
| Service provider (**SP**    | Entidad que provee un servicio o un recurso al usuario. Se basa en el SAML assertions proveído por el idP      |
| SAML Assertions    | data guardada en un XML-based que contiene información sobre el estado de la autenticación y la autorización del usuario     |

---

### Flujo de SAML

1. El user accede a un recurso proveído por el SP
2. Si el usuario no está autenticado, el SP inicia la autenticación reenviando al user al idP con una SAML request
3. El usuario se autentica con el idP
4. El idP genera una SAML assertion, la firma y la envía en una response al browser. El browser envia la SAML assertion al SP
5. El SP verifica la SAML assertion
6. El usuario pide el recurso
7. El SP provee el recurso.


