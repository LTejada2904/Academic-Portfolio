#Laboratorio 1- Exploración de Datos
#Diseñado por- Luis Gabriel Tejada Figueroa

#%% Problema 1- Creación y manejo de matrices (Numpy)

import numpy as np

#Creación de matrices
np.random.seed(27)
A = np.random.randint(-50, 50, size=(6, 6))
B = np.random.randint(-50, 50, size=(6, 4))

print("La matriz A es: \n{}" .format(A))
print("La matriz B es: \n{}" .format(B))

#Parte A- Encontrar los números comunes. 
inter = np.intersect1d(A, B)
print("\nA. La intersección de las matrices A y B es: \n{}" .format(inter))

#Parte B- Encontrar los números que están en A pero no en B. 
diff = np.setdiff1d(A, B)
print("\nB. La diferencia de las matrices A y B es: \n{}" .format(diff))

#Parte C- Separar la matriz A en dos matrices. 
A1 = A[4:,:]
A2 = A[0:4,:]

print("\nC. La matriz A1 que contiene las últimas dos filas es: \n{}" .format(A1))
print("La matriz A2 que contiene las filas restantes es: \n{}" .format(A2))

#Parte D- Agregar una columna a la matriz B con el elemento máximo de cada fila.
Armax = np.max(A, axis=1)
Bmax = np.column_stack((B, Armax))

#Parte E- Agregar una columna a la matriz B con el elemento mínimo de cada fila.
Armin = np.min(A, axis=1)
Bmin = np.column_stack((Bmax, Armin))
print("\nD. y E. La matriz B dos columnas añadidas que muestran el valor máximo y mínino es: \n{}" .format(Bmin))

#%% Problema 2- Análisis de archivo de pasajeros en el Titanic (Pandas)

import pandas as pd
df = pd.read_csv("C:\\Users\\luist\\Desktop\\passengers.csv")

#Pregunta 1- Ticket 19950
df['Survived'] = df['Survived'].map({0: 'Murió', 1: 'Sobrevivió'})
t19950 = df.loc[df['Ticket'] == '19950', ['Name', 'Survived']]
print("Pregunta 1:")
print("Los miembros de la familia con Ticket 19950 que sobrevivieron y murieron son: \n{}" .format(t19950))

#Pregunta 2- Lugar de embarcación y análisis demográfico.
Southampton = df[df['Embarked'].isin(['S'])]
Queenstown = df[df['Embarked'].isin(['Q'])]

qtyS = Southampton.shape[0] 
qtyQ = Queenstown.shape[0]

SandQ = qtyS + qtyQ

maleS = Southampton[(Southampton['Survived'] == 'Sobrevivió') & (Southampton['Sex'] == 'male')]
maleQ = Queenstown[(Queenstown['Survived'] == 'Sobrevivió') & (Queenstown['Sex'] == 'male')]

qtymS = maleS.shape[0] 
qtymQ = maleQ.shape[0]

maleSandQ = qtymS + qtymQ

print("\nPregunta 2:")
print("La cantidad de pasajeros que embarcaron en Southampton fue: %d" %(qtyS))
print("La cantidad de pasajeros que embarcaron en Queenstown fue: %d" %(qtyQ))
print("La cantidad de pasajeros que embarcaron en ambos puertos fue: %d" %(SandQ))
print("\nLa cantidad total de los pasajeros que embarcaron en ambos puertos, son hombres y sobrevivieron fue: %d" %(maleSandQ))

#Pregunta 3- Mujeres que sobrevivieron que pagaron más de $500 por pasaje.
fare500 = df[(df['Fare'] > 500) & (df['Sex'] == 'female') & (df['Survived'] == 'Sobrevivió')]
farelist = fare500['Name']

print("\nPregunta 3:")
print("Las mujeres que sobrevivieron que pagaron más de $500 por pasaje fueron:\n {}" .format(farelist))

#Pregunta 4- Sobrevivientes de la clase 3.
class3 = df[(df['Pclass'] == 3) & (df['Survived'] == 'Sobrevivió')].shape[0]

print("\nPregunta 4:")
print("De los sobrevivientes, la cantidad de personas que pertenecían a la clase 3 fue: {}" .format(class3))

#Pregunta 5- Hombres mayores de 60 años que sobrevivieron.
male60 = df[(df['Age'] > 60) & (df['Sex'] == 'male') & (df['Survived'] == 'Sobrevivió')].shape[0]

print("\nPregunta 5:")
print("De los sobrevivientes, la cantidad de hombres mayores de 60 años fue: {}" .format(male60))

#Pregunta 6- Nueva columna familia y análisis. 
df['Familia'] = df['SibSp'] + df['Parch']
fam4 = df[(df['Familia'] >= 4) & (df['Survived'] == 'Sobrevivió')].shape[0]

print("\nPregunta 6:")
print("La cantidad de sobrevivientes que viajaban con 4 o más miembros de su familia fue: {}" .format(fam4))
