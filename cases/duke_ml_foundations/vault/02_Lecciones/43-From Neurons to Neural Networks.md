---
title: "43-From Neurons to Neural Networks"
type: lesson
module: "[[M06 - Deep Learning and Course Project]]"
tags: [lesson, ml-foundations]
---

# 🎓 43-From Neurons to Neural Networks

> **Módulo:** [[M06 - Deep Learning and Course Project]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 43-From Neurons to Neural Networks
<!-- Módulo: 06-Deep Learning & Course Project | Archivo: 43-From Neurons to Neural Networks.es.vtt -->

[00:05] En la última lección, hablamos de las neuronas artificiales. Hablamos de cómo están estructuradas y de cómo podemos entrenarlas utilizando el descenso de gradiente para cambiar iterativamente los pesos hasta que encontremos los pesos óptimos que minimicen el coste. Las neuronas artificiales son potentes, pero su poder es limitado porque sólo pueden manejar problemas con límites de decisión lineales.

[00:31] Los investigadores sabían por aquel entonces, en los años 50, que añadir más neuronas para formar una red nos permitiría realizar cálculos más complejos que tuvieran límites de decisión no lineales. Sin embargo, no fue hasta los años 80, cuando se popularizó el método de retropropagación cuando realmente tuvimos una buena forma de entrenar estos modelos de redes neuronales con múltiples capas.

[00:58] Veamos qué ocurre cuando apilamos varios perceptrones juntos. Podríamos apilarlos de un par de maneras. Podríamos tomar un par de perceptrones y ponerlos uno al lado del otro, pero también podríamos tomar las salidas de esos dos perceptrones y alimentarlos en otro perceptrón más para que realice sus cálculos y genere una salida final.

[01:21] Resulta entonces que cuando apilamos estos perceptrones juntos de esta manera, podríamos realizar cálculos mucho más complejos que los que podríamos realizar utilizando una sola neurona artificial. Veamos un ejemplo para ilustrar esto. Digamos que tenemos un problema en el que estamos intentando generar un modelo para predecir alguna salida, que es una salida de clasificación binaria, ya sea un más 1 o un menos 1, y como entrada tenemos dos características X_1 y X_2.

[01:50] Una frontera de decisión, se ve así, como podemos ver en la diapositiva entre la clase más 1 y la clase menos 1. Para abordar este problema, podríamos empezar por tomar dos perceptrones individuales. Podríamos entrenar cada perceptrón de modo que fueran capaces de crear límites de decisión lineales entre la clase menos 1 y la clase positivo 1, así.

[02:15] Podemos entonces tomar la salida de cada de esos perceptrones individuales, alimentarla a un tercer perceptrón. Ahora nuestro tercer perceptrón sería capaz de combinar las salidas del primer y segundo perceptrón y crear una frontera de decisión no lineal. De este modo, nuestro modelo simple que consiste en tres perceptrones organizados en dos capas puede ahora aproximar la función de entrada que estamos intentando aproximar.

[02:46] El ejercicio que acabamos de ver era un ejemplo sencillo que utilizaba una tarea de clasificación binaria. ¿Pero qué ocurre si tenemos más de dos posibles clases de salida? Digamos que estamos clasificando animales o flores con muchas clases diferentes. En lugar de utilizar una sola salida, una sola unidad en la capa de salida, podemos utilizar múltiples unidades en la capa de salida.

[03:13] Combinamos de nuevo nuestros perceptrones en capas en las que tenemos una capa de entrada que consiste en nuestras características de entrada. Nuestras características de entrada alimentan un conjunto de perceptrones en lo que llamamos una capa oculta, y tomamos las salidas de esos perceptrones en nuestra capa oculta y lo alimentamos en otra capa de perceptrones múltiples en nuestra capa de salida.

[03:37] Entonces tenemos una salida de cada uno de estos perceptrones en su nuestra capa de salida, y la salida de cada uno de ellos representa una puntuación para cada una de las clases de nuestro problema. Entonces miramos qué clase tiene la mayor puntuación asociada, y asignamos esa etiqueta de clase al punto de datos de entrada.

[04:00] Además, cuando combinamos perceptrones o neuronas artificiales, en lugar de utilizar un perceptrón como nodo de nuestra red, que tiene una función de umbral muy simple, podemos optar por utilizar una unidad que incluya una función de activación, como una función sigmoidea, como vimos en la regresión logística.

[04:23] Pero también podemos utilizar otras funciones como la tangente hiperbólica o la función ReLu, que ahora se utiliza muy comúnmente como función de activación. Cada nodo de nuestra red consistirá ahora en una combinación lineal de nuestras entradas multiplicadas por nuestros pesos para calcular la Z, y pasando nuestra Z a través de una función de activación no lineal y proporcionando la salida a la siguiente capa de la red.

[04:50] El uso de estas funciones de activación no lineales en cada capa, en lugar de un simple umbral como el perceptrón, nos permite modelar mejor las relaciones no lineales. Echemos un vistazo a una arquitectura típica de red neuronal y están en su trabajo comienza con una capa de entrada que consiste en cada una de las características de nuestros datos de entrada.

[05:13] A continuación, las características se multiplican por un peso y se introducen en cada uno de los nodos dentro de nuestra primera capa, a la que llamamos nuestra capa oculta. De nuevo, tomamos una combinación lineal de cada una de las características de entrada por cada uno de los pesos, calculamos nuestra Z y pasamos nuestra Z por Phi de Z, que es nuestra función de activación.

[05:36] De nuevo, podemos elegir nuestra función de activación. Podría ser sigmoidea o podría ser una función ReLu. Tomamos la salida de esa función de activación y la alimentamos a la siguiente capa. En este sencillo ejemplo, tenemos una red neuronal de tres capas. Tenemos un conjunto de entradas que estamos proporcionando, multiplicando esos pesos de comprador, combinándolos en nuestra capa oculta, pasándolos a través de nuestra función de activación, y alimentando eso en nuestra capa de salida.

[06:06] A continuación, se combinan en nuestra capa de salida, multiplicando esas salidas de la capa oculta anterior por los pesos, y, de nuevo, se pasan a través de una función de activación sobre la capa de salida para calcular nuestro sombrero y o nuestra predicción de nuestra red neuronal simple.

