---
title: "34-Tree Models"
type: lesson
module: "[[M05 - Trees, Ensemble Models and Clustering]]"
tags: [lesson, ml-foundations]
---

# 🎓 34-Tree Models

> **Módulo:** [[M05 - Trees, Ensemble Models and Clustering]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 34-Tree Models
<!-- Módulo: 05-Trees, Ensemble Models and Clustering | Archivo: 34-Tree Models.es.vtt -->

[00:04] El árbol de decisión es un algoritmo de aprendizaje automático que formula una serie de preguntas con el fin de acotar una predicción para un punto de datos dado. La forma más fácil de entender el árbol de decisión es ver un ejemplo. Supongamos que queremos crear un modelo de clasificación para clasificar cuatro tipos de animales: perros, lagartos, pájaros y alces.

[00:30] Y queremos hacerlo formulando una serie de preguntas sobre cada uno de estos animales para determinar de qué animal se trata. Podríamos empezar preguntando, ¿tiene cuernos el animal? De las cuatro posibles clases de animales que tenemos, sabemos que sólo hay una clase que tenga cuernos, que es un alce.

[00:53] Así que si la respuesta a nuestra pregunta es sí, podemos predecir que el animal es un alce. Sin embargo, si la respuesta a nuestra pregunta es no, aún no estamos seguros de qué animal es. Podría ser un perro, un lagarto o un pájaro. Así que entonces hacemos una segunda pregunta, ¿cuántas patas tiene el animal?

[01:13] ¿Tiene dos patas o cuatro patas? Si el animal tiene dos patas, podemos predecir que es un pájaro. Si el animal tiene cuatro patas, todavía no estamos seguros. Podría ser un perro, pero también podría ser un lagarto. Así que hagamos una pregunta más. ¿De qué color es el animal? Si es verde, podemos predecir que el animal es un lagarto, y si es marrón, podemos suponer que el animal es un perro.

[01:43] Al hacer la serie de preguntas, ya hemos formado el árbol de decisión. Y así, si tomáramos un nuevo animal, podríamos mapearlo a través del árbol y podríamos calcular la clase predicha como la salida basada en dónde cae dentro del árbol. Entonces, ¿cómo elegimos las divisiones que forman un árbol de decisión?

[02:03] Nuestro objetivo es construir el árbol más eficiente o el que utilice el mínimo número de divisiones para dividir eficazmente los datos en nuestras clases objetivo. Para elegir las divisiones, definimos una función objetivo que nos ayude a seleccionar qué división es la mejor. Y la función objetivo que utilizamos es maximizar la ganancia de información en la división.

[02:28] La ganancia de información es igual a la disminución de la impureza al dividir nuestros datos. Así que la impureza significa lo bien mezclados que están nuestros datos en cualquier punto dentro de nuestro árbol. Si tuviera un cierto nodo en nuestro árbol, nuestros datos están altamente mezclados entre dos clases, digamos la clase A y la clase B.

[02:48] Nuestros datos tienen un alto grado de impureza. Si creamos una división que efectivamente divida nuestros datos entre A y B, tal que una hoja, tenemos etiquetas que son enteramente de la clase A, y que la otra hoja tenemos datos que son enteramente de la clase B. Hemos reducido nuestra impureza hasta cero.

[03:09] Así que hemos creado una disminución bastante significativa de la impureza. O dicho de otra manera, hemos aumentado con éxito la ganancia de información procedente de esa división. Así que la idea de crear un árbol de decisión es encontrar preguntas o divisiones que puedan reducir la mezcla de los datos o separarlos efectivamente en las clases individuales.

[03:34] Cuando estamos creando una división, miramos todas las formas posibles en las que podríamos dividir nuestros datos en ese punto del árbol. Así que miramos cada una de las características en las que podríamos dividir. Y para cada una de esas características miramos diferentes valores posibles en los que podríamos dividir.

[03:48] Y elegimos la combinación de la característica y el valor sobre el que dividirnos que dé como resultado la máxima ganancia de información, o la mayor disminución de impurezas al dividirnos sobre esa característica y ese valor. Una vez que hemos creado el árbol, ¿cómo generamos realmente predicciones a partir del árbol?

[04:11] Los nodos inferiores de un árbol se denominan hojas del árbol. Para calcular la predicción real o el valor para todos los puntos que se dan en cada hoja del árbol, generalmente tomamos una media si estamos trabajando con un modelo de regresión, o un voto mayoritario si estamos trabajando con un modelo de clasificación.

[04:33] Así que digamos que tenemos algunos datos que están mezclados en cierto nodo entre la clase A y la clase B. Hacemos una división y dividimos eso en dos hojas. Una hoja tiene una mayoría de la clase A, la otra hoja tiene una mayoría de la clase B. La predicción para esa hoja es cualquiera que sea la clase que tenga la mayoría.

[04:53] Así que para la hoja 1, la predicción para todos los puntos de datos en esa hoja sería de clase A. Y para la hoja 2, como tiene mayoría de clase B, hacemos una predicción para cada punto que llegue a esa hoja se predeciría que sería de clase B. Una de las cosas clave que tenemos que determinar cuando estamos creando un árbol es la profundidad óptima de nuestro árbol.

[05:16] Y esto realmente puede marcar una gran diferencia en términos de la capacidad de predicción de su árbol. Así que la profundidad de un árbol es el número máximo de divisiones que se producen dentro de ese árbol. Y en realidad es un número que podemos elegir. Podemos decidir crear un árbol muy poco profundo limitándonos a como mucho una o dos divisiones en nuestro árbol antes de crear las hojas.

[05:38] O podemos tener un número ilimitado de divisiones en nuestro árbol, de tal forma que cada hoja contenga un solo punto. Los árboles muy poco profundos, con un número reducido de divisiones, tienden a ajustarse mal a los datos. Son demasiado simples para captar realmente los patrones dentro de los datos y dividir eficazmente sus datos.

[05:59] Por otro lado, los árboles que son muy profundos tienden a ajustarse demasiado a los datos, porque cada ejemplo u observación puede acabar en su propia hoja. Esto puede ajustarse muy bien a su conjunto de datos de entrenamiento, pero cuando intente utilizarlo para generalizar en nuevos datos, descubrirá que se está sobreajustando y no está funcionando muy bien.

[06:19] Tomemos un ejemplo para ilustrar el impacto que tiene la profundidad del árbol en la complejidad del modelo y los resultados resultantes que es capaz de generar. En la parte izquierda de esta diapositiva, tenemos un conjunto de datos organizados a lo largo de dos características, x1 que se muestra en el eje horizontal, y x2 que se muestra en el eje vertical.

[06:37] Nuestros datos están etiquetados en las cuatro clases, que se denotan por el sombreado de color de los puntos de datos. Intentemos ahora ajustar un modelo de árbol simple para clasificar nuestros datos. Empezaremos utilizando una profundidad de árbol de uno, lo que significa que sólo tenemos un único nodo o división en nuestro modelo.

[06:55] Podríamos ver el resultado en la parte derecha de la diapositiva. Nuestro modelo de árbol de un único nodo está utilizando una única división en el valor de x2 para dividir sus datos. Debido a que está utilizando sólo una única división, puede dividir los datos en sólo dos clases.

[07:12] En realidad tenemos cuatro clases en nuestro conjunto de datos. Y por lo tanto nuestro modelo simple que utiliza sólo una única división está infraajustando o los datos al predecir sólo dos clases en relación con las cuatro clases reales que tenemos en nuestro problema. Si ahora empezamos a aumentar la profundidad de nuestro árbol, podemos trazar límites de decisión más complejos, dividiendo nuestros datos a lo largo de x1 y x2, como denotan las líneas horizontales y verticales.

[07:39] Y como resultado, podemos diferenciar nuestros puntos de datos y dividirlos en más clases. A medida que aumentamos nuestra profundidad a dos y luego a tres, puede ver que ahora empezamos a ser capaces de captar mejor la variabilidad y la división de los datos en cada una de las cuatro clases.

[08:00] A medida que seguimos aumentando la complejidad de nuestro modelo y añadimos más y más capas, podemos ver que ahora estamos cortando y dividiendo nuestro espacio de decisiones en muchas más particiones. Bien, esto puede mejorar la precisión en unos datos de entrenamiento. Lo que ocurre es que cuando ahora pasamos a un conjunto de datos de prueba, o utilizamos un modelo más complejo para generar predicciones sobre nuevos datos.

[08:22] Hemos ajustado tanto nuestro modelo al conjunto de entrenamiento que hemos creado particiones basadas en el ruido que se encuentra en el conjunto de entrenamiento. No siempre se encuentra el mismo ruido en nuestro conjunto de prueba o en un dato nuevo. Y como resultado, nuestro modelo es bastante inflexible y a menudo no genera un gran rendimiento en la predicción de datos nuevos.

[08:44] También podemos utilizar árboles para problemas de tipo regresión. En un problema de regresión, en lugar de tomar un voto mayoritario de las diferentes muestras que caen en una hoja, tomamos la media de los valores objetivo de cada una de las muestras en esa hoja. Así que digamos que tenemos un nodo concreto que da lugar a dos hojas.

[09:05] La hoja 1 tiene 4 muestras que caen en esa hoja de 5, 9, 8 y 6. Y la hoja 2 tiene 3 muestras 4, 2 y 3. Para generar la predicción para las muestras que caen en la hoja 1, sumamos los valores objetivo de las cuatro muestras, dividimos por el número de valores objetivo son cuatro. Y calculamos una predicción de siete, que es el valor predicho para cada muestra que cae en esta hoja del árbol.

[09:36] Del mismo modo, para la hoja 2, podemos calcular un valor medio de tres. Y así nuestra predicción para cada muestra que cae en esta hoja del árbol basada en las divisiones del árbol es de tres. Una de las principales ventajas de los modelos de árbol de decisión es que son muy interpretables.

[09:56] Debido a esta serie de preguntas o divisiones, es muy fácil seguir el orden de las preguntas y rastrear cómo hemos llegado a una determinada predicción dado un valor de entrada. También se entrenan muy rápidamente, y como son un modelo no paramétrico, lo que significa que no están limitados a ninguna función modelo específica, pueden manejar muy bien las relaciones no lineales.

[10:22] Tampoco requieren escalar nuestros datos o trabajo extra codificando variables categóricas antes de introducirlas en nuestro modelo. Uno de los retos de los modelos de árboles de decisión individuales es que son muy sensibles a la profundidad que elegimos para hacer crecer nuestro árbol.

[10:40] Si elegimos una profundidad pequeña, acabamos con un modelo muy simple. Realmente no hace un trabajo muy bueno de predicción ni en datos de entrenamiento ni en un conjunto de datos de prueba. Uno de los mayores problemas es elegir una profundidad que sea demasiado profunda, de tal manera que nuestro modelo funcione muy bien en los datos en los que ha sido entrenado.

[11:00] Pero nuestro modelo está en realidad sobreajustado a sí mismo a esos datos de entrenamiento. Y así, cuando intentamos utilizarlo para generalizar y crear predicciones sobre nuevos datos, realmente no hace un trabajo muy bueno.

