# -*- coding: utf-8 -*-

import sqlite3

connection = sqlite3.connect("chinook.db") #bağlantı uzantısı

cursor = connection.execute("select FirstName,LastName from customers where city like '%a%')        
#% Yüzde işareti like komutundan sonra orada a nın çevresinde olma nedeni datanın içinde a olsun gerisi ne olursa olsun demek için 
# içinde a geçen dataları çıkarmak için kullanılmaktadır.

#Burada order by FirstName diyerek dataları alfabetik sıraya dizdik
#First Name sonuna desc alfabetik olan tüm dataları terse çevirir
#y='Oslo' order by FirstName,LastName desc burada yazılan LastName eki ise isimleri aynı varsa soyisme göre sırala demek


for row in cursor: #satırın ingilizcesi row satır satır çekmek istediğimiz için row dedik ama satır diye de yazılabilir
    print("First Name = " +row[0])
    print("Last Name = " +row[1])
    print("*"*20)

#order by genellikle sorgunun sonuna yazılır 
#önce gruplayacak ki ona göre sorgulaması içindir.önüne group by city diyerek şehirleri grupladı ve sonra dedik ki kaçtane 
#neyden ne var bana bunları ver 
#en sonda eklediğimiz having count ise işte burada belli sınırın üstündeki dataları ver diyerek sınıflandırma yapmamıza yarar

                            
#where city diyerek bu şehirden kimler var diye sormuş oluyoruz dikkat tek tırnak verdik karışmaması için
#or veya and kullanarak sıralama tarzı yapabiliriz
#sql deki veriyi buraya getirmeye yarayan python komutu
#sorgu yapmak gerekiyor bunun içinde execute komutunu kullanıyoruz
#select seçme * ile kolon ismi yazma da yer seçmek için customers da müşterileri çekmek istediğimiz için

cursor = connection.execute("select city, count(*) from Customers group by city having count(*)>1 order by count(*) desc")
for row in cursor: #satırın ingilizcesi row satır satır çekmek istediğimiz için row dedik ama satır diye de yazılabilir
    print("City = " +row[0])
    print("Count = " +str(row[1])) #Burada str deme nedenimiz üstte şuan commentlenmemiş olan kodlar ile hangi şehirden 
    print("*"*20)                  #kaç müşteri var ona bakmak istediğimiz için str yani satıları metinleri kontrol ettir
    
connection.close()

#%% Like Komutu
import sqlite3

connection = sqlite3.connect("chinook.db") #bağlantı uzantısı

cursor = connection.execute("select FirstName,LastName from customers where FirstName like 'a%'")        
#% Yüzde işareti like komutundan sonra orada a nın çevresinde olma nedeni datanın içinde a olsun gerisi ne olursa olsun demek için 
# içinde a geçen dataları çıkarmak için kullanılmaktadır. Eğer ki şu şekil yaparsak 'a%' gibi yaparsak a ile başlayan dataları aramaya başlar
# Yüzde işareti a nın sonuna gelirse a ile bitenler diye arar

for row in cursor: #satırın ingilizcesi row satır satır çekmek istediğimiz için row dedik ama satır diye de yazılabilir
    print("First Name = " +row[0])
    print("Last Name = " +row[1])
    print("*"*20)

connection.close() # Bu close u koymazsak hata alırız çünkü sistem dosyayı açıp veriyi alıp bize verip dosyayı kapatması gerekir olurda
# kapatmazsak 

#%% Group By ve Having Komutu
import sqlite3

connection = sqlite3.connect("chinook.db") #bağlantı uzantısı
cursor = connection.execute("select FirstName,LastName from customers where city like '%a%'")

cursor = connection.execute("select city, count(*) from Customers group by city having count(*)>1 order by count(*) desc")
for row in cursor: #satırın ingilizcesi row satır satır çekmek istediğimiz için row dedik ama satır diye de yazılabilir
    print("City = " +row[0])
    print("Count = " +str(row[1])) #Burada str deme nedenimiz üstte şuan commentlenmemiş olan kodlar ile hangi şehirden 
    print("*"*20)                  #kaç müşteri var ona bakmak istediğimiz için str yani satıları metinleri kontrol ettir

connection.close()


#%% SelectOperasyonları
 
import sqlite3
def SelectOperasyonlari():
    connection = sqlite3.connect("chinook.db") #bağlantı uzantısı
    cursor = connection.execute("select FirstName,LastName from customers where FirstName like 'a%'")

    
    for row in cursor: #satırın ingilizcesi row satır satır çekmek istediğimiz için row dedik ama satır diye de yazılabilir
        print("FirstName = " +row[0])
        print("LastName = " +row[1]) 
        print("*"*20)                  

    connection.close()
    
SelectOperasyonlari()

#%% Insert Komutu

def insertCustomer():
    connection = sqlite3.connect("chinook.db") #insert komutu ile listelere eleman eklemeye yarar append den farkı ise istediği yere ekler
    # append dizinin sonuna ekler insert ise sizin istediğiniz yere ekleme yapar.
    connection.execute("""insert into customers (firstName,lastName,city,email)values('Şükrü','Şimşek','Manisa','sukrusimsell@gmail.com')""")  
    #Hangi tabloya insert ediceksek o tablo isimlerini yazıcaz yani customers gibi
            #Eklemek istediğimiz dataları yazıyoruz. Ayrıca values dediğimiz terim değerler demek yani eklenmesi istenen datalar

    connection.commit()
    connection.close()
insertCustomer()
                              

#%% Güncelleme Operasyonu 
#Datalarda değişen veya eski veriyi değiştirme de kullanılır
import sqlite3
def updateCostumer():
    connection = sqlite3.connect("chinook.db") #bağlantı uzantısı
    connection.execute("""update customers set country='Turkey' where city='Stockholm'""") 
    #Burada şehri şu olanların ülkesi bu olsun gibi değişikliklerde yapabiliriz.
    # update costumers set deme nedenimiz hangi alanı değiştereceğimizi söylemek için yapıyoruz.
    # eğer başka bir veriyi daha değiştiriceksek onu da virgül koyup ekliyoruz.
    connection.commit() 
    connection.close()

updateCostumer()

#%% Delete İşlemleri

def deleteCustomer():
    connection = sqlite3.connect("chinook.db") 
    connection.execute("""delete from customers where city='Muş' or country='Brazil'""") # delete from diye başlar nereden sileceğini
    #sisteme söylemek gerekiyor burada from customer dediğimiz için customer dan sileceğiz demek oluyor
    #Burada or and gibi eklentilerle başka görevlerde ekleyebiliyoruz.
    connection.commit() 
    connection.close()
deleteCustomer()  #alta en son fonksiyonun işlemini koymazsak çalışmaz

#%% Join Operasyonlarıyla Çalışmak
import sqlite3
def joinOperasyonlari():
    connection = sqlite3.connect("chinook.db") 
    cursor = connection.execute("""select albums.Title, artists.Name from artists inner join albums on artists.ArtistId = albums.ArtistId""") 
    for row in cursor: #satırın ingilizcesi row satır satır çekmek istediğimiz için row dedik ama satır diye de yazılabilir
        print("Title = " +row[0] + "*"*8 +" Name = " +row[1])
       
    connection.close()
joinOperasyonlari()
