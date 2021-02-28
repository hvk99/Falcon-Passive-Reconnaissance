from Wappalyzer import Wappalyzer, WebPage
import pickle
import os
import warnings
import requests

warnings.filterwarnings("ignore")

def what_tech(url):

	w = Wappalyzer.latest()
	webpage = WebPage.new_from_url(f"http://www.{url}")
	tech_info = w.analyze_with_versions_and_categories(webpage)

	response = requests.get(f"http://www.{url}")
	server_info = response.headers

	return server_info, tech_info