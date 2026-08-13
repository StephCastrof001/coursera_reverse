---
title: "31-Softmax Regression"
type: lesson
module: "[[M04 - Linear Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 31-Softmax Regression

> **Módulo:** [[M04 - Linear Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 31-Softmax Regression
<!-- Módulo: 04-Linear Models | Archivo: 31-Softmax Regression.es.vtt -->

[00:04] En la última lección, hablamos de la situación en la que estamos prediciendo una clase que es binaria. Es un uno o un cero. En este caso, podríamos utilizar el modelo de regresión logística con esa función sigmoidea para darnos la probabilidad de la clase positiva o la probabilidad de que y fuera igual a 1.

[00:25] ¿Pero qué pasa si tenemos un problema, en el que tenemos más de dos clases? No es tan sencillo como predecir que y es igual a uno. En realidad necesitamos predecir cuál de muchas clases, algo podría ser. En el escenario binario en el que aplicamos la regresión logística, tomamos nuestros ejes de entrada, los multiplicamos por un conjunto de pesos y calculamos la z, que se parece mucho a la regresión lineal.

[00:53] Luego tomamos la salida de esa z y la introdujimos en nuestra función sigmoidea y salió la probabilidad de que y fuera igual a uno, o la probabilidad de que la entrada perteneciera a la clase positiva uno. En la situación multiclase, en lugar de utilizar la función sigmoidea, utilizamos lo que se denomina una función softmax para darnos la probabilidad de pertenecer a cada clase.

[01:21] En este caso, tenemos que calcular por separado para cada clase, la probabilidad de que la entrada pertenezca a esa clase. Para ello, volvemos a tomar nuestro eje de entrada, pero esta vez, en lugar de multiplicarlos por un único conjunto de pesos, los multiplicamos por un conjunto de pesos para cada clase.

[01:43] Calculamos una z para cada clase, introducimos la z en nuestra función softmax, y calculamos la probabilidad de que la entrada pertenezca a cada clase. Puede pensar en la función softmax como una función sigmoide normalizada. Actúa de forma muy parecida en el sentido de que, limita nuestra salida entre cero y uno para cada clase.

[02:07] Pero ahora, como tenemos varias clases, nos gustaría que cada una de esas salidas sumara 1, de modo que las probabilidades de cada clase sumadas sobre todas las clases posibles sean iguales a 1. Podemos entonces identificar la clase que tiene la probabilidad más alta y utilizar esa como la clase predicha para la entrada.

[02:29] Veamos un ejemplo de cómo funciona esto. Supongamos que estamos creando un modelo de clasificación para clasificar cuatro tipos de animales basándonos en imágenes que proporcionamos como entrada. Los animales que estamos clasificando son perros, gatos, conejos y osos. Como entrada a nuestro modelo, proporcionaríamos una imagen.

[02:51] Las características que utilizaríamos son en realidad los valores de cada uno de los píxeles dentro de nuestra imagen de entrada. Si tenemos una imagen que proporcionamos como entrada, que tiene ocho píxeles por ocho píxeles, tenemos un total de 64 características. Si utilizamos la regresión softmax para predecir varias clases, proporcionaríamos cada una de esas 64 características de entrada, y para cada una de nuestras cuatro clases, perro, gato, conejo y oso, multiplicaríamos los valores de esos píxeles de entrada por los pesos de esa clase.

[03:25] Calcularíamos la z de esa clase, la introduciríamos en nuestra función softmax y generaríamos la predicción de que esa imagen de entrada pertenece a cada clase. Haríamos esto para nuestras cuatro clases, y nuestro resultado podría ser algo parecido a esto. Perro, 0,8, gato, 0,05, conejo, 0,05, oso, 0,1.

[03:50] Para generar ahora una predicción discreta a partir de nuestro modelo, buscaríamos la clase a la que corresponda la mayor probabilidad. En este caso, perro corresponde a una probabilidad del 80 por ciento, y, por tanto, la salida de nuestro modelo sería perro.

