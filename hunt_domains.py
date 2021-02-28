# Find domains/sun-domains using sublist3r
# List the ones which are alive using TomNomNom HTTProbe

import sublist3r

def hunt_domains(url):

	domain = url
	no_threads = 100
	savefile = 'subdomains.txt'
	ports = None
	silent = False
	verbose = False
	enable_bruteforce = False
	engines = None

	subdomains = sublist3r.main(domain, no_threads, savefile, ports, silent, verbose, enable_bruteforce, engines)

	return subdomains

# s = hunt_domains('vitap.ac.in')
# print(s)