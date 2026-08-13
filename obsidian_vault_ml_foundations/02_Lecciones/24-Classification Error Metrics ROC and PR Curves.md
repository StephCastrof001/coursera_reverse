---
title: "24-Classification Error Metrics ROC and PR Curves"
type: lesson
module: "[[M03 - Evaluating and Interpreting Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 24-Classification Error Metrics ROC and PR Curves

> **Módulo:** [[M03 - Evaluating and Interpreting Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 24-Classification Error Metrics ROC and PR Curves
<!-- Módulo: 03-Evaluating & Interpreting Models | Archivo: 24-Classification Error Metrics ROC and PR Curves.es.vtt -->

[00:04] Una de las formas habituales de evaluar los modelos de clasificación es utilizando lo que se denomina curvas ROC o curvas características operativas del receptor. La curva ROC traza la tasa de verdaderos positivos frente a la tasa de falsos positivos para una variedad de valores umbral diferentes.

[00:21] Entonces, ¿cuál es el valor umbral? La mayoría de los modelos de clasificación nos devuelven más que una predicción discreta, un uno o un cero. Nos proporcionan la probabilidad de predicción de cada clase. Así que la probabilidad de que un determinado punto de datos sea un uno positivo o cero negativo.

[00:41] Para convertir estas probabilidades en predicciones discretas de un cero o un uno, por ejemplo, tenemos que establecer algún umbral. Y decimos que si nuestra probabilidad es mayor que el umbral, generamos la predicción de esa clase. Así, por ejemplo, el umbral por defecto suele establecerse en 0,5.

[01:02] Si generamos una predicción que resulta ser 0,7 que es mayor que nuestro umbral de 0,5 predeciremos un uno la clase positiva. Y si generamos una probabilidad de 0,3 menor que nuestro umbral de 0,5, nuestra predicción es cero o la clase negativa. Así que convierten estas salidas del modelo probabilístico en salidas discretas.

[01:27] Comenzamos estableciendo un umbral. Un ejemplo en la diapositiva comencemos con el valor umbral de 0,3. Para nuestro primer punto de datos, las salidas de nuestro modelo 0,85 claramente superiores a nuestro umbral a .3, por lo que generamos un uno como nuestra predicción. La salida de nuestro segundo modelo es inferior al .3, por lo que generamos un cero, luego un uno, otro uno y finalmente otro uno más.

[01:54] A continuación, tomamos estas predicciones calculamos la tasa de verdaderos positivos y la tasa de falsos positivos comparando nuestras predicciones con los objetivos reales. A continuación, cambiamos nuestro umbral a 0.5 volvemos a calcular las predicciones comparando las salidas del modelo con nuestro nuevo valor umbral de 0,5, calculamos la TPR FPR y repetimos.

[02:18] Una vez que hayamos hecho esto varias veces, podemos trazar estos puntos en un gráfico de TPR frente a FPR y conectar los puntos para formar una curva. Esta curva se denomina entonces Curva ROC. Una métrica de error común para los modelos de clasificación asociada a la Curva ROC es lo que se denomina AUROC o Área bajo la curva ROC.

[02:42] Como su nombre indica, la forma en que calculamos nuestra ROC es simplemente tomando el área bajo la Curva ROC que hemos trazado. En el caso de un modelo de clasificación perfecto. No importa qué valor de umbral seleccionemos, siempre vamos a tener una tasa de verdaderos positivos de uno y una tasa de falsos positivos de cero.

[03:00] Así que el punto del clasificador perfecto en la Curva AUROC estaría en un valor de TPR de uno y FPR de cero. Si calculamos el área bajo esa Curva sería simplemente uno. Por otro lado, si tomáramos un modelo que simplemente adivinara al azar entre cero o uno, esperaríamos que para cada valor umbral nuestra tasa de verdaderos positivos fuera igual a nuestra tasa de falsos positivos.

[03:27] Y cuando trazamos esa Curva sobre la Curva ROC veríamos una línea recta que iría de 00- 11. Cuando calculamos el área bajo esa línea recta sería igual a aproximadamente 0,5. Por lo tanto, para los modelos del mundo real que generamos, esperaríamos que el área bajo la Curva ROC se situara entre 0,5, adivinando aleatoriamente entre cero y uno y en el límite superior sería uno indicando un modelo perfecto.

[03:56] Valores AUROC más altos indican generalmente modelos de mejor calidad. Otra técnica de evaluación que podemos utilizar, es lo que se denomina Curva de Precisión-Recuperación o Curva PR. Una Curva PR es un gráfico de la precisión frente al valor de recuperación, para un modelo a medida que cambiamos el valor umbral.

[04:18] Las curvas puras son especialmente útiles en relación con las Curvas ROC. Cuando tenemos situaciones con un alto desequilibrio de clases. Por ejemplo, tenemos muchos ceros y sólo unos pocos unos. Si pensamos en la situación de la que hablamos antes, cuando creamos un modelo para predecir pacientes con enfermedades cardiacas, ese fue un caso claro de un alto desequilibrio de clases.

[04:38] Un número muy, muy elevado de pacientes sin cardiopatía en relación con el escaso número de pacientes con nuestras curvas de precisión de enfermedad-recuperación, a diferencia de las curvas ROC no tienen en cuenta los verdaderos negativos. Por lo tanto, para situaciones como la del modelo que comentamos, no están sesgadas por el hecho de que nuestro modelo fuera capaz de predecir con éxito que muchos pacientes no padecen una enfermedad cardiaca.

[05:01] Así que cuando tengamos una situación clara de desequilibrio de clases, a menudo optaremos por utilizar una Curva de Precisión-Recuperación en lugar de la Curva ROC para evaluar nuestro modelo.

