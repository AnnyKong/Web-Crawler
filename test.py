import urllib.error
from requests_html import HTMLSession
import json
 
def test():
    try:
        rsp = session.get('http://blog.csdn.net333')
    except Exception as e:
        print(e)
        # log = {1 : str(e)}
        # with open('log.json', 'w+') as f:
        #     json.dump(log, f)
        # return 0


if __name__ == '__main__':  
    session = HTMLSession()
    test()

    print('done')

