import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np

# Importamos el modelo para el clasificador 
from sklearn.ensemble import GradientBoostingClassifier

#Importamos el modeulo de entrenamiento
from sklearn.model_selection import train_test_split
# Importamos el módulo de precisión 
from sklearn.metrics import accuracy_score 

if __name__ == "__main__":

    # Importamos el dataset 
    dt_heart = pd.read_csv('./data/heart.csv')
    # Imprimimos la descripción 
    #print(dt_heart['target'].describe())

    # Cargamos nuestro dataset excepto la variable target 
    X = dt_heart.drop(['target'], axis=1)
    # Cargamos nuestro target a y  
    y = dt_heart['target']

    # Aplicamos nuestro módulo de ajuste
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.35)

    # Definimos nuestro clasificador, definimos 50 arbole y le agregamos el ajuste
    boost = GradientBoostingClassifier(n_estimators=50).fit(X_train, y_train)

    # Generamos nuestras predicciones 
    boost_pred = boost.predict(X_test)
    print("="*64)
    print("GradientBoostingClassifier: ", accuracy_score(boost_pred, y_test)) 

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.35)

    estimators = range(10, 200, 10)
    total_accuracy = []
    for i in estimators:
        boost = GradientBoostingClassifier(n_estimators=i).fit(X_train, y_train)
        boost_pred = boost.predict(X_test)

        total_accuracy.append(accuracy_score(y_test, boost_pred))
    
    plt.plot(estimators, total_accuracy)
    plt.xlabel('Estimators')
    plt.ylabel('Accuracy')
    plt.show()
    plt.savefig('Boost.png')

    #print(np.array(total_accuracy).max()) 
