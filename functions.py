# -*- coding: utf-8 -*-

#%%
sehir = "Ankara"

print(sehir.upper())
print(sehir.endswith("q")) #endswith fonksiyonu datanın sonundaki harf veya rakam uyuyor mu uymuyor mu bakar True/False veri

#%%
def selamınAleyküm(isim = "Şu hale bak"): #Dostum yazısı default bir yazı oluyor biz altta isim vermezsek SA BABA Dostum der
    print("Merhabalar " + isim) # burada yapılan def komutu ile bir metini başka yerlerde de yazdırmak istersek direk
    # metine altta gibi selamınAleyküm() dediğimizde def de verdiğimiz komut ne ise orada da uygulamasını yapar
    
selamınAleyküm("Şükrü")
selamınAleyküm("Fatih")
selamınAleyküm("Kerem")
selamınAleyküm("Abdurrazak")
selamınAleyküm()

def selamınAleyküm2(isim = "Ziyaretçi", soyIsim =" Abuziddin"): 
    print("Merhabalar " + isim +" " +soyIsim)
    
selamınAleyküm2()
selamınAleyküm2("Şükrü", "Şimşek")


#%%
def dikUcgenAlanHesaplamasi(a,b):
    return a*b/2 #return bir dönüş anlamına gelmektedir. bir değerlerin size uygulamasını yapmanıza yarar.

alan = dikUcgenAlanHesaplamasi(5, 8)
print(alan)

#%%
dikUcgenAlaniHesapla2 = lambda a,b : a*b/2
print(dikUcgenAlaniHesapla2(7, 8))

print(type(dikUcgenAlaniHesapla2))

x = dikUcgenAlaniHesapla2

print(x(9,185))
