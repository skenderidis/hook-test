import paramiko
from scp import SCPClient
from datetime import datetime

start_time = datetime.now()

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client

ssh = createSSHClient('192.168.5.91', 22, 'root','Kostas123')
#client.transfer('/etc/local/filename', '/etc/remote/filename')

#scp = SCPClient(ssh.get_transport())
sftp = ssh.open_sftp()
sftp.get("/config/bigip_gtm.conf", "/home/kostas/gtm.conf")
sftp.close()
#ssh.close()
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))