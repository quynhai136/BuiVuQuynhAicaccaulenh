# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 02:09:14 2024

@author: USER
"""

so_xe = input("Nhập số xe (gồm 4 chữ số): ")
so_nut = 0
for chu_so in so_xe:
    if chu_so in '1470':
        so_nut += 1
print("Số xe của bạn được", so_nut, "nút")
