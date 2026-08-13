---
title: "29-Regularization"
type: lesson
module: "[[M04 - Linear Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 29-Regularization

> **Módulo:** [[M04 - Linear Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 29-Regularization
<!-- Módulo: 04-Linear Models | Archivo: 29-Regularization.es.vtt -->

[00:03] En la última lección, discutimos el método de entrenamiento para la regresión lineal, cómo calculamos la suma del error cuadrático, y buscamos encontrar los valores para los pesos o coeficientes que minimicen la suma del error cuadrático. Uno de los retos de este método de entrenamiento es que tiende a recompensar el sobreajuste en los datos de entrenamiento, porque estamos calculando e intentando minimizar la SSE sólo en los datos de entrenamiento, a veces podemos acabar con un modelo que se ajusta muy estrechamente a los datos de entrenamiento, y entonces intentamos generar predicciones sobre nuevos datos con él, y encontramos que no generaliza particularmente bien a los nuevos datos.

[00:44] ¿Cómo construimos un modelo de regresión lineal de una manera que sea un poco más equilibrada entre ajustarse firmemente a los datos de entrenamiento, pero que también siga siendo lo suficientemente flexible como para generar predicciones precisas sobre nuevos datos, como podemos probar con el conjunto de prueba.

[01:01] Un método para hacer esto es añadir un factor de penalización en nuestra función de coste que penalice la complejidad. En este caso, siendo la complejidad en forma de características, el número de características que hemos incluido, y los valores de las ponderaciones para todas esas características.

[01:19] La función de coste para la regresión lineal normal que hemos descrito antes tiene este aspecto. La suma del error al cuadrado es igual a los valores reales de y menos el valor predicho de y al cuadrado, y sumado sobre todos los puntos de datos que tenemos. Cuando aplicamos la regularización, añadimos un término de penalización.

[01:43] Eso es una función de la suma de los coeficientes o pesos en nuestra ecuación de regresión lineal. Ahora, cuando tenemos más coeficientes o valores más altos de esos coeficientes, tiende a aumentar la función de coste. Pero de otra forma, a medida que reducimos el número de coeficientes o reducimos los pesos de nuestros coeficientes, nuestra función de coste tiende a disminuir.

[02:10] Minimizar esta nueva función de coste, incluyendo esta penalización de regularización, nos ayuda a encontrar el equilibrio óptimo entre el ajuste a nuestros datos de entrenamiento y la simplicidad de un modelo en términos de el número de características y los pesos de esas características.

[02:28] La función de coste con la regularización aplicada es ahora igual a la suma del cuadrado allí, y menos y al cuadrado y sumado sobre los puntos de datos, más la suma de un valor Lambda por nuestro factor de penalización. El valor Lambda es un valor fijo que establecemos y controla la fuerza de la penalización que queremos aplicar.

[02:52] A medida que aumentamos Lambda, podemos aplicar una penalización mayor y podemos disminuir Lambda para aplicar una penalización menor. Para el factor de penalización, hay dos opciones principales entre las que podemos elegir. Una se llama regresión lasso, la otra se llama regresión ridge.

[03:09] En la regresión lasso, calculamos el factor de penalización como la suma de el valor absoluto de los coeficientes multiplicado por nuestro valor Lambda. La regresión lasso tiene en realidad el efecto de forzar los coeficientes hasta cero, si las variables de esos coeficientes no son realmente relevantes para predecir la salida.

[03:33] Si tenemos un gran número de características en el modelo que estamos tratando de construir. Pero varias de esas características realmente no están añadiendo valor y nuestra capacidad para predecir la salida. Si aplicamos una regresión lasso con un factor de penalización suficiente, realmente fuerza esos coeficientes a cero y por lo tanto elimina esas características de la ecuación por completo.

[03:57] La regresión lasso también puede considerarse una forma de selección de características porque está generalmente reduciendo el número de características que están presentes en nuestra ecuación del modelo final. Por otro lado, la regresión ridge no tiene el efecto de forzar nuestros coeficientes hasta cero.

[04:18] En la regresión de cresta, nuestro término de penalización es la suma del peso al cuadrado de todos los pesos o coeficientes de nuestra ecuación. La regresión de cresta fuerza los coeficientes de los factores irrelevantes hacia cero, pero generalmente no todo el camino hacia cero.

[04:36] La regresión de cresta puede ser una estrategia de modelado eficaz para reducir el sobreajuste y mejorar ese equilibrio entre la simplicidad y el ajuste en los datos de entrenamiento. Pero no es un método de selección de características como lo es la regresión lasso, en el sentido de que en realidad no está eliminando características que son irrelevantes.

[04:56] Sólo está reduciendo los coeficientes de esas características a algo muy cercano a cero. La regularización puede ser una estrategia muy eficaz cuando trabajamos con modelos de regresión que a menudo pueden darnos un modelo mejor que un modelo de regresión lineal estándar por sí solo.

[05:15] Especialmente cuando estamos tratando con datos complejos con muchas características. En cuanto a la elección entre el lazo y la regresión de cresta, puede que tenga una razón para preferir uno u otro, o puede probar ambos y ver cuál hace un mejor trabajo prediciendo el resultado.

[05:32] Si desea un modelo sencillo con un número menor de características, eso es más interpretable. Lasso puede ser una estrategia eficaz porque está reduciendo el número de características al eliminar características de nuestro modelo que realmente no son particularmente valiosas para predecir la salida.

[05:49] Por otro lado, si sabemos de antemano que tenemos una relación muy compleja de el objetivo de salida con muchas de nuestras características de entrada, y tenemos lo que se llama colinealidad o correlación entre algunas de nuestras características de entrada, la regresión ridge puede ser una estrategia mejor.

[06:07] En caso de duda. Es aconsejable probar ambos enfoques y ver qué enfoque hace un mejor trabajo en el modelado.

