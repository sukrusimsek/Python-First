# -*- coding: utf-8 -*-

sayi = int(input("Faktöriyel Hesaplama için Sayı Giriniz : "))

faktoriyel = 1

if sayi<0:
  print("Negatif Sayı Girdiniz !!")

elif sayi == 0:
  print("Sonuç : 1")

else:
  for i in range(1,sayi+1):
    faktoriyel = faktoriyel * i
  print("Sonuç : " ,faktoriyel)
