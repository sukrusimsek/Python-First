# -*- coding: utf-8 -*-
#substring
message = "Hello World"

print(message[2:5])

newMessage = message[:5]
print(newMessage)
#len
print(len(message)) #o satırda kaç karakter olduğunu öğrenmek için

newMessage2 = message[len(message)-1:len(message)]#son karakteri bulmak için
print(newMessage2)#bulunan karakteri yazdırma

#Lower Upper
print(message.upper())
print(message.lower())

#Replace
print(message.replace("o","ı"))

#Split and Strip
info = "Şükrü;Şimşek;23;Manisa"
print(info.split())
print(info.split(";")[1]) # ; koyarak metinde onlarla ayırıyor ayrıca 1 de ayrılanların 1. metnini veriyor
print("Adı = " + info.split(";")[0]) #adıkısmını ekleyerek konsol çıktısında adı : şükrü gibi çıktı aldık

#Input

ad = input("Adınız?")
sayi1 = input("Sayı 1 =? ")
sayi1 = input("Sayı 2 =? ")
print(sayi1 + sayi2)