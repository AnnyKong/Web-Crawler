# from requests_html import HTMLSession
# import re
# from multiprocessing import Pool, Manager, Process
# import pandas as pd
# from functools import partial
import json
import sys

# records = {}  # index -> data 
# count = 0

def read(file):
    dict = {}
    # with open(argv[1] + 'json', "w") as f:
    #     json.dump(dict, f)
    with open(file) as f:
        dict = json.load(f)

    print('----Read Success----')
    print("The file (" + file + ') has: ')
    print('\t' + str(len(dict)) + ' records.')
    print('--------------------')
    

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("python3 read.py <json_filename>")
    file = sys.argv[1]
    if not sys.argv[1].endswith('.json'):
        file += '.json'
    read(file)

