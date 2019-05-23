import pyfpgrowth
from Funcion_2D import *
import datetime
from time import time

def Supp_Time(_tabla, items, supp):
    print("asidojasid")
    star_time = time()
    patrones = pyfpgrowth.find_frequent_patterns(_tabla, items)
    print("asdkaskj")
    fpass = pyfpgrowth.generate_association_rules(patrones, supp)
    lapso = time() - star_time
    print(str(datetime.timedelta(lapso))) #obtener tiempo en hr

order_products_prior = pd.read_csv('BD/order_products__prior.csv', sep=',')
order_products_train = pd.read_csv('BD/order_products__train.csv', sep=',')
products = pd.read_csv('BD/products.csv', sep=',')

Tabla_Comp_Train = TablaCompra(products, order_products_train)
Supp_Time(Tabla_Comp_Train, 3, 0.2)
Supp_Time(Tabla_Comp_Train, 3, 0.4)
Supp_Time(Tabla_Comp_Train, 3, 0.6)
Supp_Time(Tabla_Comp_Train, 3, 0.8)
Supp_Time(Tabla_Comp_Train, 3, 1.0)

Tabla_Comp_Prior = TablaCompra(products, order_products_prior)
Supp_Time(Tabla_Comp_Prior, 3, 0.2)
Supp_Time(Tabla_Comp_Prior, 3, 0.4)
Supp_Time(Tabla_Comp_Prior, 3, 0.6)
Supp_Time(Tabla_Comp_Prior, 3, 0.8)
Supp_Time(Tabla_Comp_Prior, 3, 1.0)
