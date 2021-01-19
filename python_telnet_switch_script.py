
import getpass
import sys
import telnetlib
HOST = "192.168.120.1"
user = raw_input("Enter your telnet username: ")
password = getpass.getpass()
tn = telnetlib.Telnet(HOST)
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")


tn.write("conf t\n")

tn.write("enable\n")
tn.write("cisco\n")
tn.write("conf t\n")

#configure vlan
tn.write("vlan 2\n")
tn.write("name MARKETING DEPT\n")
tn.write("exit\n")
tn.write("vlan 3\n")
tn.write("name IT DEPT\n")

#or
#for n in range (2,4):
#    tn.write("vlan " + str(n) + "\n")
#    tn.write("name " + str(n) + "\n")
tn.write("end\n")
tn.write("exit\n")
print tn.read_all()
