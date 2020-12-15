import pandas as pd 

# Importamos el modelo para el clasificador 
from sklearn.neighbors import KNeighborsClassifier 
# Importamos el bagging clasificador 
from sklearn.ensemble import BaggingClassifier 

#Importamos el modeulo de entrenamiento
from sklearn.model_selection import train_test_split
# Importamos el módulo de precisión 
from sklearn.metrics import accuracy_score 

if __name__ == "__main__":

    # Importamos el dataset 
    dt_heart = pd.read_csv('./data/heart.csv')
    # Imprimimos la descripción 
    print(dt_heart['target'].describe())

    # Cargamos nuestro dataset excepto la variable target 
    X = dt_heart.drop(['target'], axis=1)
    # Cargamos nuestro target a y  
    y = dt_heart['target']

    # Aplicamos nuestro módulo de ajuste
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.35)
