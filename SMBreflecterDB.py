import smbserver

server = smbserver.SimpleSMBServer(listenPort=44500);
server.setLogFile('./smblog.txt');
server.start();
