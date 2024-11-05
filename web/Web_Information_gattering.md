#### ENUMERACIÓN DE SUBDOMINIOS:
##### Asset Finder
    assetfinder --subs-only pagina

##### WFUZZ
    wfuzz -c -z file,'diccionario' -u 'target' -H 'HOST:FUZZ.target'

Cancelar 404 o filesize 

    wfuzz -c -t 100 --hl=461 --hc=404 -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -H "Host: FUZZ.schooled.htb" http://10.10.10.234

#### ENUMERACIÖN DE DIRECTORIOS:
##### Dirb:
        dirb target
##### Dirsearch

        dirsearch -u target
#### Ffuf:

        ffuf -u <target_url>/FUZZ -w <wordlist_file> -e .<extension> 

#### Gobuster
##### Easy search
        gobuster dir -u "url" -w "diccionario"

##### Add files with extensions

        gobuster dir -u <target_url> -w <wordlist_file> -x <extension>



### Enum vhosts

        ffuf -w subdomains-10000.txt -H “Host: FUZZ.inlanefreight.local” -u http://MACHINE_IP -fs {size}

### Enumerar Apis

        gobuster dir -u http://192.168.50.16:5002 -w /usr/share/wordlists/dirb/big.txt -p pattern
