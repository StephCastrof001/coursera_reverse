---
title: "30-Logistic Regression"
type: lesson
module: "[[M04 - Linear Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 30-Logistic Regression

> **Módulo:** [[M04 - Linear Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 30-Logistic Regression
<!-- Módulo: 04-Linear Models | Archivo: 30-Logistic Regression.es.vtt -->

[00:03] En las dos últimas lecciones, hemos centrado nuestra discusión sobre los modelos lineales en tareas de regresión. Intentemos ahora abordar un problema de clasificación utilizando lo que hemos aprendido sobre los modelos lineales hasta ahora. Supongamos que ahora tenemos un problema sencillo en el que de nuevo tenemos una única variable de entrada llamada x y estamos intentando predecir una variable de salida y.

[00:27] Pero ahora, como se trata de una tarea de clasificación, nuestra salida es una clase. Hagámoslo sencillo y utilicemos una tarea binaria en la que nuestra salida sea un 0 o un 1. Podríamos aplicar de nuevo una regresión lineal para crear un modelo para hacer esto. Nuestra regresión lineal podría ser algo parecido a esto.

[00:51] De nuevo, adopta la forma y hat es igual a nuestro sesgo w_0 más r coeficiente w_1 multiplicado por nuestra única entrada x_1. Sin embargo, ahora tenemos un par de problemas. Uno es que, como podemos ver en el diagrama, el modelo de regresión lineal casi siempre predice el valor incorrecto.

[01:13] De nuevo, nuestros valores de salida son 0 ó 1, y en casi todos los casos que podemos ver, nuestra predicción no es ni 0 ni 1. ¿Cómo interpretamos estas predicciones que caen entre 0 y 1? Además, ¿qué pasa con los valores que nuestro modelo está prediciendo que son mayores que 1 o los valores que está prediciendo que son menores que 0.

[01:38] Una solución a algunos de estos problemas sería, en lugar de intentar predecir el valor real de y 0 o 1, ¿qué pasa si predecimos la probabilidad de que y sea igual a un 1? En este caso, aquellos valores que cayeron entre 0 y 1 ahora tienen sentido porque la probabilidad de que y sea igual a 1 está en algún lugar entre 0 y 1.

[02:04] Sin embargo, uno de los problemas que todavía tenemos, es qué hacer con aquellos valores que son mayores que 1 o menores que 0. Para resolver esto, apliquemos ahora una función que prediga las salidas que sólo caen dentro de ese rango de 0-1. Una opción aquí sería utilizar lo que se llama la función logística o la función sigmoidea.

[02:28] Tomemos simplemente una función sigmoidea es una función que predice valores que caen entre 0 en el lado inferior y 1 en el lado superior. Aplicando ahora esta función, podríamos generar predicciones que tienen sentido. Predecir la probabilidad de que y sea igual a 1, cayendo en algún lugar entre 0.

[02:47] Lo que significa que y es igual a 0 y 1 lo que significa que es 100 por cien seguro que y es igual a 1. Nuestra salida deseada del modelo es la probabilidad de que y sea igual a 1. De nuevo, hemos decidido utilizar la función sigmoidea para crear límites en las salidas de nuestro modelo de modo que caigan entre 0 y 1.

[03:12] Como entrada a esta función sigmoidea, proporcionamos las salidas de nuestro modelo de regresión lineal son sesgadas w_0 más nuestro coeficiente w_1 multiplicado por la característica de entrada x_1. En general, podemos crear un modelo que tome nuestras características de entrada X multiplicadas por los coeficientes y las combinamos en forma de regresión lineal, tomando cada característica multiplicada por su coeficiente respectivo.

[03:42] Podemos llamar a este valor z, y luego introducimos este valor z en la función sigmoidea. Al salir de la sigmoidea, tenemos un valor que cae entre 0 y 1, que luego interpretamos como la probabilidad de que y sea igual a 1. Nuestro reto ahora es encontrar los valores óptimos para los coeficientes de nuestro modelo lineal.

[04:08] Podemos abordar esto de forma similar a lo que hicimos en la regresión lineal. Primero definimos nuestra función de coste. A continuación, tratamos de encontrar los valores óptimos de los pesos o coeficientes que minimicen la función de coste. De nuevo, la forma en que podemos hacer esto es muy similar a lo que hicimos en la regresión lineal.

[04:30] Si tenemos una función que queremos minimizar, como nuestra función de coste. Para minimizar esa función, calculamos la derivada de la función, que también se llama gradiente de una función, y fijamos la derivada igual a 0. Entonces podemos resolver los valores de los coeficientes que hacen que esta ecuación sea cierta.

[04:51] En la regresión lineal, había una solución simple de forma cerrada para esto de modo que podemos calcular fácilmente los valores de nuestros coeficientes. En la regresión logística, donde hemos introducido ahora la función sigmoidea, ya no tenemos una solución simple de forma cerrada.

[05:08] Recurrimos a un método de resolución iterativo que llamamos descenso de gradiente para resolver los valores de nuestros coeficientes que minimizan la función de coste. ¿Cómo funciona el descenso de gradiente? Supongamos que queremos minimizar una función y es igual a x al cuadrado.

[05:27] Empezamos en algún punto de la curva, y es igual a x al cuadrado, y podemos movernos iterativamente hacia el mínimo y detenernos una vez que hayamos alcanzado nuestro mínimo. ¿Cómo sabemos dónde movernos? Bueno, la primera pregunta es, ¿en qué dirección debemos movernos? La respuesta a eso es que nos movemos en la dirección opuesta al valor de la derivada o el gradiente.

[05:51] Si pensamos en el cálculo, el gradiente de una función apunta en la dirección de ascenso más pronunciado de esa función. Si estamos intentando encontrar el mínimo de una función, queremos movernos en dirección opuesta a esa dirección de ascenso más pronunciado o a la dirección de descenso más pronunciado.

[06:09] Nos movemos en esa dirección opuesta al valor de el gradiente en ese punto de partida que hemos seleccionado. La segunda pregunta es, ¿hasta dónde debemos movernos en esa dirección? La respuesta a eso es que nos movemos en alguna pequeña cantidad, que es igual a un parámetro llamado tasa de aprendizaje, multiplicado por el valor del gradiente en ese punto.

[06:33] La tasa de aprendizaje es un parámetro importante en el descenso de gradiente y también es críticamente importante en las redes neuronales. Hablaremos mucho más de las tasas de aprendizaje una vez que entremos en la lección sobre redes neuronales. Pero por ahora, la respuesta a nuestra pregunta de cómo minimizar esa función es que elegimos algún punto de partida aleatorio en la curva.

[06:54] Calculamos el gradiente. Luego nos movemos en esa dirección opuesta al gradiente, y la cantidad que nos movemos en esa dirección es igual a la tasa de aprendizaje multiplicada por el valor del gradiente en ese punto. Entonces podemos hacer todo esto de nuevo y movernos un paso más en la dirección opuesta al gradiente y continuamos moviéndonos hasta que hayamos alcanzado el punto estable donde ya no nos movemos más.

[07:21] Una vez que alcanzamos el punto estable, sabemos que hemos alcanzado el valor mínimo para una función. ¿Cómo aplicamos el descenso de gradiente en el contexto de la estimación de los pesos o coeficientes óptimos para nuestro modelo de regresión logística? De nuevo, primero definimos nuestra función de coste para la regresión logística.

[07:43] A continuación, tratamos de encontrar los valores de las ponderaciones o coeficientes que minimicen esta función de coste. Para ello, aplicamos el descenso de gradiente. Primero elegimos un conjunto aleatorio de ponderaciones. Calculamos la función de coste utilizando ese conjunto aleatorio de ponderaciones y los datos de entrenamiento de los que disponemos.

[08:02] A continuación, calculamos el gradiente de esa función de coste y utilizamos nuestra regla de descenso de gradiente para actualizar iterativamente los pesos basándonos en el descenso de gradiente. Calculamos un nuevo conjunto de pesos que sea igual a los pesos anteriores que habíamos utilizado, menos la tasa de aprendizaje multiplicada por la magnitud del gradiente.

[08:26] Entonces podemos repetir esto cada vez moviendo un pequeño paso en la dirección de nuestro coste mínimo hasta que hayamos alcanzado un mínimo o después de un cierto número de movimientos, podemos terminar la función.

