import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from limpeza import dataset_limpo
from pandas import DataFrame

sns.set_theme(style="whitegrid")
sns.set_palette("muted")
df = dataset_limpo()

def visualizar_tabela(numero_linhas:int) -> DataFrame:
    return df.head(numero_linhas)

def quantidade_linhas() -> int:
    return df.shape[0]

def agrupamento_municipio_percentual(tipo:str,ordenacao:str,quantidade_linhas:int):
    fig, ax = plt.subplots(figsize=(10,5))
    if(quantidade_linhas <= 5):
        if(ordenacao == "Crescente"):
            agrupamento = df.groupby("Município")[tipo].sum().sort_values(ascending=True).head(quantidade_linhas)
        else:
            agrupamento = df.groupby("Município")[tipo].sum().sort_values(ascending=False).head(quantidade_linhas)
        grafico = sns.barplot(x=agrupamento.index,y=agrupamento.values,ax=ax)
        for valor in ax.containers:
            grafico.bar_label(valor,fmt="%.2f%%")
        ax.set_title(tipo)
        ax.set_xlabel("Municípios")
        ax.set_ylabel("Distribuição Percentual (%)")
        sns.despine()
    else:
        if(ordenacao == "Crescente"):
            agrupamento = df.groupby("Município")[tipo].sum().sort_values(ascending=True).head(quantidade_linhas)
        else:
            agrupamento = df.groupby("Município")[tipo].sum().sort_values(ascending=False).head(quantidade_linhas)
        grafico = sns.barplot(y=agrupamento.index,x=agrupamento.values,ax=ax)
        for valor in ax.containers:
            grafico.bar_label(valor,fmt="%.2f%%")
        ax.set_title(tipo)
        ax.set_ylabel("Municípios")
        ax.set_xlabel("Distribuição Percentual (%)")
        sns.despine()
    return fig

def distribuicao_alfabetismo_analfabetismo_munipicios(ordenacao:str,quantidade_linhas:int):
    fig, ax = plt.subplots(figsize=(12,5))
    if(quantidade_linhas <= 5):
        if(ordenacao == "Crescente"):
            agrupamento_nao_alfabetizados = df.groupby("Município")["Percentual Médio de não Alfabetizados"].sum().sort_values(ascending=True).head(quantidade_linhas)
            agrupamento_alfabetizados = df.groupby("Município")["Percentual Médio de Alfabetizados"].sum().sort_values(ascending=False).head(quantidade_linhas)
        else:
            agrupamento_nao_alfabetizados = df.groupby("Município")["Percentual Médio de não Alfabetizados"].sum().sort_values(ascending=False).head(quantidade_linhas)
            agrupamento_alfabetizados = df.groupby("Município")["Percentual Médio de Alfabetizados"].sum().sort_values(ascending=True).head(quantidade_linhas)
        df_nao_alfabetizados = pd.DataFrame({
            "Municípios" : agrupamento_nao_alfabetizados.index,
            "Percentual Médio de não Alfabetizados" : agrupamento_nao_alfabetizados.values,
            "Tipo" : "Não Alfabetizados" 
        })
        df_alfabetizados = pd.DataFrame({
            "Municípios" : agrupamento_alfabetizados.index,
            "Percentual Médio de não Alfabetizados" : agrupamento_alfabetizados.values,
            "Tipo" : "Alfabetizados"
        })
        df_agrupado = pd.concat([
            df_nao_alfabetizados,df_alfabetizados
        ])
        grafico = sns.barplot(
            data=df_agrupado,
            x="Municípios",
            y="Percentual Médio de não Alfabetizados",
            hue="Tipo"
        )
        for valor in grafico.containers:
            grafico.bar_label(valor,fmt="%.2f%%")
        ax.set_title("Comparativo entre Alfabetizados e Não Alfabetizados por Município")
        ax.set_xlabel("Municípios")
        ax.set_ylabel("Distribuição Percentual (%)")
    else:
        if(ordenacao == "Crescente"):
            agrupamento_nao_alfabetizados = df.groupby("Município")["Percentual Médio de não Alfabetizados"].sum().sort_values(ascending=True).head(quantidade_linhas)
            agrupamento_alfabetizados = df.groupby("Município")["Percentual Médio de Alfabetizados"].sum().sort_values(ascending=False).head(quantidade_linhas)
        else:
            agrupamento_nao_alfabetizados = df.groupby("Município")["Percentual Médio de não Alfabetizados"].sum().sort_values(ascending=False).head(quantidade_linhas)
            agrupamento_alfabetizados = df.groupby("Município")["Percentual Médio de Alfabetizados"].sum().sort_values(ascending=True).head(quantidade_linhas)
        df_nao_alfabetizados = pd.DataFrame({
            "Municípios" : agrupamento_nao_alfabetizados.index,
            "Percentual Médio de não Alfabetizados" : agrupamento_nao_alfabetizados.values,
            "Tipo" : "Não Alfabetizados" 
        })
        df_alfabetizados = pd.DataFrame({
            "Municípios" : agrupamento_alfabetizados.index,
            "Percentual Médio de não Alfabetizados" : agrupamento_alfabetizados.values,
            "Tipo" : "Alfabetizados"
        })
        df_agrupado = pd.concat([
            df_nao_alfabetizados,df_alfabetizados
        ])
        grafico = sns.barplot(
            data=df_agrupado,
            y="Municípios",
            x="Percentual Médio de não Alfabetizados",
            hue="Tipo"
        )
        for valor in grafico.containers:
            grafico.bar_label(valor,fmt="%.2f%%")
        ax.set_title("Comparativo entre Alfabetizados e Não Alfabetizados por Município")
        ax.set_ylabel("Municípios")
        ax.set_xlabel("Distribuição Percentual (%)")

    return fig

