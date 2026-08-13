---
title: "14-Algorithm Selection"
type: lesson
module: "[[M02 - The Modeling Process]]"
tags: [lesson, ml-foundations]
---

# 🎓 14-Algorithm Selection

> **Módulo:** [[M02 - The Modeling Process]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 14-Algorithm Selection
<!-- Módulo: 02-The Modeling Process | Archivo: 14-Algorithm Selection.es.vtt -->

[00:00] Hablemos ahora un poco sobre la selección de algoritmos. Entonces, el algoritmo de aprendizaje automático, se puede considerar como una plantilla que define la relación entre la entrada y la salida de un modelo. Hay muchos tipos de algoritmos centrados en diferentes tareas, como la regresión o la clasificación.

[00:25] Los algoritmos también se pueden clasificar en dos tipos principales, algoritmos paramétricos y algoritmos no paramétricos. Se pueden definir algoritmos paramétricos mediante ecuaciones matemáticas que relacionan la entrada y la salida. Por lo tanto, la regresión lineal, que muchos de ustedes sabrán, es común ejemplo de una relación paramétrica.

[00:47] Y luego algoritmos paramétricos, nuestro objetivo es definir los coeficientes de esa ecuación o el conjunto de ecuaciones, que rige la relación entre la entrada y la salida. Algoritmos no paramétricos, por otro Por otro lado, no tienen una sola ecuación o conjunto de ecuaciones que definir la relación.

[01:09] Un ejemplo común de un sistema no paramétrico un algoritmo sería un árbol de decisiones. Del que hablaremos en un módulo posterior. Una cosa importante a tener en cuenta con la selección de algoritmos, es lo que se llama el no teorema del almuerzo gratis. Y este teorema dice que hay no hay un algoritmo único que funcione de manera óptima en todos los ámbitos posibles tareas de aprendizaje automático en las que podrías estar trabajando.

[01:34] La elección del algoritmo que sea óptimo, depende realmente de la tarea particular en la que estés trabajando, el problema que intentas resolver y el conjunto particular de datos que que tienes disponible para usar. Y entonces, el enfoque típico la selección de algoritmos consiste en probar varios algoritmos y entrene modelos utilizando varios algoritmos y compárelos, y vea qué algoritmo nos da el mejor resultado en términos de rendimiento.

[02:06] Cuando seleccionamos el algoritmo, bueno Por lo general, consideramos tres criterios principales. El más obvio, es el rendimiento del modelo o la precisión del modelo. Y poder generar predicciones de la producción. Pero quizás las menos obvias son, capacidad de interpretación y eficiencia computacional.

[02:27] Por lo tanto, la interpretabilidad se refiere a qué tan fácil o es difícil entender qué está haciendo realmente el modelo cuando está generando las predicciones. Y cómo llega a ciertas predicciones. Entonces, algunos algoritmos, como un lineal regresión, por ejemplo, o árbol de decisiones.

[02:46] nos dan un alto nivel de capacidad de interpretación, lo que significa que es muy fácil observar el rendimiento del modelo y por qué genera ciertas predicciones. Así que, si tenemos que explicar la predicción a un cliente o usuario de nuestro producto. Para nosotros es muy fácil de entender cómo llegamos a esa predicción y, a su vez, poder explicársela a alguien.

[03:11] Otros algoritmos, como las redes neuronales, utilizan conjuntos muy grandes de ecuaciones complejas para generar predicciones de salida. Y puede resultar muy difícil entender cómo el modelo de red neuronal está alcanzando la predicción. Y así, si tuviéramos que explicárselo a un cliente o usuario, sería un gran desafío para nosotros para hacerlo.

[03:34] El tercer criterio que queremos considerar, es la eficiencia computacional. Modelos más simples, como las regresiones lineales, por lo general son muy eficientes, pueden correr muy rápido, pueden entrenar y generar predicciones muy rápidamente con baja potencia computacional. Otros algoritmos, como otra vez, sus propias redes pueden requerir un alto grado de potencia computacional para entrenarse, y también para su uso en la generación de predicciones.

[04:02] Podrían llevar muchas horas, días o incluso semanas para entrenar. Y requieren un montón de potencia computacional para hacerlo. Así que, cuando estamos haciendo nuestro decisión sobre los algoritmos. Queremos asegurarnos de no solo considerar el rendimiento de la precisión, sino realmente tener en cuenta el equilibrio de estos tres factores.

[04:21] Y para el problema en particular en el que estamos trabajando o el producto que estamos creando. ¿Cuál de estos factores ¿es el más importante para nosotros? Un ejemplo que me gustaría compartir aquí, de considerar estos tres factores en el equilibrio adecuado, es un ejemplo de Netflix.

[04:40] Así que, a principios de la década de 2000, Netflix funcionó un concurso llamado Premio Netflix. Y el objetivo de ese concurso era para que un equipo pueda desarrollar un modelo, que sea altamente eficaz en predecir las calificaciones que un usuario le daría a ciertos películas que vieron.

[04:59] Para crear este modelo, Netflix creó disponible un gran conjunto de datos históricos de sus usuarios que habían visto películas y las calificaciones que le habían dado cada una de las películas que habían visto. Y para ganar el premio de Netflix, un equipo tenía que ser capaz de mejorar el algoritmo interno de Netflix, en al menos un 10% en términos de generación de predicciones precisas de las valoraciones de los usuarios sobre las películas.

[05:26] Así que, después de la competencia por varios años, un equipo finalmente pudo lograrlo Umbral de mejora del rendimiento del 10%. Y fueron declarados ganadores del premio Netflix. Como compañero de equipo, la información sobre su modelo está disponible públicamente. Rápidamente aprendimos que el modelo en realidad era un conjunto complejo o una colección de varios modelos.

[05:51] Cada uno de esos modelos utiliza diferentes algoritmos como plantilla para ellos. Como los ingenieros de Netflix después la competencia evaluó la posibilidad de utilizar el modelo de equipos ganadores en lugar de sus propios algoritmos. Rápidamente se dieron cuenta de que la idea de implementar este complejo modelo utilizando su propio modelo muy grande conjuntos de datos de entrenamiento internos.

[06:14] En realidad no valía la pena el esfuerzo de ingeniería requerido para hacerlo. En la competición, los equipos recibieron millones de películas reseñas con las que trabajar para entrenar a su modelo. Netflix, internamente, se las arregla del orden de miles de millones de reseñas. Y así, para poder usar esto modelo que el equipo había construido sobre la base de los miles de millones de reseñas que Netflix tiene a su disposición.

[06:40] Fue una ingeniería tremenda esfuerzo por ampliarlo. Y según lo evaluaron los ingenieros, el esfuerzo y la potencia computacional necesarios para ejecutar este modelo, en relación con la mejora del rendimiento que cedió el modelo existente. Llegó a la conclusión de que, Vaya, interesante, decidieron seguir su modelo original.

