import pandas as pd
import matplotlib.pyplot as plt

def GraphBarraTrain(boleta, productos):
    # Hace merge con datos2
    dfmerge = pd.merge(productos, boleta, on='product_id')
    soportes = dfmerge['product_name'].value_counts()
    soportes = pd.DataFrame(soportes).reset_index()
    soportes.columns = ["product_name", "soporte"]
    print(soportes)
    print("\n")
    print(soportes[0:10])
    print("\n")

    soportes[0:10].plot.bar(x='product_name', y='soporte')
    # soportes[pos_inicial_fila: pos_final_fila]
    plt.ylabel('Soporte')
    plt.xlabel('Producto')
    plt.title('Soporte por producto Train')
    plt.savefig('Graph/Train_Barra.png', bbox_inches="tight")
    plt.show()

def GraphBarraPrior(boleta, productos):
    # Hace merge con datos2
    dfmerge = pd.merge(productos, boleta, on='product_id')
    soportes = dfmerge['product_name'].value_counts()
    soportes = pd.DataFrame(soportes).reset_index()
    soportes.columns = ["product_name", "soporte"]
    print(soportes)
    print("\n")
    print(soportes[0:10])
    print("\n")

    soportes[0:10].plot.bar(x='product_name', y='soporte')
    # soportes[pos_inicial_fila: pos_final_fila]
    plt.ylabel('Soporte')
    plt.xlabel('Producto')
    plt.title('Soporte por producto Prior')
    plt.savefig('Graph/Prior_Barra.png', bbox_inches="tight")
    plt.show()

def GraphTortaTrain(boleta, productos):
    notin = productos['product_id'].isin(boleta['product_id'])
    print(notin)
    notinConteo = notin.value_counts()
    print(notinConteo)
    labels = ['Comprados', 'No Comprados']
    sizes = [215, 130, 245, 210]
    colors = ['yellowgreen', 'lightskyblue']
    explode = (0.1, 0)  # separar primer corte
    autopct = '%1.1f%%'  # autoporcentaje
    notinConteo.plot(kind='pie', autopct=autopct, explode=explode, colors=colors, labels=labels)
    plt.axis('off')
    plt.title('Porcentaje de productos comprados y no comprados \n(TRAIN)\n')
    plt.savefig('Graph/Train_Torta.png', bbox_inches="tight")
    plt.show()

def GraphTortaPrior(boleta, productos):
    notin = productos['product_id'].isin(boleta['product_id'])
    print(notin)
    notinConteo = notin.value_counts()
    print(notinConteo)
    labels = ['Comprados', 'No Comprados']
    sizes = [215, 130, 245, 210]
    colors = ['yellowgreen', 'lightskyblue']
    explode = (0.1, 0)  # separar primer corte
    autopct = '%1.1f%%'  # autoporcentaje
    notinConteo.plot(kind='pie', autopct=autopct, explode=explode, colors=colors, labels=labels)
    plt.axis('off')
    plt.title('Porcentaje de productos comprados y no comprados \n(TRAIN)\n')
    plt.savefig('Graph/Prior_Torta.png', bbox_inches="tight")
    plt.show()