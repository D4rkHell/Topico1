import pyfpgrowth
from Funcion_2D import *
import datetime
import time
from random import randrange
import os

if os.path.exists("Resultados") is False:
    os.mkdir("Resultados")

train2506 = open('Resultados/train2506.txt', 'a')
train2507 = open('Resultados/train2507.txt', 'a')
train2508 = open('Resultados/train2508.txt', 'a')
train2509 = open('Resultados/train2509.txt', 'a')
train2510 = open('Resultados/train2510.txt', 'a')
train5006 = open('Resultados/train5006.txt', 'a')
train5007 = open('Resultados/train5007.txt', 'a')
train5008 = open('Resultados/train5008.txt', 'a')
train5009 = open('Resultados/train5009.txt', 'a')
train5010 = open('Resultados/train5010.txt', 'a')

prior2506 = open('Resultados/prior2506.txt', 'a')
prior2507 = open('Resultados/prior2507.txt', 'a')
prior2508 = open('Resultados/prior2508.txt', 'a')
prior2509 = open('Resultados/prior2509.txt', 'a')
prior2510 = open('Resultados/prior2510.txt', 'a')
prior5006 = open('Resultados/prior5006.txt', 'a')
prior5007 = open('Resultados/prior5007.txt', 'a')
prior5008 = open('Resultados/prior5008.txt', 'a')
prior5009 = open('Resultados/prior5009.txt', 'a')
prior5010 = open('Resultados/prior5010.txt', 'a')

def Supp_Time(_arch, _tabla, items, supp):
    star_time = datetime.datetime.now()
    #print(star_time)
    patrones = pyfpgrowth.find_frequent_patterns(_tabla, items)
    fpass = pyfpgrowth.generate_association_rules(patrones, supp)
    end_time = datetime.datetime.now()
    #print(end_time)
    total = end_time - star_time
    #print(fpass)
    _arch.write(str(total)+str(supp)+"\n")
    return fpass

def Guardar(_arch, tabla):
    for k,v in tabla.items():
        _arch.write(str(k)+str(v)+"\n")

order_products_prior = pd.read_csv('BD/order_products__prior.csv', sep=',')
order_products_train = pd.read_csv('BD/order_products__train.csv', sep=',')
products = pd.read_csv('BD/products.csv', sep=',')

Tabla_Comp_Train = TablaCompra(products, order_products_train)

train25 = []
largo_train25 = int(len(Tabla_Comp_Train)/4)
train50 = []
largo_train50 = int(len(Tabla_Comp_Train)/2)
i=0
while i < largo_train25:
    rand = randrange(0,len(Tabla_Comp_Train))
    train25.append(Tabla_Comp_Train[rand])
    i = i + 1
i=0
while i < largo_train50:
    rand = randrange(0, len(Tabla_Comp_Train))
    train50.append(Tabla_Comp_Train[rand])
    i = i + 1
del Tabla_Comp_Train
datos = Supp_Time(train2506, train25, 3, 0.6)
Guardar(datos, train2506)
datos = None
datos = Supp_Time(train5006, train50, 3, 0.6)
Guardar(datos, train5006)
datos = None
datos = Supp_Time(train2507, train25, 3, 0.7)
Guardar(datos, train2507)
datos = None
datos = Supp_Time(train5007, train50, 3, 0.7)
Guardar(datos, train5007)
datos = None
datos = Supp_Time(train2508, train25, 3, 0.8)
Guardar(datos, train2508)
datos = None
datos = Supp_Time(train5008, train50, 3, 0.8)
Guardar(datos, train5008)
datos = None
datos = Supp_Time(train2509, train25, 3, 0.9)
Guardar(datos, train2509)
datos = None
datos = Supp_Time(train5009, train50, 3, 0.9)
Guardar(datos, train5009)
datos = None
datos = Supp_Time(train2510, train25, 3, 1.0)
Guardar(datos, train2510)
datos = None
datos = Supp_Time(train5010, train50, 3, 1.0)
Guardar(datos, train5010)
datos = None

Tabla_Comp_Prior = TablaCompra(products, order_products_prior)
#print(len(Tabla_Comp_Prior))

prior25 = []
largo_prior25 = int(len(Tabla_Comp_Prior)/4)
prior50 = []
largo_prior50 = int(len(Tabla_Comp_Prior)/2)
i=0
while i < largo_prior25:
    rand = randrange(0,len(Tabla_Comp_Train))
    prior25.append(Tabla_Comp_Prior[rand])
    i = i + 1
i=0
while i < largo_prior50:
    rand = randrange(0, len(Tabla_Comp_Train))
    prior50.append(Tabla_Comp_Prior[rand])
    i = i + 1
del Tabla_Comp_Prior
datos = Supp_Time(prior2506, prior25, 3, 0.6)
Guardar(datos, prior2506)
datos = None
datos = Supp_Time(prior5006, prior50, 3, 0.6)
Guardar(datos, prior5006)
datos = None
datos = Supp_Time(prior2507, prior25, 3, 0.7)
Guardar(datos, train2507)
datos = None
datos = Supp_Time(prior5007, prior50, 3, 0.7)
Guardar(datos, prior5007)
datos = None
datos = Supp_Time(prior2508, prior25, 3, 0.8)
Guardar(datos, prior2508)
datos = None
datos = Supp_Time(prior5008, prior50, 3, 0.8)
Guardar(datos, prior5008)
datos = None
datos = Supp_Time(prior2509, prior25, 3, 0.9)
Guardar(datos, train2509)
datos = None
datos = Supp_Time(prior5009, prior50, 3, 0.9)
Guardar(datos, train5009)
datos = None
datos = Supp_Time(prior2510, prior25, 3, 1.0)
Guardar(datos, train2510)
datos = None
datos = Supp_Time(prior5010, prior50, 3, 1.0)
Guardar(datos, prior5010)
datos = None
