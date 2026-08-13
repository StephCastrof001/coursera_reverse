---
title: "08-Types of Machine Learning"
type: lesson
module: "[[M01 - What is Machine Learning]]"
tags: [lesson, ml-foundations]
---

# 🎓 08-Types of Machine Learning

> **Módulo:** [[M01 - What is Machine Learning]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 08-Types of Machine Learning
<!-- Módulo: 01-What is Machine Learning | Archivo: 08-Types of Machine Learning.es.vtt -->

[00:04] En esta sección, hablaremos de los tipos principales de aprendizaje automático. Hay tres tipos principales de aprendizaje automático, el aprendizaje supervisado, el aprendizaje no supervisado y el aprendizaje por refuerzo. En el aprendizaje supervisado, nuestro objetivo es predecir una variable objetivo dado un conjunto de observaciones.

[00:25] Cumplimos dos tareas principales, una es la clasificación o reconocimiento de una categoría o clase de un objeto. La segunda se denomina regresión o predicción de algún tipo de variable numérica , como el precio de una casa en venta. En el aprendizaje supervisado, generalmente disponemos de un gran conjunto de datos de observaciones pasadas para utilizarlos en el entrenamiento, así como la variable objetivo asociada a cada una de esas observaciones.

[00:51] Así, algunos ejemplos de aprendizaje supervisado serían el uso de imágenes de rayos X para identificar una neumonía en los pulmones o la predicción de los precios inmobiliarios. En el aprendizaje no supervisado, nuestro objetivo es un poco diferente, aquí estamos organizando los datos por algún tipo de estructura inherente.

[01:09] Generalmente disponemos de un conjunto de observaciones del pasado, pero no tenemos las variables objetivo asociadas para cada una de esas observaciones. Así que los tipos comunes de aprendizaje no supervisado serían la agrupación o la detección de anomalías y se utiliza para cosas como la segmentación del mercado, donde no hay definiciones comúnmente acordadas de segmentos de mercado.

[01:30] Pero nuestro objetivo es tomar los compradores o clientes potenciales para un determinado producto y dividirlos en grupos lógicos basados en algún tipo de patrón u orden inherente en esos clientes. El tercer tipo de aprendizaje automático se llama aprendizaje de refuerzo. Aquí nuestro objetivo es aprender una determinada estrategia a través de la interacción o alcanzar un objetivo.

[01:53] Este es el tipo de aprendizaje automático que se suele utilizar para enseñar a los ordenadores a entrenarse para aprender a jugar a cosas como el ajedrez o las damas. Ahora profundizaremos un poco más en el aprendizaje supervisado frente al no supervisado. En el aprendizaje supervisado, tenemos algún conjunto de observaciones pasadas de las características y tenemos el objetivo asociado para cada una de esas observaciones.

[02:17] Podemos utilizarlas para desarrollar un modelo. Así que digamos que queremos construir un modelo para reconocer manzanas. Tenemos un conjunto de imágenes de manzanas, y para cada una de esas imágenes, tenemos una etiqueta que dice que esto es una manzana. Construimos un modelo utilizando ese conjunto de imágenes de manzanas, y entonces nuestro modelo es ahora capaz de reconocer nuevas imágenes de manzanas, así que podemos alimentarlo con una imagen de una manzana diferente y debería ser capaz de reconocer que esto también es de hecho una manzana.

[02:48] En el aprendizaje no supervisado, tenemos observaciones pero generalmente no tenemos valores objetivo que estén asociados a esas observaciones. Así que siguiendo con nuestro ejemplo de la fruta aquí, podríamos proporcionar un gran conjunto de imágenes de diferentes tipos de frutas a nuestro modelo.

[03:04] Nuestro modelo sería entonces capaz de organizar o agrupar esas frutas basándose en algún tipo de patrón o estructura inherente. Podría utilizar el color o la forma, por ejemplo, para separar las manzanas de las naranjas de los plátanos, pero no sabría necesariamente que estas son manzanas o estos son plátanos porque no hemos proporcionado la información objetivo para cada una de las observaciones para poder aprender ese objetivo.

[03:29] Nuestro objetivo, de nuevo, es diferente. Estamos intentando agrupar u organizar cosas, no predecir un objetivo de salida específico. Existen dos tipos principales de aprendizaje supervisado, la regresión y la clasificación. En la regresión, nuestro objetivo es predecir alguna variable objetivo numérica.

[03:47] Hemos hablado del ejemplo del precio de la vivienda. Otros tipos de regresión podrían utilizarse para cosas como predecir la demanda de un determinado producto nuevo que se va a lanzar, predecir los cortes de electricidad o la demanda de electricidad a lo largo del tiempo, para lo que tomaré valores numéricos.

[04:05] En la clasificación, en lugar de predecir un valor numérico continuo, estamos prediciendo o identificando una clase o categoría para una determinada observación. Ejemplos de esto podrían ser la detección de enfermedades pulmonares, la identificación de diferentes tipos de plantas o flores, la detección de si un mensaje de correo electrónico, un mensaje de spam, o no es un mensaje de spam.

[04:30] En todos estos casos, tenemos un conjunto de categorías que puede ser binario, ya sea sí o no, uno o cero o quizá una de entre muchas categorías posibles, como tipos de flores. Y nuestro objetivo es predecir la categoría en la que cae una nueva observación de entrada .

