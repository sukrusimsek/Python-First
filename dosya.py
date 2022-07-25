# -*- coding: utf-8 -*-

# f = open("musteriler2.txt","x") 
                               #f file demek open dosya açmak demek 
                               #w write dan yeni dosya oluşturmaya yarar 
                               #a append komutu ise dosyayı okumaktan ziyade yazmayada yarar append den gelmekte ekleme anlanımda
                               #x create komutu direk dosyayı oluştur demektir. bu isimde dosya varsa oluşturmaz
                               #r read komutu okuma en sık kullanılandır genellikle okumak gerekeceği için r işe yaramaktadır

f = open("musteriler2.txt")                  
# print(f.read())              #Tekrar özet geçmek gerekirse read komutu tüm dosyayı okur readline ise satır satır okur

# print(f.readline()) # readline komutu satır satır okumaya yarar ilk readline ilk satır sonraki 2.satır anlamına gelir

for l in f:
    print(l)
    print("*"*20)
    
f.close() #dosyayı kapatmak için yapılır.

fileToAppend = open("ogrenciler.txt")
fileToAppend.write("\n")
fileToAppend.write("Sukru")
fileToAppend.close()

#%%
import os

if os.path.exists("ogrenciler.txt"): #Burada Dosyanın olup olmadığını kontrol ettik
    os.remove("ogrenciler.txt") #Burada ise eğer varsa sil dedik import os komutları dosya kontrol komutlarıdır
    
else:
    print("Dosya Yok")
    
os.rmdir("empty") #Burada da direk dosya silme işlemi için kullanılan rmdir komutunu gördük