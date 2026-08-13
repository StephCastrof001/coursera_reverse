---
title: "39-Module Wrap-up"
type: lesson
module: "[[M05 - Trees, Ensemble Models and Clustering]]"
tags: [lesson, ml-foundations]
---

# 🎓 39-Module Wrap-up

> **Módulo:** [[M05 - Trees, Ensemble Models and Clustering]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 39-Module Wrap-up
<!-- Módulo: 05-Trees, Ensemble Models and Clustering | Archivo: 39-Module Wrap-up.es.vtt -->

[00:04] En los dos últimos módulos, presentamos algunos de los algoritmos de aprendizaje automático más comunes. Empezamos con una discusión sobre un conjunto de algoritmos llamados modelos lineales, que incluyen la regresión lineal, que se utiliza normalmente para tipos de regresión de tareas de aprendizaje automático, y la regresión logística, que se utiliza para tareas de clasificación.

[00:27] A continuación, hablamos de un conjunto muy diferente de modelos, que se denominan modelos no paramétricos. Concretamente, los árboles de decisión y los modelos de conjunto, entre los que se incluyen los bosques aleatorios, que se componen de muchos árboles de decisión. hemos hablado de algunas de las ventajas de este tipo de algoritmos de aprendizaje automático, y también de algunas de sus desventajas en relación con los modelos lineales más sencillos.

[00:53] Es importante tener en cuenta que, a la hora de evaluar y elegir los algoritmos a utilizar para los problemas de aprendizaje automático, hay tres criterios clave que tenemos en cuenta. El más obvio es el rendimiento. Un algoritmo puede darnos naturalmente un rendimiento mejor o peor que otro algoritmo que elijamos para nuestro problema.

[01:14] El segundo criterio que queremos considerar es la interpretabilidad. Una de las grandes cosas de los modelos lineales es que son altamente interpretables. Es muy fácil entender cómo un modelo lineal está generando su predicción. Si estamos creando un modelo en el que es importante que seamos capaces de explicar a el usuario de nuestro modelo cómo logramos la predicción, podríamos considerar algo como una simple regresión lineal.

[01:40] Del mismo modo, los árboles de decisión son también muy sencillos de entender cómo se genera una predicción siguiendo el camino a través de un árbol. Pero a medida que llegamos a cosas más complejas como los modelos de conjunto, perdemos interpretabilidad, y se nos hace mucho más difícil realmente explicar cómo un modelo está generando sus predicciones.

[01:59] En algunos casos, eso podría estar bien, donde es más aceptable tratar un modelo como una caja negra que genera predicciones. Pero cuando estamos trabajando con cosas que tienen consecuencias muy significativas para los individuos, consecuencias financieras, o de otro tipo, tenemos que asegurarnos de que estamos construyendo modelos que tienen algún nivel de interpretabilidad, de modo que cuando tengamos que ir a ver por qué el modelo está generando los resultados que está generando, que seamos capaces de hacerlo.

[02:29] El último criterio es el coste computacional. Cada uno de estos diferentes algoritmos viene con un nivel diferente de coste computacional y recursos para entrenar el modelo en primer lugar, y luego para ejecutar la inferencia, o generar predicciones utilizando el modelo sobre una base de ir hacia adelante en un producto.

[02:47] A medida que comparamos algoritmos, y construimos modelos seleccionando un algoritmo a utilizar, necesitamos tener en mente cada uno de estos tres criterios para impulsar nuestras decisiones. También abordamos brevemente en este último módulo el aprendizaje no supervisado, y, en concreto, la agrupación.

[03:06] Examinamos la agrupación k-means. Lo fundamental que hay que recordar para la agrupación es que la decisión más importante que tenemos que tomar es cómo estamos definiendo la similitud entre las cosas. Volvamos a un ejemplo anterior en el que estábamos construyendo un modelo para predecir los precios de la vivienda.

[03:23] Digamos que vamos a aplicar una técnica no supervisada a este tipo de problema. En lugar de generar predicciones de los precios de venta de esas casas, vamos a intentar clasificar las casas en diferentes grupos lógicos. De nuevo, la clave aquí para que este tipo de modelo funcione es decidir cómo definimos si las casas son similares o diferentes.

[03:48] Hay muchas formas de hacerlo. Podríamos definir la similitud basándonos en algo como el tamaño, donde utilizamos los metros cuadrados, o el número de dormitorios o baños. Podríamos definir la similitud basándonos en el año de construcción, donde las casas más antiguas son más similares entre sí, independientemente de su tamaño en relación con las casas nuevas.

[04:10] O podríamos elegir algo como la ubicación, el barrio en el que se encuentra la casa, o el distrito escolar en el que las casas, se encuentran. El mismo barrio, un distrito escolar, son más similares entre sí independientemente de su tamaño o edad. Pensar bien cómo definir la similitud entre las cosas es realmente la clave del éxito en los enfoques de agrupación independientemente del algoritmo de agrupación específico que decida aplicar.

