# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 00:36:22 2024

@author: quynh ai
"""

# Nhập lần lượt ngày, tháng, năm sinh
ngay, thang, nam = input("Nhập ngày, tháng, năm sinh (cách nhau bởi dấu cách): ").split()

# a) Xuất ra theo định dạng Ngày/tháng/năm
print(f"{ngay}/{thang}/{nam}")

# b) Xuất ra theo định dạng Ngày/tháng/năm với năm chỉ có 2 chữ số
print(f"{ngay}/{thang}/{nam[-2:]}")

# c) Xuất ra theo định dạng Năm/tháng/ngày
print(f"{nam}/{thang}/{ngay}")
