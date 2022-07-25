# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir","Manisa"]
# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])

for x in sehirler: #tüm sehirler içindeki dataları almaya yarar
    if x != "Manisa": #!= dersek tam tersini verir cevap olarak manisayı almaz yani
        print(x + " İçin Kısaltma = " + x[0:3]) #burada için kısaltma eki ekledik
        print("*"*20)
