# -*- coding: utf-8 -*-

import matematikModule #import ile başka yazılan bir modülü çekerken kullanıyoruz. Yani bir hesap makinesi yaparken 
                        #toplama ve çıkarma modülleri elimizde var ise onları importlıyarak kullanabiliriz.
matematikModule.carp(6,7)
matematikModule.topla(6,7)

import matematikModule as mm #burada as ile matematikModule olarak kaydedilen modülü farklı isimle kullanmaya yarıyor.
mm.carp(5,55)

print(mm.customer["firstName"])

from matematikModule import topla #from sadece o modülden belli bir kısmı çekmek istediğimizde kullanıyoruz.

topla(5,8)
