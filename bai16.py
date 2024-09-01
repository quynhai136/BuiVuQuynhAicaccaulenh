# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 01:04:16 2024

@author: quynh ai
"""

gio = float(input("Nhập số giờ: "))
phut = float(input("Nhập số phút: "))
giay = float(input("Nhập số giây: "))
tong_giay = gio * 3600 + phut * 60 + giay
print("Tổng số giây là:", tong_giay)
    