
import os


def stat_size(path):
    size = 0
    for item in os.listdir(path):
        next_path = os.path.join(path, item)
        if os.path.isdir(next_path):
            size += stat_size(next_path)  # 文件夹则递归调用
        else:
            size += os.path.getsize(next_path)
    return size


if __name__ == '__main__':
    res = stat_size(r'/文件处理')
    print(res)
