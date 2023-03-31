import subprocess
import json
import xml.etree.ElementTree as ET
from net_gat import get_network
from filterers import get_hosts


def search_exploits(search_string):

    if search_string is not None:
        if search_string.isdigit() and len(search_string) == 1:
            search_string = None
    cmd = f"searchsploit -j {search_string}"
    exploits = subprocess.check_output(cmd, shell=True)
    output1 = exploits.decode('utf-8')
    to_json = json.loads(output1)

    return to_json


def host_discover(arg: str):
    hosts_request = f"sudo nmap -sn -n -PS -oX hosts.xml {get_network(arg)}"
    host_discovery = subprocess.check_output(hosts_request, shell=True)

    hosts = get_hosts(arg, 1)
    return hosts

def host_forced_discover(arg: str):
    hosts_request = f"sudo nmap -sn -n -PS -oX hosts.xml {arg}"
    host_discovery = subprocess.check_output(hosts_request, shell=True)

    hosts = get_hosts(arg, 3)
    return hosts


# def host_simple_analizer(hosts: list, arg: bool):
#    for host in hosts:
#        print(f"\033[1;32m------------------------------------------------------------")
#        print(f"\033[1;37mPort scan started for host: \033[1;32m{host}")
#        counter = 0
#        if arg:
#            service_request = f"sudo nmap -sV -O -n -oX {host}.xml {host}"
#            print(f"\033[1;37m OS detection \033[1;33menabled\033[0;m")
#        else:
#            service_request = f"sudo nmap -sV -n -oX {host}.xml {host}"
#
#        service_discovery = subprocess.check_output(service_request, shell=True)
#        tree = ET.parse(f'{host}.xml')
#        root = tree.getroot()
#        print(f"\033[1;37m Port scan ended for host\033[0;m")
#        print(f"\033[1;33m Data file created in exports directory")
#
#        print(f"\033[1;37m Searching for \033[1;34m EXPLOITS")
#        for port in root.findall('.//port'):
#
#            protocol = port.get('protocol')
#            portid = port.get('portid')
#            state = port.find('state')
#            port_status = state.get('state')
#            service = port.find('service')
#
#            if service is not None:
#                name = service.get('name')
#                product = service.get('product')
#                version = service.get('version')
#
#                if version is not int:
#                    versions.append(create_search(product, version))
#                else:
#                    versions.append(create_search(product))
#                events = search_exploits(create_search(product, version))
#
#                for event in events['RESULTS_EXPLOIT']:
#                    hosters.append(host)
#                    protocols.append(protocol)
#                    portids.append(portid)
#                    ports_status.append(port_status)
#                    names.append(name)
#                    exploits_name.append(event['Title'])
#                    urls.append(event['Application'])
#                    paths.append(event['Path'])
#                    counter += 1
#        if counter == 0:
#            print(f"\033[1;31m No exploits found")
#        else:
#            print(f"\033[1;37m Found: \033[1;32m {counter} EXPLOITS")
