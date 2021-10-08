import requests
import json
from datetime import datetime
from urllib3.exceptions import InsecureRequestWarning


# Suppress only the single warning from urllib3 needed.
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

start_time = datetime.now()
x=0
url = "https://192.168.5.91/mgmt/tm/gtm/wideip/a"

while True:

    x=x+1


    headers = {
    'Authorization': 'Basic YWRtaW46S29zdGFzMTIz',
    'Content-Type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, verify=False)

    print(response.text)
    if x>=200:
        break;


print("Successfull queries requests:" + str(x))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))