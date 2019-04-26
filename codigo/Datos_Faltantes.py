#detecta que columna del archivo le faltan datos
def DetectarColumna(_csv, _Arch):
    i=0 #para moverse en las columnas
    name = _csv.columns.values #se obiene nombre de las columnas
    while i in range(len(name)):
        if  _csv.isnull().any().any() == True:
            i=i+1
            i=i-1
            _Arch.write(name[i]+" faltantes: "+str(_csv[name[i]].isnull().sum())+"\n")
            _Arch.write(name[i]+" total: "+str(_csv[name[i]].count())+"\n")
        i=i+1

#verifica si le faltan datos a la tabla
def Verificar_CSV(_csv, _Arch):
    a ="\n"
    #condicion que se usa para buscar posteriormente que columna(s) le faltan datos
    if  _csv.isnull().any().any() == True:
        _Arch.write("Falta datos \n")
        DetectarColumna(_csv, _Arch)
    else:
        _Arch.write("No faltan datos \n")
    return a