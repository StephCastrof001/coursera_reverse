---
title: "22-Regression Error Metrics"
type: lesson
module: "[[M03 - Evaluating and Interpreting Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 22-Regression Error Metrics

> **Módulo:** [[M03 - Evaluating and Interpreting Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 22-Regression Error Metrics
<!-- Módulo: 03-Evaluating & Interpreting Models | Archivo: 22-Regression Error Metrics.es.vtt -->

[00:04] Comencemos la discusión de las métricas de salida hablando de las métricas de regresión . Para los problemas de modelado de regresión, normalmente utilizaremos una de las tres métricas comunes, error cuadrático medio medio, error absoluto medio o error porcentual absoluto medio. Empecemos por el más popular, que se llama error cuadrático medio.

[00:25] Cuando calculamos el error cuadrático medio es sumando las diferencias entre el valor objetivo real y un valor predicho elevado al cuadrado y dividiéndolo después por el número de observaciones que tenemos. Uno de los retos del error cuadrático medio es que está muy influido por los valores atípicos.

[00:44] Cuando tenemos un caso particular de un gran error debido al término cuadrático en la fórmula, tenemos una fuerte penalización que se aplica y como resultado, obtenemos un MSC muy alto. El error cuadrático medio también está influido por la escala de nuestros datos. Por lo tanto, es imposible comparar un error cuadrático medio en un problema con un error cuadrático medio en otro problema porque estamos trabajando con conjuntos de datos completamente diferentes utilizando escalas diferentes.

[01:14] A veces utilizaremos lo que se llama nuestro MSC, o error cuadrático medio, en lugar de error cuadrático medio. Nuestro MSC es simplemente la raíz cuadrada del error cuadrático medio. Una segunda métrica común de los resultados de la regresión es el error medio absoluto. En el MAE, nuestro error medio absoluto, estamos sumando el valor absoluto de la diferencia entre el objetivo y la predicción en todas las predicciones que realizamos y dividiéndolo por el número total de predicciones.

[01:49] El MAE también está influido por la escala del problema es por tanto imposible comparar un valor MAE en un problema con otro problema. Sin embargo, en comparación con el error cuadrático medio, el MAE es más robusto a los valores atípicos o errores muy grandes, tiende a penalizar los errores grandes, mucho menos que el MSC porque no contiene ese término cuadrático en la fórmula.

[02:14] El MAE también puede ser un poco más fácil de interpretar en el contexto de un problema porque no tenemos ese término cuadrático en la fórmula. Y por lo tanto, el MAE tiende a estar en una escala similar al valor que estaban tratando de predecir. Así que es un poco más lógico para nosotros entender cuando vemos un valor MAE relativo a un valor MSC en el contexto de las predicciones que estamos tratando de hacer.

[02:39] También utilizamos a veces error porcentual absoluto medio en lugar de error absoluto medio. Error porcentual absoluto medio, o MAPE, se calcula como el valor absoluto de la diferencia entre el valor real y las predicciones regenerando dividido por los valores reales. Sumamos eso y lo dividimos por el número total de producciones para obtener nuestro valor MAPE.

[03:06] MAPE convierte el error en un porcentaje en lugar de un número absoluto. MAPE suele ser muy popular, particularmente entre audiencias no técnicas. Debido a que es fácil de entender, es una métrica común que se utiliza para presentar a los clientes, de nuevo, porque es fácil de entender e interpretar.

[03:27] Uno de los retos del MAPE es que está sesgado por errores porcentuales altos para valores bajos de y. Así que consideremos un caso en el que tenemos un valor muy bajo de un objetivo, podemos tener un error muy pequeño, pero relativo al valor bajo de un objetivo. Cuando convertimos esa pequeña área en un porcentaje, acaba siendo un porcentaje muy alto.

[03:50] Así que para entender la diferencia entre error medio absoluto y error cuadrático medio, veamos un ejemplo. A un lado, tenemos dos situaciones. En cada situación, tenemos cinco puntos de datos de salida de un modelo que hemos construido. En el caso uno, tenemos una pequeña varianza y errores para cada uno de esos cinco puntos.

[04:13] Los valores de error son una unidad o dos unidades para cada uno de los cinco puntos. En el caso dos, tenemos cuatro puntos en los que hemos hecho una predicción perfecta y tenemos un error cero en nuestra predicción. Y para el quinto punto, tenemos un gran error de siete unidades.

[04:31] En cada caso, el error total en los cinco puntos es igual a siete. Pero en el primer caso, si calculamos nuestro error absoluto medio, obtenemos 1.4. Del mismo modo, para el caso dos, podemos calcular el MAE y también llegamos a 1,4. Sin embargo, cuando calculamos el error cuadrático medio, para el caso uno, resulta ser 2,2, y para el caso dos, resulta ser 9,8.

[05:01] ¿Por qué? Porque el error cuadrático medio penaliza severamente los errores graves o los valores de error grandes, incluso si se trata de un único error. En el caso dos, tuvimos un único error grande de siete unidades. Y debido al término cuadrado en la fórmula para el error cuadrático medio, penaliza severamente ese único valor de error.

[05:25] A veces esto puede ser algo bueno y a veces no. En algunos problemas que estamos tratando de modelar, estar fuera por una gran cantidad, o tener un error muy grande, una sola vez puede ser algo realmente malo. En otros casos, realmente no nos importa mucho si estamos fuera una vez o dos veces por grandes valores de error.

[05:47] Pero lo que es realmente malo es si nos equivocamos sistemáticamente por valores pequeños. Si realmente nos preocupamos por minimizar las posibilidades de que se produzcan errores atípicos grandes y graves, el error medio al cuadrado puede ser una métrica mejor para ayudarnos a hacernos una idea realista de ello.

[06:05] Si nos preocupamos más por saber si acertamos o fallamos sistemáticamente por pequeñas cantidades cada vez que hacemos una predicción, es posible que queramos fijarnos en el error medio absoluto. Así que entremos ahora en esta terminología que se utiliza para calcular r al cuadrado.

[06:20] La desviación total de la media, a la que nos referimos como suma total cuadrada, o SST, es igual a la suma de los valores y reales menos el valor y medio al cuadrado. La SST es el resultado de la suma de dos términos, la suma de regresión al cuadrado, o SSR, y el error total al cuadrado, o SSE.

[06:45] La suma de regresión al cuadrado, o SSR, se calcula como la diferencia entre los valores y predichos y el valor y medio. O dicho de otro modo, la cantidad de la varianza que explica nuestro modelo. El error total al cuadrado, o SSE, es la suma de los valores y reales menos los valores y predichos, o la varianza no explicada, o el error en nuestro modelo.

[07:10] Nuestro cuadrado entonces es igual a la suma de la regresión al cuadrado sobre la suma al cuadrado total, o la cantidad de variabilidad explicada por nuestro modelo, dividida por la variabilidad total en nuestros valores y. O dicho de otro modo, nuestro cuadrado puede calcularse como uno menos la suma del error al cuadrado, dividido por la suma del total al cuadrado.

[07:31] El valor r al cuadrado de un modelo suele estar entre cero y uno, donde en r al cuadrado de uno indicaría un modelo perfecto que es capaz de explicar completamente todas las variantes encontradas en los valores y o los valores objetivo. R al cuadrado de cero significaría que el modelo no está explicando ninguna de las variantes encontradas en nuestros valores y o los valores objetivo.

