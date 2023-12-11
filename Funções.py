#Funções de similaridade para o auxílio na recomendação de livros


def jaccard(list1, list2):
    intersection = len(list(set(list1).intersection(list2)))
    union = (len(list1) + len(list2)) - intersection
    return float (intersection)/union


    