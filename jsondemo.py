# -*- coding: utf-8 -*-

import json

with open("users.json") as users:
    data = json.load(users)
    
    for x in range(5):
        print(data[x]["username"])
        print(data[x]["email"]) #Burada datayı açıp ardından datadan istediğimiz verileri talep edip onları yazdırıyoruz.
        print(data[x]["address"]["city"]) #Bu şekilde adresin şehri gibi detaylarıda isteyebiliriz
        print(data[x]["company"])
        