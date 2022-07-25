# -*- coding: utf-8 -*-

import sys #Bir modüldür hatanın detayını verir

liste = [7,'Şükrü',0,1071,"6"]
#for tüm datayı rahatlıkla gezmeye kontrol etmeye yarar
for x in liste:
    try:
        print("Sayı : " + str(x))
        sonuc = 1/int(x)
        print("Sonuc : " + str(sonuc))
    except ValueError:
        print(str(x) + " Bir Sayı Değil")
    except ZeroDivisionError:
        print(str(x) + "Sayı Tam Sayı Değil")
    except:
        print(str(x) + "Hesaplamadı")
        print("Sistem Diyor ki =" + str(sys.exc_info()[0])) #exc_indo except in info yani detay veren modül halidir 
    finally:
        print("İşlemler Bitti") #try veya except ten sonra kullanılır. 