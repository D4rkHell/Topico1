import pandas as pd
from GeneraKmeans import *
import os
import numpy as np
import scipy.stats
from sklearn.preprocessing import MultiLabelBinarizer
from sklearn.cluster import KMeans

from Funcion_2D_02 import TablaCompra

order_products_train = pd.read_csv('order_products__train.csv', sep=',')
#, chunksize=131209
transacciones = TablaCompra(order_products_train)

#print(len(transacciones))
#mlb = MultiLabelBinarizer().fit_transform(transacciones)
#print(mlb)

def extraeDatos_Cluster(cluster, labels, tipo, setDatos):
  datos = []
  i = 0
  while i < len(setDatos):
    if (tipo == "mlb"):
      if (labels[i] == cluster):
        datos.append(setDatos[i])
    if (tipo == "transacciones"):
      if (labels[i] == cluster):
        datos.append(setDatos[i])
    i = i + 1
  return datos


def calculo_Mayor_Varianza(k, labels, setDatos):
  varianzas = []
  i = 0
  while i < k:
    datos = extraeDatos_Cluster(i, labels, "mlb", setDatos)
    var = np.var(datos)
    varianzas.append(var)
    i = i + 1

  pos = varianzas.index(max(varianzas))
  return pos

def kmeans(X, k):
  km = KMeans(
        n_clusters=k, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=0,
        n_jobs=1
    )
  labels = km.fit_predict(X)
  return labels


def kmeans_en_mayor_varianza(transacciones, mlb):
  copiaTransacciones = transacciones
  copiaMLB = mlb
  i = 0
  k = 6

  while k > 1:
    labels = kmeans(copiaMLB, k)
    print("clusters: ", labels)
    pos = calculo_Mayor_Varianza(k, labels, copiaMLB)
    print("cluster de mayor varianza: ", pos)

    copiaMLB = extraeDatos_Cluster(pos, labels, "mlb", copiaMLB)

    copiaTransacciones = extraeDatos_Cluster(pos, labels, "transacciones", copiaTransacciones)
    print("transacciones del cluster con mayor varianza")
    print(copiaTransacciones)
    print("\n")

    k = k - 2

  return copiaTransacciones
"""
trans = []
i=0
for i in range(int(len(transacciones)/2)):
  trans.append(transacciones[i])

del transacciones
"""
mlb = MultiLabelBinarizer().fit_transform(transacciones)
asd = kmeans_en_mayor_varianza(transacciones, mlb)
print("\ntransacciones después de kmeans iterativo sobre cluster con mejor varianza:\n",asd)