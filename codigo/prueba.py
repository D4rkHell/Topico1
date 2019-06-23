import datetime
import random
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MultiLabelBinarizer
from Funcion_2D import *
import os

if os.path.exists("Limpieza") is False:
    os.mkdir("Limpieza")
if os.path.isfile("Limpieza/arch_train.txt") is True:
    os.remove("Limpieza/arch_train.txt")
if os.path.isfile("Limpieza/arch_pares_train.txt") is True:
    os.remove("Limpieza/arch_pares_train.txt")
if os.path.isfile("Limpieza/arch_prior.txt") is True:
    os.remove("Limpieza/arch_prior.txt")
if os.path.isfile("Limpieza/arch_pares_prior.txt") is True:
    os.remove("Limpieza/arch_pares_prior.txt")


def EliminarInfrecuencia(_order_product):
    i=0
    for i in range(5):
        _order_product = _order_product[_order_product.duplicated(subset=["order_id"], keep=False)]
        _order_product = _order_product[_order_product.duplicated(subset=["product_id"], keep=False)]

    return _order_product

def Guardar(_order_product, _archivo):

    for index, row in _order_product.iterrows():
        _archivo.write(str(row['order_id'])+","+str(row['product_id'])+"\n")

def Contingencia(orden, productos, archivo):
    table = []
    w = 0
    x = 0
    y = 0
    z = 0
    orden = orden.applymap(str)
    productos = productos.applymap(str)
    dfmerge = pd.merge(productos, orden, on='product_id')

    soportes = dfmerge['product_name'].value_counts()
    soportes2 = dfmerge['product_id'].value_counts()

    soportes = pd.DataFrame(soportes).reset_index()
    soportes.columns = ["product_name", "soporte"]
    soportes2 = pd.DataFrame(soportes2).reset_index()
    soportes2.columns = ["product_id", "soporte"]
    soportes_final = pd.merge(soportes, soportes2, on='soporte')

    #La tabla "soportes_final" presenta sus cabezera en el siguiente orden: product_name, soporte y product_id
    #print(soportes_final)

    while x < len(orden):
        if x == 0:
            table += [[]]
            y = orden.iloc[x]["order_id"]
        if x > 0:
            z = orden.iloc[x]["order_id"]
            if z != y:
                table += [[]]
                y = z
                w += 1
        table[w].append(orden.iloc[x]["product_id"])
        # if x > len(_csv):
        x = x + 1

    #table es la tabla con las ordenes
    #print("tabla", table)

    print("Matriz Binaria", str(datetime.datetime.now()))

    table3 = []
    i = 0
    total = (len(table))
    cant = int(total/2)
    rand = random.sample(range(total), cant)
    # print(rand)
    # rand = randrange(0, len(transactions))
    while i < cant:
        table3.append(table[rand[i]])
        i = i + 1
    #print(table3)

    mlb = MultiLabelBinarizer().fit_transform(table3)
    #print("matriz")
    #print(mlb)
    kmeans = KMeans(n_clusters=4, random_state=4, algorithm=elkan).fit(mlb)
    #print("kmeans")
    # print(kmeans.labels_)
    y_kmeans = kmeans.predict(mlb)
    # print("cluster")
    print(kmeans.cluster_centers_)

    plt.scatter(mlb[:, 0], mlb[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()

    """
    mlb = MultiLabelBinarizer().fit_transform(table)
    print("matriz")
    print(mlb)
    kmeans = KMeans(n_clusters=2, random_state=0).fit(mlb)
    print("kmeans")
    # print(kmeans.labels_)
    y_kmeans = kmeans.predict(mlb)
    # print("cluster")
    print(kmeans.cluster_centers_)

    plt.scatter(mlb[:, 0], mlb[:, 1], c=y_kmeans, s=50, cmap='viridis')
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
    plt.show()
    """

    print("Matriz Binaria FIN", str(datetime.datetime.now()))

print("inicio " + str(datetime.datetime.now()))
print("P1 train inicio")

arch_train = open('Limpieza/arch_train.txt', 'a')
arch_train.write("order_id,product_id\n")
#lectura de archivo train
order_products_train = pd.read_csv('BD/order_products__train.csv', sep=',', low_memory=False)
order_products_train = order_products_train.drop(['add_to_cart_order','reordered'], axis=1)#remover columnas que no se necesitan
order_products_train = EliminarInfrecuencia(order_products_train)
arch_train.write(str(Guardar(order_products_train, arch_train)))
del order_products_train

print("P1 train final")
"""
print(str(datetime.datetime.now()))
print("P1 prior inicio")

arch_prior = open('Limpieza/arch_prior.txt', 'a')
arch_prior.write("order_id,product_id\n")
#lectura archivo prior
order_products_prior = pd.read_csv('BD/order_products__prior.csv', sep=',', low_memory=False)
order_products_prior = order_products_prior.drop(['add_to_cart_order','reordered'], axis=1)#remover columnas que no se necesitan
order_products_prior = EliminarInfrecuencia(order_products_prior)
arch_prior.write(str(Guardar(order_products_prior, arch_prior)))
del order_products_prior

print("P1 prior final")
"""
print(str(datetime.datetime.now()))
print("P2 train inicio")

products = pd.read_csv('BD/products.csv', sep=',')
arch_train = pd.read_csv('Limpieza/arch_train.txt', sep=',', low_memory=False)
arch_pares_train = open('Limpieza/arch_pares_train.txt', 'a')
arch_pares_train.write("order_id,product_id\n")
print("P2 train inicio contingencia")
arch_pares_train.write(str(Contingencia(arch_train, products, arch_pares_train)))
del arch_train

print("P2 train final")
print(str(datetime.datetime.now()))
"""
print("P2 prior inicio")

arch_prior = pd.read_csv('Limpieza/arch_prior.txt', sep=',', low_memory=False)
arch_pares_prior = open('Limpieza/arch_pares_prior.txt', 'a')
arch_pares_prior.write("order_id,product_id\n")
print("P2 prior inicio contingencia")
arch_pares_prior.write(str(Contingencia(arch_prior, products, arch_pares_prior)))

print("P2 prior final")
print(str(datetime.datetime.now()))
"""
"""
centroids = kmeans.cluster_centers_
print(centroids)

plt.scatter(order_products_train['product_id'][:100].values, order_products_train['order_id'][:100].values, c= kmeans.labels_.astype(float), s=50)#, alpha=0.5)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=50)
plt.show()
"""
