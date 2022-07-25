sozluk = {
    "book" : "kitap",
    "table" : "masa",
    "computer" : "bilgisayar",
    "mouse" : "fare"
    } #bu şekil kıvrık parantez ile kütüphaneler oluşturabiliz.




sozluk["pencil"] = "kalem" #ekstra kütüphaneye ekleme yapılması için
# print(sozluk)

del(sozluk["book"]) #bu şekilde remove demeden del ile detay vererek silme yapabiliyoruz.
print(sozluk)

print(len(sozluk))
