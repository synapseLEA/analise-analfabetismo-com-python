from pathlib import Path

import streamlit as st
from analise import *
from clusters import *

st.title("Análise de Dados Sociais com Python")

descricao = st.container(border=True)
descricao.text("Esta aplicação web foi desenvolvida com o propósito de facilitar a visualização e manipulação de dados sociais, enfatizando a taxa de analfabetismo da população de 15 anos ou mais por município do maranhão.")

st.subheader("Visualização dos Dados")
visualizacao_dados = st.container(border=True)
linhas_visualizacao = visualizacao_dados.number_input(
    "Selecione a quantidade de linhas que deseja visualizar:",
    min_value=1,
    max_value=quantidade_linhas(),
    value=5
)
visualizacao_dados.dataframe(visualizar_tabela(linhas_visualizacao))
visualizacao_dados.download_button(label="Baixar dados tratados", data = df.to_csv(index=False), file_name = 'dataframe_analfabetismo_tratado')

st.subheader("Visualização Gráfica Percentual de cada Município")
visualizacao_grafica_percentual = st.container(border=True)
tipo = visualizacao_grafica_percentual.selectbox(
    "Selecione qual o tipo de dado que deseja filtrar:",
    options=["Percentual Médio de não Alfabetizados","Percentual Médio de Alfabetizados"]
)
ordenacao = visualizacao_grafica_percentual.radio(
    "Seleciona qual o tipo de ordenação deseja:",
    options=["Crescente","Decrescente"],
    key=1
)
linhas = visualizacao_grafica_percentual.number_input(
    "Selecione a quantidade de dados que deseja visualizar:",
    min_value=1,
    value=5,
    max_value=quantidade_linhas()
)

visualizacao_grafica_percentual.pyplot(
    fig=agrupamento_municipio_percentual(
        tipo,
        ordenacao,
        linhas
    ),
    width="stretch"
)

st.subheader(
    "Visualização Gráfica da Distribuição da População Alfabetizada e não Alfabetizada por Município"
)
distribuicao = st.container(border=True)
linhas = distribuicao.number_input(
    "Selecione a quantidade de municípios que deseja visualizar:",
    min_value=1,
    value=5,
    max_value=quantidade_linhas()
)
ordenacao = distribuicao.radio(
    "Seleciona qual o tipo de ordenação deseja para os dados da população não alfabetizada:",
    options=["Crescente","Decrescente"],
    key=2
)
distribuicao.pyplot(
    fig=distribuicao_alfabetismo_analfabetismo_munipicios(
        ordenacao,
        linhas
    ),
    width="stretch"
)

st.subheader(
    "Visualização da Distribuição dos Valores Numéricos de Cada Ano"
)
st.pyplot(
    fig=distribuicao_anos(),
    width="stretch"
)

st.subheader(
    "Visualização da Progressão do Analfabetismo por Município ao Decorrer dos Anos"
)
progressao_analfabetismo = st.container(border=True)
municipio_escolhido = progressao_analfabetismo.selectbox(
    "Seleciona qual o município que deseja visualizar a progressão do analfabetismo:",
    options=nomes_municipios(),
    key=3
)
progressao_analfabetismo.pyplot(
    fig=grafico_progressao_unico_municipio(
        municipio_escolhido
    ),
    width="stretch"
)

st.subheader(
    "Visualização Comparativa da Taxa de Analfabetismo entre Municípios"
)
grafico_comparativo = st.container(border=True)
municipios_escolhidos = grafico_comparativo.multiselect(
    "Selecione os municípios que deseja comparar: ",
    options=nomes_municipios(),
    placeholder="",
    default=["São Luís", "Imperatriz"]
)
if(len(municipios_escolhidos) > 1):
    grafico_comparativo.pyplot(
        fig=grafico_progressao_municipios(municipios_escolhidos),
        width="stretch"
    )
else:
    grafico_comparativo.warning("Por favor, selecione mais de um município para continuar.")


# Funcionalidades novas referentes a segunda versão do projeto

