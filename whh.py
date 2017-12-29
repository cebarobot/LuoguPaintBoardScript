import os
from scipy import ndimage
import re
import time
import json
from urllib import requests
import threading
import queue

color = [
    (0, 0, 0),
    (255, 255, 255),
    (170, 170, 170),
    (85, 85, 85),
    (254, 211, 199),
    (255, 196, 206),
    (250, 172, 142),
    (255, 139, 131),
    (244, 67, 54),
    (233, 30, 99),
    (226, 102, 158),
    (156, 39, 176),
    (103, 58, 183),
    (63, 81, 181),
    (0, 70, 112),
    (5, 113, 151),
    (33, 150, 243),
    (0, 188, 212),
    (59, 229, 219),
    (151, 253, 220),
    (22, 115, 0),
    (55, 169, 60),
    (137, 230, 66),
    (215, 255, 7),
    (255, 246, 209),
    (248, 203, 140),
    (255, 235, 59),
    (255, 193, 7),
    (255, 152, 0),
    (255, 87, 34),
    (184, 63, 39),
    (121, 85, 72)
]

# Get gif map info
im_array = ndimage.imread("ubuntu.png", mode="RGB")
len_row = len(im_array)
len_col = len(im_array[0])

print(len_row, len_col)

# cookies 
mycookies = {
... 'UM_distinctid': '15ff28eb3dbd7-07a2a49a1b07b18-74256751-fa000-15ff28eb3e35',
... '__client_id': 'aad097a12030c1660ed6a276f6133cc57ed14b68',
... 'CNZZDATA5476811': 'cnzz_eid%3D1669199593-1495260563-%26ntime%3D1514561910'
... }


# 基础绘画基准
base_row, base_col = 361, 292

mydata = {
    'x': 399,
    'y': 799,
    'color': '5'
}

s = requests.Session()
rr = s.post('https://www.luogu.org/paintBoard/paint', data = mydata, cookies = mycookies)

