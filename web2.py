from requests_html import HTMLSession
import re
from multiprocessing import Pool, Manager, Process
import pandas as pd
from functools import partial
import json
import urllib.error

def get_single_record(records, photoId):
    # print("---start %s ---" % photoId)
    session = HTMLSession()

    url = 'http://ucr.emuseum.com/view/objects/asitem/3631/' + str(photoId)
    try: response = session.get(url, timeout=100)
    except Exception as e:
        print(e)
        log = {photoId : str(e)}
        with open('dicts3/log' + str(photoId) + '.json', 'w+') as f:
            json.dump(log, f)
        return 0

    else: # 程序继续。
        sel = '#singlemedia > div:nth-child(1) > a > img[src^="/internal/media/dispatcher/"]'

        singlemedia = response.html.find(sel, first=True)
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

        with open('dicts3/my_dict_script_'+str(index)+'-'+str(photoId)+'.json', 'w+') as f:
            json.dump(records.copy(), f)
        # ff = open('photo-infos/'+ str(index) + '.txt','w+',encoding='utf-8') 
        # ff.write(str(records))

        print(str(photoId) + "(" + str(index) + ")" + "Done!")
        # print(str(++count) + "Done!")

if __name__ == '__main__':
    manager = Manager()
    records = manager.dict()
    pool = Pool(processes=4)
    # pool.starmap(get_single_record, [(records, i) for i in range(45197)])
    pool.starmap(get_single_record, [(records, i) for i in range(45197)])
    pool.close()
    pool.join()

    # print(records)
    # df = pd.DataFrame(records)
    # df.to_csv('photo_infos_1000.csv', encoding='utf-8', index=False)
    # print("photo_infos_1000.csv created!")

    with open('dicts3/my_dict_script_45197.json', 'w+') as f:
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
