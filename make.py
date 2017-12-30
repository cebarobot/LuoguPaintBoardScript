import os
from scipy import ndimage
import re
import time
import json
import requests
import threading
import queue

color = {
    '(0, 0, 0)': '0',
    '(255, 255, 255)': '1',
    '(170, 170, 170)': '2',
    '(85, 85, 85)': '3',
    '(254, 211, 199)': '4',
    '(255, 196, 206)': '5',
    '(250, 172, 142)': '6',
    '(255, 139, 131)': '7',
    '(244, 67, 54)': '8',
    '(233, 30, 99)': '9',
    '(226, 102, 158)': 'a',
    '(156, 39, 176)': 'b',
    '(103, 58, 183)': 'c',
    '(63, 81, 181)': 'd',
    '(0, 70, 112)': 'e',
    '(5, 113, 151)': 'f',
    '(33, 150, 243)': 'g',
    '(0, 188, 212)': 'h',
    '(59, 229, 219)': 'i',
    '(151, 253, 220)': 'j',
    '(22, 115, 0)': 'k',
    '(55, 169, 60)': 'l',
    '(137, 230, 66)': 'm',
    '(215, 255, 7)': 'n',
    '(255, 246, 209)': 'o',
    '(248, 203, 140)': 'p',
    '(255, 235, 59)': 'q',
    '(255, 193, 7)': 'r',
    '(255, 152, 0)': 's',
    '(255, 87, 34)': 't',
    '(184, 63, 39)': 'u',
    '(121, 85, 72)': 'v'
}

# Get gif map info
im_array = ndimage.imread("earthman.bmp", mode="RGB")
len_row = len(im_array)
len_col = len(im_array[0])

print(len_row, len_col)

arr = [[0 for i in range(len_col)] for i in range(len_row)]

def main():
    for i in range(0, len_row):
        for j in range(0, len_col):
            arr[i][j] = color[str(tuple(im_array[i][j]))]
    print(arr)
    
if __name__ == "__main__":
    main()