st.subheader(
    "Aplicação de Algoritmos de Regressão para Previsão da Taxa do Analfabetismo nos Anos Posteriores"
)
sessao_algoritmos_regressao = st.container(border=True)
sessao_algoritmos_regressao.warning(
    """
    Todos os modelos de aprendizado de máquina foram implementados utilizando a biblioteca Scikit-learn (sklearn) e CatBoost. 
    Os dados foram divididos em conjuntos de treino e teste, utilizando 80% para treinamento e 20% para teste.

    As métricas utilizadas para avaliar e selecionar o melhor modelo foram:

    - **MSE (Mean Squared Error - Erro Quadrático Médio)**: Esta métrica calcula a média dos quadrados dos erros, ou seja, a diferença quadrática entre os valores preditos e os valores reais. O MSE é útil porque penaliza erros maiores de forma mais severa, dando maior peso aos outliers. Quanto menor o valor do MSE, melhor é o desempenho do modelo.

    - **R² Score (Coeficiente de Determinação)**: Esta métrica indica a proporção da variância dos dados que é explicada pelo modelo. O R² varia de 0 a 1, onde valores mais próximos de 1 indicam que o modelo consegue explicar melhor a variabilidade dos dados. Em outras palavras, quanto maior o R², mais preciso é o modelo em suas predições.
    """
)
sessao_algoritmos_regressao.markdown(
    "**Aplicando Modelo de Regressão Linear Simples**"
)
sessao_regressao_linear = sessao_algoritmos_regressao.container(border=True)
sessao_regressao_linear.pyplot(
    fig = modelo_regressao_linear()[-1],
    width="stretch"   
)
sessao_regressao_linear.markdown(
    f"""
    Resultados do Modelo:
    - **MSE:** {modelo_regressao_linear()[0]:.2f}
    - **R² :** {modelo_regressao_linear()[1] * 100:.2f} %
    """
)


sessao_algoritmos_regressao.markdown(
    "**Aplicando o Modelo de Árvore de Decisão**"
)

sessao_arvore_decisao = sessao_algoritmos_regressao.container(border=True)
sessao_arvore_decisao.pyplot(
    fig = modelo_arvore_decisao()[-1],
    width="stretch"
)
sessao_arvore_decisao.markdown(
    f"""
    Resultados do Modelo:
    - **MSE:** {modelo_arvore_decisao()[0]:.2f}
    - **R² :** {modelo_arvore_decisao()[1] * 100:.2f} %
    """
)


sessao_algoritmos_regressao.markdown(
    "**Aplicando o Modelo de Random Forest**"
)

sessao_random_forest = sessao_algoritmos_regressao.container(border=True)
sessao_random_forest.pyplot(
    fig = modelo_random_forest()[-2],
    width="stretch"
)
sessao_random_forest.markdown(
    f"""
    Resultados do Modelo:
    - **MSE:** {modelo_random_forest()[0]:.2f}
    - **R² :** {modelo_random_forest()[1] * 100:.2f} %
    """
)

st.subheader("Previsão da Taxa de Analfabetismo")
sessao_previsao_taxa = st.container(border = True)
municipio_escolhido = sessao_previsao_taxa.selectbox(
    "Seleciona qual o município que deseja realizar a previsão da taxa de analfabetismo",
    options=nomes_municipios(),
    key=4
)
ano_escolhido = sessao_previsao_taxa.number_input(
    "Escolha o ano da previsão",
    min_value = 2023
)


sessao_previsao_taxa.text(
    f"Taxa prevista para o ano de {ano_escolhido}: {previsao_taxa_analfabetismo(municipio_escolhido, ano_escolhido)[-1]:.2f}%"
)
sessao_previsao_taxa.pyplot(
    fig = grafico_previsao(municipio_escolhido, ano_escolhido),
    width="stretch"
)

df = clusterizacao(df)
df, clusters_media = gruposclusters(df)
grupos = grupos_alerta(df)

st.subheader("Aplicação de Clusters Hierárquicos para Geração de Alertas")

sessao_clusters = st.container(border=True)

sessao_clusters.warning(
    """
    Aplicação de clusters hierárquicos para a criação de alertas para municípios em
    diferentes grupos, com base no percentual médio de não alfabetizados.
    """
)

grupo_escolhido = sessao_clusters.selectbox(
    "Selecione um grupo",
    options=list(grupos.keys()),
    key="clusters_grupo"
)

sessao_grupo_cluster = sessao_clusters.container(border=True)

sessao_grupo_cluster.subheader(f"Municípios em {grupo_escolhido}")

sessao_grupo_cluster.dataframe(
    grupos[grupo_escolhido][
        [
            "Município",
            "Percentual Médio de não Alfabetizados",
            "categoria_alerta",
            "cluster",
        ]
    ],
    width="stretch"
)

diretorio_arquivo = Path(__file__).resolve().parent
caminho_logo = diretorio_arquivo / '..' / 'img' / 'logo.png'
redes_sociais = st.container(border=True)
redes_sociais.image(caminho_logo)

