import xml.etree.ElementTree as ET
from net_gat import get_mi_ip


def get_hosts(obj: str, trucker:int):
    up_hosts = []
    tree = ET.parse('hosts.xml')
    root = tree.getroot()
    for address in root.findall('.//address'):
        addr = address.get('addr')
        if trucker == 1:
            if addr != get_mi_ip(obj):
                if address.get('addrtype') == 'ipv4':
                    up_hosts.append(addr)
        else:
            if address.get('addrtype') == 'ipv4':
                    up_hosts.append(addr)
    return up_hosts


def create_search(product, version=None):
    if product != None and version != None:
        return product + ' ' + version
    elif product != None and version == None:
        return product
    elif product == None and version != None:
        return version
    else:
        return None
