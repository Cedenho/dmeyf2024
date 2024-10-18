import pandas as pd

###se trae el archivo con la marcación de la clase ternaria
data = pd.read_csv("C:/Users/Aleja/Documents/Maestria/DMEyF/datasets/competencia_01.csv")

###se filtra por baja+2
data = data[data['clase_ternaria'] == 'BAJA+2']
 
###revisar la cantidad de dimensiones
print(data.shape)

###tengo una columnas que no voy a usar, entonces las borro
data = data.drop(columns=['mes_1', 'mes_2','clase_ternaria'])

###descripcion de las columnas
info = data.describe(include= 'all')
print(info)

#####clustering libreria
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans 
import matplotlib.pyplot as plt

###identificar las columnas numericas
num = data.select_dtypes(include=['int64','float64']).columns

###inicializar el metodo de scalar
scaler = StandardScaler()
data[num] = scaler.fit_transform(data[num])

###inicializar el metodo de kmeans
kmeans = KMeans(n_clusters = 4, random_state = 42)
data['Cluster'] = kmeans.fit_predict(data)

###mirar que hacer con los nulos para poder realizar un kmeans