from modules.sqli import sqli_search
from modules.ssl_scan import ssl_scan
from modules.lib2 import lib_search
from modules.reporter_pdf2 import pdf_maker
from modules.clickjacker import clickjacker


host = 'https://tienda.claro.com.py'
host2 = "http://172.16.77.130"
resultados = {}

################################# ssl scan

print("[+] Buscando certificados")
resultados['certificados'] = ssl_scan(host)

##################################  lib search

print("[+] Buscando librerías")
resultados['librerias'] = lib_search(host2)

################################# Clickjacker
print("[+] Analizando headers")
resultados['Headers'] = clickjacker(host)

################################## SQLI

#print("[+] Buscando SQLI")
#resultados['SQLI'] = sqli_search(host2)

################################# PDF export

pdf_maker(resultados)

