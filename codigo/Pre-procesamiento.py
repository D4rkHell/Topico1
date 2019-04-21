import pandas as pd
import numpy as np
from Datos_Faltantes import *


#cargar archivos csv
aisles = pd.read_csv('BD/aisles.csv') #se debe conservar como esta
departments = pd.read_csv('BD/departments.csv') #se debe conservar como esta
order_products_prior = pd.read_csv('BD/order_products__prior.csv')
order_products_train = pd.read_csv('BD/order_products__train.csv')
orders = pd.read_csv('BD/orders.csv')
products = pd.read_csv('BD/products.csv')

#identificar tablas que le faltan datos
print("aisles: ", Verificar_CSV(aisles), "\n")
print("departments: ", Verificar_CSV(departments), "\n")
print("order_products_prior: ", Verificar_CSV(order_products_prior), "\n")
print("order_products_train: ", Verificar_CSV(order_products_train), "\n")
print("orders: ", Verificar_CSV(orders), "\n")
print("products: ", Verificar_CSV(products), "\n")

"""
cnum = len(orders['days_since_prior_order'])
print(cnum)
for c in cnum:
    orders[c] = orders[c].fillna(-1)
"""