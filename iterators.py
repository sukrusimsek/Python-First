# -*- coding: utf-8 -*-

sehirler = ["Manisa","Ankara","İstanbul","İzmir"]

iteratorum = iter(sehirler) #iterator bizim for da kullandığımız gibi kendimize komutlar hazırladığımız fonksiyonlar oluşturmaya yarar
#Pek kullanılmaz

print(next(iteratorum))
print(next(iteratorum))
print(next(iteratorum))

for sehir in sehirler:
    print(sehir)