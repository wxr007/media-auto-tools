# coding=utf-8

def chinese_to_pinyin(x):
    y = ''
    dic = {}
    with open("unicode_py.txt") as f:
        for i in f.readlines():
            dic[i.split()[0]] = i.split()[1]
    for w in x:
        if w == '\n':
            continue
        i = str(w.encode('unicode_escape'))[-5:-1].upper()
        try:
            y += dic[i] + ' '
        except:
            y += w #非法字符我们用XXXX代替
    return y

with open(file="文字转拼音.txt",mode='r',encoding='utf-8') as cf:
    for i in cf.readlines():
        pinyin = chinese_to_pinyin(i)
        print(pinyin)

# pinyin =  chinese_to_pinyin("秋水共长天一色")
# print(pinyin)