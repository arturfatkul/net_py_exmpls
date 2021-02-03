#!/usr/bin/env python

import paramiko

key = paramiko.RSAKey.from_private_key_file('id_server_rsa')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect('10.12.0.100', username='user', password='Test123', pkey=key)
stdin, stdout, stderr = client.exec_command('ls -la')
result = stdout.read()
print(result)
stdin, stdout, stderr = client.exec_command('pwd')
result = stdout.read()
print(result)



