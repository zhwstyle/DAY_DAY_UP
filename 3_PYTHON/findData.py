# coding:utf-8

import os
from glob import glob

# coding:utf-8


"""
获取当前路径下所有内容
判断每个内容的类型（文件夹还是文件）
若是文件夹则继续递归查找
"""

path = glob(os.path.join('', '*.java'))
final_result = []


target = os.getcwd()

result = glob(target)
print(result)

def search(path, target):       # 定义 search() 函数，传入 "path" 文件路径， "target" 要查找的目标文件
    result = glob.glob(path)

    for data in result:         # for 循环判断递归查到的内容是文件夹还是文件
        if glob.os.path.isdir(data):    # 若是文件夹，继续将该文件夹的路径传给 search() 函数继续递归查找
            _path = glob.os.path.join(data, '*')
            search(_path, target)
        else:                           # 若是文件，则将该查询到的文件所在路径插入 final_result 空列表
            f = open(data, 'r')         # 利用 open() 函数读取文件，并通过 try...except... 捕获不可读的文件格式（.zip 格式）
            try:
                content = f.read()
                if target in content:
                    final_result.append(data)
            except:
                print('这是不可读文件格式的文件的所在路径：{} '.format(data))
                continue
            finally:
                f.close()
    return final_result


if __name__ == '__main__':
    result = search(path, target='@Path(')
    print(result)




