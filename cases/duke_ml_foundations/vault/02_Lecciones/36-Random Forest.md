---
title: "36-Random Forest"
type: lesson
module: "[[M05 - Trees, Ensemble Models and Clustering]]"
tags: [lesson, ml-foundations]
---

# 🎓 36-Random Forest

> **Módulo:** [[M05 - Trees, Ensemble Models and Clustering]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 36-Random Forest
<!-- Módulo: 05-Trees, Ensemble Models and Clustering | Archivo: 36-Random Forest.es.vtt -->

[00:06] Un método específico que se utiliza habitualmente para construir modelos de conjunto es lo que se denomina bagging, que es la abreviatura de bootstrap aggregating. En el bagging, utilizamos muestras bootstrap para entrenar múltiples modelos que juntamos en un conjunto. ¿Qué significa bootstrap?

[00:25] Significa muestreo con reemplazo. Así que digamos que tenemos un gran número de muestras u observaciones en nuestros datos. Sacamos aleatoriamente un cierto número de esas observaciones para utilizarlas para entrenar un modelo. Y cada vez que sacamos una observación para utilizarla, la reemplazamos en el conjunto original.

[00:43] Lo que significa que en realidad podríamos tomar la misma observación múltiples veces porque seguimos reemplazándola. Así que bootstrapping significa muestreo con reemplazo cada vez que muestreamos una fila para utilizarla. Seleccionamos el tamaño del subconjunto de bagging que elegimos, y podemos definirlo como un porcentaje del número original de filas en nuestros datos, o simplemente como un número de filas que elegimos utilizar.

[01:16] Cuando creamos modelos de ensamblaje, como cada modelo se entrena en un subconjunto diferente de datos, las predicciones de salida de cada modelo pueden considerarse casi independientes. Por lo tanto, obtenemos los beneficios de los modelos de ensamblaje cuando los combinamos. Normalmente, los combinamos utilizando una media, ya sea media simple o media ponderada.

[01:39] Y al combinarlos, que se crean cada uno en un subconjunto de ensamblaje separado, reducimos la varianza en las predicciones de salida globales y reducimos la probabilidad de sobreajuste a nuestros datos. El tipo más común de modelo de ensamblaje es lo que se denomina bosque aleatorio.

[01:59] Si recordamos nuestra discusión sobre los modelos de árboles de decisión, uno de los retos de los árboles de decisión es que tienden a sobreajustar los datos. Para superar este reto, en lugar de cultivar un único árbol de decisión para un problema que estamos intentando modelar, podemos cultivar múltiples árboles de decisión y tomar un voto mayoritario entre los árboles.

[02:20] Para asegurarnos de que cada árbol está lo más cerca posible de ser independiente de los otros árboles, cultivamos árboles utilizando un subconjunto de bolsas de nuestros datos. Así, para cada árbol que queremos hacer crecer, aplicamos la agregación bootstrap o bagging para crear un subconjunto de datos.

[02:40] Y tomamos muestras de las filas u observaciones de nuestros datos originales, pero también de las columnas o las características de los datos. De modo que cada subconjunto sobre el que entrenamos un modelo consta de cierto número de filas y cierto número de características de nuestros datos originales.

[03:00] Así, de nuevo, los modelos de árbol que cultivamos pueden considerarse casi independientes unos de otros , porque se entrenan en subconjuntos diferentes de datos. Combinamos estos modelos de árbol y tomamos un voto mayoritario en el caso de la clasificación. O si estamos aplicando nuestro bosque aleatorio a un problema de agresión, tomamos una media simple de las predicciones que genera cada uno.

[03:24] Al hacer esto, reducimos la varianza de las predicciones de salida y reducimos la probabilidad de sobreajustar nuestro modelo de bosque aleatorio conjunto a los datos. Los bosques aleatorios son estupendos para trabajar con problemas complejos del mundo real en los que tenemos relaciones altamente no lineales entre entradas y salidas.

[03:45] Aunque perdemos parte de la interpretabilidad de los árboles de decisión individuales, donde podemos mirar dentro del árbol para entender cómo se están generando las predicciones. La ventaja que ganamos es que reducimos la varianza y reducimos la probabilidad de sobreajuste en los datos de entrenamiento.

[04:03] Uno de los retos de aplicar modelos de conjunto de bosques aleatorios es que hay una serie de decisiones que tenemos que tomar y cómo construyen el bosque aleatorio. Estas decisiones se dividen en tres categorías principales. La primera es el número de árboles que vamos a cultivar en nuestro modelo de bosque aleatorio , o el número de modelos de árboles individuales que vamos a combinar en nuestro modelo de conjunto .

[04:27] La segunda decisión que tenemos que tomar es nuestra estrategia de muestreo para aplicar el ensamblaje. ¿Cómo vamos a elegir un subconjunto de datos de los datos originales para utilizarlo en el crecimiento de cada modelo de árbol? Nuestra estrategia de muestreo incluye dos partes.

[04:43] La primera es el tamaño de la muestra de embolsamiento como porcentaje del conjunto total de datos originales, en términos del número de filas u observaciones que tenemos. La segunda parte de nuestra estrategia de muestreo es el número máximo de características que queremos que estén representadas en cada muestra de embolsamiento.

[05:03] Por lo tanto, cuando aplicamos el muestreo en bolsas, no tenemos que muestrear todas las características de cada fila que elijamos utilizar en nuestro subconjunto. En su lugar, podemos elegir utilizar un determinado porcentaje de características. De nuevo, esto ayuda a garantizar que los modelos de árbol que crecemos basándonos en las diferentes submuestras de datos sean lo más parecido posible a ser independientes entre sí .

[05:35] La tercera elección que tenemos que hacer es la profundidad de cada árbol de nuestro bosque aleatorio. Y de nuevo, la profundidad del árbol controla el equilibrio entre el ajuste insuficiente y el ajuste excesivo de nuestros datos. Podemos establecerlo de dos maneras. Una es que podemos especificar la profundidad máxima, o el número máximo de divisiones o nodos en cada uno de nuestros árboles.

[05:52] Y la segunda forma en que podemos especificar esto es estableciendo un número mínimo de muestras por hoja en nuestro árbol. Así que si no especificamos esto, podemos hacer crecer un árbol muy grande tal que cada hoja en el árbol termine con una sola observación en la hoja. Esto sería un modelo de árbol de decisión muy complejo que se ajusta estrechamente a unos datos de entrenamiento.

[06:15] Cuando hacemos esto, también podemos correr el riesgo de sobreajustarnos a los datos de entrenamiento. Así que en lugar de permitir que crezca tanto que cada hoja contenga sólo una muestra, podemos especificar un número mínimo de muestras por hoja. De manera que el árbol deje de crecer por sí mismo cuando alcance ese número mínimo de muestras en cada una de sus hojas.

[06:36] Esto da como resultado un árbol menos profundo, que tiene menos probabilidades de sobreajustarse a los datos de entrenamiento.

