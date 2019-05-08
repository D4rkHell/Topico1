import pandas as pd
from Datos_Faltantes import *
from Funcion_1D import *
from Funcion_2D import *
from Graph import *
import os

if os.path.exists("Archivos") is False:
    os.mkdir("Archivos")
if os.path.exists("Graph") is False:
    os.mkdir(("Graph"))

# cargar archivos csv
aisles = pd.read_csv('BD/aisles.csv', sep=',')
departments = pd.read_csv('BD/departments.csv', sep=',')
order_products_prior = pd.read_csv('BD/order_products__prior.csv', sep=',')
order_products_train = pd.read_csv('BD/order_products__train.csv', sep=',')
orders = pd.read_csv('BD/orders.csv', sep=',')
products = pd.read_csv('BD/products.csv', sep=',')

#identificar tablas que le faltan datos (se guarda archivo en carpeta Archivos[tiene que estar creada])
Arch_Dat_Falt = open('Archivos/Datos_Faltantes', 'a')
Arch_Dat_Falt.write("aisles: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(aisles, Arch_Dat_Falt)))
Arch_Dat_Falt.write("departments: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(departments, Arch_Dat_Falt)))
Arch_Dat_Falt.write("order_products_prior: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(order_products_prior, Arch_Dat_Falt)))
Arch_Dat_Falt.write("order_products_train: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(order_products_train, Arch_Dat_Falt)))
Arch_Dat_Falt.write("orders: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(orders, Arch_Dat_Falt)))
Arch_Dat_Falt.write("products: \n")
Arch_Dat_Falt.write(str(Verificar_CSV(products, Arch_Dat_Falt)))
Arch_Dat_Falt.close()

#eliminicacion de tablas y/o columna que no se usaran
#datos desde csv
del order_products_prior['add_to_cart_order']
del order_products_prior['reordered']
del order_products_train['add_to_cart_order']
del order_products_train['reordered']
del aisles
del orders
del departments

Archivo_2D = open('Archivos/Archivo_2D', 'a')
Tabla_Comp_Train = TablaCompra(products, order_products_train)
Archivo_2D.write(str(Apriori(Tabla_Comp_Train, Archivo_2D)))

GraphBarraTrain(order_products_train, products)
GraphBarraPrior(order_products_prior, products)
GraphTortaTrain(order_products_train, products)
GraphBarraPrior(order_products_prior, products)
