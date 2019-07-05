import sys
import time
from skillpub_ssh import SSH
import re


def my_print(data):
    if ('Subs Count') in data:
        res = re.findall(" (\\d*) \|", data)
        count = [str(res)]
        clean_count = count[0]
        print(clean_count.replace("['", "").replace("']",""))
    else:
        return


ssh = SSH()
res = ssh.connect(host='xx.xxx.xxx.xxx', port=22, username='xxx', password='xxx', callback=my_print)

if res == 1:
    print("не получилось")
    sys.exit()

ssh.cmd('sudo Imysql.client idx -e "select count(*) as \'Subs Count\' from Subscription"')

time.sleep(2)
ssh.close()