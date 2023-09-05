l = [('小白', 5), ('小红', 6), ('小蓝', 8), ('黑黑', 9), ('白白', 5)]
m = {k: v for k, v in l if not k.startswith('小')}
print(m)
