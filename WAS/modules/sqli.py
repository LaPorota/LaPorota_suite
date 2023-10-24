import subprocess
import os
import xml.etree.ElementTree as ET
import pandas as pd

def sqli_search(host):
    proto, link= host.split('//')
    service_request = f"nmap --script ./scripts/sqli.nse -p 80 -oX {link}_sqli.xml {link}"

    service_discovery = subprocess.check_output(
                service_request, shell=True)
    tree = ET.parse(f'{link}_sqli.xml')
    root = tree.getroot()
    


    script_element = root.find(".//port/script")
    script_output = script_element.get('output')



    filtered_output = script_output.replace("Possible sqli for queries:", "").strip()


    urls = [url.strip() for url in filtered_output.split('\n')]


    data = {'URL': urls}
    df = pd.DataFrame(data)
    
    os.remove(f'{link}_sqli.xml')
    return {'SQLI':df}

if __name__=="__main__":
    sqli_search("http://172.16.77.130")