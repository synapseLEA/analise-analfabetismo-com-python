import os

import pandas as pd
from pandas import DataFrame
from pathlib import Path

def limpezaDataframe() -> DataFrame:
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
    diretorio_arquivo = Path(__file__).resolve().parent
    caminho_dataframe = diretorio_arquivo / '..' / 'data' / 'dados_analfabetismo_municipios.csv'
    df = pd.read_csv(caminho_dataframe, sep=";", decimal=",")
    
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
    df["Percentual Médio de não Alfabetizados"] = df[colunas_anos].mean(axis=1).round(2)
    
    # Calcula o percentual médio de alfabetizados subtraindo o valor anterior de 100 e cria uma nova coluna
    df["Percentual Médio de Alfabetizados"] = (100 - df["Percentual Médio de não Alfabetizados"]).round(2)
    
    # Retorna o DataFrame limpo e com as novas colunas
    return df


#Cria um DataFrame tratado para aplicar modelos de aprendizado de máquina
def dataframe_modificado_ml() -> DataFrame:
    df = limpezaDataframe()
    
    #Remove as colunas de valores não numéricos
    colunas_remover = ['Município',
                   'Sigla',
                   'Código',
                   'Percentual Médio de Alfabetizados']
    
    #Renomeia colunas para facilitar a chamada das colunas
    colunas_renomear = {
        '1991 (%)' : '1991',
        '2000 (%)' : '2000',
        '2010 (%)' : '2010',
        '2022 (%)' : '2022'
    }
    
    #Removendo as colunas no DataFrame
    df = df.drop(columns=colunas_remover)
    
    #Renomeando as colunas no DataFrame
    df = df.rename(columns=colunas_renomear)
    
    #Transforma os anos em linhas, mantendo a média como identificador
    df_alterado = df.melt(id_vars = 'Percentual Médio de não Alfabetizados',
                  value_name = 'Taxa', var_name= 'Ano')
    
    #Certifica que a coluna de ano são números inteiros
    df_alterado['Ano'] = df_alterado['Ano'].astype(int)
    
    #Retorna DataFrame atualizado para o uso de aprendizado de máquina
    return df_alterado

def dataframe_previsao():
    df = limpezaDataframe().copy()

    colunas_remover = ['Sigla',
                   'Código']
    
    df = df.drop(columns=colunas_remover)
    
    colunas_renomear = {
        '1991 (%)' : '1991',
        '2000 (%)' : '2000',
        '2010 (%)' : '2010',
        '2022 (%)' : '2022'
    }

    df = df.rename(columns=colunas_renomear)

    df_melt = df.melt(
        id_vars=['Município', 'Percentual Médio de não Alfabetizados'],
        value_vars=['1991', '2000', '2010', '2022'],
        var_name='Ano',
        value_name='Taxa'
    )

    df_melt['Ano'] = df_melt['Ano'].astype(int)

    return df_melt