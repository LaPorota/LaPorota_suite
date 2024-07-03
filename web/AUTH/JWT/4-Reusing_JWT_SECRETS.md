Muchas organizaciones reutilizan las secret keys de los tokens al momento de crear nuevas aplicaciones web.

Esto nos permite aprovechar tokens de otros sitios, incluso aprovechando los privilegios de los mismos:

Supongamos que una empresa libera dos redes sociales: socialA.com y socialB.com. El usuario Tomás es moderador en socialA.com pero es un usuario común en socialB.com; Si ambas redes sociales utilizan la misma firma de token, Tomás podría reutilizar el token de socialA.com en socialB.com y elevar sus privilegios a moderador.
