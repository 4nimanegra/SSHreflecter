#   _____ _____ _   _ ______      __ _           _   
#  /  ___/  ___| | | || ___ \    / _| |         | |  
#  \ `--.\ `--.| |_| || |_/ /___| |_| | ___  ___| |_ 
#   `--. \`--. \  _  ||    // _ \  _| |/ _ \/ __| __|
#  /\__/ /\__/ / | | || |\ \  __/ | | |  __/ (__| |_ 
#  \____/\____/\_| |_/\_| \_\___|_| |_|\___|\___|\__|
#                                                   

# SSHreflecter
#
# by animanegra
#

#
# This suite is composed of two programms. The first is a service that listen
# in the ssh port and will output on the stdout all the IP addresses that can
# be accessed by using the same credentials used on the incomming connection.
#
# The idea is to kindnap the botnets by using the same credentials they use to
# atack. If you are being attacked by a kindnapped device this device was kindnapped
# by using the same dictionary database that will be used to try to atack you.
# If we reproduce all the user and password the atacker tries to the same atacker we could obtain
# the user and password to login on it.
#
# The program needs to be executed by using the python interpreter and uses the paramiko ssh lib.
#	https://www.python.org/
#	https://github.com/paramiko/
#
# The basic program is:
#
#	SSHreflecter.py
#
# in order to make an ssh rsa key the user have to execute on the shell in linux:
#
#	ssh-keygen -t rsa -N "" -f RSA_key_file
#
# The command mus be executed by the following way:
#
#	python SSHreflecter.py path_to_rsa_key_file
#
# The program starts and as new connections tries to log the server will reflect the atack to the atacket
# in order to know if the credentials succesfully logs on the atacker. If this happend, the IP address, the 
# user and the password will be shown on screen.
#
#
# An alternative program is presented too:
#
#	SSHreflecterDBgen.py
#
# The command has to be executed like the previous one:
#
#	python SSHreflecterDBgen.py path_to_rsa_key_file
#
# The program will start to show all the users and password on stdout. The program will remains passive and
# will not try to log into the remote hosts.
#
