import requests
from .consultor import researcher
def scan_site(domain):
    api_url = f'https://api.ssllabs.com/api/v3/analyze?host={domain}&all=on'
    response = requests.get(api_url)
    data = response.json()
    return data



def ssl_scan(host):
    initial, host2 = host.split("//")
    result = scan_site(host2)
    protocols = result['endpoints'][0]['details']['protocols']

    protocol_data = []

    for protocol in protocols:
        protocol_name = protocol['name']
        protocol_version = protocol['version']
        print(f"Protocolo: {protocol_name} {protocol_version}")
        protocol_data.append( f"{protocol_name} {protocol_version}")

    
    if len(protocol_data) >= 1:
        cert_dict= {}
        print("[+] Buscando vulnerabilidades: ")

        
        for i in protocol_data:
            cert_list =researcher(i)
            cert_dict[i] = cert_list
        
        return cert_dict
    
    
#
#
#        return df
    else:
        return "NO hubo protocolos encontrados"

if __name__=="__main__":
    ssl_scan("tienda.claro.com.py")