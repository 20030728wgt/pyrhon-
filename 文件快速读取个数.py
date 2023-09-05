with open(r'E:\桌面\wgt python\new wenjian\wen.txt', mode='rt', encoding='utf-8') as f:
    res = sum(len(line) for line in f)
    print(res)
