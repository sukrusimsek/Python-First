# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir","Manisa"]
# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])

for x in sehirler: 
    if x == "İzmir": 
        break #kırma işlemidir ve sonrasındaki herşeyi durdurur iptal eder
        # continue #döngüde sadece belirtilen yeri okumuyor ve tek bir datayı silip sistemin çalışmasını istersek kullanıyoruz
    print(x + " İçin Kısaltma = " + x[0:3]) 
    print("*"*20)