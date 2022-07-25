# -*- coding: utf-8 -*-

sehirler = ["Ankara","İstanbul","İzmir","Manisa"]
# print(sehirler[0])
# print(sehirler[1])
# print(sehirler[2])

#%% For intro #bu bölme işlemi satırları ayrı ayrı çalıştırıp kontrol etmeye yardımcı olmaktadır.
for x in sehirler: 
    if x == "İzmir": 
        continue #döngüde sadece belirtilen yeri okumuyor ve tek bir datayı silip sistemin çalışmasını istersek kullanıyoruz
    print(x + " İçin Kısaltma = " + x[0:3]) 
    print("*"*20)
    
#%% For range
for x in range(1,100,2):
    print(x) # Eğer saymayı 1 den başlatmak istersek ekstra yazdırma satırına +1 eklemeliyiz.
    