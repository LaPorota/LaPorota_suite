from Wappalyzer import Wappalyzer, WebPage
from .consultor import researcher

def lib_search(host):
    wappalyzer = Wappalyzer.latest()
    webpage = WebPage.new_from_url(host)
    lib_json = wappalyzer.analyze_with_versions_and_categories(webpage)

    filtered_list = []

    for key, value in lib_json.items():
        if value['versions']:
            filtered_list.append(f"{key} {', '.join(value['versions'])}")



    if len(filtered_list)>= 1:
        print("Librerías encontradas: ")
        for i in filtered_list:
            print(i)

        print("[+] Buscando vulnerabilidades: ")

        libs_dictio= {}
        for i in filtered_list:
            lib_df =researcher(i)
            libs_dictio[i] =lib_df

        return libs_dictio
    else:
        print("No se encontraron librerías")

if __name__ == "__main__":
    lib_search("http://172.16.77.130")