import os
print("Elija Opcion")
print("1.- Pre-Procesamiento")
print("2.- Fp-growth")
print("3.- K-means")
var = int(input("Ingrese opcion: "))
while var!=0:
    if var==1:
        os.system("python3 Pre-procesamiento.py")
    elif var==2:
        os.system("python3 fp-growthvstiempo.py")
    elif var==3:
        os.system("python3 k-means.py")
    else:
        print("opcion no existe")
