import pandas as pd


def create_similarity_table(similarity_map, name):
    # Criar um DataFrame a partir do dicionário de similaridade
    df = pd.DataFrame.from_dict(similarity_map, orient='index')
    
    if(name == "book_similarity"):
    # Adicionar rótulos às colunas
        df.columns = [f'Livro {book}' for book in df.columns]
    
    #Adicionando rótulos às linhas
        df.index = [f'Livro {book}' for book in df.index]

    if(name == "user_similarity"):
    # Adicionar rótulos às colunas
        df.columns = [f'Usuário {user}' for user in df.columns]
    
    #Adicionando rótulos às linhas
        df.index = [f'Usuário {user}' for user in df.index]

    # Preencher células vazias com NaN (ou qualquer valor padrão desejado)
    df = df.fillna('-')

    return df

