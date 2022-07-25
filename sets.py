studentsSet = {"Şükrü","Fatih","Ahmet","Salih"}
print(studentsSet)

for student in studentsSet:
    print(student)
    
# print("Salih" in studentsSet)
# print("salih" in studentsSet) #false çıkmakta çünkü Salih in s sini küçük yaptık

if "Şükrü" in studentsSet:
    print("Listede Var")
    
studentsSet.add("Ali") #listeye yeni data eklemek için kullanılır
print(studentsSet)

studentsSet.update(["Merve","Kerem"]) #Listeye birden fazla data eklemek istersek kullanılır
print(studentsSet)

print(len(studentsSet))

studentsSet.remove("Ahmet")
print(len(studentsSet))

studentsSet.discard("Salih") #hem silme ancak silme işlemlerinde hata vermemesi için kullanılır
print(len(studentsSet))

x = studentsSet.clear() #Setin komple tüm datalarını silmeye yarar
print(len(studentsSet))
# del studentsSet #Tüm seti yok eder böyle bir set olmadığını konsolda verir


