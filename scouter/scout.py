import os
import datetime
from argparse import ArgumentParser, Namespace
from files_manager import search_create_directory, create_template, delete_template
from graphic_adds import separate_bar, banner
from export_data import export_file
from analizers import host_discover, host_forced_discover, host_simple_analizer, ninja_host_scan
from data_handlers import simple_scan_df, final_host_resume
from config import BASE_DIR

banner()


################################################# ARGS ###################################

parser = ArgumentParser()
parser.add_argument('-d', "--directory",
                    help='Directory to export files \"home/kali/\033[1;33mpath-to-your-file\" \033[0;37m',
                    type=str,
                    required=True)
parser.add_argument('-i', "--interface",
                    help='select an interface [default \033[1;33meth0\033[0;37m]',
                    type=str,
                    default='eth0')
parser.add_argument(
    '-o', "--OS", help='Ask to find the OS of the hosts. \033[1;33mIt\'s not a default option\033[0;m',
    action='store_true')
parser.add_argument(
    '-e', "--export",
    help='Name of the results file [\033[1;33mdefault=results\033[0;m]',
    type=str, default='result')

parser.add_argument('-f', '--force-segment',
                    help='Allows you to force a \033[1;33msegment \033[1;31m(not recomended) \033[0;mor a \033[1;33msingle ip\033[0;m',
                    type=str
                    )
parser.add_argument('-n', '--ninja',
                    help='works sigilous as a ninja [\033[1;33mit\'s SLOW \033[0;m]',
                    action='store_true')
args: Namespace = parser.parse_args()


################################################ Script Start ############################

separate_bar()

start_time = datetime.datetime.now()
print(
    f"\033[1;37mScript started at: \033[1;32m {start_time.strftime('%Y-%m-%d %H:%M:%S')}")


# Defines output directory
dir_path = f"{BASE_DIR}{args.directory}"

search_create_directory(dir_path)

print(f"\033[1;37mOutput data will be stored in: \033[1;32m {dir_path}")
os.chdir(dir_path)


print(" ")

# Defines the host discovery
if args.force_segment == None:

    hosts = host_discover(args.interface)
else:

    hosts = host_forced_discover(args.force_segment)


found_hosts = ""

for host in hosts:
    found_hosts += host + "\n"

separate_bar()
print(f"""\033[1;37mHosts up in the network: \033[1;32m {found_hosts}""")

if args.ninja:
    print(f'Ninja mode \033[1;33mENABLED\033[1;32m. It may take several minutes\033[0;m')
    host_analizer = ninja_host_scan(hosts, dir_path)
else:

    host_analizer = host_simple_analizer(hosts)

separate_bar()
print(f"\033[1;33mBUILDING DATA SOURCE...")


df = simple_scan_df(host_analizer[0], host_analizer[1], host_analizer[2],
                    host_analizer[3], host_analizer[4], host_analizer[5], host_analizer[6])

create_template()

export_file(args.export, df)

delete_template()
hosts_quantity = len(hosts)

end_time = datetime.datetime.now()


final_host_resume(end_time, start_time, hosts, host_analizer[4])
