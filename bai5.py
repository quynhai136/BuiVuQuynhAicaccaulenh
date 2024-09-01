# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 01:02:32 2024

@author: quynh ai
"""

thoi_gian = input("Nhập thời gian theo định dạng hh:mm:ss: ")
gio, phut, giay = map(int, thoi_gian.split(':'))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:", tong_giay)
