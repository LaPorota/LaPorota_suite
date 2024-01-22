#### Buscar en el código fuente si un sitio es joomla:

    curl -s http://dev.inlanefreight.local/ | grep Joomla

#### Buscar versión manualmente:

    curl -s http://dev.inlanefreight.local/administrator/manifests/files/joomla.xml | xmllint --format -

#### Brute-forcing:

    sudo python3 joomla-brute.py -u http://dev.inlanefreight.local -w /usr/share/metasploit-framework/data/wordlists/http_default_pass.txt -usr admin

#### Automated scan:

    perl joobscan.pl -u <site> --enumerate-components 
    
