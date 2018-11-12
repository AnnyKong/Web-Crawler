from requests_html import HTMLSession
import re
from multiprocessing import Pool, Manager, Process
import pandas as pd
from functools import partial
import json
import urllib
 
# def scrape(url):
#     try:
#         print requests.get(url)
#     except ConnectionError:
#         print 'Error Occured ', url
#     finally:
#         print 'URL ', url, ' Scraped'

# records = {}  # index -> data 
# count = 0

def get_single_record(records, photoId):
    # print("---start %s ---" % photoId)
    session = HTMLSession()

    url = 'http://ucr.emuseum.com/view/objects/asitem/3631/' + str(photoId)
    try: response = session.get(url, timeout=100)
    except urllib.HTTPError as e:
        print(e)
        with open('my_dict_script_part_' + photoId + '.json', 'w+') as f:
            json.dump(records.copy(), f)
    else: # 程序继续。
        sel = '#singlemedia > div:nth-child(1) > a > img[src^="/internal/media/dispatcher/"]'

        singlemedia = response.html.find(sel, first=True)
        # src = singlemedia.('/internal/media/dispatcher/{}/resize:format=preview')
        src = singlemedia.attrs['src']
        index = re.search(r'\d+', src).group()

        # print(singlemedia)
        print(index)


        selData = '#singledata > div'
        # sel2 = '#singledata > div'
        # selLabels = '#singledata > div > span'
        # selDatas = '#singledata > div'
        data = response.html.find(selData)
        # singledata = response.html.find(sel2)
        # labels = response.html.find(selLabels)
        # datas = response.html.find(selDatas)
        
        info = {}
        info['Webpage'] = url
        for j in range(len(data)):
    #         print(data[j].text)
            line = data[j].text.strip()
            if (line != ''):
                l = line.split(':', 1)[0].strip()
                r = line.split(':', 1)[1].strip()
                
                if (l == 'Subjects'):
                    r = r.split('\n')
    #                 print(r)
    #             print(l + ":\n" + r + "\n")
                info[l] = r    
            
        records[index] = info
        # print(records[index])

        with open('dicts/my_dict_script_'+str(index)+'-'+str(photoId)+'.json', 'w+') as f:
            json.dump(records.copy(), f)
        # ff = open('photo-infos/'+ str(index) + '.txt','w+',encoding='utf-8') 
        # ff.write(str(records))

        print(str(photoId) + "(" + str(index) + ")" + "Done!")
        # print(str(++count) + "Done!")

if __name__ == '__main__':
    manager = Manager()
    records = manager.dict()
    # l = manager.list(range(10))
    pool = Pool(processes=4)
    # pool.starmap(get_single_record, [(records, i) for i in range(45197)])
    pool.starmap(get_single_record, [(records, i) for i in range(10000)])
    pool.close()
    pool.join()

    # for i in range(4):
    # p1 = Process(target=get_single_record, args=(records, l))
    # p2 = Process(target=get_single_record, args=(records, l))
    # p1.start()
    # p2.start()
    # p1.join
    # p2.join

    # print(records)
    # df = pd.DataFrame(records)
    # df.to_csv('photo_infos_1000.csv', encoding='utf-8', index=False)
    # print("photo_infos_1000.csv created!")

    with open('my_dict_script_10000.json', 'w+') as f:
        json.dump(records.copy(), f)
    print("my_dict_script_45197.json created!")


# records = {}  # index -> data
# for i in range(45197):
# # for i in range(3):
#     print("---start %s ---" % i)
#     get_single_record(records, i)
#     print("Done!")
    
# get_single_record(records, 2)
# print(records)
