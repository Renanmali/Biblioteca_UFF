import csv 

i = 0
j = 0

matriz = []
linha = []

with open(file="Biblioteca_base.csv") as file:
    csvreader = csv.reader(file)
    for percorre in csvreader:
        if(percorre == ['number ', 'book '] or percorre == ['number ', 'book ', 'value ']):
           continue
        if(percorre[0] != ''):
            matriz.append(percorre[0])
            i+=1
        if(percorre[1] != ''):
            linha.append(percorre[1])
            j+=1

print(matriz, linha)
