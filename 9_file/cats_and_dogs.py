# 10-8 10-9
def findFile(filePath):
    try:
        with open(filePath) as fileObeject:
            names = fileObeject.readlines()
    except FileNotFoundError:
        pass
        # print('Can not find ' + filePath + '!')
    else:        
        for name in names:
            print(name.strip())

findFile('9_file\cats.txt')