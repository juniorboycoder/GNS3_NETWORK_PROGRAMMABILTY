
import getpass
import sys
#telnet library
import telnetlib

#routers ip address
HOST = "192.168.122.181"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")

#configure loopback interfaces
tn.write("int loop 0\n")
tn.write("ip address 1.1.1.1 255.255.255.255\n")
tn.write("int loop 1\n")
tn.write("ip address 2.2.2.2 255.255.255.255\n")
#configure eigrp
tn.write("router eigrp 1\n")
tn.write("network 0.0.0.0 255.255.255.255\n")
tn.write("end\n")
tn.write("exit\n")

print tn.read_all()
