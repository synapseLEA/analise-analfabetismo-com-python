import pandas as pd
from pandas import DataFrame

def dataset_limpo() -> DataFrame:
    """
    Realiza a limpeza, transformação e a engenharia de atributos no conjunto de dados.

    A função carrega o arquivo 'bancodados.csv', renomeia colunas,
    ajusta tipos de dados e calcula novas colunas percentuais.

    Returns:
        DataFrame: Um DataFrame limpo e preparado para análise, contendo
                   as colunas originais e as novas colunas calculadas
                   'Percentual Médio de não Alfabetizados' e
                   'Percentual Médio de Alfabetizados'.
    """
    
    # Carrega o arquivo CSV usando ponto e vírgula como separador e vírgula como decimal
    df = pd.read_csv("bancodados.csv", sep=";", decimal=",")
    
    # Remove a primeira linha do DataFrame, que contém dados irrelevantes
    df = df.drop(0, axis=0)
    
    # Dicionário para armazenar os nomes das colunas originais para nomes mais claros
    nomes_colunas = {
        "Unnamed: 0": "Sigla",
        "Unnamed: 1": "Código",
        "Unnamed: 2": "Município",
        "Unnamed: 3": "1991 (%)",
        "Unnamed: 4": "2000 (%)",
        "Unnamed: 5": "2010 (%)",
        "Unnamed: 6": "2022 (%)",
    }
    
    # Renomeia as colunas do DataFrame
    df = df.rename(columns=nomes_colunas)
    
    # Converte a coluna 'Código' para o tipo inteiro
    df["Código"] = df["Código"].astype(int)
    
    # Lista as colunas de anos para facilitar os cálculos
    colunas_anos = ["1991 (%)", "2000 (%)", "2010 (%)", "2022 (%)"]
    
    # Calcula o percentual médio de não alfabetizados para cada município e cria uma nova coluna
    df["Percentual Médio de não Alfabetizados"] = df[colunas_anos].mean(axis=1)
    
    # Calcula o percentual médio de alfabetizados subtraindo o valor anterior de 100 e cria uma nova coluna
    df["Percentual Médio de Alfabetizados"] = 100 - df["Percentual Médio de não Alfabetizados"]
    
    # Retorna o DataFrame limpo e com as novas colunas
    return df


