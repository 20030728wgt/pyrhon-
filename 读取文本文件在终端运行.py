with open(r'E:\桌面\wgt python\new wenjian\wen.txt', mode='rt', encoding='utf-8') as f:
    for line in f:
        m, n = line.strip().split('---')
        print(m)
        print(n)
