---
title: "15-Bias-Variance Tradeoff"
type: lesson
module: "[[M02 - The Modeling Process]]"
tags: [lesson, ml-foundations]
---

# 🎓 15-Bias-Variance Tradeoff

> **Módulo:** [[M02 - The Modeling Process]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 15-Bias-Variance Tradeoff
<!-- Módulo: 02-The Modeling Process | Archivo: 15-Bias-Variance Tradeoff.es.vtt -->

[00:03] Una de las cosas que hace que el modelado con aprendizaje automático sea un desafío es encontrar el título correcto de complejidad para un modelo que está creando para un problema dado. La complejidad de un modelo es el resultado de tres fuentes primarias. Uno es el número de características que decida incluir en su modelo.

[00:22] Obviamente, cuanto más características que incluyas, más complejas el modelo se convierte en. La segunda fuente de complejidad está en el algoritmo o en la plantilla que estás utilizando para el formulario modelo que estás creando. Son algoritmos como la regresión lineal que son mucho más simples, y algoritmos como como redes neuronales que son mucho más complejas.

[00:43] La tercera fuente de complejidad en la modelización proviene de los valores de lo que llamamos hiperparámetros, que son, de nuevo, esas perillas que afinas y que son específicas de tu elección del algoritmo que seleccionaste para tu problema. Juntas, estas tres cosas resultan en una cierta cantidad de complejidad del modelo, que luego podemos variar y hacerlo más simple o más complejo mediante nuestra selección de estas tres cosas: número de características, selección del algoritmo y selección de valores para nuestros hiperparámetros.

[01:13] La complejidad de un el modelo que cree tiene un impacto directo en el error de ese modelo. El modelo promedio puede dividirse en dos términos principales; sesgo y varianza. El sesgo se refiere al error que se introduce modelando un problema complejo de la vida real utilizando un modelo más simple, donde ese modelo simple no puede capturar completamente el subyacente patrones dentro de sus datos.

[01:40] Los modelos con un sesgo alto serían modelos simples que son consistentemente se desvían un poco del objetivo al generar sus predicciones porque simplemente no son capaces de capturarlos por completo patrones dentro de los datos. La varianza se refiere a la sensibilidad de un modelo a lo pequeño fluctuaciones en los datos.

[01:58] Modelos con alta varianza se ajustan muy bien a los datos de entrenamiento y como como resultado de ese ajuste tan ajustado, han interpretado el ruido en los datos de entrenamiento como patrones reales y han intentado modelar esos patrones, que en realidad son solo ruido. Como resultado, cuando los modelos con alta varianza reciben nuevos conjuntos de datos para al generar predicciones, las predicciones pueden ser un tanto dispersas con una varianza alta.

[02:25] Hay un natural compensación entre el sesgo y el varianza de un modelo. Modelos que son los más simples suelen tener un sesgo más alto porque son incapaces de capturar completamente lo real patrones subyacentes en sus datos y también tienen una varianza baja. Por otro lado, los modelos más complejos no tienen un sesgo mucho más bajo, son mucho mejores para capturar esos patrones subyacentes, pero a menudo tienen mayor varianza o el efecto de dispersión al ajustarse muy estrechamente a los datos de entrenamiento.

[02:56] El error total de un modelo es la suma del sesgo y los distintos términos. En términos técnicos, decimos que el error total es igual al sesgo cuadrático más la varianza, más un error adicional término que se refiere al error inherente en cualquier conjunto de datos o el ruido aleatorio que es inherente a cualquier problema particular que estás intentando modelar.

[03:19] En la práctica, a menudo usamos los términos inadecuación y sobreadaptación se refieren a situaciones en las que hemos creado modelos que son demasiado simples o demasiado complejos para el problema en el que nos encontramos intentando modelar. El subajuste se refiere al situación en la que hemos elegido un modelo muy simple y como resultado, tenemos un modelo que tiene un sesgo muy alto y una varianza baja, pero juntos, el sesgo y la varianza equivalen a un error que superior al óptimo.

[03:45] En underfit, nuestro el modelo es demasiado simple y es incapaz de captar realmente las causas subyacentes patrones en nuestros datos. El sobreajuste es el problema opuesto, donde hemos seleccionado o desarrolló un modelo que es demasiado complejo para los datos y el problema que estamos intentando modelar.

[04:02] En sobreajuste, tenemos un sesgo bajo, pero tenemos un sesgo muy alto varianza y, como resultado, nuestro error total, la suma del sesgo y la varianza es superior a nuestro valor óptimo. La complejidad óptima del modelo se produce cuando se suman el sesgo y la varianza está en un punto mínimo.

[04:20] Para mostrarles un ejemplo de lo que es sobreajustar y consideremos este ejemplo: un ajuste insuficiente. Nuestra verdadera función en estos gráficos está representada por la curva naranja. Nuestra función modelo es representada por la línea azul. Lo podemos ver en el gráfico en el lado izquierdo, hemos modelado esta función con una regresión lineal simple y nuestro modelo, de hecho, es demasiado simple para capturarlo realmente ese patrón subyacente en nuestros datos y este sería un caso claro de falta de adaptación.

[04:51] En el diagrama central, hemos hecho un bonito buen trabajo al hacer coincidir nuestro modelo con el verdadero función subyacente en nuestros datos, por lo que nuestro modelo se ajusta bastante bien aún tiene algún grado de error, que se refiere a eso error o ruido inherente que se encuentra en cada conjunto de datos.

[05:08] La imagen de la derecha es una buena representación de más de se ajusta al lugar donde hemos elegido el modelo función que se ha ajustado muy bien al datos y, como resultado, tiene una forma muy compleja. Esto puede funcionar en nuestros datos de entrenamiento, pero cuando presentamos esto función que hemos creado con datos nuevos para generar predicciones sobre, nuestro modelo termina haciendo un trabajo bastante malo para generar predicciones precisas, porque se ha adaptado al ruido en el que se encuentra el conjunto de datos de entrenamiento y ese mismo ruido pueden no estar presente en los nuevos datos que presentamos para generar predicciones.

