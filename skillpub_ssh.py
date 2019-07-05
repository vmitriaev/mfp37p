import paramiko
import time
import re
import threading
import warnings

warnings.filterwarnings(action='ignore', module='.*paramiko.*')


class SSH_RECV(threading.Thread):
    def __init__(self, shell, callback=None):
        threading.Thread.__init__(self)
        self.shell = shell
        self.callback = callback
        self.LOOP_DELAY = 1

    def run(self):
        while True:
            time.sleep(self.LOOP_DELAY)
            if self.shell.recv_ready():
                data = self.shell.recv(65535)
                if self.callback is not None: self.callback(data.decode())


class SSH:
    def __init__(self):
        self.host = ""
        self.username = ""
        self.password = ""
        # self.SSHKEY = "/home/skillpub/.ssh/skillpub_key"
        self.shell = None
        self.client = None
        self.callback = None

    def connect(self, host, port=22, username=None, password=None, callback=None, timeout=5):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.callback = callback
        self.timeout = timeout
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password,
                           timeout=self.timeout)
            shell = client.invoke_shell()
            self.shell = shell
            self.client = client
            self.ssh_recv = SSH_RECV(self.shell, self.callback)
            self.ssh_recv.start()
            return (0)
        except:
            self.callback("no connection")
            return (1)

    def cmd(self, command):
        command += "\n"
        try:
            self.shell.send(command)
            return (0)
        except:
            return (1)

    def close(self):
        if self.client is not None:
            try:
                self.client.close()
                return (0)
            except:
                return (1)

    def is_connected(self):
        try:
            return (not self.shell.closed)
        except:
            return (False)