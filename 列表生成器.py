
# 列表生成器： [结果 for item in 可迭代对象 if 条件](结果可以放列表表达式会生成好几个列表)
l = ['小白', '小红', '小蓝', '黑黑', '白白']
new_l = [name for name in l if name.startswith('小')]
print(new_l)
