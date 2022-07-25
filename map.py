# -*- coding: utf-8 -*-

sayilar = [1,2,3,4,5]

sayilarKareli = []

for sayi in sayilar:
    sayilarKareli.append(sayi*sayi)

print(sayilarKareli) #Bu tipte halletme yolu for döngüsü ile komple diziye baktırıp sonrasında karesini istediğimiz için ikisini birbiri 
# ile çarptırıp sonucu elde ettik.

#%% Mapping yöntemi

sayilar = [1,2,3,4,5]

sayilarKareli = list(map(lambda sayi: sayi**2,sayilar)) #Bu tip yazı üssü anlamına gelmektedir. sayi*sayi da yapabilirdik

print(sayilarKareli)

#%% def komutu ile karesini alma

def karesi(sayi):
    return sayi*sayi

sayilar = range(1,10)

map(karesi,sayilar)

print(karesi(5))

#%% Filtreleme komutu

sayilar = [1,2,3,4,5]

sayilarFiltreli = list(filter(lambda sayi : sayi>3,sayilar))

print(sayilarFiltreli)

#%% Reducu Komutu Kümülatif işlemler yapıp niahi bir sonuç elde edilmeye çalışılır

sayilar = [1,2,3,4,5]

from functools import reduce #Bunu yapma nedenimiz bazen fonksiyonlar gelmeyebilir kütüphanelerinden import edilmesi gerekir
sayilarFaktoriyel = reduce(lambda x,y:x*y,sayilar) 
print(sayilarFaktoriyel)
