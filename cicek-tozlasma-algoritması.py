#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 21:31:16 2022

@author: barisbalci
"""

import math
from random import random
import numpy as np 

for dongu in range(0,durma_kriteri):
    if sp>random():

#başlangıç çözüm matrisinde amaç fonksiyonunu minimum yapan çözüm (çicek) ve bu çözüme ait tasarım değişkenlerinin elde edilmesi

    for cicek in range(0,nf):
        deger=min(OPT[AF][:])
        
        X1gennew=OPT[0][sira]
        X2gennew=OPT[1][sira]
    
#levy dağılımının hesaplanması
    levy=(1/math.sqrt(2*math.pi))*(random()**-1.5)*mathexp(1)**(-1/(2*random()))
    
#tasarım değişkenlerinin global arama kurallarına göre yeniden oluşturulması
    X1new1=OPT[0][cicek]+levy*(X1gennew-OPT[0][cicek])
    X1new1=OPT[1][cicek]+levy*(X1gennew-OPT[1][cicek])
    
    else:
        for cicek in range(0,nf):
            #yerel arama süreci için gerekli iki farklı çözümün (k ve m çiceğinin )rassal olarak belirlenmesi
            
                m=math.ceil(random()*nf)
                k=math.ceil(random()*nf)
                
            while (m==k):
                m=math.ceil(random()*nf)
                k=math.ceil(random()*nf)
                
                m=m-1
                k=k-1
                
#tasarım değişkenlerinin yerel arama kurallarına göre yeniden oluşturulması
    X1new=OPT[0][cicek]+random()*(OPT[0][m]-OPT[0][k])
    X1new=OPT[1][cicek]+random()*(OPT[1][m]-OPT[1][k])
    
deger=min(OPT[AF][:])
sira=np.argmin(OPT[AF])
