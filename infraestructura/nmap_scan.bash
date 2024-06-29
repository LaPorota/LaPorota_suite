for i in {rango de puertos}; do; echo "--------$i-------"; sudo nmap -sV -p $i ip -oN Desktop/scans/scan_$i; sleep $(shuf -i min-max -n 1); done; 


21,22,23,25,53,80,111,139,445,512,513,514,1099,1524,2049,2121,3306,3632,5432,5900,6000,6667,6697,8009,8180,8787,35459,38644,40354,60266
