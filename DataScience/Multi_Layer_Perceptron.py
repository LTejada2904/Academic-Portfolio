#Laboratorio 8- Perceptron Multicapa
#Disenado por- Luis G. Tejada Figueroa

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import tensorflow.keras as keras
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("C:\\Users\\luist\\Desktop\\dataset.csv")

# Separar datos en dos matrices
X = df.iloc[:, :-1] #Features
y = df.iloc[:, -1] #Target

# Codificar las etiquetas
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)

#%% Ejercicio 1- MLP 1
# Configurar el modelo MLP con Keras
def mlp_1():
    model = keras.Sequential([
        keras.layers.Input(shape=(X.shape[1],)),
        keras.layers.Dense(50, activation='relu'),
        keras.layers.Dense(50, activation='relu'),
        keras.layers.Dense(50, activation='relu'),
        keras.layers.Dense(50, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    optimizer = keras.optimizers.SGD(learning_rate=0.1)
    model.compile(optimizer=optimizer, loss='mse', metrics=['accuracy'])
    return model

# Preparación para K-fold cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Arrays para almacenar resultados
loss_per_fold = []
acc_per_fold = []
history_list = []

# Bucle de K-fold Cross Validation
for train, test in kfold.split(X, y):
    model = mlp_1()
    
    # Entrenamiento
    history = model.fit(X.iloc[train], y[train], epochs=5, batch_size=64, verbose=0, validation_data=(X.iloc[test], y[test]))
    history_list.append(history)
    
    # Evaluación del modelo
    scores = model.evaluate(X.iloc[test], y[test], verbose=0)
    acc_per_fold.append(scores[1] * 100)
    loss_per_fold.append(scores[0])

# Gráfico de precisión vs. épocas
plt.figure(figsize=(12, 6))
for i, history in enumerate(history_list):
    plt.plot(history.history['accuracy'], label=f'Fold {i+1}')
plt.title('Accuracy vs Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()

# Promedio de precisiones
print(f'Average accuracy: {np.mean(acc_per_fold)}%')

#%% Ejercicio 2- MLP 2
# Configurar el modelo MLP con Keras
def mlp_2():
    model = keras.Sequential([
        keras.layers.Input(shape=(X.shape[1],)),
        keras.layers.Dense(60, activation='relu'),
        keras.layers.Dense(60, activation='relu'),
        keras.layers.Dense(60, activation='relu'),
        keras.layers.Dense(60, activation='relu'),
        keras.layers.Dense(60, activation='relu'),
        keras.layers.Dense(60, activation='relu'),
        keras.layers.Dense(1, activation='sigmoid')
    ])
    
    optimizer = keras.optimizers.Adam(learning_rate=0.01)
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Preparación para K-fold cross-validation
kfold = KFold(n_splits=5, shuffle=True, random_state=42)

# Arrays para almacenar resultados
acc_per_fold = []
history_list = []

# Bucle de K-fold Cross Validation
for train, test in kfold.split(X, y):
    model = mlp_2()
    
    # Entrenamiento
    history = model.fit(X.iloc[train], y[train], epochs=5, batch_size=128, verbose=0, validation_data=(X.iloc[test], y[test]))
    history_list.append(history)
    
    # Evaluación del modelo
    scores = model.evaluate(X.iloc[test], y[test], verbose=0)
    acc_per_fold.append(scores[1] * 100)

# Gráfico de precisión vs. épocas
plt.figure(figsize=(12, 6))
for i, history in enumerate(history_list):
    plt.plot(history.history['accuracy'], label=f'Fold {i+1}')
plt.title('Accuracy vs Epochs')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.show()

# Promedio de precisiones y test del último fold
average_accuracy = np.mean(acc_per_fold)
print(f'Average accuracy after K-fold CV: {average_accuracy}%')