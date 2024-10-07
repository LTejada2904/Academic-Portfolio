# Laboratorio 6- Métricas y Dataset_Desbalanceado
# Diseñado por- Luis Gabriel Tejada Figueroa

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, cohen_kappa_score

from imblearn.over_sampling import SMOTE
from collections import Counter

df = pd.read_csv("C:\\Users\\luist\\Desktop\\dataset.csv")

# Separar datos en dos matrices
X = df.iloc[:, :-1] #Features
y = df.iloc[:, -1] #Target

#%% Procedimiento 1- Distribución de atributos
fig, ax = plt.subplots(12, 3, figsize=(15, 48))
for i in range(35):
    row, col = divmod(i, 3)
    ax[row, col].hist(df.iloc[:, i], bins=20, color='lightsteelblue', edgecolor='black')
    ax[row, col].set_title(f'Atributo {i}')

#%% Procedimiento 2- Correlación entre atributos
numeric_columns = X.select_dtypes(include=[np.number])
corr_matrix = numeric_columns.corr()

#%% Procedimiento 3- Investigación de valores faltantes
# Verificar y contar los valores faltantes en 'age'
missing_age_values = X['age'] == '?'
missing_age_count = missing_age_values.sum()

# Calcular la proporción de valores faltantes en 'age'
total_rows = X.shape[0]
missing_age_proportion = (missing_age_count / total_rows)*100

print("La cantidad de valores de edad restantes: %0.2f." %(missing_age_count))
print("Porcentaje de valores de edad restantes: %0.2f." %(missing_age_proportion))

# Reemplazar '?' con NaN
X.replace('?', pd.NA, inplace=True)

# Convertir la columna 'age' a numérica
X['age'] = pd.to_numeric(X['age'])

# Imputación por la mediana para 'age'
imputer = SimpleImputer(strategy='median')
X['age'] = imputer.fit_transform(X[['age']])

# Calcular nueva matriz de correlación
corr_matrix = X.corr()

# Calcular máxima y mínima correlación excluyendo la diagonal
max_corr = corr_matrix.mask(np.eye(len(corr_matrix), dtype=bool)).stack().max()
min_corr = corr_matrix.mask(np.eye(len(corr_matrix), dtype=bool)).stack().min()

# Localizar pares de características con la máxima y mínima correlación
max_pair = corr_matrix.mask(np.eye(len(corr_matrix), dtype=bool)).stack().idxmax()
min_pair = corr_matrix.mask(np.eye(len(corr_matrix), dtype=bool)).stack().idxmin()

print("Valor máximo de correlación (excluyendo diagonal): %0.4f, entre %s" % (max_corr, max_pair))
print("Valor mínimo de correlación (excluyendo diagonal): %0.4f, entre %s" % (min_corr, min_pair))

#%% Procedimiento 4- Estandarización de datos y clasificación
# Codificación de la etiqueta 'Age' usando LabelEncoder
label_encoder = LabelEncoder()
X['age'] = label_encoder.fit_transform(X['age'])

# Estandarización de los atributos numéricos
scaler = StandardScaler()
features_scaled = scaler.fit_transform(X)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
#Crear Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

param_grid = {
    'svm__C': [0.1, 1, 10, 100],
    'svm__gamma': [1, 0.1, 0.01, 0.001]
}

#Buscar los mejores parámetros
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', verbose=1)
grid_search.fit(X_train, y_train)

# Mejores parámetros y puntuación
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Mejores parámetros del SVM:", best_params)
print("Mejor precisión obtenida: %0.4f" % best_score)

# Predicción sobre el conjunto de prueba usando el mejor modelo encontrado
y_pred = grid_search.predict(X_test)

# Métricas de evaluación
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
kappa = cohen_kappa_score(y_test, y_pred)

# Imprimir las métricas de evaluación
print("\nMatriz de Confusión:\n", conf_matrix)
print("Accuracy: %0.4f" % accuracy)
print("Precision: %0.4f" % precision)
print("Recall: %0.4f" % recall)
print("F1 Score: %0.4f" % f1)
print("Cohen's Kappa: %0.4f" % kappa)

#%% Procedimiento 5- Distribución de clases
# Calcular la distribución de las clases
class_distribution = y.value_counts()

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
class_distribution.plot(kind='bar')
plt.title('Distribución de las Clases en el Conjunto de Datos')
plt.xlabel('Clase')
plt.ylabel('Número de Instancias')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')

#%% Procedimiento 6- Balanceo de datos
# Aplicar SMOTE para balancear los datos
smote = SMOTE()
X_smote, y_smote = smote.fit_resample(X, y)

# Calcular la nueva distribución de las clases después de aplicar SMOTE
class_distribution_smote = Counter(y_smote)

# Crear el gráfico de barras para la nueva distribución de las clases
plt.figure(figsize=(10, 6))
plt.bar(class_distribution_smote.keys(), class_distribution_smote.values())
plt.title('Distribución de las Clases después de SMOTE')
plt.xlabel('Clase')
plt.ylabel('Número de Instancias')
plt.xticks(list(class_distribution_smote.keys()))
plt.grid(axis='y', linestyle='--')

#%% Procedimiento 7- Estandarización y clasifficación con SMOTE
# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_smote, y_smote, test_size=0.2, random_state=42)
    
#Crear Pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

param_grid = {
    'svm__C': [0.1, 1, 10, 100],
    'svm__gamma': [1, 0.1, 0.01, 0.001]
}

#Buscar los mejores parámetros
grid_search = GridSearchCV(pipeline, param_grid, cv=5, scoring='accuracy', verbose=1)
grid_search.fit(X_train, y_train)

# Mejores parámetros y puntuación
best_params = grid_search.best_params_
best_score = grid_search.best_score_

print("Mejores parámetros del SVM con SMOTE:", best_params)
print("Mejor precisión obtenida con SMOTE: %0.4f" % best_score)

# Predicción sobre el conjunto de prueba usando el mejor modelo encontrado
y_pred = grid_search.predict(X_test)

# Métricas de evaluación
conf_matrix = confusion_matrix(y_test, y_pred)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='weighted')
recall = recall_score(y_test, y_pred, average='weighted')
f1 = f1_score(y_test, y_pred, average='weighted')
kappa = cohen_kappa_score(y_test, y_pred)

# Imprimir las métricas de evaluación
print("\nMatriz de Confusión con SMOTE:\n", conf_matrix)
print("Accuracy con SMOTE: %0.4f" % accuracy)
print("Precision con SMOTE: %0.4f" % precision)
print("Recall con SMOTE: %0.4f" % recall)
print("F1 Score con SMOTE: %0.4f" % f1)
print("Cohen's Kappa con SMOTE: %0.4f" % kappa)