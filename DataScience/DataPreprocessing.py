# Laboratorio 4- Preprocesamiento de Datos
# Diseñado por- Luis Gabriel Tejada Figueroa

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from numpy import mean
from numpy import std
from sklearn.model_selection import cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.pipeline import make_pipeline
from sklearn.decomposition import PCA
from sklearn.feature_selection import RFE
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler, StandardScaler

df = pd.read_csv("C:\\Users\\luist\\Desktop\\dataset_1.csv")

# Separar datos en dos matrices

x = df.iloc[:, 0:50] #Features
y = df.iloc[:, 50] #Target

#%% Ejercicio 1- Reducción de Dimensiones

#Exactitud con todas las columnas
acc = LogisticRegression(max_iter=1000)
ereg = cross_val_score(acc, x, y, scoring='accuracy')
print("Exactitud sin procesar : %0.3f (%0.3f)" %(mean(ereg), std(ereg)))

# Análisis de exactitud con PCA
n_components_list = list(range(1,21))
acc_pca = []

for n_components in n_components_list:
    pca_pipeline = make_pipeline(PCA(n_components=n_components), LogisticRegression(max_iter=1000))
    epca = cross_val_score(pca_pipeline, x, y, scoring='accuracy')
    acc_pca.append(mean(epca))

