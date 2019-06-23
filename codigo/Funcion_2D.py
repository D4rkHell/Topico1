import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from apyori import apriori
#from mlxtend.frequent_patterns import apriori
import math
import numpy as np
import csv
np.set_printoptions(suppress=True)

def Apriori(_csv, _Archivo):
    i=0
    association_rules = list(apriori(_csv, min_support=0.0045, min_confidence=0.0045, min_lift=0.0045, max_length=2))

    print(len(association_rules))
    while i < len(association_rules):
        _Archivo.write(str(association_rules[i]) + "\n")
        _Archivo.write("=====================================\n")
        i=i+1

def TablaCompra(_csv):
    table = []
    w = 0
    x = 0
    y = 0
    z = 0
    #print(len(_csv))

    while x < len(_csv):
        if x == 0:
            table += [[]]
            y = _csv.iloc[x]["order_id"]
            #print(y)
        if x > 0:
            z = _csv.iloc[x]["order_id"]
            if z != y:
                table += [[]]
                y = z
                #print("paso a la siguinte orden")
                w += 1
            #print(z)
        table[w].append(_csv.iloc[x]["product_id"])
        #table = list(filter(None, table))
        #if x > len(_csv):
            #print(table)
        #print(table)
        x = x + 1

    #table = list(filter(None, table))
    #print(table)
    return table

def calculo_coeficiente_phi(t):
    "Calcula coeficiente phi de una tabla de contingencia"
    # Variables para calculos
    A11 = int(t[0])
    A10 = int(t[1])
    A01 = int(t[2])
    A00 = int(t[3])
    TotalX = A11 + A10
    TotalY = A11 + A01
    TotalnX = A01 + A00
    TotalnY = A10 + A00
    Total = TotalX + TotalnX

    # Calculo de probabilidades
    pxy = (A11 / Total)
    px = (TotalX / Total)
    py = (TotalY / Total)
    uno_menos_px = (TotalnX / Total)
    uno_menos_py = (TotalnY / Total)

    # Coeficiente phi
    numerador = pxy - (px * py)
    denominador = px * uno_menos_px * py * uno_menos_py
    denominador = math.sqrt(denominador)

    coeficiente_phi = numerador / denominador
    t[4] = coeficiente_phi
    return round(coeficiente_phi,4)

def TablaContingencia(orden, productos, archivo):
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
        # print(table)
        # print(table)
        x = x + 1

    coeficiente = 0
    F11 = 0
    F01 = 0
    F10 = 0
    F00 = 0
    posicion_productos = 0
    posicion_productos_aux = 1
    posicion_ordenes = 0

    # productos
    # 4 debe ser 10 mejores productos - 2, es decir 8
    while posicion_productos < 10 - 2:
        if posicion_productos_aux == 10 - posicion_productos or posicion_productos_aux > 10 - posicion_productos:
            # print("i: ", i)
            posicion_productos += 1
            posicion_productos_aux = 1
        # ordenes
        while posicion_ordenes < (len(table)):
            if soportes_final.iloc[posicion_productos][2] in table[posicion_ordenes] and \
                    soportes_final.iloc[posicion_productos + posicion_productos_aux][2] in table[posicion_ordenes]:
                F11 += 1
            if soportes_final.iloc[posicion_productos][2] not in table[posicion_ordenes] and \
                    soportes_final.iloc[posicion_productos + posicion_productos_aux][2] in table[posicion_ordenes]:
                F01 += 1
            if soportes_final.iloc[posicion_productos][2] in table[posicion_ordenes] and \
                    soportes_final.iloc[posicion_productos + posicion_productos_aux][2] not in table[posicion_ordenes]:
                F10 += 1
            if soportes_final.iloc[posicion_productos][2] not in table[posicion_ordenes] and \
                    soportes_final.iloc[posicion_productos + posicion_productos_aux][2] not in table[posicion_ordenes]:
                F00 += 1
            posicion_ordenes += 1
        posicion_ordenes = 0

        tabla2 = [0, 0, 0, 0, 0]
        tabla2[0] = F11
        tabla2[1] = F10
        tabla2[2] = F01
        tabla2[3] = F00

        calculo_coeficiente_phi(tabla2)

        arch2 = csv.writer(archivo)
        arch2.writerow(tabla2)
        F11 = 0
        F01 = 0
        F10 = 0
        F00 = 0
        posicion_productos_aux += 1
