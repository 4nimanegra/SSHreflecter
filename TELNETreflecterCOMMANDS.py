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
#try:

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

		mysocket.settimeout(4);
		connection, addr = mysocket.accept();

		connection.send("user: ");
		user = connection.recv(512);
		connection.send("password: ");
		password=connection.recv(512);
		connection.send("Welcome home JACK.\nbash>");

		commandstmp=connection.recv(2048);
		commands="";

		while len(commandstmp) > 0:

			if "cat /proc/mounts; /bin/busybox" in commandstmp:

				connection.send("rootfs / rootfs rw 0 0\n");
				connection.send("proc /proc proc rw,relatime 0 0\n");
				connection.send("/dev/sda1 / ext3 rw,relatime,errors=continue,barrier=1,data=ordered 0 0\n");
				connection.send("io /etc/blkio cgroup rw,relatime,blkio 0 0\n");
				connection.send("command not found\n\n");
				
			else:

				commands=commands+"\n"+commandstmp;
				connection.send(commandstmp+": command not found\n");

			connection.send("bash>");
			commandstmp=connection.recv(2048);

		connection.close();
		user=str(user);

		if len(user) > 0:

			if user[len(user)-1] == '\n':	
				user=user[:-1];
			if user[len(user)-1] == '\r':
				user=user[:-1];

			if user[0]==chr(0xFF):
				continue;

			if len(user) > 1:

				if len(password) > 1:

					if user[len(user)-1] == '\r':
						user=user[:-1];
					password=str(password);
					if password[len(password)-1] == '\r':
						password=password[:-1];
					if password[len(password)-1] == '\n':
						password=password[:-1];

			if len(password) > 1:
				if password[len(password)-1] == '\r':
					password=password[:-1];

		print(str(time.time())+":"+str(addr[0])+":"+user+":"+password+"\n");
		print("COMMANDS INIT\n");
		print(commands);
		print("COMMANDS END\n");
	except socket.error:
		try:
			connection.close();
		except:
			mysocket.settimeout(4);

	except:
		try:
			connection.close();
		except:
			mysocket.settimeout(4);

#except:
#	mysocket.close();
