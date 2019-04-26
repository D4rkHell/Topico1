from statistics import *

"""
    verifica los tipos de dato de una columna para saber que proceso usar
    sea moda[mode], media[mean], desviacion estandar[stdev], mediana[median]
"""
def TipoDatos(_csv, _Arch):
    a="\n"
    i=0
    name = _csv.columns.values  # se obiene nombre de las columnas
    while i in range(len(name)):
        if i > 1:
            #verifica si columna es int64 para saber luego si es binario o no
            if _csv[name[i]].dtypes == 'Int64':
                if len(_csv[name[i]].unique()) == 2:
                    try:
                        _Arch.write("la moda de "+name[i]+"es: "+str(mode(_csv[name[i]]))+"\n")
                    except StatisticsError:
                        _Arch.write("No unique mode found\n")
                        pass
                else:
                    try:
                        _Arch.write("la media de "+name[i]+"es: "+str(mean(_csv[name[i]]))+"\n")
                        _Arch.write("la moda de "+name[i]+"es: "+str(mode(_csv[name[i]]))+"\n")
                        _Arch.write("la desviacion estandar de "+name[i]+"es: "+str(stdev(_csv[name[i]]))+"\n")
                        _Arch.write("la mediana de "+name[i]+"es: "+str(median(_csv[name[i]]))+"\n")
                    except StatisticsError:
                        _Arch.write(str(name[i])+" No unique found\n")
            #si es columna flotante se sacara moda y media
            elif _csv[name[i]].dtypes == 'Float64':
                try:
                    _Arch.write("la media de "+name[i]+"es: "+str(mean(_csv[name[i]]))+"\n")
                    _Arch.write("la moda de "+name[i]+"es: "+str(mode(_csv[name[i]]))+"\n")
                    _Arch.write("la desviacion estandar de "+name[i]+"es: "+str(stdev(_csv[name[i]]))+"\n")
                    _Arch.write("la mediana de "+name[i]+"es: "+str(median(_csv[name[i]]))+"\n")
                except StatisticsError:
                    _Arch.write(name[i]+"No unique found\n")
                    pass
            #en caso contrario
            else:
                i = i + 1
                continue
        i = i + 1
    return a