---
title: "28-Linear Regression"
type: lesson
module: "[[M04 - Linear Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 28-Linear Regression

> **Módulo:** [[M04 - Linear Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 28-Linear Regression
<!-- Módulo: 04-Linear Models | Archivo: 28-Linear Regression.es.vtt -->

[00:04] Comenzaremos la discusión de modelos lineales con la regresión lineal simple. Muchos de ustedes probablemente estén familiarizados con la regresión lineal. Aparece en casi todos los campos imaginables, desde la economía hasta muchas ramas de las ciencias. Un modelo de regresión lineal supone una relación lineal entre la entrada y la salida.

[00:29] Las entradas son las características de los datos que hemos definido y la salida es el objetivo que intentamos predecir. Esta relación se define mediante un conjunto de coeficientes que son multiplicadores de cada una de las características de entrada. Si la regresión lineal es tan sencilla y común, ¿por qué dedicamos tiempo a hablar de ella?

[00:51] En realidad, hay un par de respuestas a esa pregunta. La primera es que, aunque es sencilla, la regresión lineal constituye la base de muchos de los modelos de aprendizaje automático más complejos que utilizamos. En particular, las redes neuronales, de las que hablaremos en una lección posterior, realmente se fundamentan en la base de la regresión lineal simple.

[01:12] Las regresiones también pueden ser modelos sorprendentemente eficaces en determinadas situaciones si se utilizan adecuadamente. También son un primer modelo estupendo para aplicarlo para obtener un punto de referencia o una idea del rendimiento esperado que podría esperar alcanzar en una tarea concreta de aprendizaje automático.

[01:30] Por cierto, siempre recomiendo que cuando esté trabajando en una tarea de modelado, empiece con un modelo sencillo como una regresión lineal. Aplique eso como primer paso y vea qué rendimiento le da. Luego, una vez que pase a algoritmos más complejos, puede compararlos con su punto de referencia original y ver si realmente está haciendo una mejora o no.

[01:53] Por último, una de las cosas realmente buenas de la regresión lineal es que es altamente interpretable y nos resulta muy fácil entender las relaciones entre las entradas y las salidas en el modelo que estamos construyendo. ¿Cómo funciona un modelo de regresión lineal simple? Tomemos el ejemplo en el que estábamos trabajando antes de predecir los precios de venta de las viviendas.

[02:22] Si estuviéramos construyendo una regresión lineal simple que involucrara una sola variable, que es el número de dormitorios, podríamos proporcionar esa variable, los dormitorios en un modelo y como salida de nuestro modelo, estaríamos prediciendo el precio de venta de la vivienda.

[02:41] Nuestro modelo podría ser algo como esto. y=W_0 + W_1X. W_0 es lo que llamamos el término de sesgo. O puede pensar en esto como la intersección y. Si todas las características, o en este caso la única característica que tenemos fuera cero, cuál sería el valor y. Llamamos a esto de nuevo el sesgo.

[03:05] W_1 sería el coeficiente, o a veces también llamado el peso de la variable x, que representa el número de dormitorios de nuestra casa. Este sería el multiplicador de esa característica para calcular el valor total de nuestro precio de venta objetivo. Pasemos ahora del modelo de regresión lineal simple al modelo de regresión lineal múltiple.

[03:30] En este caso, tenemos más de una característica. De hecho, tenemos tantas características como queramos incluir en nuestro modelo. Podríamos añadir características adicionales en este caso, como los metros cuadrados de nuestra casa, el distrito escolar o el barrio en el que se encuentra nuestra casa.

[03:45] De nuevo, representamos esto con una ecuación que contiene ese término de sesgo W_0. Pero ahora tenemos múltiples coeficientes, uno para cada una de nuestras características de entrada. Podemos tener un coeficiente W_1, que representa el peso del número de dormitorios en el cálculo del precio de venta objetivo final.

[04:05] W_2 podría ser el coeficiente de los metros cuadrados de nuestra vivienda. W_3 podría representar el coeficiente de el distrito escolar en el que nos encontramos, y así sucesivamente. Sumamos todo esto. Los coeficientes son pesos multiplicados por los valores de las características para calcular nuestro valor y o nuestro precio de venta objetivo.

[04:29] Cuando entrenamos un modelo de regresión lineal, realmente lo que estamos haciendo es aprender los valores óptimos de estos coeficientes o ponderaciones que pueden modelar eficazmente la relación entre las características de entrada y el objetivo de salida. El primer paso para identificar los valores óptimos de esos coeficientes o ponderaciones, es calcular el error total del modelo.

[04:55] A continuación, alteraremos los coeficientes de forma que, con suerte, reduzcamos ese error total hasta el punto en el que ahora hayamos minimizado nuestro error total. ¿Cómo calculamos el error total de nuestro modelo? Bien, el error para cualquier punto dado, en este caso, cualquier casa en venta dada, es el precio real al que, esa casa se vendió menos el precio de venta predicho.

[05:20] O en notación matemática, lo llamamos y menos nuestra predicción, a la que llamamos y-hat. Alternativamente, por conveniencia computacional, a menudo definimos el error en términos de lo que llamamos Suma de Errores Cuadrados o SSE. La suma de errores al cuadrado, SSE, se calcula como la suma de todas las predicciones menos los reales al cuadrado o y-hat menos y al cuadrado y se suma sobre todos los puntos de datos que tenemos.

[05:54] Cuando construimos nuestro modelo, lo que realmente estamos tratando de hacer es buscar los coeficientes que puedan minimizar ese valor total de la Suma del Error Cuadrado. SSE, en terminología de modelado se llama nuestra función de coste, o también llamada función de pérdida. En este caso, nuestra función de coste, o SSE es la suma de la y menos y al cuadrado para cada punto de datos.

[06:20] De nuevo, cuando estamos entrenando nuestro modelo de regresión lineal, buscamos encontrar los valores para aquellos coeficientes o ponderaciones que minimicen el total de nuestra función de coste. Para ello, utilizamos los datos de entrenamiento, las entradas x y las salidas y de que disponemos y resolvemos para los pesos o coeficientes que den como resultado el mínimo de la función de coste.

[06:44] En el caso de la regresión lineal, normalmente podemos hacer esto utilizando una solución de forma cerrada. En otros tipos de modelos, aplicamos la misma estrategia, pero a menudo no existe una solución de forma cerrada, así que utilizamos algunos métodos más complejos para calcular los valores que dan como resultado el mínimo de la función de coste.

[07:06] Mucha gente pensará que la regresión lineal sólo funciona cuando hay una relación lineal entre las entradas y las salidas. En realidad, también se pueden modelizar relaciones no lineales entre entradas y salidas. Para ello, lo que hacemos es transformar una característica de entrada mediante alguna función de transformación no lineal y crear una nueva característica que luego utilizaremos como entrada a un modelo.

[07:34] Por ejemplo, podemos tomar una característica de entrada x a cierta potencia x al cuadrado o x al cubo, por ejemplo. O podemos tomar el logaritmo de x y crearemos eso como una nueva característica de entrada. Lo introduciremos en nuestro modelo y ahora podremos capturar mejor algunas de esas no linealidades de la relación entre las entradas y nuestras salidas.

[07:58] Cuando hacemos esto, se denomina regresión polinómica. En realidad hay un número ilimitado de transformaciones que podemos aplicar. Veamos un ejemplo de cuando esto resulta útil. En este caso, nuestro objetivo de nuestra tarea de modelado es predecir la eficiencia del combustible de los coches dados los caballos de potencia del motor.

[08:19] Puede ver aquí en esta diapositiva que he ajustado una regresión lineal simple a los caballos de potencia. Parece que hace un trabajo aceptable a la hora de capturar la variabilidad en el patrón que vemos en la salida de millas por galón. Pero ciertamente hay margen de mejora. En esta pantalla he mostrado, el Error Cuadrático Medio, como podemos ver para el conjunto de entrenamiento y el conjunto de prueba.

[08:44] Ahora echemos un vistazo a lo que ocurre cuando utilizamos una transformación no lineal y aplicamos una regresión polinómica a la misma tarea. En este caso, he tomado caballos de potencia al cubo y lo he utilizado como entrada para mi modelo. Ahora estoy prediciendo las millas por galón basado en una sola entrada caballos de fuerza al cubo.

[09:08] Como podemos ver, nuestro modelo está haciendo un trabajo mucho mejor al capturar esa relación no lineal entre caballos de fuerza y millas por galón y como resultado, el Error Cuadrático Medio en tanto nuestro conjunto de entrenamiento como nuestro conjunto de prueba ha mejorado significativamente.

