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
		print(user+':'+password)
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
			sock.bind(('', 22))

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

					t = paramiko.Transport(client, gss_kex=DoGSSAPIKeyExchange)
					t.set_gss_host(socket.getfqdn(""))

					t.add_server_key(host_key)

					server = Server(addr[0])

					try:

						t.start_server(server=server)

					except paramiko.SSHException:

						exit

					chan = t.accept(20)

				except Exception as e:
					exit

		except:

			exit

else:

	print('#'+sys.argv[0] + ': An SSH reflecting server.')
	print('#')
	print('#Ussage: ' + sys.argv[0] + ' RSA_key_file ')
	print('#	RSA_key_file:	path to rsa key file.')
	print('#			to generate file just execute from shell:')
	print('#				ssh-keygen -t rsa -N "" -f RSA_key_file')
