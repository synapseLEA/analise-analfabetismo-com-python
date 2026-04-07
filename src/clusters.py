from analise import *
from limpeza import *
from scipy.cluster.hierarchy import fcluster, dendrogram, linkage
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


def dendrogama(df):
    dfnum = df.select_dtypes(include=['number'])
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(dfnum)

    z = linkage(x_scaled, method='ward')
    dendrogram(z)
    plt.show()

    return z

def clusterizacao(df):
    z = dendrogama(df)
    clusters = fcluster(z, t=4, criterion='maxclust')
    df["cluster"] = clusters
    
    return df

def gruposclusters(df):
    clusters_media = df.groupby("cluster")["Percentual Médio de não Alfabetizados"].mean().sort_values(ascending=False)

    labels = ["Alerta Vermelho", "Alerta Laranja", "Alerta Amarelo", "Alerta Verde"]

    categorias_alerta = {
        clusters_media.index[i]: labels[i]
        for i in range(len(clusters_media))
    }

    df["categoria_alerta"] = df["cluster"].map(categorias_alerta)

    return df, clusters_media
    
def grupos_alerta(df):
    grupos = {}

    for alerta in df["categoria_alerta"].unique():
        grupos[alerta] = df[df["categoria_alerta"] == alerta].sort_values(
            "Percentual Médio de não Alfabetizados",
            ascending=False)

    return grupos