# Proyecto: Algoritmos y métodos para clasificación
 
Heart disease prediction: Es un subconjunto de variables de un estudio que realizado en 1988 en diferentes regiones del planeta para predecir el riesgo a sufrir una enfermedad relacionada con el corazón. 
 
> **_Nota:_** En este readme sólo se mostrarán los resultados, para más detalles ver el código el la carpeta code de este repo. 
 
## Proyecto 1: Análisis de componentes principales 
 
**¿Por qué usamos este algoritmo?**
 
- Porque en machine learning es normal encontrarnos con problemas donde tengamos una enorme cantidad de features en donde hay relaciones complejas entre ellos y con la variable que queremos predecir.
 
Pistas donde se puede utilizar un algoritmo PCA:
 
- Nuestro dataset tiene un número alto de features y no todos son significativos.
- Hay una alta correlación entre los features.
- Cuando hay overfitting.
- Cuando implica un alto coste computacional.
 
---
 
**¿En qué consiste el algoritmo PCA?**
 
Básicamente consiste en reducir la complejidad del problema:
 
**1.-** Seleccionando solamente las variables relevantes.
 
**2.-** Combinandolas en nuevas variables que mantengan la información más importante (varianza de los features).
 
![6](https://user-images.githubusercontent.com/63415652/103370614-dc802b80-4a92-11eb-94f3-8603c15c4953.PNG)
 
Ahora aplicándolo a nuestro dataset logramos esta precisión: 
 
![8](https://user-images.githubusercontent.com/63415652/103371135-4f3dd680-4a94-11eb-9f04-e409c3c9587b.PNG)
 
Bueno de entrada vemos que los 2 algoritmos tienen casi el mismo rendimiento, pero, ¿qué logramos con esto? 
 
El dataset original tenía 13 features para intentar predecir una clasificación binaria sobre si tiene el paciente una enfermedad cardiaca o no la tiene, y ahora con PCA solo necesitamos 3 features artificiales para llegar a un resultado suficientemente bueno. 
 
 > **_Entonces en conclusión,_** nos estamos ahorrando coste computacional, ya que solo estamos utilizando la información relevante para nuestro modelo. 
 
## Proyecto 2: Kernels y KPCA
 
**Ahora que ya sabemos el algoritmo de PCA, ¿qué otras alternativas tenemos?**
 
---
 
Bueno, una alternativa son los Kernels. Un Kernel es una función matemática que toma mediciones que se comportan de manera no lineal y las proyecta en un espacio dimensional más grande en donde son linealmente separables.
 
**Y, ¿esto para qué puede servir?**
 
![9](https://user-images.githubusercontent.com/63415652/103372032-93ca7180-4a96-11eb-8c4b-28ae4ffc6020.PNG)
 
Sirve para casos en donde no son linealmente separables. En la primera imagen no es posible separarlos con una línea y en la imagen 2 si lo podemos hacer mediante Kernels. Lo que hace la función de Kernels es proyectar los puntos en otra dimensión y así volver los datos linealmente separables.
 
Ahora vamos a medir el rendimiento de nuestro modelo basado en kernel:
 
![10](https://user-images.githubusercontent.com/63415652/103372281-32ef6900-4a97-11eb-8c9b-d4fb4f3abf94.PNG)
 
> **_Conclusión:_** Implementar un kernel es relativamente fácil y tiene una buena precisión, el problema más grande con el que nos enfrentaremos es identificar cuándo necesitaremos para modelar un espacio dimensional superior. 
 
## Métodos de ensamble
 
### Bagging:
 
¿Qué tal si en lugar de depender de la opinión de un solo "experto" consultamos la opinión de varios expertos en paralelo e intentamos lograr un consenso? 
 
Para ello nos tenemos que imaginar que nuestro modelo de ML es un experto, pero, ¿si pudiéramos tener la opinión de varios expertos? Pues sería mucho mejor, ¿verdad? Entonces, en este algoritmo se toma en consideración varios votos de expertos y para ello se puede hacer un conteo o simplemente un promedio.
 
### Boosting. 
 
* Significa impulsar / propulsar. 
* Es un método secuencial. 
* Busca fortalecer gradualmente un modelo de aprendizaje usando siempre el error residual de las etapas anteriores.
 
* El resultado final también se consigue por consenso entre todos los modelos. 
 
Ahora, vamos a ver los resultados implementando los métodos en código. 
 
Aquí podemos ver la percepción que tuvieron todos los métodos de ensamble en relación a el KNN sin método de ensamble: 
 
![12](https://user-images.githubusercontent.com/63415652/103423141-a910d000-4b6a-11eb-8255-38255ac7a2bc.PNG)
 
Y por último la precisión de boosting: 
 
![13](https://user-images.githubusercontent.com/63415652/103423142-aa41fd00-4b6a-11eb-8f84-c6e2682d0bad.PNG)
 
Como podemos ver, el método de Boosting nos dió una exactitud muy significativa. 
 
Con los métodos de ensamble, aún cuando cuando teníamos un clasificador que no era tan bueno, podemos llegar a muchos mejores resultados utilizando los métodos de ensamble. Además, un clasificador por sí solo no siempre es tan poderoso como aplicar muchas veces ese clasificador con diferentes parámetros y diferentes configuraciones con un método de consenso aplicado.
 
>**_Conclusión:_** En un ejercicio de la vida real estamos clasificando un paciente y tenemos un porcentaje súper alto de exactitud a la hora de predecir un paciente entonces esto es un excelente soporte para un médico en una clínica en su trabajo cotidiano. 






 
