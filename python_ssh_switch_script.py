#netmiko library foo ssh
from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.120.72',
    'username': 'Junior',
    'password': 'cisco',
}


net_connect = ConnectHandler(**iosv_l2)
net_connect.find_prompt()
output = net_connect.send_command('show ip int brief')
print output

#configure loopback interface
config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print output



for n in range (2,4):
    print "Creating VLAN " + str(n)
    config_commands = ['vlan ' + str(n), 'name  ' + str(n)]
    output = net_connect.send_config_set(config_commands)
    print output 
