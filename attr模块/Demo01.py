from abc import ABC, abstractmethod

import attr
from loguru import logger


class Person(ABC):  # ABC 抽象类 Abstract Base Classes 简称 ABC 抽象基类

    @abstractmethod  # 抽象方法
    def method01(self):
        pass


@attr.s(auto_attribs=True)
class Student(Person):
    id: int
    age: int
    name: str
    gender: str

    def method01(self):
        logger.info("this is student implements")

    def __attrs_post_init__(self):
        self.gender = self.gender.upper()
        logger.info("after __init__ method is called")


dct = {"id": 1, "age": 2, "name": "<NAME>", "gender": "M"}  # noqa: E501
s1 = Student(**dct)
logger.info(s1)
