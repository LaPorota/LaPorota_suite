import pandas as pd
from graphic_adds import separate_bar


def urls_fix(urls):
    urls2 = []
    for i in urls:
        urls2.append(i.replace(".com", ".com/"))
    return urls2


def simple_scan_df(hosters: list, protocols: list, portids: list, ports_status: list, exploits_name: list, urls: list, paths: list):
    df = pd.DataFrame({
        'Host': hosters,
        'Protocol': protocols,
        'Port ID': portids,
        'Port Status': ports_status,
        "Exploits": exploits_name,
        "URL": urls_fix(urls),
        'Paths': paths

    })

    separate_bar()
    print(f"\033[1;36mEXPORTING DATA...")

    return df


def final_host_resume(end_time, start_time, hosts, exploits_name):
    separate_bar()

    print(
        f"\033[1;37mScripts ending: \033[1;32m{end_time.strftime('%Y-%m-%d %H:%M:%S')}")
    duration_time = (end_time - start_time)
    hosts_quantity = len(hosts)
    exploit_quantity = len(exploits_name)
    if hosts_quantity > 1:
        print(
            f"\033[1;32m{hosts_quantity} \033[1;37mhosts scanned. Scan time: \033[1;32m{str(duration_time).split('.')[0]}")
    else:
        print(
            f"\033[1;32m{hosts_quantity} \033[1;37mhost scanned. Scan time: \033[1;32m{str(duration_time).split('.')[0]}")

    if exploit_quantity > 1:
        print(
            f"\033[1;31m{exploit_quantity} \033[1;34mEXPLOITS \033[1;37mFOUNDED")
    else:
        print(f"{exploit_quantity} EXPLOIT FOUNDED")
