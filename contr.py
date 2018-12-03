# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:58
# @Author  : Lyb
# @File    : contr.py

from expro_ui import *
from model_Pyqt import model


class MyWidgets(Ui_Dialog):
    tmp = ""
    md = model()

    def setupUi(self, Dialog):
        super().setupUi(Dialog)
        self.btn_0.clicked.connect(self.getnum0)
        self.btn_1.clicked.connect(self.getnum1)
        self.btn_2.clicked.connect(self.getnum2)
        self.btn_3.clicked.connect(self.getnum3)
        self.btn_4.clicked.connect(self.getnum4)
        self.btn_5.clicked.connect(self.getnum5)
        self.btn_6.clicked.connect(self.getnum6)
        self.btn_7.clicked.connect(self.getnum7)
        self.btn_8.clicked.connect(self.getnum8)
        self.btn_9.clicked.connect(self.getnum9)
        self.btn_plush.clicked.connect(self.getplus)
        self.btn_sub.clicked.connect(self.getsub)
        self.btn_mul.clicked.connect(self.getmul)
        self.btn_div.clicked.connect(self.getdiv)
        self.btn_eq.clicked.connect(self.geteq)
        self.btn_clean.clicked.connect(self.getclean)

    def getnum0(self):
        if self.tmp != "":
            self.tmp += self.btn_0.text()
            self.lbl_display.setText(self.tmp)

    def getnum1(self):
        self.tmp += self.btn_1.text()
        self.lbl_display.setText(self.tmp)

    def getnum1(self):
        self.tmp += self.btn_1.text()
        self.lbl_display.setText(self.tmp)

    def getnum1(self):
        self.tmp += self.btn_1.text()
        self.lbl_display.setText(self.tmp)

    def getnum2(self):
        self.tmp += self.btn_2.text()
        self.lbl_display.setText(self.tmp)

    def getnum3(self):
        self.tmp += self.btn_3.text()
        self.lbl_display.setText(self.tmp)

    def getnum4(self):
        self.tmp += self.btn_4.text()
        self.lbl_display.setText(self.tmp)

    def getnum5(self):
        self.tmp += self.btn_5.text()
        self.lbl_display.setText(self.tmp)

    def getnum6(self):
        self.tmp += self.btn_6.text()
        self.lbl_display.setText(self.tmp)

    def getnum7(self):
        self.tmp += self.btn_7.text()
        self.lbl_display.setText(self.tmp)

    def getnum8(self):
        self.tmp += self.btn_8.text()
        self.lbl_display.setText(self.tmp)

    def getnum9(self):
        self.tmp += self.btn_9.text()
        self.lbl_display.setText(self.tmp)

    def getplus(self):
        num1: int = int(self.tmp)
        self.md.set_num1(num1)
        self.tmp = ""
        self.md.set_flag("+")

    def getsub(self):
        num1 = int(self.tmp)
        self.md.set_num1(num1)
        self.tmp = ""
        self.md.set_flag("-")

    def getmul(self):
        num1 = int(self.tmp)
        self.md.set_num1(num1)
        self.tmp = ""
        self.md.set_flag("*")

    def getdiv(self):
        num1: int = int(self.tmp)
        self.md.set_num1(num1)
        self.tmp = ""
        self.md.set_flag("/")

    def geteq(self):
        num2 = int(self.tmp)
        self.md.set_num2(num2)
        result = str(self.md.doExpro())
        self.lbl_display.setText(result)

    def getclean(self):
        self.tmp = ""
        self.lbl_display.setText('0')


