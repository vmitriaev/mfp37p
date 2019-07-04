import paramiko

host = '10.216.192.195'
user = 'admusr'
secret = 'Dukw1@m?'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
channel = сlient.get_transport().open_session()
channel.get_pty()
channel.settimeout(5)
channel.exec_command('sudo ls')
channel.send(password+'\n')
#print channel.recv(1024)
channel.close()
client.close()

#stdin, stdout, stderr = client.exec_command('ls -l')
#data = stdout.read() + stderr.read()
#cif = client.
#print(stdin)
#print(stdout)
#print(stderr)
#print(data)
#client.close()