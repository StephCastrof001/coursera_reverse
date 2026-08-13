---
title: "17-Cross Validation"
type: lesson
module: "[[M02 - The Modeling Process]]"
tags: [lesson, ml-foundations]
---

# 🎓 17-Cross Validation

> **Módulo:** [[M02 - The Modeling Process]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 17-Cross Validation
<!-- Módulo: 02-The Modeling Process | Archivo: 17-Cross Validation.es.vtt -->

[00:04] En la última lección, hablamos de la importancia de apartar un subconjunto de sus datos con fines de prueba, para que sirva como indicador imparcial del rendimiento del modelo. También hablamos de que podemos utilizar un conjunto de validación para ayudarnos en la evaluación del rendimiento de diferentes modelos como reentrenamiento y construcción de esos modelos.

[00:28] Otra estrategia común para evaluar y comparar múltiples modelos es lo que se denomina validación cruzada. En la validación cruzada, en lugar de utilizar un único subconjunto fijo de datos como nuestro conjunto de validación para comparar el rendimiento de los modelos, en realidad ejecutaremos múltiples iteraciones, y para cada iteración, elegiremos un subconjunto diferente de datos para que sirva como conjunto de validación, y el resto de los datos estarán a nuestra disposición para el entrenamiento del modelo.

[01:00] Un método común de validación cruzada es lo que se denomina validación cruzada K-folds. En la validación cruzada K-folds, dividimos nuestros datos en un número de subconjuntos o pliegues, como los llamamos. Normalmente, utilizamos cinco pliegues o 10 pliegues. Si realizáramos una validación cruzada de cinco pliegues, dividiríamos nuestros datos de entrenamiento en cinco pliegues.

[01:26] A continuación, ejecutamos cinco iteraciones, y para cada iteración, utilizaríamos una quinta parte de nuestros datos como conjunto de validación, y los cuatro restantes de éstos servirían como conjunto de entrenamiento. El conjunto de validación, cada pliegue rotaría. En la primera iteración, utilizamos la primera quinta parte de nuestros datos para la validación, las últimas cuatro quintas partes para el entrenamiento.

[01:50] En la segunda iteración, utilizaríamos la segunda quinta parte de nuestros datos para la validación, y el resto para el entrenamiento. Después de haber realizado las cinco iteraciones, podemos calcular el error como la media del error en cada pliegue de validación en cada iteración.

[02:12] Calculamos el error en el pliegue de validación para cada una de las cinco iteraciones, sumaríamos los errores, y dividimos por cinco para obtener el error medio a través de la validación K-fold. La validación cruzada se utiliza muy comúnmente en la industria para evaluar el rendimiento de los modelos como reentrenamiento y comparación de múltiples modelos.

[02:34] De hecho, generalmente se considera el enfoque preferido en lugar de utilizar un único conjunto de validación fijo. Hay un par de razones para ello. La primera es que la validación cruzada maximiza los datos disponibles para el entrenamiento del modelo. Utilizando un único subconjunto de validación fijo, eliminamos ese subconjunto para utilizarlo en el entrenamiento de nuestro modelo.

[02:57] Mientras que en la validación cruzada, debido a que el conjunto de validación rota cada vez, somos capaces de utilizar todos los datos disponibles para nosotros en algún momento durante una de las iteraciones para entrenar nuestro modelo. Si tenemos un conjunto de datos muy grande, esto es realmente menos preocupante.

[03:14] Pero si estamos haciendo un conjunto de datos más pequeño, esto puede convertirse rápidamente en una preocupación mucho mayor para nosotros. En segundo lugar, la validación cruzada generalmente proporciona una mejor evaluación de lo bien que el modelo puede generalizar para ser capaz de generar predicciones precisas sobre nuevos datos que nunca ha visto antes.

[03:32] Uno de los riesgos de utilizar un único conjunto de validación fijo es que podemos sesgar accidentalmente el rendimiento del modelo en ese conjunto, a través de la elección de los puntos de datos a incluir en ese único conjunto de validación fijo. En la validación cruzada, como nuestro subconjunto de validación va rotando en cada iteración, utilizamos todos los puntos de datos de que disponemos una sola vez para la validación.

[03:58] Así, podemos comparar y evaluar el rendimiento de los modelos en una gama mucho más amplia de puntos de datos, y reducimos las posibilidades de sesgar o el rendimiento del modelo a través de nuestra elección de los datos a utilizar en el conjunto de validación.

