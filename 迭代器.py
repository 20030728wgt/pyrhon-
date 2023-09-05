l = {'key': 1, 'key2': 2, 'key3': 3}
res = l.__iter__()
while 1:
    try:
        print(l[res.__next__()])
    except StopIteration:
        break


