# -*- coding: utf-8 -try: # kodları except için dener çalışmazsa except te verilen kod çalışır
try: # kodları except için dener çalışmazsa except te verilen kod çalışır
    sayi = int(input("Sayı Giriniz"))
except ValueError: #Burada verildiği gibi hata isimleri yazılırsa ona göre hataları ayıklama yapabilmektedir.
  print("Tip Uyuşmazlığı : Lütfen Sayı Giriniz")
except ZeroDivisionError:
  print("Payda Sıfır Olamaz")
except: #Çalışmazsa bunu yap demek için
  print("Bir hata oluştu")
#ikisi bir arada asla çalışmaz hataları bulmaya yarar
except (ValueError,ZeroDivisionError):#Eğer ki hatadan tam emin değil isek 2 farklı hatayı kontrol ettirebiliriz.O da bu şekilde olmakta.