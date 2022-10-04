# 10-12
import json

def get_num():
    """如果存在这个数字，就获取"""
    filename = '9_file\\numbers.json'
    try:
        with open(filename) as fileObj:
            num = json.load(fileObj)
    except FileNotFoundError:
        return None
    else:
        return num

def show_num():
    """提示最喜欢的数字"""
    num = get_num()
    if num:
        print("I know your favorite number! It's " + num)
    else:
        filename = '9_file\\numbers.json'
        num = input("Enter your favorite number: ")
        with open(filename,'w') as fileObj:
            json.dump(num,fileObj)
            print("I get it! It's " + num + "!")


show_num()