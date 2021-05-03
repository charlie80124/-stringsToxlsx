import openpyxl
import os
from pathlib import Path
import xlsxwriter

def removeSpecialCharacter(text, special):
    result = ''
    isSet = False
    startIdx = 0
    endIdx = 0 

    for i in range(0, len(text)):
        char = text[i]
        if char == '"':
            if isSet == False: 
                startIdx = i+1
                isSet = True
                continue
            else:
                endIdx = i 
    
    result = text[startIdx:endIdx]
    return result


path = '.strings'
xlsxPath = '.xlsx'

file = open(path, 'r')
excel = xlsxwriter.Workbook(xlsxPath)
sheet = excel.add_worksheet()
dict = {}

lines = file.readlines()
print(len(lines))
for line in lines:
    arr = line.split('=')
    if len(arr) == 2:
        key = arr[0]
        key = removeSpecialCharacter(key, '"')

        value = arr[1]
        value = removeSpecialCharacter(value, '"')
        dict[key] = value

    else:
        print(line)


#寫入xlsx
idx = 1 
print(len(dict))
for k,v in dict.items(): 

    sheet.write(idx, 0, k)
    sheet.write(idx, 1, v)
    idx += 1 
excel.close()
file.close()

