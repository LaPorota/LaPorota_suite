import subprocess
import os
import xml.etree.ElementTree as ET
import pandas as pd
import datetime
from argparse import ArgumentParser, Namespace
from net_gat import get_network
from files_manager import search_create_directory, create_template, delete_template
from filterers import get_hosts, create_search
from graphic_adds import separate_bar, banner
from export_data import export_file
from analizers import search_exploits, host_discover, host_forced_discover
from data_handlers import simple_scan_df, final_host_resume

banner()



################################################# ARGS ###################################
parser = ArgumentParser()
parser.add_argument('-d', "--directory",
                    help='Directory to export files \"home/kali/\033[1;33mpath-to-your-file\" \033[0;37m',
                    type=str,
                    required=True)
parser.add_argument('-i', "--interface",
                    help='select an interface [default \033[1;33meth0\033[0;37m]',
                    type=str,
                    default='eth0')
parser.add_argument(
                    '-o', "--OS", help='Ask to find the OS of the hosts. \033[1;33mIt\'s not a default option\033[0;m',
                    action='store_true')
parser.add_argument(
                    '-e', "--export", 
                    help='Name of the results file \033[1;33mdefault = results\033[0;m',
                    type=str, default='result')

parser.add_argument('-f', '--force-segment',
                    help='Allows you to force a \033[1;33msegment \033[1;31m(not recomended) \033[0;mor a \033[1;33msingle ip\033[0;m',
                    type=str
                    )
args: Namespace = parser.parse_args()


################################################ Script Start ############################

separate_bar()

start_time = datetime.datetime.now()
print(f"\033[1;37mScript started at: \033[1;32m {start_time.strftime('%Y-%m-%d %H:%M:%S')}")



################################# Defines output directory
dir_path = f"/home/kali/{args.directory}"

search_create_directory(dir_path)

print(f"\033[1;37mOutput data will be stored in: \033[1;32m {dir_path}")
os.chdir(dir_path)


hosters = []
protocols = []
portids = []
ports_status = []
names = []
versions = []
exploits_name = []
urls = []
paths = []

print(" ")

if args.force_segment == None:
    print("entro por none")
    hosts = host_discover(args.interface)
else:
    print("entro forzado")
    hosts = host_forced_discover(args.force_segment)


found_hosts = ""

for host in hosts:
    found_hosts += host + "\n"

separate_bar()
print(f"""\033[1;37mHosts up in the network: \033[1;32m {found_hosts}""")


for host in hosts:
    print(f"\033[1;32m------------------------------------------------------------")
    print(f"\033[1;37mPort scan started for host: \033[1;32m{host}")
    counter = 0
    if args.OS:
        service_request = f"sudo nmap -sV -O -n -oX {host}.xml {host}"
        print(f"\033[1;37m OS detection \033[1;33menabled\033[0;m")
    else:
        service_request = f"sudo nmap -sV -n -oX {host}.xml {host}"

    service_discovery = subprocess.check_output(service_request, shell=True)
    tree = ET.parse(f'{host}.xml')
    root = tree.getroot()
    print(f"\033[1;37m Port scan ended for host\033[0;m")
    print(f"\033[1;33m Data file created in exports directory")

    print(f"\033[1;37m Searching for \033[1;34m EXPLOITS")
    for port in root.findall('.//port'):

        protocol = port.get('protocol')
        portid = port.get('portid')
        state = port.find('state')
        port_status = state.get('state')
        service = port.find('service')

        if service is not None:
            name = service.get('name')
            product = service.get('product')
            version = service.get('version')

            if version is not int:
                versions.append(create_search(product, version))
            else:
                versions.append(create_search(product))
            events = search_exploits(create_search(product, version))

            for event in events['RESULTS_EXPLOIT']:
                hosters.append(host)
                protocols.append(protocol)
                portids.append(portid)
                ports_status.append(port_status)
                names.append(name)
                exploits_name.append(event['Title'])
                urls.append(event['Application'])
                paths.append(event['Path'])
                counter += 1
    if counter == 0:
        print(f"\033[1;31m No exploits found")
    else:
        print(f"\033[1;37m Found: \033[1;32m {counter} EXPLOITS")


separate_bar()
print(f"\033[1;33mBUILDING DATA SOURCE...")


df = simple_scan_df(hosters, protocols, portids,
                    ports_status, exploits_name, urls, paths)

create_template()

export_file(args.export, df)

delete_template()
hosts_quantity = len(hosts)

end_time = datetime.datetime.now()


final_host_resume(end_time, start_time, hosts, exploits_name)
