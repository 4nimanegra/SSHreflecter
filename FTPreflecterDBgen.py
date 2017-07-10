import time
import socket
import sys

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

print("#______ ___________          __ _           _            ");
print("#|  ___|_   _| ___ \        / _| |         | |           ");
print("#| |_    | | | |_/ / __ ___| |_| | ___  ___| |_ ___ _ __ ");
print("#|  _|   | | |  __/ '__/ _ \  _| |/ _ \/ __| __/ _ \ '__|");
print("#| |     | | | |  | | |  __/ | | |  __/ (__| ||  __/ |   ");
print("#\_|     \_/ \_|  |_|  \___|_| |_|\___|\___|\__\___|_|   ");
print("#                                                        ");
print('#'+sys.argv[0]+' by animanegra\n#');

if len(sys.argv)==2: 
        DUMMYPORT=1; 
else: 
        DUMMYPORT=0;
try:

	try:
		if DUMMYPORT==0:
			mysocket.bind(('',21));
		else:
			mysocket.bind(('',2100));
	except socket.error:
		print("Error at bind.");
		sys.exit();

	mysocket.listen(1);

	while 1==1:
		try:

			connection, addr = mysocket.accept();

			connection.send("220 \r\n");
			user = connection.recv(512);
			connection.send("331 \r\n");
			password=connection.recv(512);
			connection.send("530 User cannot log in.\r\n");

			connection.close();
			user=str(user);

			if len(user) > 5:
				user=user[5:];
				user=user[:-1];

				if user[len(user)-1] == '\r':
					user=user[:-1];
				password=str(password);

				if len(password) > 5:

					password=password[5:];
					password=password[:-1];

					if password[len(password)-1] == '\r':
						password=password[:-1];
			
					print(str(time.time())+":"+str(addr[0])+":"+user+":"+password);
		except socket.error:
			connection.close();
		except:
			connection.close();
			mysocket.close();
			sys.exit();

except:	
	mysocket.close();
