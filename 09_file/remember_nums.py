# 10-11
import json

num = input("Enter your favorite number: ")

filename = '9_file\\numbers.json'
with open(filename,'w') as fileObj:
    json.dump(num, fileObj)