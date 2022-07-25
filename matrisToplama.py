# -*- coding: utf-8 -*-

# 1 3 5
# 2 4 1
# 1 5 7

# 3 3 4
# 2 4 1
# 3 5 4

# 4 6 9
# 4 8 2
# 4 10 11

x = [[1,3,5],[2,4,1],[1,5,7]]
y = [[3,3,4],[2,4,1],[3,5,4]]

sonuc = [[0,0,0],[0,0,0],[0,0,0]]

sonuc[0][0] = x[0][0]+y[0][0]

for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j] = x[i][j]+y[i][j]

print(sonuc)


# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 21:47:32 2022

@author: Şükrü
"""

x = [1,3,5]
y = [2,4,1]
z = [1,5,7]

a = [3,3,4]
b = [2,4,1]
c = [3,5,4]

d = (x[0]+a[0]),(x[1]+a[1]),(x[2]+a[2])
e = (y[0]+b[0]),(y[1]+b[1]),(y[2]+b[2])
f = (z[0]+c[0]),(z[1]+c[1]),(z[2]+c[2])

print(d)
print(e)   
print(f)