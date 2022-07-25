# -*- coding: utf-8 -*-

print("*"*20)
print("HOŞGELDİZ.")
print("*"*20)
print("\n")
for i in range(0,3,1):
  print("*"*20)
  sayi1 = int(input("1.sayi: "))
  sayi2 = int(input("2.sayi: "))
  sayi3 = int(input("3.sayi: "))
  print("*"*20)
  if sayi1>sayi2 and sayi1>sayi3:
    print("büyük olan sayı",sayi1,"'dir'")
    if sayi2>sayi3:
      print("En küçük sayı",sayi3,"'dir'")
    else:
      print("En küçük sayı",sayi2,"'dir'")
    
  elif sayi2>sayi1 and sayi2>sayi3:
    print("büyük olan sayı",sayi2,"'dir'")
    if sayi3>sayi1:
      print("En küçük sayı",sayi1,"'dir'")
    else:
      print("En küçük sayı",sayi3,"'dir'")
    
 
  elif sayi3>sayi1 and sayi3>sayi2:
    print("büyük olan sayı",sayi3,"'dir'")
    if sayi1>sayi2:
      print("En küçük sayı",sayi2,"'dir'")
    else:
      print("En küçük sayı",sayi1,"'dir'")
  else:
    print("*"*20)
    print("SATILAR EŞİT VEYA YANLIŞ TUŞLAMA")
    print("*"*20)
print("*"*20)
print("\nBİZİ TERCİH ETTĞİNİZ İÇİN TEŞEKKÜRLER.")
print("*"*20)