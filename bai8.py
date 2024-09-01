# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:28:49 2024

@author: quynh ai
"""

can_nang = float(input("Nhập cân nặng của bạn (kg): "))
chieu_cao = float(input("Nhập chiều cao của bạn (m): "))
BMI = can_nang / (chieu_cao ** 2)
print("Chỉ số BMI của bạn là:", BMI)
