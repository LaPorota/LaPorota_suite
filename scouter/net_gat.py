import subprocess
import re


def get_mi_ip(obj:str):
    output = subprocess.check_output(['ifconfig', obj]).decode()
    match = re.search(r'inet\s+(?P<ip>\d+\.\d+\.\d+\.\d+)', output)
    if match:
        private_ip = match.group('ip')
        return private_ip
    else:
        print("\033[1;31mPrivate IP address not found for eth0")


def get_network(obj:str):
    oct1, oct2, oct3, oct4 = get_mi_ip(obj).split(".")
    network_to_scan = f'{oct1}.{oct2}.{oct3}.0/24'
    print("")
    print(f"\033[1;32m------------------------------------------------------------")
    print(f"\033[1;37mNetwork Range found: \033[1;32m{network_to_scan}")
    return network_to_scan


