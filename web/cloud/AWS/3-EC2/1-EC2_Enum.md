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

# Listar imágenes de aws

    aws --profile attacker ec2 describe-images --owners amazon --executable-users all

si buscamos algo puntual podemos agregar la flag filter

    aws --profile attacker ec2 describe-images --executable-users all --filters "Name=name,Values=*Offseclab*"

# Buscar snapshots

    aws --profile attacker ec2 describe-snapshots --filters "Name=description,Values=*offseclab*"
