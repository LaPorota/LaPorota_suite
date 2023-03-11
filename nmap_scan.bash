for i in {rango de puertos}; do; echo "--------$i-------"; sudo nmap -sV -p $i ip -oN Desktop/scans/scan_$i; sleep $(shuf -i min-max -n 1); done; 
