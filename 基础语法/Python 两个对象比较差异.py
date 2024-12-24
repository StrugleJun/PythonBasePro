class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city


def compare_objects(obj1, obj2):
    differences = {}

    # 获取对象的所有属性
    attrs1 = vars(obj1)
    attrs2 = vars(obj2)

    # 遍历属性并比较
    for attr in attrs1.keys():
        if attrs1[attr] != attrs2.get(attr):
            differences[attr] = {
                'obj1': attrs1[attr],
                'obj2': attrs2.get(attr)
            }

    return differences


# 示例使用
person1 = Person(name='Alice', age=30, city='New York')
person2 = Person(name='Alice', age=25, city='Los Angeles')

diff = compare_objects(person1, person2)
print(diff)
