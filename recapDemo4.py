# -*- coding: utf-8 -*-

ogrenciler = ["Şükrü","Fatih","Taha","Kerem","Aslı"]

fileToAppend = open("ogrenciler.txt","a")

for ogrenci in ogrenciler:
    fileToAppend.write(ogrenci)
    fileToAppend.write("\n")
    
    
fileToAppend.close()

import os
os.remove("ogrenciler.txt") #spyder da srun var remove komutu aç kapa yapmadan çalışmıyor