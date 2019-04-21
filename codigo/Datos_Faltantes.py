def DetectarColumna(_csv):
    i=0
    name = _csv.columns.values
    while i in range(len(name)):
        print(name[i], _csv[name[i]].isnull().any().any())
        i=i+1


def Verificar_CSV(_csv):
    if  _csv.isnull().any().any() == True:
        DetectarColumna(_csv)
    return _csv.isnull().any().any()