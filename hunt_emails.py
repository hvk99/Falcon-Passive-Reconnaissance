import requests
from pyhunter import PyHunter

def hunt_emails(url):

	api_key = "ec9a041767c7f735013e3ddca6e67c8f0033a0bf"

	hunter = PyHunter(api_key)
	data = hunter.domain_search(url)
	emails = data['emails']
	people = []

	for email in emails:
		person = {}
		person['first_name'] = email['first_name']
		person['last_name'] = email['first_name']
		person['email'] = email['value']
		people.append(person)

	return people