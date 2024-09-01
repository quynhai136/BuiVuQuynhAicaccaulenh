# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:59:11 2024

@author: quynh ai
"""

import math

# Nhập giá trị của a và b từ người dùng
a = float(input("Nhập giá trị của a: "))
b = float(input("Nhập giá trị của b: "))

# Tính toán các phần tử trong biểu thức
tu_so = (a + b) / (math.pow(math.sqrt(a) + math.sqrt(b), 3) - math.pow(math.pow(a*b, 1/3), 3))
mau_so = math.pow(math.pow(a, 1/3) - math.pow(b, 1/3), 2)

# Tính giá trị của biểu thức
ket_qua = tu_so / mau_so

# In kết quả ra màn hình
print("Kết quả của biểu thức là:", ket_qua)

