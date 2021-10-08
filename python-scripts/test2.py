import requests
import json
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning
import time

# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

start_time = datetime.now()
x=0
url = "https://192.168.5.91/mgmt/tm/util/bash"

while True:

    x=x+1

    time.sleep(10)

    payload = json.dumps({
    "command": "run",
    "utilCmdArgs": "-c /config/my_bash.sh"
    })
    headers = {
    'Authorization': 'Basic YWRtaW46S29zdGFzMTIz',
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)

    print(response.text)
    if x>=200:
        break;


print("Successfull queries requests:" + str(x))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))