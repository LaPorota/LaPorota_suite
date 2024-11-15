#### Recursive scanning:
    ffuf -w dictionary:FUZZ -u http://SERVER_IP:PORT/FUZZ -recursion -recursion-depth 1 -e .php -v

#### File fuzzing:
    ffuf -w SecLists/Discovery/Web-Content/web-extensions.txt:FUZZ -u http://SERVER_IP:PORT/blog/indexFUZZ


#### Sub-domine enum:
    ffuf -w dictionary:FUZZ -u http://FUZZ.site/

#### vhosts enum:
    ffuf -w dictionary:FUZZ -u http://site:PORT/ -H 'Host: FUZZ.site'

#### GET parameter fuzzing:
    ffuf -w dictionary:FUZZ -u http://site:PORT/admin/admin.php?FUZZ=key -fs xxx (SecLists/Discovery/Web-Content/burp-parameter-names.txt)

#### POST parameter fuzzing:
    ffuf -w dictionary:FUZZ -u http://site:PORT/path/file.php -X POST -d 'FUZZ=key' -H 'Content-Type: application/x-www-form-urlencoded' -fs xxx
#### Get the answer with curl
  
    curl http://site:PORT/admin/admin.php -X POST -d 'parameter=value' -H 'Content-Type: application/x-www-form-urlencoded'



name values dictionary= SecLists/Usernames/xato-net-10-million-usernames.tx


seclists/Discovery/Web-Content/raft-medium-directories.txt
