import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
import datetime
from sklearn.decomposition import PCA
import numpy as np
import math
from sklearn.preprocessing import MultiLabelBinarizer
import scipy.stats
from Funcion_2D import TablaCompra
from scipy.stats import sem, t
from scipy import mean

def Entropia(labels):
    N = sum(labels)
    probs = (freq/N for freq in labels if freq>0)
    #print ("Entropia: "+str(-sum(x * math.log(x, 2) for x in probs)))
    return -sum(x * math.log(x, 2) for x in probs)

def extraeDatosCluster(cluster, transacciones, labels):
  datos = []
  mlb = MultiLabelBinarizer().fit_transform(transacciones)
  i=0
  while i < len(transacciones):
    if (labels[i] == cluster):
      datos.append(mlb[i])
    i = i+1
  return datos

def calculoVarianzas(k, data, labels):
  varianzas = []
  tab = TablaCompra(data)
  i=0
  while i < k:
    datos = extraeDatosCluster(i, tab, labels)
    var = np.var(datos)
    varianzas.append(var)
    i = i+1
  return varianzas

def Confianza(data, confianza):
    n = len(data)
    m = mean(data)
    std_err = sem(data)
    h = std_err * t.ppf((1 + confianza) / 2, n - 1)
    end = m + h
    print ("confianza: "+str(end)+"\n")


#Cluster
def RepresentarCluster(data, cantidad, archivo):
    i=0

    star_time = datetime.datetime.now()
    X, y = make_blobs(
       n_samples=len(data), n_features=cantidad,
       centers=cantidad, cluster_std=0.5,
       shuffle=True, random_state=0
    )

    # plotear
    plt.scatter(
       X[:, 0], X[:, 1],
       c='white', marker='o',
       edgecolor='black', s=10
    )
    #plt.show()

    km = KMeans(
        n_clusters=cantidad, init='random',
        n_init=10, max_iter=300,
        tol=1e-04, random_state=0,
        n_jobs = -1
    )
    y_km = km.fit_predict(X)
    label_name = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10",
    "c11", "c12", "c13", "c14", "c15", "c16", "c17", "c18", "c19", "c20"]
    color = ["lightgreen", "red", "blue", "purple", "darkgreen", "darkblue", "lightblue",
    "darkred", "magenta", "yellow", "white", "orange", "cyan", "lightyellow",
    "turquoise", "gold", "pink", "maroon", "lightpink", "darkorange"]
    while i < cantidad:
        plt.scatter(
            X[y_km == i, 0], X[y_km == i, 1],
            s=50, c=color[i],
            marker='o', edgecolor='black',
            label=label_name[i]
        )
        i=i+1

    # plot the centroids
    plt.scatter(
        km.cluster_centers_[:, 0], km.cluster_centers_[:, 1],
        s=250, marker='*',
        c='black', edgecolor='black',
        label='centroids'
    )
    end_time = datetime.datetime.now()
    total = end_time - star_time
    segundos =(total).total_seconds() #se tiene tiempo en segundos
    minutos = segundos/60 #se tiene tiempo en minutos
    archivo.write(str(cantidad)+","+str(minutos)+"\n")

    plt.legend(scatterpoints=1)
    plt.grid()
    plt.savefig('KMeans/'+str(cantidad)+'.png')
    plt.show()
    largo = len(km.cluster_centers_[:,0])
    centro=[]
    i=0
    while i < largo:
        centro.append(math.sqrt(math.pow(km.cluster_centers_[i,0],2)+math.pow(km.cluster_centers_[i,1],2)))
        i = i+1
    entropia = Entropia(y_km)
    print("entropia: ", entropia)
    #comienza binarizar
    varianzas = calculoVarianzas(cantidad, data, y_km)
    varianzas2 = varianzas
    varianzas.sort(reverse = True)
    print("varianzas ordenadas de mayor a menor")
    print(varianzas)

    Confianza(X,0.95)

    return minutos
