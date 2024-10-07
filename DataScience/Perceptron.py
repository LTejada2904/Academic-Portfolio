#Laboratorio 7- Perceptron
#Disenado por- Luis G. Tejada Figueroa

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\luist\\Desktop\\data_lab.csv")

# Separar datos en dos matrices
X = df.iloc[:, :-1] #Features
y = df.iloc[:, -1] #Target

#Creacion de la clase Perceptron
class Perceptron:
    def __init__(self, learning_rate=0.1, epochs=10):
        self.lr = learning_rate
        self.epochs = epochs
        self.weights = None
        self.bias = None
        self.accuracy_history = []

    def activate(self, x):
        return np.where(x >= 0, 1, -1)

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        for epoch in range(self.epochs):
            accuracy = 0
            for idx, x_i in enumerate(X.values):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.activate(linear_output)
                update = self.lr * (y[idx] - y_predicted)
                self.weights += update * x_i
                self.bias += update
                accuracy += 1 if y_predicted == y[idx] else 0
            accuracy /= n_samples
            self.accuracy_history.append(accuracy)
            print("Epoch %d/%d, Accuracy: %0.2f%%" % (epoch+1, self.epochs, accuracy*100))
    
    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        return self.activate(linear_output)
    
#%% Procedimiento 1- Clasificacion del Dataset
# Creamos y entrenamos el Perceptrón
perceptron = Perceptron(learning_rate=0.01, epochs=10)
perceptron.fit(X, y)

# Graficamos Accuracy vs. Epoch para verificar el resultado
plt.plot(range(1, perceptron.epochs + 1), perceptron.accuracy_history, marker='o', linestyle='-', color='b')
plt.title("Accuracy vs. Epoch")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

#%% Procedimiento 2- Ajustes
#Ajustamos la taza de aprendizaje y cantidad de epocas
perceptron = Perceptron(learning_rate=0.001, epochs=20)
perceptron.fit(X, y)

# Graficamos Accuracy vs. Epoch para verificar el resultado
plt.plot(range(1, perceptron.epochs + 1), perceptron.accuracy_history, marker='o', linestyle='-', color='b')
plt.title("Accuracy vs. Epoch")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")

#%% Procedimiento 3- Epocas variables
def accuracy_find(X, y, learning_rate=0.01, desired_accuracy=0.95):
    X = X.values
    n_samples, n_features = X.shape
    weights = np.zeros(n_features)
    bias = 0
    epochs = 0
    accuracy_history = []
    
    while True:
        accuracy = 0
        for idx, x_i in enumerate(X):
            linear_output = np.dot(x_i, weights) + bias
            y_predicted = np.where(linear_output >= 0, 1, -1)
            update = learning_rate * (y[idx] - y_predicted)
            weights += update * x_i
            bias += update
            accuracy += 1 if y_predicted == y[idx] else 0
        accuracy /= n_samples
        accuracy_history.append(accuracy)
        print(f"Epoca {epochs+1}, Accuracy: {accuracy*100:.2f}%")
        
        if accuracy >= desired_accuracy:
            print(f"Accuracy deseado de {desired_accuracy*100:.2f}% alcanzado en la epoca {epochs+1}")
            break
        
        epochs += 1
    
    return accuracy_history

desired_accuracy = 0.97
accuracy_history = accuracy_find(X, y, learning_rate=0.01, desired_accuracy=desired_accuracy)

# Graficamos Accuracy vs. Epoch
plt.plot(range(1, len(accuracy_history) + 1), accuracy_history, marker='o', linestyle='-', color='b')
plt.title("Accuracy vs. Epoch (Accuracy Alcanzado)")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.grid(True)
plt.show()
