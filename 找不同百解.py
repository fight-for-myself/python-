Localfile = open('/Users/dugutong/Desktop/Main.txt', 'r')
#存放原始数据
key = input('请输入要查找的字：')

count = 0
local = []
location = ''
key = []
place = 0

Local = Localfile.readlines()
local = ''.join(Local)

for i in range(len(local)):
    if local[i] == key:
        location = location + str(i) + '  '
        flag = True
        key.append(local[i])
        count = count + 1
        place = place + 1


if count == 0:
    print('未找到')
else:
    print('发现字母：%s.\n共发现：%d 个.\n位置为：%s' % (key, count, location))

Localfile.close()
