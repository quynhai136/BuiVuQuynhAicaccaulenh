# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:59:38 2024

@author: quynh ai
"""

N = float(input("Nhập số nguyên dương N có 2 chữ số: "))
hang_chuc = N // 10
hang_don_vi = N % 10
tong_chu_so = hang_chuc + hang_don_vi
print("Tổng các chữ số của", N, "là:", tong_chu_so)
