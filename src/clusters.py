from analise import *
from limpeza import *
from scipy.cluster.hierarchy import fcluster, dendrogram, linkage
from sklearn.preprocessing import StandardScaler




#df = limpezaDataframe()

def dendrogama(df):
    dfnum = df.select_dtypes(include=['number'])
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(dfnum)
    
    z = linkage(x_scaled, method='ward')
    dendrogram(z)
    plt.show()
    return z

#z = dendrogama(df) 
#clusters = fcluster(z, t=4, criterion='maxclust')
#df['cluster'] = clusters

def clusterizacao(df):
    clusters = fcluster(z, t=4, criterion='maxclust')
    df["clusters"] = clusters
 

    return df

def gruposclusters(df):
    clusters_media = df.groupby("cluster")["Percentual Médio de não Alfabetizados"].mean().sort_values(ascending=False)

    categorias_alerta = {
        clusters_media.index[0]: "Alerta Vermelho",
        clusters_media.index[1]: "Alerta Laranja",
        clusters_media.index[2]: "Alerta Amarelo",
        clusters_media.index[3]: "Alerta Verde"
    }

    df["categorias_alerta"] = df["cluster"].map(categorias_alerta)

    return df, clusters_media

#for col in df.columns:
#    print(col)

#df_teste, cluster_media = gruposclusters(df)

#print(cluster_media)
#print(df_teste.head())


