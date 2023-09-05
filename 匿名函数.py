l = {'小白': 2000, '小黑': 2500, '小蓝': 6000, '小梁': 5000}
res = max(l, key=lambda k: l[k])
print(res)

m = [(2, 1), (3, 5), (5, 4), (6, 3)]
m.sort(key=lambda item: item[0])
print(m)
