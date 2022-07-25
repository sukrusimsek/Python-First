# -*- coding: utf-8 -*-

ogrenciler = ["Şükrü","Yavuz","Fatih","Mustafa"]
ogrenciler[0] = "Şimşek"
ogrenciler.append("Ahmet") #ekleme konutu listeye yeni üye eklerken falan
ogrenciler.remove("Yavuz") #üye kaldırma komutu listeden kolayca silmeye yarar
print(ogrenciler)

sehirler = list(("Ankara","İstanbul","Manisa","Bursa","Eskişehir"))
print(sehirler)
print(len(sehirler))


# print(sehirler.clear())
print("Manisa Şehri Sayısı = " + str(sehirler.count("Manisa"))) #str deme nedenimiz string olması gerekiyor
print("Ankara indexi = " + str(sehirler.index("Ankara"))) #index komutu aranan şeyi ilk bulduğu yeri söyler
sehirler.pop(3)
sehirler.insert(0, "Manisa") #insert komutu ile yer değiştirme yapılır örnekteki gibi manisayı 0. sıraya getirme gibi
print(sehirler.reverse()) #komple tüm dizini terse çevirme komutudur
print(sehirler)

sehirler3 = sehirler.copy() # bu ise sehirler i sehirler3 e kopyalama anlamına gelmekte

sehirler2 = sehirler #bu tümünü eşitleme anlamına geliyor
sehirler2[0] = "İzmir"

print(sehirler)
# print(sehirler2)
print(sehirler3)

sehirler.extend(sehirler3) #birleştirme komutu extend
sehirler.sort() # alfabetik veya sayıya göre sıralama komutudur
sehirler.reverse()
print(sehirler)

