#revisar funcion
def TipoDatos(_csv):
    count=0
    i=0
    j=0
    k=0
    name = _csv.columns.values  # se obiene nombre de las columnas
    while i in range(len(name)):
        #print(name[i], _csv[name[i]].dtypes)
        #print(name[i])
        if i>0:
            while j in range(len(_csv)):
                print(_csv.loc[j:k,name[i]])
                j = j + 1
                k = k + 1
        i = i + 1
        j = 0