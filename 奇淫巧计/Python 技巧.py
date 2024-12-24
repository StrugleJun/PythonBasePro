# 一、12个高级字典使用技巧 : https://mp.weixin.qq.com/s/hZXSn2QYNBMOOCIlxZJi6Q
# 1.1 字典推导式是创建字典的优雅方式，特别适合从列表或其他字典中快速构建新字典。
# 从一对列表创建字典
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dct = {k: v for k, v in zip(keys, values)}
print(dct)  # {'a': 1, 'b': 2, 'c': 3}
print(type(dct))  # <class 'dict'>

# 1.2 get()方法避免KeyError
"""
Traceback (most recent call last):
  File "E:/PythonProject/PythonBasic/Python 技巧.py", line 12, in <module>
    v = dct["e"]
        ~~~^^^^^
KeyError: 'e'

Process finished with exit code 1
"""
# v = dct["e"]
# print(v)

v = dct.get("e")
print(v)  # None

v = dct.get("e", "defaultValue")
print(v)  # defaultValue

# 1.3: 利用setdefault()添加键值对

dct = {}
dct.setdefault("age", [])
print(dct.get("age"))
