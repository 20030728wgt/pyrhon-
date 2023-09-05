with open(r'/wgt.txt', mode='rt', encoding='utf-8') as f:
    res = f.read()
    lists = list(res)
    lists.insert(1, '我')
    new_wgt = ''.join(lists)
    print(new_wgt)
