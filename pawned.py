from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pawned(emails):

	pawned = []

	# option = webdriver.ChromeOptions()
	# option.add_argument('headless')
	# option.add_argument('--window-size=800,600')

	driver = webdriver.Chrome(executable_path='chromedriver.exe')

	driver.get('https://haveibeenpwned.com/')

	for email in emails:

		driver.find_element_by_id('Account').send_keys(f'{email}')
		time.sleep(3)
		driver.find_element_by_id('searchPwnage').click()
		time.sleep(3)
		pawnage = driver.find_element_by_id('pwnCount').get_attribute('innerHTML')

		if pawned != '':
			pawned.append(email)

	return pawned
	

# result = pawned(['hvkushwaha@gmail.com', 'hvkushwaha@gmail.con'])
# print(result)