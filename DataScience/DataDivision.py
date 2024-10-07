# Laboratorio 5- División de Datos
# Diseñado por- Luis Gabriel Tejada Figueroa

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import cross_val_score, train_test_split, StratifiedKFold, KFold
from sklearn.pipeline import make_pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv("C:\\Users\\luist\\Desktop\\data_Lab5.csv")

# Separar datos en dos matrices

X = df.iloc[:, :-1] #Features
y = df.iloc[:, -1] #Target

#%% Ejercicio 1- Clasificación de Datos Crudos
# División de datos en training y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3)

# Normalización de datos
norm = MinMaxScaler()
X_train_normalized = norm.fit_transform(X_train)
X_test_normalized = norm.fit_transform(X_test)

# Clasificación
classifier = LogisticRegression()
classifier.fit(X_train_normalized, y_train)

# Predicción
print("Exactitud sin validación cruzada: %.3f" % classifier.score(X_test_normalized, y_test))

#%% Ejercicio 2- Validación Cruzada
# Normalización de datos
norm = MinMaxScaler()
X_train_normalized = norm.fit_transform(X_train)
X_test_normalized = norm.fit_transform(X_test)

# Realización validación cruzada
pipeline = make_pipeline(MinMaxScaler(), classifier)
kf = StratifiedKFold(n_splits=20)

acc = cross_val_score(pipeline, X, y, cv=kf)

# Imprimir la exactitud media con validación cruzada
print("Exactitud con validación cruzada: %.3f" % acc.mean())

#%% Ejercicio 3- Validación Cruzada Manual
# Método de KFold
kfm = KFold(n_splits=20, shuffle=True, random_state=1)

accm = []
for train_index, test_index in kfm.split(X):
    # Dividir los datos
    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
    y_train, y_test = y.iloc[train_index], y.iloc[test_index]
    
    # Normalización
    norm = MinMaxScaler()
    X_train_normalized = norm.fit_transform(X_train)
    X_test_normalized = norm.transform(X_test)
    
    # Clasificación
    classifier = LogisticRegression()
    classifier.fit(X_train_normalized, y_train)
    
    # Predicciones y cálculo de la exactitud
    pred = classifier.predict(X_test_normalized)
    acc = accuracy_score(y_test, pred) 
    accm.append(acc)

# Imprimir la exactitud media con validación cruzada manual
print("Exactitud promedio con validación cruzada manual: %.3f" % np.mean(accm))

#%% Preguntas- Sección de apoyo (Solo de ser necesario)
# Pregunta 1- Gráfica
plt.figure(figsize=(10, 6))
for class_value in y.unique():
    # Separar datos por clase
    row_ix = (y == class_value)
    plt.scatter(X.loc[row_ix, X.columns[0]], X.loc[row_ix, X.columns[1]], label=f'Class {int(class_value)}')
plt.title('Scatter Plot of the Data by Class')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()