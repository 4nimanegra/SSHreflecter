import time
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

	addr='';

	def __init__(self,addr):
		self.event = threading.Event();
		self.addr=addr;

	def check_auth_password(self, user, password):
		print(str(time.time())+":"+self.addr+":"+user+':'+password);
		return paramiko.AUTH_FAILED;
	def get_allowed_auths(self, username):
		return 'password';
	
print('# _____ _____ _   _           __ _           _            ');
print('#/  ___/  ___| | | |         / _| |         | |           ');
print('#\ `--.\ `--.| |_| |_ __ ___| |_| | ___  ___| |_ ___ _ __ ');
print('# `--. \`--. \  _  | \'__/ _ \  _| |/ _ \/ __| __/ _ \ \'__|');
print('#/\__/ /\__/ / | | | | |  __/ | | |  __/ (__| ||  __/ |   ');
print('#\____/\____/\_| |_/_|  \___|_| |_|\___|\___|\__\___|_|   ');
print('#                                                         ');

print('#'+sys.argv[0]+' by animanegra\n#');

if len(sys.argv)==3:
	DUMMYPORT=1;
else:
	DUMMYPORT=0;
if len(sys.argv)>=2:

	DoGSSAPIKeyExchange = False;
	host_key=None;

	try:

		paramiko.util.log_to_file("sshreflecter.log");
		host_key = paramiko.RSAKey(filename=sys.argv[1]);

	except IOError:

		print('File does not contains a valid rsa key');

	if host_key==None:

		sys.exit();

	else:

		try:

			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
			sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1);
			if DUMMYPORT == 0:
				sock.bind(('', 22));
			else:
				sock.bind(('',2200));

		except Exception as e:

			print('failed: ' + str(e));
			sys.exit();

		try:

			while 1==1:

				try:

					sock.listen(100);
					client, addr = sock.accept();

				except Exception as e:

					print('failed: ' + str(e));
					sys.exit();

				try:

					t = paramiko.Transport(client, gss_kex=DoGSSAPIKeyExchange);
					t.set_gss_host(socket.getfqdn(""));

					t.add_server_key(host_key);

					server = Server(addr[0]);

					try:
						t.local_version = 'SSH-2.0-OpenSSH_6.6.1';
						t.start_server(server=server);

					except paramiko.SSHException:

						sys.exit();

					chan = t.accept(20);

				except Exception as e:
					sys.exit();

		except:

			sys.exit();

else:

	print('#'+sys.argv[0] + ': An SSH reflecting server.');
	print('#');
	print('#Ussage: ' + sys.argv[0] + ' RSA_key_file '+'[-d]');
	print('#	RSA_key_file:	path to rsa key file.');
	print('#			to generate file just execute from shell:');
	print('#				ssh-keygen -t rsa -N "" -f RSA_key_file');
	print('#	-d:		Makes the server listen on 2200 instead of 22.');
