import json

dic_person = {'name': '小白', 'salary': 2330, 'age': 15}
# json_res = json.dumps(dic_person, ensure_ascii=False)
# with open(r'E:\桌面\wgt python\文件处理\wgt.txt', mode='wt', encoding='utf-8') as f:
#     f.write(json_res)
# with open(r'E:\桌面\wgt python\文件处理\wgt.txt', mode='rt', encoding='utf-8') as f:
#     json_rest = f.read()
#     json_new = json.loads(json_rest)
#     print(json_new)
# 第二种方式
with open(r'E:\桌面\wgt python\文件处理\wgt1.txt', mode='wt', encoding='utf-8') as f:
    json.dump(dic_person, f, ensure_ascii=False)
with open(r'E:\桌面\wgt python\文件处理\wgt1.txt', mode='rt', encoding='utf-8') as f:
    json_res = json.load(f)
    print(json_res)

# pickle的使用和json的使用方式一样只是pickle可以兼容python的所有数据格式(只能用b模式)
