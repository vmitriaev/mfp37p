import paramiko

host = '10.216.192.195'
user = 'admusr'
secret = 'Dukw1@m?'
port = 22

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(hostname=host, username=user, password=secret, port=port)
stdin, stdout, stderr = client.exec_command('sudo Imysql.client idx -e \"select count(*) as \'Subs Count\' from Subscription\";')
data = stdout.read() + stderr.read()
print(stdin)
print(stdout)
print(stderr)
print(data)
client.close()