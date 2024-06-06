import pandas as pd
import numpy as np

# Generar 200 precios en el rango de 50 a 500
np.random.seed(0)  # Para reproducibilidad
precios = np.random.uniform(50, 500, 500)

# Simular la demanda (cantidad) con una relación inversa al precio más algo de ruido
cantidades = 1000 / precios + np.random.normal(0, 10, 500)

# Crear un DataFrame
df = pd.DataFrame({
    'precio': precios,
    'cantidad': cantidades
})

# Asegurarse de que las cantidades sean positivas
df['cantidad'] = df['cantidad'].clip(lower=0)

# Mostrar los primeros registros del DataFrame
print(df.head())

# Guardar el DataFrame en un archivo CSV
df.to_csv('dataset_demanda_electrodomesticos.csv', index=False)
