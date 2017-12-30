import os
from scipy import ndimage
import re
import time
import json
import requests
import threading
import queue

arr = 

# Get gif map info
im_array = ndimage.imread("earthman.bmp", mode="RGB")
len_row = len(im_array)
len_col = len(im_array[0])

print(len_row, len_col)

# cookies 
mycookies = {
    'UM_distinctid': '160a5a02f1e34c-00a286642c06828-173a7640-e1000-160a5a02f1f5c8',
    '__client_id': '236f31d4e24a406d3dba65cce3ec5f24da66437a',
    'CNZZDATA5476811': 'cnzz_eid%3D322944717-1514602952-%26ntime%3D1514602952'
}

# 基础绘画基准
base_row, base_col = 0, 40

mydata = {
    'x': 0,
    'y': 1,
    'color': '5'
}

s = requests.Session()
rr = s.post('https://www.luogu.org/paintBoard/paint', data = mydata, cookies = mycookies)
print(rr.text)

def main():
    for
    
if __name__ == "__main__":
    main()
