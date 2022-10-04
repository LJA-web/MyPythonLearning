# 10-11
import json

filename = '9_file\\numbers.json'
with open(filename) as fileObj:
    num = json.load(fileObj)
    print("I know your favorite number! It's " + num)