---
title: "07-What is a Model"
type: lesson
module: "[[M01 - What is Machine Learning]]"
tags: [lesson, ml-foundations]
---

# 🎓 07-What is a Model

> **Módulo:** [[M01 - What is Machine Learning]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 07-What is a Model
<!-- Módulo: 01-What is Machine Learning | Archivo: 07-What is a Model.es.vtt -->

[00:05] Entonces, ¿qué es exactamente un modelo? Un modelo es simplemente una aproximación de la relación entre dos o más variables. Típicamente con un modelo, tenemos una o más variables de entrada, que llamamos x, y tenemos una o más variables de salida de nuestro modelo, que generalmente llamamos y.

[00:25] Un modelo simplemente aproxima la relación entre x e y. En la forma de y es una función de x más un término de error en reconocimiento que generalmente nunca podemos crear un modelo perfecto que pueda predecir completamente los valores de y sin error. Así que siempre añadimos un término de error adicional para reconocerlo.

[00:48] Pongamos un ejemplo de modelo. Supongamos que hemos recopilado un montón de datos sobre motores de coches y nos gustaría intentar aproximar la eficiencia del combustible de un coche en millas por galón a partir de los datos que hemos recopilado sobre los caballos de potencia del motor del coche.

[01:03] Puede ver en la pantalla un gráfico sencillo en el que trazamos los caballos de potencia en el eje horizontal y las millas por galón en el eje vertical. En este caso, los caballos de potencia sirven como variable de entrada a nuestro modelo y la variable que estamos tratando de predecir las millas por galón es nuestra variable de salida.

[01:24] Podemos crear un modelo en el que las millas por galón sean una función de los caballos de potencia más algún término de error. Como puede ver en la pantalla, el modelo puede aproximarse aproximadamente a las millas por galón dada la información sobre los caballos de potencia. Pero no es capaz de capturar perfectamente la aleatoriedad de los datos que tenemos sobre las millas por galón.

[01:45] Y, por lo tanto, es importante tener siempre presente que siempre hay alguna pequeña cantidad de error en su modelo. Volvamos ahora al ejemplo que estábamos utilizando anteriormente, en el que nos gustaría crear un modelo para predecir el precio de venta de las viviendas en venta.

[02:01] En este ejemplo, las características de las viviendas en venta, como el distrito escolar, los metros cuadrados de la vivienda, el número de dormitorios de los atributos de cada vivienda serían los valores x, lo que llamamos las características de nuestro modelo. Disponemos de una serie de observaciones históricas de estas características que están representadas por datos que hemos recopilado sobre viviendas que han estado a la venta en el pasado.

[02:29] Asimismo, para cada una de esas observaciones, también tenemos nuestro valor y, que es el precio de venta real de esa vivienda. Podemos utilizar estas observaciones históricas de nuestros datos de entrada. Y estos valores y históricos o valores objetivo para crear entonces un modelo que pueda aproximar la relación entre los datos de entrada representados por nuestras características y los objetivos de salida.

[02:57] Para crear un modelo, hay cuatro cosas que tenemos que definir. La primera es el conjunto de características a utilizar o los atributos de nuestros datos que queremos utilizar como entradas de nuestro modelo. La segunda cosa que tenemos que definir es nuestra elección del algoritmo.

[03:14] En el aprendizaje automático, hay una variedad de algoritmos diferentes que podemos elegir. Y el algoritmo actúa como una forma general o una plantilla para el modelo que estamos creando para definir la forma aproximada y la estructura del modelo. Cada algoritmo también tiene un conjunto de valores de hiperparámetros que luego tenemos que definir.

[03:35] Puede pensar en los valores de hiperparámetro como perillas que podemos girar en el algoritmo para hacer nuestro algoritmo más simple o más complejo para que se ajuste mejor a nuestros problemas. Y la cuarta cosa que necesitamos encontrar es una elección de la función de pérdida, que estamos buscando optimizar.

[03:52] Y así es como entrenamos nuestro modelo. Una función de pérdida es una forma de cuantificar el error en nuestro modelo y a medida que construimos y entrenamos nuestro modelo, buscamos minimizar el error. Es entonces cuando definimos la función de pérdida. Nuestro trabajo es minimizar la función de pérdida o minimizar la cantidad de error y ajustar los valores de nuestro modelo para que den como resultado ese mínimo de la función de pérdida.

[04:19] Cuando entrenamos nuestro modelo, utilizamos datos históricos generalmente en las entradas, así como en las salidas. Nuestro algoritmo y nuestros hiperparámetros, proporcionan una forma o estructura general para un modelo. Y a medida que entrenamos nuestro modelo utilizando esos datos históricos, estamos aprendiendo valores para el modelo que minimizan nuestra función de pérdida o minimizan la cantidad de error en el modelo final que creamos.

