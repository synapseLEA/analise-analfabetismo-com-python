import streamlit as st
from analise import *

st.title("Análise de Dados Sociais com Python")

descricao = st.container(border=True)
descricao.text("Esta aplicação web foi desenvolvida com o proprósito de facilitar a visualização e manipulação de dados sociais, enfatizando a taxa de analfabetismo da população de 15 anos ou mais por município do maranhão.")

st.subheader("Visualização dos Dados")
visualizacao_dados = st.container(border=True)
linhas_visualizacao = visualizacao_dados.number_input(
    "Selecione a quantidade de linhas que deseja visualizar:",
    min_value=1,
    max_value=quantidade_linhas(),
    value=5
)
visualizacao_dados.dataframe(visualizar_tabela(linhas_visualizacao))

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

st.pyplot(
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
st.pyplot(
    fig=distribuicao_alfabetismo_analfabetismo_munipicios(
        ordenacao,
        linhas
    ),
    width="stretch"
)

st.subheader(
    "Visualização da Distribuição dos Valores Númericos de Cada Ano"
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
st.pyplot(
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
    st.pyplot(
        fig=grafico_progressao_municipios(municipios_escolhidos),
        width="stretch"
    )
else:
    grafico_comparativo.warning("Por favor, selecione mais de um município para continuar.")


redes_sociais = st.container(border=True)
redes_sociais.image("logo.png")
