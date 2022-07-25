setA = {1,2,3,4,5}
setB = {1,3,4,6,7,8}

print(setA | setB) #union yani birleştirne işlemi

print(setA.union(setB)) #farklı bir union yapma metodu
print(setB.union(setA))

print(setA & setB) #kesişim noktasını hesaplamak için

print(setA.intersection(setB)) #intersection kesişim demek oldığu için kesişimi gösterir
print(setB.intersection(setA))

print(setA - setB) #diğer gruptan farkı gösterir

print(setA.difference(setB)) #diğer grupran farkı gösterir
print(setB.difference(setA))

print(setA ^ setB) #simetrik farkı verir yani sadece a ve sadece b de olanları verir

print(setA.symmetric_difference(setB)) #simetrik farkı verir 
print(setB.symmetric_difference(setA))