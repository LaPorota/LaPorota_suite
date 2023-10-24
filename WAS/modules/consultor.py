import requests
import pandas as pd
from fpdf import FPDF

def fetch_nist_cves(product):
    base_url = f"https://services.nvd.nist.gov/rest/json/cves/1.0"
    params = {
        "keyword": product,
        "resultsPerPage": 10,  
        "startIndex": 0
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        return data["result"]["CVE_Items"]
    else:
        print("Error:", response.status_code)
        return None

def fetch_mitre_cve_data(cve_id):
    base_url = f"https://cve.circl.lu/api/cve/{cve_id}"
    
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error:", response.status_code)
        return None

def calculate_severity(cvss_score):
    if cvss_score != None:
        if cvss_score >= 9.0:
            return "Critical"
        elif cvss_score >= 7.0:
            return "High"
        elif cvss_score >= 4.0:
            return "Medium"
        else:
            return "Low"


def researcher(product):
    nist_cves = fetch_nist_cves(product)

    if nist_cves:
        results = []
        
        for nist_cve in nist_cves:
            cve_id = nist_cve["cve"]["CVE_data_meta"]["ID"]
            mitre_cve_data = fetch_mitre_cve_data(cve_id)
            
            if mitre_cve_data:
                cvss_score = mitre_cve_data["cvss"]
                severity = calculate_severity(cvss_score)
                description = mitre_cve_data["summary"]
                
                result = {
                    "CVE ID": cve_id,
                    "Description": description,
                    "CVSS Score": cvss_score,
                    "Severity": severity
                }
                
                results.append(result)
            
        df = pd.DataFrame(results)
        
    return df

