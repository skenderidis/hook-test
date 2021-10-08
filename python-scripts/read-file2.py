import http.client
import ssl
import json
from datetime import datetime

start_time = datetime.now()



x=0
while True:

    x=x+1
    conn = http.client.HTTPSConnection("192.168.5.91",context = ssl._create_unverified_context())
    payload = json.dumps({
    "command": "run",
    "utilCmdArgs": "-c /config/my_bash.sh"
    })
    headers = {
    'Authorization': 'Basic YWRtaW46S29zdGFzMTIz',
    'Content-Type': 'application/json'
    }
    conn.request("POST", "/mgmt/tm/util/bash", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    if x>=200:
        break;


print("Successfull queries requests:" + str(x))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))