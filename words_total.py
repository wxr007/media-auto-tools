# coding=utf-8
import jieba

def test():
    sentence = '今天天气不错适合出去玩'
    print("精准模式",jieba.lcut(sentence))
    print('全模式',jieba.lcut(sentence,cut_all=True))
    print('搜索引擎模式',jieba.lcut_for_search(sentence))

def test_read_file():
    txt = open('三国演义.txt','r',encoding='utf-8').read()
    wordsls = jieba.lcut(txt)
    wcdict={}
    for word in wordsls:
        if len(word)==1:
            continue
        else:
            wcdict[word]=wcdict.get(word,0)+1
    #word在wcdict中没有找到对应的词语，则返回0
    wcls=list(wcdict.items())#键值对变成列表
    wcls.sort(key=lambda x:x[1],reverse=True)
    for i in range(25):
        print(wcls[i])

#test()
test_read_file()