
import csv
import Funções
import numpy as np
import Table
import pandas as pd

#Criando um mapa de livros 
books = {}


# Criando um mapa de usuários 
users = {}
rating = 1

# Criando um mapa para a similaridade
book_similarity = {}
user_similarity = {}
list1 = []
list2 = []
list3 = []
cont = 0



# Abrindo o csv e enumerando quais livros cada usuário leu 
with open('Biblioteca_base1.csv', 'r') as arquivo:
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
        if bookid not in books:
            books[bookid] = dict()
        users[userid][bookid] = rating
        books[bookid][userid] = rating
    
# Enumerando todos os usuários e fazendo a similaridade de Jaccard para cada um deles 
    for user in enumerate(users):
        a = user
        list3.append(a) 
        cont += 1
    for i in users:
        aux = 0
        position = 0
        user_similarity[i] = dict()
        for j in users[i]:
            list1.append(j)
        while(aux < cont):
            if(aux != i):
                for j in users[list3[aux][1]]:
                    list2.append(j)
            result = Funções.jaccard(list1, list2)  
            user_similarity[i][list3[aux][1]] = result
            aux += 1
            list2 = []
        list1 = []

#Enumerando todos os livros e fazendo a similaridade de Jaccard para cada um deles
    list3 = []
    cont = 0

    for book in enumerate(books):
        a = book
        list3.append(a) 
        cont += 1
    for i in books:
        aux = 0
        position = 0
        book_similarity[i] = dict()
        for j in books[i]:
            list1.append(j)
        while(aux < cont):
            if(aux != i):
                for j in books[list3[aux][1]]:
                    list2.append(j)
            result = Funções.jaccard(list1, list2)  
            book_similarity[i][list3[aux][1]] = result
            aux += 1
            list2 = []
        list1 = []


similarity_table = Table.create_similarity_table(book_similarity, "book_similarity")
similarity_table1 = Table.create_similarity_table(user_similarity, "user_similarity")

# Imprimir a tabela
print(similarity_table)

print( " ------------------------------------------------------------------------------------------------------------------ ")

print(similarity_table1)