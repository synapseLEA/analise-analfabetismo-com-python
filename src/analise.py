import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from limpeza import Path, dataframe_modificado_ml, limpezaDataframe
from pandas import DataFrame
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid")
sns.set_palette("muted")
df = limpezaDataframe()

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
    for _, linha in df_agrupado_municipios.iterrows():
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

def conjunto_treino_teste():
    df_alterado = dataframe_modificado_ml()
    X = df_alterado.drop(columns='Taxa', axis = 1)
    y = df_alterado['Taxa']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size = 0.2, random_state = 42
    )
    return X_train, X_test, y_train, y_test

def modelo_regressao_linear():
    fig, axs = plt.subplots(figsize=(12,5))
    X_train, X_test, y_train, y_test = conjunto_treino_teste()
    LR = LinearRegression()
    LR.fit(X_train, y_train)
    LR_pred = LR.predict(X_test)
    mse = mean_absolute_error(y_test, LR_pred)
    r2 = r2_score(y_test, LR_pred)
    sns.regplot(x = y_test, y = LR_pred, line_kws={'color' : 'red'})
    axs.set_xlabel("Valores Reais")
    axs.set_ylabel("Valores Previstos")
    axs.set_title("Previsão com o modelo de Regressão Linear Simples")
    return mse, r2, fig

def modelo_arvore_decisao():
    fig, axs = plt.subplots(figsize=(12,5))
    X_train, X_test, y_train, y_test = conjunto_treino_teste()
    DT = DecisionTreeRegressor(
    criterion = 'squared_error',
    random_state = 42
    )
    DT.fit(X_train, y_train)
    DT_pred = DT.predict(X_test)
    mse = mean_absolute_error(y_test, DT_pred)
    r2 = r2_score(y_test, DT_pred)
    sns.regplot(x = y_test, y = DT_pred, line_kws={'color' : 'red'})
    axs.set_xlabel("Valores Reais")
    axs.set_ylabel("Valores Previstos")
    axs.set_title("Previsão com o modelo de Árvore de Decisão")
    return mse, r2, fig

def modelo_random_forest():
    fig, axs = plt.subplots(figsize=(12,5))
    X_train, X_test, y_train, y_test = conjunto_treino_teste()
    RF = RandomForestRegressor(
        n_estimators = 100,
        criterion = 'squared_error',
        random_state = 42
    )
    RF.fit(X_train, y_train)
    RF_pred = RF.predict(X_test)
    mse = mean_absolute_error(y_test, RF_pred)
    r2 = r2_score(y_test, RF_pred)
    sns.regplot(x = y_test, y = RF_pred, line_kws={'color' : 'red'})
    axs.set_xlabel("Valores Reais")
    axs.set_ylabel("Valores Previstos")
    axs.set_title("Previsão com o modelo de Random Forest")
    return mse, r2, fig, RF

def previsao_taxa_analfabetismo(nome_municipio: str, ano_previsao: int):
    dataframe_original = limpezaDataframe()
    dados_municipio = dataframe_original[dataframe_original['Município'] == nome_municipio]
    media_analfabetismo = dados_municipio['Percentual Médio de não Alfabetizados'].values[0]
    dados_previsao = pd.DataFrame(
        {'Percentual Médio de não Alfabetizados': [media_analfabetismo],
        'Ano': [ano_previsao]}
    )
    previsao = modelo_random_forest()[-1].predict(dados_previsao)
    taxa_prevista = previsao[0]
    return media_analfabetismo, taxa_prevista

def grafico_previsao(nome_municipio: str, ano_previsao: int):
    fig, axs = plt.subplots(figsize=(17, 8))
    df_melt = dataframe_modificado_ml()
    media_analfabetismo, taxa_prevista = previsao_taxa_analfabetismo(nome_municipio, ano_previsao)
    dados_historicos = df_melt[df_melt['Percentual Médio de não Alfabetizados'] == media_analfabetismo]
    axs.plot(dados_historicos['Ano'], dados_historicos['Taxa'], 'o-', label='Dados Históricos', linewidth=2)
    axs.plot(ano_previsao, taxa_prevista, 'rs', label=f'Previsão {ano_previsao}', markersize=10)
    axs.set_xlabel('Ano')
    axs.set_ylabel('Taxa de Analfabetismo (%)')
    axs.set_title(f'Taxa de Analfabetismo - {nome_municipio}')
    axs.legend()
    axs.grid(True, alpha=0.3)
    return fig