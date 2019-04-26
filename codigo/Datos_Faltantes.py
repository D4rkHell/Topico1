#detecta que columna del archivo le faltan datos
def DetectarColumna(_csv):
    faltante=0
    i=0 #para moverse en las columnas
    name = _csv.columns.values #se obiene nombre de las columnas
    while i in range(len(name)):
        #print(name[i], _csv[name[i]].isnull().any().any()) #dice si la columna le faltan datos
        if _csv[name[i]].isnull().any().any() == True:
            i=i+1
            i=i-1
            #print(name[i], "faltantes: ", _csv[name[i]].isnull().sum())
            #print(name[i], "total: ", _csv[name[i]].count())
        i=i+1

#verifica si le faltan datos a la tabla
def Verificar_CSV(_csv):
    #condicion que se usa para buscar posteriormente que columna(s) le faltan datos
    if  _csv.isnull().any().any() == True:
        DetectarColumna(_csv)
    #retorna False/True dependiendo estado de las tablas
    return _csv.isnull().any().any()