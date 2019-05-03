import pandas as pd

def TablaContingencia(_product, _csv):
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
            print(z)
        table[w].append(_csv.iloc[x]["product_id"])
        #table = list(filter(None, table))
        if x > len(_csv):
            print(table)
        #print(table)
        x = x + 1

    #table = list(filter(None, table))
    #print(table)
    return table