plt.figure(figsize=(10, 6))
plt.plot(n_components_list, acc_pca, marker='o', linestyle='-', color='b')
plt.title('PCA n_components vs. Accuracy')
plt.xlabel('Number of PCA Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud PCA : %0.3f (%0.3f)" %(mean(acc_pca), std(acc_pca)))

# Análisis de exactitud con RFE
acc_rfe = []

for n_features_to_select in n_components_list:
    rfe_pipeline = make_pipeline(RFE(estimator=LogisticRegression(max_iter=1000), n_features_to_select=n_features_to_select), LogisticRegression(max_iter=10000))
    erfe = cross_val_score(rfe_pipeline, x, y, scoring='accuracy')
    acc_rfe.append(mean(erfe))

plt.figure(figsize=(10, 6))
plt.plot(n_components_list, acc_rfe, marker='o', linestyle='-', color='b')
plt.title('RFE n_features_to_select vs. Accuracy')
plt.xlabel('Number of RFE Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud RFE : %0.3f (%0.3f)" %(mean(acc_rfe), std(acc_rfe)))

# Análisis de exactitud con LDA
n_classes = len(np.unique(y))
max_n_components_lda = min(50, n_classes - 1)

acc_lda = []
n_components_list_lda = list(range(1, max_n_components_lda + 1))
for n_components in n_components_list_lda:
    lda_steps = [('lda', LinearDiscriminantAnalysis(n_components=n_components)), ('m', LogisticRegression(max_iter=1000))]
    lda_pipeline = Pipeline(steps=lda_steps)
    scores = cross_val_score(lda_pipeline, x, y, scoring='accuracy')
    mean_accuracy = np.mean(scores)
    acc_lda.append(mean_accuracy)
    
plt.figure(figsize=(10, 6))
plt.plot(n_components_list_lda, acc_lda, marker='o', linestyle='-', color='b')
plt.title('LDA n_components vs. Accuracy')
plt.xlabel('Number of LDA Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud LDA : %0.3f (%0.3f)" %(mean(acc_lda), std(acc_lda)))

#%% Ejercicio 2- Normalización

norm = MinMaxScaler()
norm_data = norm.fit_transform(df)
norm_data_df = pd.DataFrame(norm_data, columns=df.columns)

xn = norm_data_df.iloc[:, 0:50] #Features
yn = norm_data_df.iloc[:, 50] #Target

# Exactitud con todas las columnas normalizadas
accn = LogisticRegression(max_iter=1000)
enorm = cross_val_score(accn, xn, yn, scoring='accuracy')
print("Exactitud con todas las columnas normalizadas : %0.3f (%0.3f)" %(mean(enorm), std(enorm)))

# Análisis de exactitud con PCA y datos normalizados
n_components_list = list(range(1,21))
acc_pca = []

for n_components in n_components_list:
    pca_pipeline = make_pipeline(PCA(n_components=n_components), LogisticRegression(max_iter=1000))
    epca = cross_val_score(pca_pipeline, xn, yn, scoring='accuracy')
    acc_pca.append(mean(epca))

plt.figure(figsize=(10, 6))
plt.plot(n_components_list, acc_pca, marker='o', linestyle='-', color='b')
plt.title('PCA n_components vs. Accuracy (Normalized Data)')
plt.xlabel('Number of PCA Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud PCA : %0.3f (%0.3f)" %(mean(acc_pca), std(acc_pca)))

# Análisis de exactitud con RFE y datos normalizados
acc_rfe = []

for n_features_to_select in n_components_list:
    rfe_pipeline = make_pipeline(RFE(estimator=LogisticRegression(max_iter=1000), n_features_to_select=n_features_to_select), LogisticRegression(max_iter=10000))
    erfe = cross_val_score(rfe_pipeline, xn, yn, scoring='accuracy')
    acc_rfe.append(mean(erfe))

plt.figure(figsize=(10, 6))
plt.plot(n_components_list, acc_rfe, marker='o', linestyle='-', color='b')
plt.title('RFE n_features_to_select vs. Accuracy (Normalized Data)')
plt.xlabel('Number of RFE Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud RFE : %0.3f (%0.3f)" %(mean(acc_rfe), std(acc_rfe)))

# Análisis de exactitud con LDA y datos normalizados
n_classes = len(np.unique(yn))
max_n_components_lda = min(50, n_classes - 1)

acc_lda = []
n_components_list_lda = list(range(1, max_n_components_lda + 1))
for n_components in n_components_list_lda:
    lda_steps = [('lda', LinearDiscriminantAnalysis(n_components=n_components)), ('m', LogisticRegression(max_iter=1000))]
    lda_pipeline = Pipeline(steps=lda_steps)
    scores = cross_val_score(lda_pipeline, xn, yn, scoring='accuracy')
    mean_accuracy = np.mean(scores)
    acc_lda.append(mean_accuracy)

plt.figure(figsize=(10, 6))
plt.plot(n_components_list_lda, acc_lda, marker='o', linestyle='-', color='b')
plt.title('LDA n_components vs. Accuracy (Normalized Data)')
plt.xlabel('Number of LDA Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud LDA : %0.3f (%0.3f)" %(mean(acc_lda), std(acc_lda)))

#%% Ejericio 3- Estandarización
est = StandardScaler()
est_data = est.fit_transform(df)
est_data_df = pd.DataFrame(est_data, columns=df.columns)

xe = est_data_df.iloc[:, 0:50] #Features
ye = est_data_df.iloc[:, 50] #Target

# Exactitud con todas las columnas normalizadas
acce = LogisticRegression(max_iter=1000)
eest = cross_val_score(acce, xe, ye, scoring='accuracy')
print("Exactitud con todas las columnas estandarizadas : %0.3f (%0.3f)" %(mean(eest), std(eest)))

# Análisis de exactitud con PCA y datos estandarizados
n_components_list = list(range(1,21))
acc_pca_est = []

for n_components in n_components_list:
    pca_pipeline = make_pipeline(PCA(n_components=n_components), LogisticRegression(max_iter=1000))
    epca = cross_val_score(pca_pipeline, xe, ye, scoring='accuracy')
    acc_pca_est.append(mean(epca))

plt.figure(figsize=(10, 6))
plt.plot(n_components_list, acc_pca_est, marker='o', linestyle='-', color='b')
plt.title('PCA n_components vs. Accuracy (Standardized Data)')
plt.xlabel('Number of PCA Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud PCA : %0.3f (%0.3f)" %(mean(acc_pca_est), std(acc_pca_est)))

# Análisis de exactitud con RFE y datos estandarizados
acc_rfe_est = []

for n_features_to_select in n_components_list:
    rfe_pipeline = make_pipeline(RFE(estimator=LogisticRegression(max_iter=1000), n_features_to_select=n_features_to_select), LogisticRegression(max_iter=10000))
    erfe = cross_val_score(rfe_pipeline, xe, ye, scoring='accuracy')
    acc_rfe_est.append(mean(erfe))

plt.figure(figsize=(10, 6))
plt.plot(n_components_list, acc_rfe_est, marker='o', linestyle='-', color='b')
plt.title('RFE n_features_to_select vs. Accuracy (Standardized Data)')
plt.xlabel('Number of RFE Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud RFE : %0.3f (%0.3f)" %(mean(acc_rfe_est), std(acc_rfe_est)))

# Análisis de exactitud con LDA y datos estandarizados
n_classes = len(np.unique(ye))
max_n_components_lda = min(50, n_classes - 1)

acc_lda_est = []
n_components_list_lda = list(range(1, max_n_components_lda + 1))
for n_components in n_components_list_lda:
    lda_steps = [('lda', LinearDiscriminantAnalysis(n_components=n_components)), ('m', LogisticRegression(max_iter=1000))]
    lda_pipeline = Pipeline(steps=lda_steps)
    scores = cross_val_score(lda_pipeline, xe, ye, scoring='accuracy')
    mean_accuracy = np.mean(scores)
    acc_lda_est.append(mean_accuracy)

plt.figure(figsize=(10, 6))
plt.plot(n_components_list_lda, acc_lda_est, marker='o', linestyle='-', color='b')
plt.title('LDA n_components vs. Accuracy (Standardized Data)')
plt.xlabel('Number of LDA Components')
plt.ylabel('Accuracy')
plt.grid(True)

print("Exactitud LDA : %0.3f (%0.3f)" %(mean(acc_lda_est), std(acc_lda_est)))
