import socket

def port_scanner(url):

	try:
		target = socket.gethostbyname(url)
	except:
		return ['This sub domain is dead']

	open_ports = []

	ports_to_scan = [21, 22, 23, 25, 53, 80, 110, 111,
					 135, 139, 143, 443, 445, 993, 995,
 					 1723, 3306, 3389, 5900, 8080]

	for port in ports_to_scan:

		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
		socket.setdefaulttimeout(1)
		connect_status = s.connect_ex((target,port))

		if connect_status == 0:
			open_ports.append(port)

	return open_ports

# sub_domains = ['www.vitap.ac.in',
# 			'beta.vitap.ac.in',
# 			'www.beta.vitap.ac.in',
# 		  'cpanel.vitap.ac.in',
# 			'cpcalendars.vitap.ac.in',
# 			'cpcontacts.vitap.ac.in',
# 			'icafd.vitap.ac.in',
# 			'www.icafd.vitap.ac.in',
# 			'mail.vitap.ac.in',
# 			'stage.vitap.ac.in',
# 			'www.stage.vitap.ac.in',
# 			'vtop.vitap.ac.in',
# 			'vtop1.vitap.ac.in',
# 			'webdisk.vitap.ac.in',
# 			'webmail.vitap.ac.in']

# for i in sub_domains:
# 	print(port_scanner(i))

