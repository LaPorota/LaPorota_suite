# Intro

Las lambdas son funciones del ecosistema de AWS. En ellas se encapsula el código fuente y las configuraciones necesarias para su ejecución.

Cada función realiza una tarea, es llamada de manera independiente y no persiste datos en sí. 

Es el pilar de la arquitectura serverless.

---

# Enumeración

## Listar todas las funciones lambda

    aws lambda list-functions

## Ver detalles de una lambda

    aws lambda get-function --function-name <funcion>

## Ver politicas de una lambda

    aws lambda get-policy --function-name <funcion>

## Mapear fuentes de eventos de invocación

    aws lambda list-event-source-mappings --function-name <funcion>

## Listar capas de lambda

Las layers asociadas con las funciones lambda pueden contener bibliotecas o dependencias compartidas

    aws lambda list-layers
