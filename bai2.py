# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:56:00 2024

@author: USER
"""

a = float(input("Nhập số nguyên thứ nhất: "))
b = float(input("Nhập số nguyên thứ hai: "))
tong = a + b
hieu = a - b
tich = a * b
thuong_2_chu_so = round(a / b, 2)
thuong_3_chu_so = round(a / b, 3)
print("Tổng của 2 số là:", tong)
print("Hiệu của 2 số là:", hieu)
print("Tích của 2 số là:", tich)
print("Thương của 2 số (làm tròn 2 chữ số):", thuong_2_chu_so)
print("Thương của 2 số (làm tròn 3 chữ số):", thuong_3_chu_so)
