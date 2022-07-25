# -*- coding: utf-8 -*-

import json

data = '{"firstName":"Şükrü","lastName":"Şimşek","phoneNumber":"05896587412"}'

y = json.loads(data)  #üstteki satır string yani metin iken onu json tipine çevirmeye yarar loads komutu

print(y["firstName"]) 
print(y["lastName"]) 
print(y["phoneNumber"]) 

customer = {
    "firstName" : "Şükrü", #şurada , unuttuk çalışmadı unutma , 
    "email" : "sukrusimsekll@gmail.com",
    "birth" : "11.05.1999",
    "phoneNumber":"05896587412"
    }
customerJson = json.dumps(customer) #python nesnesini json a çevirdiğimiz için dumps yaptık.
print(customer)

print(json.dumps("Abdurrazak")) #burada str datayı json olarak yazdırdık str de istendiğinde json a çevrilebilir 