def distribuicao_anos():
    colunas_anos = ["1991 (%)","2000 (%)","2010 (%)","2022 (%)"]
    colunas_anos_formatada = [valor.replace(" (%)","") for valor in colunas_anos]
    fig,axis = plt.subplots(nrows=4,ncols=3,figsize=(16,4 * 5))
    for i, coluna in enumerate(colunas_anos):
        Quartil1 = df[coluna].quantile(0.25)
        Quartil3 = df[coluna].quantile(0.75)
        IntervaloInterquartil = Quartil3 - Quartil1
        LimiteInferior = Quartil1 - 1.5 * IntervaloInterquartil
        cores = ["red" if valor < LimiteInferior else "c" for valor in df[coluna]]

        sns.boxplot(data=df[coluna],ax=axis[i][0])
        axis[i][0].set_title("Resumo Estatístico das Taxas de Analfabetismo por Município")
        axis[i][0].set_ylabel("Taxa de Analfabetismo (%)")
        axis[i][0].set_xlabel(f"Ano de {colunas_anos_formatada[i]}")

        sns.scatterplot(x=df.index,y=df[coluna],ax=axis[i][1],color=cores)
        axis[i][1].set_title("Dispersão das Taxas de Analfabetismo nos Municípios")
        axis[i][1].set_ylabel("Taxa de Analfabetismo (%)")
        axis[i][1].set_xlabel("Dispersão das Taxas")
        
        sns.violinplot(data=df[coluna],ax=axis[i][2],orient='h')
        
        axis[i][2].set_title("Densidade e Distribuição das Taxas de Analfabetismo")
        axis[i][2].set_xlabel("Taxa de Analfabetismo (%)")
        axis[i][2].set_ylabel(f"Ano de {colunas_anos_formatada[i]}")

    plt.tight_layout()
    return fig

def nomes_municipios():
    return df["Município"].values

def grafico_progressao_unico_municipio(municipio:str):
    colunas_anos = ["1991 (%)","2000 (%)","2010 (%)","2022 (%)"]
    colunas_anos_formatada = [valor.replace(" (%)","") for valor in colunas_anos]
    dados_municipio = df[df["Município"] == municipio]
    anos = colunas_anos_formatada
    valores = dados_municipio[colunas_anos].values.reshape(1,-1)[0]
    fig, ax = plt.subplots(figsize=(10,5))
    sns.lineplot(
        x=anos,
        y=valores,
        ax=ax,
        marker="o",
        linestyle="--"
    )
    for i, valor in enumerate(valores):
        ax.text(
        i,
        valor + 1,
        f"{valor:.2f}%",
        ha="center",
        fontweight="bold")
    ax.grid(
        True,
        linestyle="--",
        alpha=0.6
    )
    ax.set_title(f"Taxa de Analfabetismo em {municipio} ao Decorrer dos Anos")
    ax.set_xlabel("Ano")
    ax.set_ylabel("Taxa de Analfabetismo (%)")
    ax.set_ylim(
        0,
        valores.max() * 1.5
    )
    return fig

def grafico_progressao_municipios(municipios:str):
    fig, ax = plt.subplots(figsize=(10,5))
    colunas_anos = ["1991 (%)","2000 (%)","2010 (%)","2022 (%)"]
    colunas_anos_formatada = [valor.replace(" (%)","") for valor in colunas_anos]
    df_comparacao = df[df["Município"].isin(municipios)]
    df_comparacao = df_comparacao.rename(columns=dict(zip(colunas_anos, colunas_anos_formatada)))
    df_agrupado_municipios = pd.melt(
        df_comparacao,
        id_vars=["Município"],
        value_vars=colunas_anos_formatada,
        var_name="Ano",
        value_name="Taxa"
    )
    sns.lineplot(
        data=df_agrupado_municipios,
        x="Ano",
        y="Taxa",
        hue="Município",
        marker="o",
        linestyle="--"
    )
    for posicao, linha in df_agrupado_municipios.iterrows():
        ax.text(
            x=linha["Ano"],
            y=linha["Taxa"] + 1.5,
            s=f"{linha["Taxa"]:.2f}%",
            ha="center",
            va="bottom",
            fontsize=8,
            fontweight="bold"
        )
    municipios_str = ', '.join(municipios)
    ax.set_title(f"Taxa de Analfabetismo entre os Municípios {municipios_str}")    
    ax.set_xlabel("Ano")
    ax.set_ylabel("Taxa de Analfabetismo (%)")
    return fig
    
    