
import csv
import numpy as np

# Criando um mapa de usuários 
users = {}
rating = 1

# Criando um mapa para a similaridade
similarity = {}
list1 = []
list2 = []
list3 = []
cont = 0

# Criando a função para calcular a similaridade Jaccard
def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float (intersection)/union



# Abrindo o csv e enumerando quais livros cada usuário leu 
with open('Biblioteca_base.csv', 'r') as arquivo:
    reader = csv.reader(arquivo)
    for i, linha in enumerate(arquivo):
        if i==0: continue
        linha = linha.replace('\n', '')
        linha_dividida = linha.split(';')
        userid = int(linha_dividida[0])
        bookid = int(linha_dividida[1])
        if len(linha_dividida) > 2:
            rating = int(linha_dividida[2])
        if userid not in users:
            users[userid] = dict()
        users[userid][bookid] = rating
    
# Enumerando todos os usuários e fazendo a similaridade de Jaccard para cada um deles 
    for user in enumerate(users):
        a = user
        list3.append(a) 
        cont += 1
    for i in users:
        aux = 0
        position = 0
        similarity[i] = dict()
        for j in users[i]:
            list1.append(j)
        while(aux < cont):
            if(aux != i):
                for j in users[list3[aux][1]]:
                    list2.append(j)
            result = jaccard(list1, list2)  
            similarity[i][list3[aux][1]] = result
            aux += 1
            list2 = []
        list1 = []

print(similarity[95450])

    