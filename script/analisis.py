from scipy import stats as st
import numpy as np
import pandas as pd

def mean(arr):
    means = []
    for v in arr :
        means.append(np.mean(v))
    return np.array(means)

def hmean(arr):
    means = []
    for v in arr :
        means.append(st.hmean(v))
    return np.array(means)

# Leer datos
b_df = pd.read_excel('../datos/datos_benchmark.xlsx')

# Obtener datos de tiempo de respuesta
rt_data = np.c_[
    b_df['GZip'].values, b_df['DCRAW'].values, b_df['FLAC'].values, 
    b_df['GnuPG'].values, b_df['MAFFT'].values, b_df['MrBayes'].values, 
    b_df['MPlayer'].values, b_df['PHP'].values
]

# Obtener datos de desempeño
pr_data = np.c_[		
    b_df['REDIS_LPOP'].values, b_df['REDIS_SADD'].values,
    b_df['REDIS_LPUSH'].values, b_df['REDIS_GET'].values, 
    b_df['REDIS_SET'].values
]

# Calculando medida de tiempo de respuesta (media armónica)
arm_mean = hmean(rt_data)

# Calculando medida de rendimiento (media aritmética)
arit_mean = mean(pr_data)

#Imprimiendo resultados
for i in range(len(arit_mean)):
    print(i+1, ': arit:', arit_mean[i], 'arm:', arm_mean[i])

# Normalizando y recalculando medias
n = arm_mean.sum()
n_arm_mean = hmean(rt_data / n)

n = arit_mean.sum()
n_arit_mean = mean(pr_data / n)

#Imprimiendo resultados
print('Normalizado')
for i in range(len(n_arit_mean)):
    print(i+1, ': arit:', n_arit_mean[i], 'arm:', n_arm_mean[i])
