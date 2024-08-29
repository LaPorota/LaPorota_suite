# Listar instancias de EC2

    aws ec2 describe-instances

# Detalles de una instancia específica

    aws ec2 describe-instances --instance-ids <id>

# Detallar atributos de una instancia específica

    aws ec2 describe-instance-attribute --attribute userData --instance-id <id>

# Ver asociaciones de perfiles de IAM

    aws ec2 describe-iam-instance-profile-associations

# Ver grupos de seguridad configurados

    aws ec2 describe-security-groups


