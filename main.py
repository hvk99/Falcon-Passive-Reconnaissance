import os
import json
import what_tech
import hunt_emails
# import pawned
import hunt_domains
import port_scanner
import google_fu
# import search_dirs
import pyfiglet

class Main:
	
	def __init__(self, url):
		self.url = url
		self.server_info = []
		self.techs = []
		self.emails = []
		self.pawned_emails = []
		self.sub_domains = []
		self.open_ports = {}
		self.public_files = []
		self.DATA_PATH = 'D:/College Semesters/Semester 7/Capstone Project/New Project/data'

	def save_files(self):

		self.folder_name = self.url.split('.')[0]
		self.folders = os.listdir(self.DATA_PATH)

		if self.folder_name in self.folders:
			print('Reconnaisance on the given domain has already been performed')
			print('Updating all the information')
			os.removedirs(f'{self.DATA_PATH + "/" +self.folder_name}')
				
		os.mkdir(f'{self.DATA_PATH + "/" +self.folder_name}')

		file_server_info = f'{self.DATA_PATH + "/" + self.folder_name + "/server-info.txt"}'
		file_techs = f'{self.DATA_PATH + "/" + self.folder_name + "/technologies.txt"}'
		file_email = f'{self.DATA_PATH + "/" + self.folder_name + "/emails.txt"}'
		file_sub_domains = f'{self.DATA_PATH + "/" + self.folder_name + "/sub-domains.txt"}'
		file_open_ports = f'{self.DATA_PATH + "/" + self.folder_name + "/open-ports.txt"}'
		file_public_files = f'{self.DATA_PATH + "/" + self.folder_name + "/files.txt"}'

		file = open(file_server_info, 'w+')
		file.write(str(self.server_info))
		file.close()

		file = open(file_techs, 'w+')
		file.write(json.dumps(self.techs))
		file.close()

		file = open(file_email, 'w+')
		file.write(json.dumps(self.emails))
		file.close()

		file = open(file_sub_domains, 'w+')
		file.write(json.dumps(self.sub_domains))
		file.close()

		file = open(file_open_ports, 'w+')
		file.write(json.dumps(self.open_ports))
		file.close()

		file = open(file_public_files, 'w+')
		file.write(json.dumps(self.public_files))
		file.close()

		print('You can find the details in "' + self.DATA_PATH + "/" + self.folder_name + '"')

		return

# print(pyfiglet.figlet_format('FALCON', font='isometric1'))
print(pyfiglet.figlet_format('FALCON'))

print('[+] Welcome to the FALCON v1.1')
print('[+] This tool will do the following:')
print('[1] Fetch the server information')
print('[2] Perform a technology lookup')
print('[3] Find all the public available emails')
print('[4] Find all the sub-domains')
print('[5] Look for all the open ports on these sub-domains')
print('[6] Look for all the files publicly available')


url = input('Inset URL (Ex - If url "http://www.example.org" enter "example.org"): ')
# url = 'vitap.ac.in'
print('Starting all the processes...')

process = Main(url)

print('Performing a technology lookup on the webiste.  ..')
process.server_info, process.techs = what_tech.what_tech(process.url)

print('Hunting all the emails...')
process.emails = hunt_emails.hunt_emails(process.url)
print(f'Was able to successfully grab {len(process.emails)} e-mails.')

# print('Lets check how many emails have been pawned...')
# for email in process.emails:
# 	if pawned.pawned(email):
# 		process.pawned_emails.append(email)

# print(f'Out of {len(process.emails)} e-mails found, {len(process.pawned_emails)} were pawned.')

print('Starting to harvest sub-domains...')
process.sub_domains = hunt_domains.hunt_domains(process.url)

print('Also checking for open-ports on domain and sub-domains...')
for domain in process.sub_domains:
	process.open_ports[domain] = port_scanner.port_scanner(domain)

print('Checking for compromised files using Google Fu')
process.public_files = google_fu.google_fu(process.url)

print('All the information collection is complete now.')
print('Saving everything in files')
process.save_files()
print('All Done! You are good to go.')
