# Laboratorio 3- Visualización y Exploración
# Diseñado por- Luis Gabriel Tejada Figueroa

# Problema- Visualización y Exploración de Datos

# Importación de librerías y archivo
import numpy as np
import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, MinMaxScaler, StandardScaler
from pandas.plotting import scatter_matrix

passengers = pd.read_csv("C:\\Users\\luist\\Desktop\\passangers_2.csv")

#%% Parte 1- Reemplazo de valores nan a promedio

#Reemplazar valores nan al valor promedio de la columna fare
fare_mean = passengers['Fare'].mean()
passengers['Fare'].fillna(fare_mean, inplace=True)

#Reemplazar valores de letras por el valor promedio
passengers['Ticket_numeric'] = pd.to_numeric(passengers['Ticket'], errors='coerce')
ticket_mean = passengers['Ticket_numeric'].mean()  

passengers['Ticket_numeric'].fillna(ticket_mean, inplace=True)
passengers.drop('Ticket', axis=1, inplace=True)  
passengers.rename(columns={'Ticket_numeric': 'Ticket'}, inplace=True)

#%% Parte 2- Usar función OrdinalEncoder de la librería sklearn

encoder = OrdinalEncoder()
columns_to_encode = ['Sex', 'Embarked']
passengers[columns_to_encode] = encoder.fit_transform(passengers[columns_to_encode])

#%% Parte 3- Correlaciones visuales

attributes1 = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Ticket"]
scatter_matrix(passengers[attributes1], alpha=0.2, figsize=(20, 20))

#%% Parte 4- Correlaciones con coeficiente de Pearson

numeric_columns = passengers.select_dtypes(include=[np.number])
corr_matrix = numeric_columns.corr()

#%% Parte 5- Contestación a pregunta

#Para hallar la contestación a la pregunta 5, favor de referirse al informe de la asignación. 

#%% Parte 6- Fila de Familia

# Creación de columna familia
passengers['Familia'] = passengers['SibSp'] + passengers['Parch']

# Calculo de correlación usando coeficiente de Pearson
attributes2 = ["Survived", "Pclass", "Sex", "Age", "SibSp", "Parch", "Fare", "Embarked", "Ticket", "Familia"]

corrf_matrix = passengers[attributes2].corr()


#%% Parte 7- Normalizar y estandarizar conjunto de datos

# Normalizacion de datos
norm = MinMaxScaler()
norm_data = norm.fit_transform(passengers[attributes2])

# Estandarización de datos
est = StandardScaler()
est_data = est.fit_transform(passengers[attributes2])

#Calcular coeficiente de Pearson con datos normalizados
norm_data_df = pd.DataFrame(norm_data, columns=attributes2)
norm_numbers = norm_data_df.select_dtypes(include=[np.number])

corrn_matrix = norm_numbers.corr()

#Calcular coeficiente de Pearson con datos estandarizados
est_data_df = pd.DataFrame(est_data, columns=attributes2)
est_numbers = est_data_df.select_dtypes(include=[np.number])

corre_matrix = est_numbers.corr()
