---
title: "23-Classification Error Metrics Confusion Matrix"
type: lesson
module: "[[M03 - Evaluating and Interpreting Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 23-Classification Error Metrics Confusion Matrix

> **Módulo:** [[M03 - Evaluating and Interpreting Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 23-Classification Error Metrics Confusion Matrix
<!-- Módulo: 03-Evaluating & Interpreting Models | Archivo: 23-Classification Error Metrics Confusion Matrix.es.vtt -->

[00:03] En la última lección, hablamos de métricas de salida comunes que se utilizan para problemas de regresión. Ahora hablaremos del escenario de clasificación y cubriremos algunas de las métricas populares utilizadas para tipos de tareas de clasificación. Con diferencia, la métrica de clasificación más común es la precisión.

[00:23] La precisión es muy popular, es fácil de entender, y encontrará valores de precisión por todas partes. La exactitud simplemente se refiere a el número de predicciones que hemos conseguido correctas dividido por el número total de predicciones que hemos generado. El reto con la exactitud es que a veces puede ser engañosa en situaciones en las que tenemos lo que se llama desequilibrio de clases, lo que significa que en nuestro problema dado tenemos un número muy grande de una clase y un número relativamente mucho menor de valores en nuestra otra clase.

[01:00] Para ilustrar esto, consideremos una situación. Estoy construyendo un modelo para predecir si los pacientes padecerán o no una enfermedad cardiaca. Para este modelo utilizo datos de un estudio médico que incluía miles de pacientes y varias características para cada paciente junto con una etiqueta que es un uno o un cero, indicando si fueron diagnosticados con una enfermedad cardiaca o no.

[01:25] Utilizo este conjunto de datos, creo un modelo clasificador, y evalúo el resultado de mi modelo utilizando la precisión, y descubro que he logrado una precisión del 99,4 por ciento. Suena genial. Tengo un modelo excelente. ¿Cuál es el problema? El problema es que, si miramos en nuestro conjunto de datos un poco más a fondo, descubrimos que teníamos un desequilibrio de clases muy alto en nuestro conjunto de datos.

[01:49] La gran mayoría de los pacientes del estudio no tenían enfermedades cardiacas. Así que el modelo que creamos en realidad sólo predijo un cero o ninguna enfermedad cardiaca para cada uno de los pacientes y el modelo acertó el 99,4 por ciento de las veces pero el modelo era en realidad bastante inútil.

[02:08] Un método mejor para evaluar el resultado de un modelo de clasificación es utilizar lo que se denomina matriz de confusión. Una matriz de confusión es una matriz que ilustra en un eje los valores verdaderos de nuestra y. En el caso de una clasificación binaria, o una clasificación de cero o uno, la dividiríamos en valores negativos y positivos de cero y uno, y en el otro eje de nuestra matriz destacaríamos la clase predicha o sombrero y, de nuevo, separando en uno o cero.

[02:45] Utilizando nuestra matriz de confusión podemos entonces empezar a calcular las métricas de error de clasificación. En el cuadrante superior izquierdo de nuestra matriz, en el caso en el que el valor verdadero de y fuera un uno y el valor predicho fuera un uno, llamamos a estos verdaderos positivos.

[03:05] En la esquina opuesta, en la que nuestro valor verdadero fuera un cero o una clase negativa y predijéramos con éxito un cero, llamamos a estos verdaderos negativos. En el caso en el que el valor real fuera un cero pero predijéramos un uno o positivo, lo llamamos falso positivo. Del mismo modo, cuando el valor real fuera un uno pero predijéramos un cero o negativo, lo llamamos falso negativo.

[03:33] Una de las métricas de error que utilizaremos basándonos en esta matriz de confusión es lo que se llama tasa de verdaderos positivos o también llamada recall o sensibilidad de un modelo. La tasa de verdaderos positivos o recall se refiere a de todos los positivos cuántos identificamos correctamente como positivos.

[03:54] Lo calculamos como el número de verdaderos positivos dividido por la suma de los verdaderos positivos más los falsos negativos. También podemos identificar la tasa de falsos positivos o FPR de un modelo. La FPR se refiere a de todos los negativos cuántos clasificó incorrectamente el modelo como positivos.

[04:18] Para calcular el FPR, tomamos nuestros falsos positivos divididos por la suma de los falsos positivos más nuestros verdaderos negativos. El valor de precisión de nuestro modelo se refiere a algo un poco diferente, de los valores que predijimos como de la clase positiva o como unos, cuántos de esos fueron realmente positivos.

[04:45] Lo calculamos utilizando los verdaderos positivos divididos por los verdaderos positivos más los falsos positivos. En los ejemplos anteriores, vimos una configuración de clasificación binaria y la matriz de confusión resultante. También podemos aplicar una matriz de confusión a problemas en los que tenemos múltiples clases que estamos intentando predecir.

[05:06] Generamos la matriz de confusión del mismo modo, excepto que ahora, en lugar de un único uno o cero en cada eje, tenemos múltiples clases. Utilizamos esta matriz de confusión multiclase para mostrarnos dónde el modelo tiene dificultades para diferenciar entre determinadas clases. También podemos calcular métricas utilizando la matriz de confusión multiclase, igual que hicimos en la configuración binaria.

[05:29] Sin embargo, ahora podemos calcular estas métricas para cada clase, por ejemplo, el recuerdo y la precisión de cada clase de nuestro problema. También podemos calcular métricas medias en todas las clases, a las que llamamos el macro promedio del recuerdo o el macro promedio de la precisión.

