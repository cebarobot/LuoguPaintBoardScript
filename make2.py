import os
from scipy import ndimage
import re
import time
import json
import requests
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

mynum = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v']

# Get gif map info
im_array = ndimage.imread("earthman.bmp", mode="RGB")
len_row = len(im_array)
len_col = len(im_array[0])

print(len_row, len_col)

arr = [[0 for i in range(len_col)] for i in range(len_row)]

def makechar():
    global arr
    for i in range(0, len_row):
        for j in range(0, len_col):
            mnid, mnvl = 0, 999999
            for k in range(0, 32):
                vvvv = ((im_array[i][j][0] - color[k][0]) * (im_array[i][j][0] - color[k][0])
                        + (im_array[i][j][1] - color[k][1]) * (im_array[i][j][1] - color[k][1])
                        + (im_array[i][j][2] - color[k][2]) * (im_array[i][j][2] - color[k][2]))
                if vvvv < mnvl :
                    mnid = k
                    mnvl = vvvv
            arr[i][j] = mynum[mnid]
    print("charpic finished!~")

# cookies 
mycookies = [
    {
        'UM_distinctid': '160a5a02f1e34c-00a286642c06828-173a7640-e1000-160a5a02f1f5c8',
        '__client_id': '236f31d4e24a406d3dba65cce3ec5f24da66437a',
        'CNZZDATA5476811': 'cnzz_eid%3D322944717-1514602952-%26ntime%3D1514602952'
    },
]

base_row, base_col = 275, 635

def getBoard():
    global data
    ret = requests.get('https://www.luogu.org/paintBoard/board', cookies = mycookies[0])
    data = ret.text.split('\n')

def draw():
    getBoard()
    count = 0
    for i in range(len_row):
        for j in range(len_col):
            print("now at", base_col + j, base_row + i)
            if data[base_col + j][base_row + i] != arr[i][j]:
                print("darwing", base_col + j, base_row + i, arr[i][j])
                mydata = {
                    'x': base_col + j,
                    'y': base_row + i,
                    'color': arr[i][j]
                }
                ret = requests.post('https://www.luogu.org/paintBoard/paint', data = mydata, cookies = mycookies[count % len(mycookies)])
                print(ret.text)
                count = count + 1
                time.sleep(30 / len(mycookies))
    

def main():
    makechar()
    draw()

if __name__ == "__main__":
    main()
