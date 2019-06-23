import pandas as pd
from GeneraKmeans import *
import os

if os.path.exists("Archivos") is False:
    os.mkdir("Archivos")
if os.path.exists("Graph") is False:
    os.mkdir(("Graph"))
if os.path.exists("KMeans") is False:
    os.mkdir(("KMeans"))

bandera_grafico=0
archivo = open('Archivos/tiempo-kmeans.csv', 'a')
archivo.write("k,tiempominutos\n")

def Generar_Grafico(_k, _time):
    global bandera_grafico
    x_val = [x for x in _k]
    y_val = [y for y in _time]

    plt.plot(x_val,y_val)
    plt.plot(x_val,y_val,'or')
    plt.title("Tiempo(minutos) vs K(unidad)")
    if bandera_grafico == 0:
        plt.savefig('Graph/kmeansTiempoKtrain.png')
    else:
        plt.savefig('Graph/kmeansTiempoKprior.png')
    plt.show()
    bandera_grafico = bandera_grafico + 1

order_products_train = pd.read_csv('BD/prueba.csv', sep=',')
del order_products_train['add_to_cart_order']
del order_products_train['reordered']

minutos = []
cantidad_cluster = []
i=2
while i <= 20:
    min = RepresentarCluster(order_products_train, i, archivo)
    minutos.append(min)
    cantidad_cluster.append(i)
    i = i + 2

Generar_Grafico(cantidad_cluster, minutos)
