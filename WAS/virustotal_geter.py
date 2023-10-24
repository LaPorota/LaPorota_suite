import requests

# Configura tu API key de VirusTotal
API_KEY = 'dbb07d533b3db77ec8b1cf9aa3533bb15de5aa00decfbe532d5c39f15d34755d'

def search_url(url):
    params = {'apikey': API_KEY, 'query': url}
    response = requests.get('https://www.virustotal.com/api/v3/search', params=params)
    data = response.json()
    return data

def get_subdomains(domain_id):
    headers = {'x-apikey': API_KEY}
    response = requests.get(f'https://www.virustotal.com/api/v3/domains/{domain_id}/subdomains?limit=300', headers=headers)
    data = response.json()
    return data

if __name__ == '__main__':
    url = input('Ingrese la URL: ')
    
    
        
    subdomain_data = get_subdomains(url)

    subdomines_list=[]    
    if 'data' in subdomain_data:
            subdomains = subdomain_data['data']
            print(f"Subdominios encontrados para '{url}':")
            for subdomain in subdomains:
                subdomines_list.append(subdomain['id'])
            print(f"Cantidad de subdominios {len(subdomines_list)}")
            print(subdomines_list)
            
    else:
            print('No se encontraron subdominios.')
else:
        print('No se encontraron resultados para la URL.')
