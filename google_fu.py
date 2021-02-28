from googlesearch import search
import socket

def google_fu (url):

	final_list = {'pdf' : [],
				  'doc' : [],
				  'ppt' : [],
				  'xls' : [],
				  'txt' : []}

	try:
		query1 = f"filetype:pdf site:{url}"
		result1 = search(query1, pause=2)
		for file in result1:
			final_list['pdf'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')

	try:
		query2 = f"filetype:txt site:{url}"
		result2 = search(query2, pause=2)
		for file in result2:
			final_list['txt'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')

	try:
		query3 = f"filetype:doc site:{url}"
		result3 = search(query3, pause=2)
		for file in result3:
			final_list['doc'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')

	try:
		query4 = f"filetype:docx site:{url}"
		result4 = search(query4, pause=2)
		for file in result4:
			final_list['doc'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')

	try:
		query5 = f"filetype:xls site:{url}"
		result5 = search(query5, pause=2)
		for file in result5:
			final_list['xls'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')

	try:
		query6 = f"filetype:xlsx site:{url}"
		result6 = search(query6, pause=2)
		for file in result6:
			final_list['xls'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')

	try:
		query7 = f"filetype:ppt site:{url}"
		result7 = search(query7, pause=2)
		for file in result7:
			final_list['ppt'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')

	try:
		query8 = f"filetype:pptx site:{url}"
		result8 = search(query8, pause=2)
		for file in result8:
			final_list['ppt'].append(file)

	except socket.timeout:
		print('Your internet seems slow...')
	except:
		print('Issues occured in making the connection.')


	# for result in result1, result2, result3, result4, result5, result6, result7, result8:
	# 	for i in list(result):
	# 		final_list.append[i]

	return final_list

# files = google_fu('vitap.ac.in')

# print(files)