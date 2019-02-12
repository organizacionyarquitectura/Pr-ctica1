from scipy import stats as st
import numpy as np
import pandas as pd

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
arm_mean = []

for v in rt_data :
    arm_mean.append(st.hmean(v))

# Calculando medida de rendimiento (media aritmética)
arit_mean = []

for v in pr_data :
    arit_mean.append(np.mean(v))

#Imprimiendo resultados
for i in range(len(arit_mean)):
    print(i+1, ': arit:', arit_mean[i], 'arm:', arm_mean[i])
