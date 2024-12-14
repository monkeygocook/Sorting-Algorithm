# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 03:16:51 2024

@author: monkeygorun
"""

import time
import main_def as md
import sys
sys.setrecursionlimit(10**6)


# อ่านข้อมูลจากไฟล์
with open('outputT.txt', 'r') as fin:
    all_records = []

    for record in fin:
        # ลบช่องว่างด้านข้างของบรรทัด
        record = record.strip()

        # ตรวจสอบว่าบรรทัดว่างหรือไม่
        if not record:
            continue

        # แยกข้อมูลในแต่ละบรรทัด
        data = record.split()

        # จัดเก็บข้อมูลทั้งหมดในรูปแบบ string
        new_record = ' '.join(data)

        # เพิ่มข้อมูลในรายการ all_records
        all_records.append(new_record)
        
if __name__ == '__main__':
    bu = list(all_records) 
    In = list(all_records)
    se = list(all_records)
    me = list(all_records)
    qu = list(all_records)
    
    start_b = time.time()    
    md.bubblesort(bu)
    end_b = time.time()
    b = (end_b-start_b) * 10**3
    print("bubblesort ใช้เวลาทั้งหมด", b ,"มิลลิวินาที")
    time_bu = b
    print()
    
    start_i = time.time()    
    md.InsertionSort(In)
    end_i = time.time()
    i = (end_i-start_i) * 10**3
    print("insertionSort ใช้เวลาทั้งหมด", i ,"มิลลิวินาที")
    time_in = i
    print()
    
    start_s = time.time()    
    md.SelectionSort(se)
    end_s = time.time()
    s = (end_s-start_s) * 10**3
    print("SelectionSort ใช้เวลาทั้งหมด", s ,"มิลลิวินาที")
    time_se = s
    print()
    
    start_m = time.time()    
    md.MergeSort(me)
    end_m = time.time()
    m = (end_m-start_m) * 10**3
    print("MergeSort ใช้เวลาทั้งหมด", m ,"มิลลิวินาที")
    time_me = m
    print()
    
    start_q = time.time()    
    md.QuickSort(qu,0 ,len(qu)-1)
    end_q = time.time()
    q = (end_q-start_q) * 10**3
    print("QuickSort ใช้เวลาทั้งหมด", q ,"มิลลิวินาที")
    time_qu = q
    print()
    
    total_time = [time_bu, time_in, time_se, time_me, time_qu]

    md.bubblesortLOW(total_time)
    
    print(total_time[0])
    a = input("กรุณาใส่ชื่ออัลกอลึมทึม เช็คได้จากข้างบน ใส่,ก่อนใส่ชื่อด้วย = ")
    total_time[0] = f"{total_time[0]}{a}"
    print(total_time[1])
    b = input("กรุณาใส่ชื่ออัลกอลึมทึม เช็คได้จากข้างบน ใส่,ก่อนใส่ชื่อด้วย = ")
    total_time[1] = f"{total_time[1]}{b}"
    print(total_time[2])
    c = input("กรุณาใส่ชื่ออัลกอลึมทึม เช็คได้จากข้างบน ใส่,ก่อนใส่ชื่อด้วย = ")
    total_time[2] = f"{total_time[2]}{c}"
    print(total_time[3])
    d = input("กรุณาใส่ชื่ออัลกอลึมทึม เช็คได้จากข้างบน ใส่,ก่อนใส่ชื่อด้วย = ")
    total_time[3] = f"{total_time[3]}{d}"
    print(total_time[4])
    e = input("กรุณาใส่ชื่ออัลกอลึมทึม เช็คได้จากข้างบน ใส่,ก่อนใส่ชื่อด้วย = ")
    total_time[4] = f"{total_time[4]}{e}"
    
    print("เรียงเวลาที่ Algorithm ใช้เวลาในการทำจาก น้อยไปมาก ", total_time)
    print()
    print("ใช้เวลามากที่สุด", total_time[-1])
    print()
    print("ใช้เวลาน้อยที่สุด", total_time[0])
    print()
    print("ใช้เวลากลาง ๆ ", total_time[2])