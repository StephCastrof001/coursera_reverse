---
title: "42-Artificial Neurons"
type: lesson
module: "[[M06 - Deep Learning and Course Project]]"
tags: [lesson, ml-foundations]
---

# 🎓 42-Artificial Neurons

> **Módulo:** [[M06 - Deep Learning and Course Project]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 42-Artificial Neurons
<!-- Módulo: 06-Deep Learning & Course Project | Archivo: 42-Artificial Neurons.es.vtt -->

[00:05] Para entender la intuición qué hay detrás de cómo funcionan las redes neuronales y cómo las entrenamos, empecemos por entender cómo funciona una neurona artificial individual. Existen diferentes tipos de artificiales neuronas, pero empecemos por la primera y la más básica, que es llamado perceptrón.

[00:24] Así que la percepción es un modelo simple en el que tomamos un conjunto de entradas x multiplicado por un conjunto de pesos o coeficientes w. Sumamos los resultados y los pasamos a través de lo que se llama una función de umbral, donde podemos empareja la salida de esa cierta z con 0.

[00:47] Si la salida es superior a 0, generamos un 1. Si la salida es inferior a 0, generamos un -1. Por lo tanto, el perceptrón es un modelo que se utilizaría para un tipo de clasificación binaria de una tarea. Al observar este modelo, es posible que reconozca gran parte de esto en nuestra discusión sobre los modelos lineales.

[01:07] Y, de hecho, el perceptrón realmente lo es un modelo lineal muy simple comienza con una combinación lineal de nuestras características de entrada x multiplicados por coeficientes o ponderaciones, sumándolos y comparándolos con la función de umbral para generar una predicción de salida.

[01:24] Otro tipo de artificial La neurona es la regresión logística, de la que hablamos en un módulo anterior. La regresión logística es, de hecho, muy similar al perceptrón, pero ahora agregamos un componente más a nuestro modelo que es la función de activación. O en este caso de regresión logística, utilizamos una función sigmoidea como nuestra función de activación.

[01:47] Así que en la regresión logística, empezamos con nuestra entrada x, multiplicamos cada una de nuestras características en x veces el peso o el coeficiente y los sumamos en una puntuación. Luego pasamos nuestra z a través de la activación función o la función sigmoidea para la regresión logística.

[02:05] Y como resultado de eso, obtenemos la probabilidad de que y sea igual a 1 o la probabilidad de que ese punto de datos pertenece a la clase positiva. Pasamos entonces esta probabilidad de que y es igual a 1 a través de nuestra función de umbral. Y si la probabilidad es superior a 0,5, decimos que nuestra predicción es igual a 1.

[02:28] Si la probabilidad es inferior a 0,5, Tu predicción es igual a 0. También podemos usar eso en sus inmediatos valor, la probabilidad y es igual a 1 que salió de nuestra función de activación para calcular nuestro costo o una pérdida. Por lo tanto, nuestro objetivo es la regresión logística así como el perceptrón y todos nuestros otros modelos, es encontrar los valores de pesos que minimizan esta función de coste.

[02:57] Así que ahora repasemos el proceso del entrenamiento en una neurona artificial. Una vez más, nuestro objetivo en el entrenamiento y la neurona es encontrar los valores de la pesos que minimicen nuestra función de costes. Como recordamos, para minimizar una función, podemos tomar la derivada de esa función y ponerla en 0.

[03:18] Cuando abordemos los modelos de regresión lineal, podemos simplemente tomar la derivada de nuestra función de costo se iguala a 0 y calcula los valores de ponderación eso hizo que la ecuación fuera 0. Cuando introducimos lo no lineal funciones de activación como la función sigmoidea que es utilizado en la regresión logística, ya no hay una forma fácil de encontrar una solución de forma cerrada para resolver los valores de peso que forman la derivada igual a 0.

[03:46] Por lo tanto, utilizamos una resolución iterativa métodos como el descenso por gradiente. Empezamos con algunos valores iniciales aleatorios de nuestros pesos, calculamos el costo y luego nos movemos lentamente en una dirección opuesto al gradiente o la derivada de la función de costo.

[04:03] Hacia el punto al que lleguemos un nivel de coste mínimo y calculamos las ponderaciones que permiten alcanzarlo valor mínimo para nuestra función de costes. Echemos un vistazo a cómo lo hacemos usando un proceso llamado gradiente de descenso estocástico. En el descenso por gradiente estocástico, usamos un punto de datos a la vez.

[04:25] Realizamos un descenso en gradiente, actualizamos nuestros pesos, luego tomamos otro punto de datos, hacemos lo mismo y continuamos durante todo nuestro conjunto de datos hasta que hayamos usado todos los puntos. El primer paso para entrenar una neurona usando El gradiente de descenso estocástico se denomina propagación hacia adelante.

[04:44] En este paso, tomamos nuestro primer punto de datos y lo propagamos a través del modelo. Es decir, tomamos nuestro punto de datos y multiplicamos nuestras características de entrada multiplicado por los coeficientes o las ponderaciones. Calcula nuestra z, pasa nuestra z a través de nuestra función de activación, que es la función sigmoidea de la regresión logística, y calculamos nuestra predicción es una salida.

[05:10] Una vez que hayamos calculado nuestro valor y predicción, entonces podemos calcular el costo usando esa predicción comparándolo con el valor y real y también calculando el gradiente de esa función de costo. Calculamos el gradiente del costo función con respecto a cada uno de los pesos o coeficientes que están en nuestro modelo.

[05:34] Una vez que hayamos calculado el gradiente del función de coste con respecto a cada peso , ahora podemos actualizar los valores de cada uno de esos pesos utilizando nuestro proceso de descenso por gradiente. Por lo tanto, nuestro nuevo valor para un peso es igual al valor anterior de esa ponderación menos nuestra tasa de aprendizaje multiplicada por la derivada de nuestro costo función con respecto a ese peso.

[05:56] Podemos analizar cada uno de nuestros pesos y actualícelos utilizando esta regla de actualización. Luego repetimos el proceso tomando el siguiente punto de datos de nuestro conjunto de datos, pasándolo por nuestro modelo, calculando nuestro y eso, calculando nuestro costo y la derivada de un costo y luego actualizando las ponderaciones una vez más.

[06:15] Y continuamos este proceso hasta que tengamos revisó todo nuestro conjunto de datos. Finalmente, nuestro gradiente de descenso el proceso debería converger en valores de pesos que dan como resultado el costo mínimo y estas son las ponderaciones que tenemos luego úsalo en nuestro modelo final.

[06:34] Uno de los parámetros clave que tenemos Lo que necesitamos configurar para habilitar este proceso es la tasa de aprendizaje que vimos en la ecuación de actualización anterior. La tasa de aprendizaje controla el tamaño de un paso que damos cada vez que realizamos ese paso de descenso en pendiente.

[06:52] Como veremos más adelante en nuestro sección sobre redes neuronales, la tasa de aprendizaje puede tener un gran impacto en tu capacidad para entrenar en redes neuronales. Si estableces el ritmo de aprendizaje demasiado bajo, cada vez que realizas ese paso de descenso en pendiente, estás dando un paso muy, un paso muy, muy pequeño.

[07:09] Y como resultado, su algoritmo puede tardarán mucho tiempo en converger. Por otro lado, si configuras un tamaño demasiado grande de un ritmo de aprendizaje, terminas dando grandes pasos cada vez y puedes dependa de su función de costes y nunca encuentre ese valor mínimo. Por lo tanto, establezca la tasa de aprendizaje en un punto donde no es demasiado pequeño y tarda demasiado tiempo ni demasiado grande y ejecuta el el riesgo de divergir es una de las cosas clave en las que debes concentrarte como entrenamiento de modelos de redes neuronales.

[07:43] En el ejemplo anterior, entrenamos una neurona artificial usando qué lo llamamos gradiente de descenso estocástico. O tomando un punto de observación o dato a la vez para calcular iterativamente el gradiente y actualizar las ponderaciones, luego pasamos al siguiente y revisamos nuestros datos un punto a la vez.

[08:03] Este enfoque funciona muy bien para grandes conjuntos de datos y también es el enfoque principal utilizado en lo que llamamos aprendizaje en línea. Que es el caso en el que tenemos un modelo de producción en el que recibimos puntos de datos de un usuario, por ejemplo, una vez y cada vez que recibimos un punto de datos, estamos reentrenando y actualizando nuestro modelo.

[08:24] Una de las desventajas del gradiente estocástico El descenso es que tenemos que usar un bucle utilizando una sola observación a la vez y, por lo tanto, podemos aprovechar más operaciones vectorizadas o matriciales eficientes. El enfoque alternativo es lo que llamamos descenso por lotes.

[08:43] En el gradiente de descenso por lotes, utilizamos el conjunto de datos completo para cada actualización. Así que estamos calculando el gradiente y estamos actualizando los pesos en función de todas las observaciones de nuestro entrenamiento conjunto de datos en cada iteración. La principal ventaja del gradiente por lotes el descenso es que ahora podemos aprovechar las operaciones vectorizadas o matriciales y realizando esto y podemos realizar estas operaciones mucho más eficientemente.

[09:13] Uno de los desafíos del gradiente por lotes El descenso es que si tiene conjuntos de datos muy grandes, a veces puede resultar imposible debido a a la potencia de cálculo requerida para realizar un descenso de gradiente por lotes en cada iteración. Así que, como compromiso, es muy Es común que usemos un enfoque para entrenar redes neuronales llamado reduce este gradiente de descenso en lotes pequeños.

[09:36] En el descenso de gradiente en minilotes, dividimos nuestros datos de entrenamiento en subconjuntos más pequeños o lotes más pequeños. Por ejemplo, un lote de ocho observaciones a la vez o 32 observaciones a la vez. Entonces podemos realizar el lote descenso del gradiente utilizando todas nuestras observaciones internas este minilote cada vez.

[09:59] Por lo tanto, podemos aprovechar de las operaciones vectorizadas que podemos realizar usando gradiente de descenso por lotes. Pero no estamos usando ni mucho menos tan tanta potencia computacional como si tratáramos de usar nuestra conjunto completo de datos dentro de cada lote. El gradiente de descenso en minilotes es muy común en el entrenamiento de redes neuronales porque funciona muy bien para grandes conjuntos de datos y, al mismo tiempo, nos permite lograr operaciones computacionales eficientes.

[10:28] Uno de los desafíos que encontrará con el descenso en minilotes, ¿no es tan bueno como el descenso en gradiente estocástico para aprendizaje en línea cuando a menudo tenemos una sola observación por venir en ese momento para un usuario y deseo de volver a capacitarse como cada uno entra una sola observación

