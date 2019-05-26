import pyfpgrowth
from Funcion_2D import *
import datetime
import time
from random import randrange
import os

if os.path.exists("Resultados") is False:
    os.mkdir("Resultados")

train502 = open('Resultados/train502.txt', 'a')
train504 = open('Resultados/train504.txt', 'a')
train506 = open('Resultados/train506.txt', 'a')
train508 = open('Resultados/train508.txt', 'a')
train510 = open('Resultados/train510.txt', 'a')

prior102 = open('Resultados/prior102.txt', 'a')
prior104 = open('Resultados/prior104.txt', 'a')
prior106 = open('Resultados/prior106.txt', 'a')
prior108 = open('Resultados/prior108.txt', 'a')
prior110 = open('Resultados/prior110.txt', 'a')

def Supp_Time(_arch, _tabla, items, supp):
    star_time = datetime.datetime.now()
    #print(star_time)
    patrones = pyfpgrowth.find_frequent_patterns(_tabla, items)
    fpass = pyfpgrowth.generate_association_rules(patrones, supp)
    end_time = datetime.datetime.now()
    #print(end_time)
    total = end_time - star_time
    #print(fpass)
    _arch.write(str(total)+"\n"+str(supp)+"\n")
    return fpass

def Guardar(_arch, tabla):
    for k,v in tabla.items():
        _arch.write(str(k)+str(v)+"\n")


print("inicio " + str(datetime.datetime.now()))
order_products_train = pd.read_csv('BD/order_products__train.csv', sep=',')
products = pd.read_csv('BD/products.csv', sep=',')
print("cargo csv\n")
Tabla_Comp_Train = TablaCompra(products, order_products_train)
print("genera compra\n")

print("elimino csv train\n")
del order_products_train

train5 = []
largo_train5 = int(len(Tabla_Comp_Train)/20)
print(largo_train5)
i=0
while i < largo_train5:
    rand = randrange(0,len(Tabla_Comp_Train))
    train5.append(Tabla_Comp_Train[rand])
    i = i + 1
print("hizo random")
del Tabla_Comp_Train


datos = Supp_Time(train502, train5, 3, 0.2)
Guardar(train502, datos)
del datos
print("fin supp 0.2\n")
datos = Supp_Time(train504, train5, 3, 0.4)
Guardar(train504, datos)
del datos
print("fin supp 0.4\n")
datos = Supp_Time(train506, train5, 3, 0.6)
Guardar(train506, datos)
del datos
print("fin supp 0.6\n")
datos = Supp_Time(train508, train5, 3, 0.8)
Guardar(train508, datos)
del datos
print("fin supp 0.8\n")
datos = Supp_Time(train510, train5, 3, 1.0)
Guardar(train510, datos)
del datos
print("fin supp 1.0\n")

print("fin train " + str(datetime.datetime.now()))

print("comienza prior" + str(datetime.datetime.now()))

order_products_prior = pd.read_csv('BD/order_products__prior.csv', sep=',')
products = pd.read_csv('BD/products.csv', sep=',')
print("cargo csv\n")
Tabla_Comp_Prior = TablaCompra(products, order_products_prior)
del order_products_prior

prior1 = []
largo_prior1 = int(len(Tabla_Comp_Prior)/100)
i=0
while i < largo_prior1:
    rand = randrange(0,len(Tabla_Comp_Prior))
    prior1.append(Tabla_Comp_Prior[rand])
    i = i + 1
print("se genero random prior\n")
del Tabla_Comp_Prior
datos = Supp_Time(prior102, prior1, 3, 0.2)
Guardar(prior102, datos)
del datos
print("fin supp 0.2\n")
datos = Supp_Time(prior104, prior1, 3, 0.4)
Guardar(prior104, datos)
del datos
print("fin supp 0.4\n")
datos = Supp_Time(prior106, prior1, 3, 0.6)
Guardar(prior106, datos)
del datos
print("fin supp 0.6\n")
datos = Supp_Time(prior108, prior1, 3, 0.8)
Guardar(prior108, datos)
del datos
print("fin supp 0.8\n")
datos = Supp_Time(prior110, prior1, 3, 1.0)
Guardar(prior110, datos)
del datos
print("fin supp 1.0\n")
print("termino prior " + str(datetime.datetime.now()))
