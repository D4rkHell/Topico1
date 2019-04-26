from  statistics import *

"""
    verifica los tipos de dato de una columna para saber que proceso usar
    sea moda[mode], media[mean], desviacion estandar[stdev], mediana[median]
"""
def TipoDatos(_csv):
    i=0
    name = _csv.columns.values  # se obiene nombre de las columnas
    while i in range(len(name)):
        if i > 1:
            #verifica si columna es int64 para saber luego si es binario o no
            if _csv[name[i]].dtypes == 'Int64':
                if len(_csv[name[i]].unique()) == 2:
                    try:
                        print("la moda de ", name[i], "es: ", mode(_csv[name[i]]))
                    except StatisticsError:
                        print("No unique mode found")
                        pass
                else:
                    try:
                        print("la media de ", name[i], "es: ", mean(_csv[name[i]]))
                        print("la moda de ", name[i], "es: ", mode(_csv[name[i]]))
                        print("la desviacion estandar de ", name[i], "es: ", stdev(_csv[name[i]]))
                        print("la mediana de ", name[i], "es: ", median(_csv[name[i]]))
                    except StatisticsError:
                        print("No unique found")
            #si es columna flotante se sacara moda y media
            elif _csv[name[i]].dtypes == 'Float64':
                try:
                    print("la media de ", name[i], "es: ", mean(_csv[name[i]]))
                    print("la moda de ", name[i], "es: ", mode(_csv[name[i]]))
                    print("la desviacion estandar de ", name[i], "es: ", stdev(_csv[name[i]]))
                    print("la mediana de ", name[i], "es: ", median(_csv[name[i]]))
                except StatisticsError:
                    print("No unique found")
                    pass
            #en caso contrario
            else:
                i = i + 1
                continue
        i = i + 1