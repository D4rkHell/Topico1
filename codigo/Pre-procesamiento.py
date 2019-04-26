import pandas as pd
from Datos_Faltantes import *
from Funcion_1D import *

#cargar archivos csv
aisles = pd.read_csv('BD/aisles.csv', sep=',')
departments = pd.read_csv('BD/departments.csv')
order_products_prior = pd.read_csv('BD/order_products__prior.csv')
order_products_train = pd.read_csv('BD/order_products__train.csv')
orders = pd.read_csv('BD/orders.csv')
products = pd.read_csv('BD/products.csv')

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

#se hacen los procesos de 1D
Arch_1D = open('Archivos/Archivo_1D', 'a')
Arch_1D.write("aisles: \n")
Arch_1D.write(str(TipoDatos(aisles, Arch_1D)))
Arch_1D.write("departments: \n")
Arch_1D.write(str(TipoDatos(departments, Arch_1D)))
Arch_1D.write("order_products_prior: \n")
Arch_1D.write(str(TipoDatos(order_products_prior, Arch_1D)))
Arch_1D.write("order_products_train: \n")
Arch_1D.write(str(TipoDatos(order_products_train, Arch_1D)))
Arch_1D.write("oreders: \n")
Arch_1D.write(str(TipoDatos(orders, Arch_1D)))
Arch_1D.write("products: \n")
Arch_1D.write(str(TipoDatos(products, Arch_1D)))
Arch_1D.close()