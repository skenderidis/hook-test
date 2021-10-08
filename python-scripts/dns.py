import socket
from datetime import datetime


start_time = datetime.now()

#addr1 = socket.gethostbyname('google123_12312.com')

#print(addr1)
x=0
y=0
while True:
    x=x+1
    try:
        addr1 = socket.gethostbyname('aaa.test.kostas')
#        print(addr1)

    except Exception, exc:
        print("error while processing item:")
#        y=y+1
    if x>=1000:
        break;


end_time = datetime.now()

print("Successfull DNS requests:" + str(x))
print("Failed DNS requests:" + str(y))
print('Duration: {}'.format(end_time - start_time))
#print(addr1)

#file = open("dns_text.txt",'w')
#file.write("123")
#file.close()