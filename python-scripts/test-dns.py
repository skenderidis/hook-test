import socket
from datetime import datetime
import time

limit = 500   ### "How many DNS requets you want to execute? (for example 10,000): ")
dns_name = "aaa.test.kostas"  #### "What is the hostname you want to resolve? (for example www.test.local): ")
start_time = datetime.now()
addr1="Failed"
sleep_time = 0.005

x=0
y=0
while True:
    x=x+1
    time.sleep(sleep_time)
    try:
        addr1 = socket.gethostbyname(dns_name)
#        print(addr1)

    except Exception, exc:
#        print("error while processing item:")
        y=y+1
    if x>=limit:
        break;


end_time = datetime.now()

print("Attemptedl DNS requests:" + str(x))
print("Failed DNS requests:" + str(y))
print('Duration: {}'.format(end_time - start_time))
print(addr1)

