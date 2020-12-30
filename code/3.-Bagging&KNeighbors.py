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
    #print(dt_heart['target'].describe())

    # Cargamos nuestro dataset excepto la variable target 
    X = dt_heart.drop(['target'], axis=1)
    # Cargamos nuestro target a y  
    y = dt_heart['target']

    # Aplicamos nuestro módulo de ajuste
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.35)

    # Utilizamos un clasificador por KNN y lo ajustamos 
    knn_class = KNeighborsClassifier().fit(X_train, y_train)
    # Hacemos las predicciones 
    knn_pred = knn_class.predict(X_test)
    # Imprimimos el resultado de nuestra clasificación 
    print("="*64)
    print("KNeighborsClassifier: ", accuracy_score(knn_pred, y_test))
    
    # Agregamos nuestro clasificador por ensamble, le podemos 50 modelos para que lo use  y lo ajustamos 
    bag_class = BaggingClassifier(base_estimator=KNeighborsClassifier(), n_estimators=50).fit(X_train, y_train) 
    # Ajustamos las predicciones 
    bag_pred = bag_class.predict(X_test) 
    # Imprimimos el resultado 
    print("="*64)
    print("BaggingClassifier: ", accuracy_score(bag_pred, y_test))    

    