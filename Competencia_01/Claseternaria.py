import pandas as pd
import numpy as np

###leer archivo de excel
datos = pd.read_csv("C:/Users/Aleja/Documents/Maestria/DMEyF/datasets/competencia_01_crudo.csv")
datosO = datos.copy()

###agregar dos columnas
datos['mes_1'] = datos['foto_mes'] + 1
datos['mes_2'] = datos['foto_mes'] + 2

###dejar solo dos columnas del dataset2
datosO = datosO[['numero_de_cliente','foto_mes']]

###hacer las combinaciones
combinacion = pd.merge(datos, datosO, left_on=['numero_de_cliente','mes_1'], right_on=['numero_de_cliente','foto_mes'], how = 'left')
combinacion = pd.merge(combinacion, datosO, left_on=['numero_de_cliente','mes_2'], right_on=['numero_de_cliente','foto_mes'], how = 'left')

###crear clase ternaria
condiciones = [
    (combinacion['foto_mes_y']>0) & (combinacion['foto_mes']>0),
    (combinacion['foto_mes_y']>0) & (combinacion['foto_mes'].isnull()) & (combinacion['foto_mes_x'] != 202105),
    (combinacion['foto_mes_y'].isnull()) & (combinacion['foto_mes'].isnull()) & (combinacion['foto_mes_x'] != 202106),
    (combinacion['foto_mes_y'].isnull()) & (combinacion['foto_mes']>0)
]

respuesta = ['CONTINUA', 'BAJA+2', 'BAJA+1', 'CONTINUA']

combinacion['clase_ternaria'] = np.select(condiciones, respuesta, default = '')
###eliminar columnas
combinacion = combinacion.drop(columns=['foto_mes', 'foto_mes_y','mes_1','mes_2','cprestamos_personales','mprestamos_personales'])

###actualizar el nombre de una columna
combinacion = combinacion.rename(columns={'foto_mes_x': 'foto_mes'})


combinacion.to_csv("C:/Users/Aleja/Documents/Maestria/DMEyF/datasets/competencia_01.csv")
