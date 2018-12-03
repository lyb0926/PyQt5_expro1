# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 13:47
# @Author  : Lyb
# @File    : model_Pyqt.py


class model():
    num1 = 0
    num2 = 0
    flag: str = ""

    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.flag = ''

    def set_num1(self, num):
        self.num1 = num

    def set_num2(self, num):
        self.num2 = num

    def set_flag(self, flag: object) -> object:
        self.flag = flag

    def doExpro(self):
        if self.flag is "+":
            result = self.num1 + self.num2
            return str(result)
        elif self.flag is "-":
            result = self.num1 - self.num2
            return str(result)
        elif self.flag is "*":
            result = self.num1 * self.num2
            return str(result)
        elif self.flag is "/":
            if self.num2 == 0:
                result = "ERROR"
                return str(result)
            result = self.num1 / self.num2
            return str(result)


# mod = model()
# mod.set_num1(1)
# mod.set_num2(3)
# mod.set_flag("+")
# result = mod.doExpro()
# print(result)
