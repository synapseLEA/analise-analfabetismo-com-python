
# Análise da taxa de analfabetismo da população com 15 anos ou mais nos municípios do Maranhão.

Este projeto foi desenvolvido com o propósito de disponibilizar, de forma gratuita (open source), um **dashboard interativo online** que contém informações sobre a taxa de analfabetismo nos municípios do estado do Maranhão. Dessa forma, proporcionamos à população uma visualização rápida e simples dos dados, permitindo realizar comparações anuais, observar a evolução da taxa ao decorrer dos anos, fazer análises específicas por município e verificar o percentual da população alfabetizada e não alfabetizada.

## Funcionalidades

- Visualização dos Dados
- Visualização Gráfica Percentual de cada Município
- Visualização Gráfica da Distribuição da População Alfabetizada e não Alfabetizada por Município
- Visualização da Distribuição dos Valores Numéricos de Cada Ano
- Visualização da Progressão do Analfabetismo por Município ao Decorrer dos Anos
- Visualização Comparativa da Taxa de Analfabetismo entre Municípios



## Tecnologias Utilizadas

- **Linguagem:** Python 3.x
- **Análise de Dados:** Pandas, NumPy
- **Interface (Front-end):** Streamlit
- **Cloud/Hospedagem:** Streamlit Cloud (Community Cloud)


## Rodar Localmente

Para executar o projeto localmente na sua máquina, siga os passos abaixo:

1 - Clone o repositório:

```bash
  git clone https://github.com/synapseLEA/analise-analfabetismo-com-python.git
```

2 - Vá para a pasta do projeto:

```bash
  cd analise-analfabetismo-com-python
```

3 - Crie um ambiente virtual:

```bash
    python -m venv .ambienteVirtual
```

4 - Ative o ambiente vitual

- **Windows:**
```bash
    .ambienteVirtual\Scripts\activate
```
- **Linux/Mac:**
```bash
    source .ambienteVirtual/bin/activate
```

5 - Instale as dependências

```bash
  pip install -r requirements.txt
```

6 - Inicie o servidor do Streamlit

```bash
  streamlit run src/site.py
```


## Autores

O projeto foi desenvolvido pela equipe do **Synapse Lab**, vertente de análise de dados do **Laboratório de Engenharia Aplicada (LEA)**, situado na Universidade Estadual do Maranhão (UEMA).

- [@JulioCesra](https://github.com/JulioCesra)
- [@L-MaiaCode](https://github.com/L-MaiaCode)
- [@amorimcarlos](https://github.com/amorimcarlos)
- [@elisasilva06](https://github.com/elisasilva06)
- [@samyralobo](https://github.com/samyralobo)
- [@BrunoAndrade-dev](https://github.com/BrunoAndrade-dev)


