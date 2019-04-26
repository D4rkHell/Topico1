import pandas as pd
from Datos_Faltantes import *
from Funcion_1D import *

#cargar archivos csv
aisles = pd.read_csv('BD/aisles.csv', sep=',') #se debe conservar como esta
departments = pd.read_csv('BD/departments.csv') #se debe conservar como esta
order_products_prior = pd.read_csv('BD/order_products__prior.csv') #se debe conservar como esta
order_products_train = pd.read_csv('BD/order_products__train.csv') #se debe conservar como esta
orders = pd.read_csv('BD/orders.csv') #modificar
products = pd.read_csv('BD/products.csv') #se debe conservar como esta

#identificar tablas que le faltan datos (si dice True es porque le faltan datos)
print("archivo aisles: ", Verificar_CSV(aisles), "\n")
print("archivo departments: ", Verificar_CSV(departments), "\n")
print("archivo order_products_prior: ", Verificar_CSV(order_products_prior), "\n")
print("archivo order_products_train: ", Verificar_CSV(order_products_train), "\n")
print("archivo orders: ", Verificar_CSV(orders), "\n")
print("archivo products: ", Verificar_CSV(products), "\n")

TipoDatos(aisles)
TipoDatos(departments)
TipoDatos(order_products_prior)
TipoDatos(order_products_train)
TipoDatos(orders)
TipoDatos(products)