import time
import socket
import sys

mysocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM);

print("#_____ _____ _      _   _  _____ _____         __ _           _            ");
print("#|_   _|  ___| |    | \ | ||  ___|_   _|       / _| |         | |           ");
print("#  | | | |__ | |    |  \| || |__   | |_ __ ___| |_| | ___  ___| |_ ___ _ __ ");
print("#  | | |  __|| |    | . ` ||  __|  | | '__/ _ \  _| |/ _ \/ __| __/ _ \ '__|");
print("#  | | | |___| |____| |\  || |___  | | | |  __/ | | |  __/ (__| ||  __/ |   ");
print("#  \_/ \____/\_____/\_| \_/\____/  \_/_|  \___|_| |_|\___|\___|\__\___|_|   ");
print("#                                                                           ");
print("#"+sys.argv[0]+" by animanegra\n#");

if len(sys.argv)==2:
        DUMMYPORT=1;
else:
        DUMMYPORT=0;
try:

	try:

		if DUMMYPORT==0:

			mysocket.bind(('',23));
		else:
			mysocket.bind(('',2300));	
			
	except socket.error:
		print("Error at bind.");
		sys.exit();

	mysocket.listen(1);

	while 1==1:
		try:

			connection, addr = mysocket.accept();

			connection.send("user: ");
			user = connection.recv(512);
			connection.send("password: ");
			password=connection.recv(512);
			connection.send("Bad password.\n");

			connection.close();
			user=str(user);

			if len(user) > 0:
	
				user=user[:-1];

				if user[0]==0xFF:
					print("Tesiria jump");
					continue;

				if len(user) > 1:

					if len(password) > 1:

						if user[len(user)-1] == '\r':
							user=user[:-1];
						password=str(password);
						password=password[:-1];

				if len(password) > 1:
					if password[len(password)-1] == '\r':
						password=password[:-1];

			print(str(time.time())+":"+str(addr[0])+":"+user+":"+password);
		except socket.error:
			connection.close();
		except Exception as e:
			print(str(e));
			connection.close();
			mysocket.close();
			sys.exit();

except Exception as e:
	print(str(e));	
	mysocket.close();
