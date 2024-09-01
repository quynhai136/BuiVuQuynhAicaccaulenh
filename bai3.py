# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:58:01 2024

@author: quynh ai
"""

a = float(input("Nhập số nguyên dương thứ nhất: "))
b = float(input("Nhập số nguyên dương thứ hai: "))
phan_nguyen = a // b
phan_du = a % b
print("Phần nguyên của phép chia", a, "cho", b, "là:", phan_nguyen)
print("Phần dư của phép chia", a, "cho", b, "là:", phan_du)
