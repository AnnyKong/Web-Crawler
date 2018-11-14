from requests_html import HTMLSession
import re
from multiprocessing import Pool, Manager, Process
import pandas as pd
from functools import partial
import json
import urllib.error
import sys

keyword = ""
count = 0
search_url_l = 'http://ucr.emuseum.com/view/objects/asitem/search@/'
search_url_r = '/title-asc?t:state:flow=244cf9d6-dd0b-4e9a-b5ce-4f530845e864'


def get_single_record(records, search_id):
	# print("---start %s ---" % photoId)
	session = HTMLSession()

	url = search_url_l + str(search_id) + search_url_r
	print(url)
	try: 
		response = session.get(url)
	except Exception as e:
	    print(e)
	    log = {search_id : str(e)}
	    with open('dicts4/log' + str(search_id) + '.json', 'w+') as f:
	        json.dump(log, f)
	    return 0

	else: # 程序继续。

		print(response.html.text)
		ff = open('dicts4/'+ str(search_id) + '.txt','w+',encoding='utf-8') 
		ff.write(response.html.text)
		sel = '#singlemedia > div:nth-child(1) > a > img[src^="/internal/media/dispatcher/"]'

		singlemedia = response.html.find(sel, first=True)
		print(singlemedia)
		src = singlemedia.attrs['src']
		index = re.search(r'\d+', src).group()

		selData = '#singledata > div'
		data = response.html.find(selData)
		print(index)

		info = {}
		info['Webpage'] = url
		for j in range(len(data)):
		    line = data[j].text.strip()
		    if (line != ''):
		        l = line.split(':', 1)[0].strip()
		        r = line.split(':', 1)[1].strip()
		        
		        if (l == 'Subjects'):
		            r = r.split('\n')
		#             print(l + ":\n" + r + "\n")
		        info[l] = r    
		    
		records[index] = info

		with open('dicts4/' + keyword + '_'+str(index)+'-'+str(search_id)+'.json', 'w+') as f:
		    json.dump(records.copy(), f)
		# ff = open('photo-infos/'+ str(index) + '.txt','w+',encoding='utf-8') 
		# ff.write(str(records))

		print(str(search_id) + "(" + str(index) + ")" + "Done!")
		# print(str(++count) + "Done!")

# def get_urls(search_url)

if __name__ == '__main__':
	if len(sys.argv) != 3:
		print("python3 read.py <keyword> <count>")
	keyword = sys.argv[1]
	count = int(sys.argv[2])
	print(keyword)
	print(count)

	htmls = [i for i in range(count)]
	# temp = {}
	# file = "my_dict_script_124059-43710.json"
	# with open(file) as f:
	# 	print("loading")
	# 	temp = json.load(f)


	# for i in temp.keys():
	# 	seen_html = temp[i]['Webpage']
	# 	# print(seen_html)
	# 	seen_index = re.search(r'\d+$', seen_html).group()
	# 	if int(seen_index) in htmls:
	# 		# print("remove " + str(seen_index))
	# 		htmls.remove(int(seen_index))

	print(len(htmls))


	# manager = Manager()
	# records = manager.dict()
	# pool = Pool(processes=1)
	# pool.starmap(get_single_record, [(records, i) for i in htmls])
	# pool.close()
	# pool.join()

	records = {}
	for i in htmls:
	    get_single_record(records, i)

	# print(records)
	# df = pd.DataFrame(records)
	# df.to_csv('photo_infos_1000.csv', encoding='utf-8', index=False)
	# print("photo_infos_1000.csv created!")

	with open('dicts4/' + keyword + '_' + str(count) + '.json', 'w+') as f:
	    json.dump(records.copy(), f)
	print(keyword + '_' + str(count) + '.json created!')


# records = {}  # index -> data
# for i in range(45197):
# # for i in range(3):
#     print("---start %s ---" % i)
#     get_single_record(records, i)
#     print("Done!")
    
# get_single_record(records, 2)
# print(records)
