---
title: "16-Test and Validation Sets"
type: lesson
module: "[[M02 - The Modeling Process]]"
tags: [lesson, ml-foundations]
---

# 🎓 16-Test and Validation Sets

> **Módulo:** [[M02 - The Modeling Process]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 16-Test and Validation Sets
<!-- Módulo: 02-The Modeling Process | Archivo: 16-Test and Validation Sets.es.vtt -->

[00:03] En esta lección, estamos vamos a hablar sobre la evaluación de rendimiento del modelo. Evaluamos el rendimiento del modelo de dos maneras diferentes. La primera forma es tal como estamos construyendo y entrenando un modelo, mientras evaluamos diferentes algoritmos para nuestro modelo, o modificarlos hiperparámetros, ajustando los diales del modelo, queremos evaluar el rendimiento así sabemos si estamos mejorando las cosas o empeorando las cosas.

[00:31] La segunda forma: evaluar el rendimiento es que, después de finalizar nuestro modelo, también queremos evaluar el rendimiento utilizando nuevos datos invisibles. ¿Por qué lo hacemos dos veces? Bueno, el objetivo de la predicción modelar es crear un modelo que sea muy eficaz en la generación de predicciones sobre los nuevos datos que tiene el modelo nunca antes visto, por lo que datos que no se utilizaron para crear o entrenar el modelo en primer lugar.

[00:58] No podemos estimar el rendimiento de los datos que no tenemos, que son datos nuevos. En cambio, lo que hacemos es tomar los datos que hemos recopilado, nuestro conjunto de entrenamiento, y dividirlos en dos subconjuntos diferentes. El primer subconjunto que utilizamos para el entrenamiento de modelos, así que lo usamos para construir y luego entrenar el modelo y evaluar y comparar diferentes tipos de modelos.

[01:23] El segundo subconjunto es denominado conjunto de pruebas. Usamos el conjunto de datos de prueba para evaluar el rendimiento del modelo final que hemos creado. Hacemos esto para ser representativos de la la capacidad del modelo para generar predicciones precisas sobre nuevos datos que el modelo nunca había visto antes y que no se usaron originalmente entrenando el modelo.

[01:47] Por lo general, cuando dividimos nuestros datos en un entrenamiento y un conjunto de pruebas, usaremos aproximadamente Entre el 80 y el 90 por ciento de los datos disponibles que hemos recopilado durante la formación y seleccionar el modelo. Luego reservaremos aproximadamente Del 10 al 20 por ciento para usarlo como conjunto de pruebas al evaluar el rendimiento de nuestro modelo final.

[02:08] El problema común en la creación de modelos de aprendizaje automático es lo que se denomina fuga de datos. La fuga de datos se produce cuando algunos de los datos que tenemos Lo que se destina a nuestro set de pruebas se utiliza accidentalmente en la construcción o el entrenamiento el modelo de alguna manera.

[02:25] Esto puede suceder en muchas formas diferentes, algunas de las cuales son realmente no es tan obvio. Por ejemplo, si usáramos todo nuestro conjunto de datos, incluido el entrenamiento, pero también el conjunto de pruebas para seleccionar las características de un modelo o para compare diferentes algoritmos, en realidad ya lo hemos hecho usó los datos del conjunto de pruebas como parte de uno de los pasos de construir nuestro modelo.

[02:51] Por lo tanto, un conjunto de pruebas los datos ya no son representativos del la capacidad del modelo para generar predicciones sobre datos nuevos. Ya que ya tenemos lo usé como parte de la maqueta proceso en sí mismo, realmente se ha convertido datos de entrenamiento en su lugar. ¿Qué pasa cuando tenemos una fuga de datos y utilizamos accidentalmente nuestro pruebe los datos como parte de la construcción del modelo el proceso es que invalida lo estimado rendimiento del modelo.

[03:20] En general, lo haremos descubre que provoca la estimación del rendimiento ser demasiado optimista. El rendimiento en el conjunto de prueba es en realidad mejor que lo que podríamos esperar de la actuación centrarse en generar predicciones utilizando los nuevos datos que tiene el modelo nunca antes visto.

[03:38] A menudo, durante la construcción de modelos y la formación, queremos comparar diferentes modelos. Modelos en los que se puede basar en diferentes algoritmos, o tal vez usando valores diferentes para estos hiperparámetros o estos diales que podemos ajustar en el modelo. Si tuviéramos que usar nuestro conjunto de pruebas para comparar el rendimiento de diferentes modelos, nuestro conjunto de pruebas ya no es un indicador imparcial del rendimiento de nuestro modelo final.

[04:04] En cambio, generalmente divida aún más nuestro conjunto de datos de entrenamiento y divídalo en otros dos subconjuntos. Uno es un set de entrenamiento y el segundo es lo que llamado conjunto de validación. Luego podemos construir y entrenar el modelo en nuestra capacitación subconjunto y utilizamos este nuevo conjunto de validación para comparar diferentes modelos y realizar la selección del modelo.

[04:30] Una vez que hayamos seleccionado nuestro modelo final, reentrenamos nuestro modelo final utilizando el entrenamiento y el validamos los datos juntos y, a continuación, podemos evaluarlos el rendimiento del modelo utilizando el conjunto de pruebas. De esta forma, nos aseguramos de que el equipo de prueba siempre queda a un lado y solo se usa una vez que hemos hecho una selección final de nuestro modelo para que el conjunto de prueba pueda permanecer un indicador imparcial de la capacidad del modelo para generalizar y generar predicciones precisas sobre datos nuevos que nunca antes se habían visto.

[05:03] Por lo general, cuando haz esto y divide nuestro conjunto de entrenamiento en un entrenamiento y un conjunto de validación, usaremos aproximadamente 60- El 80 por ciento de nuestro conjunto para fines de entrenamiento y luego aproximadamente del 10 al 20 porcentaje para la validación.

