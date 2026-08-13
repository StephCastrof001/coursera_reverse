---
title: "35-Ensemble Models"
type: lesson
module: "[[M05 - Trees, Ensemble Models and Clustering]]"
tags: [lesson, ml-foundations]
---

# 🎓 35-Ensemble Models

> **Módulo:** [[M05 - Trees, Ensemble Models and Clustering]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 35-Ensemble Models
<!-- Módulo: 05-Trees, Ensemble Models and Clustering | Archivo: 35-Ensemble Models.es.vtt -->

[00:00] Uno de los desafíos comunes que tenemos Al crear modelos de aprendizaje automático, nos enfrentamos a sobredimensionar nuestros modelos a los datos de entrenamiento. Una estrategia popular para superar el desafío del sobreajuste es crear lo que se denomina modelos de conjunto. El objetivo del ensamblaje es combinar varios modelos en un metamodelo que sea más capaz de generalice la predicción a partir de nuevos datos.

[00:32] Promediando nuestros modelos y el resultado predicciones de cada modelo en conjunto. Es menos probable que encajemos demasiado sus datos de entrenamiento y, como resultado, somos más flexibles y estamos en mejores condiciones de generalice la predicción a partir de nuevos datos. La razón de esto es que promediar las predicciones de salida de los modelos, suponiendo que cada uno de esos modelos es independiente entre sí, son casi independientes, pueden reducir la varianza en comparación con la varianza de un modelo individual.

[01:02] Al reducir las variantes, mejoramos el rendimiento en la predicción. Entonces, ¿cómo funciona el ensamblaje? Comenzamos el proceso de ensamblaje mediante la creación de varios conjuntos de datos a partir de nuestro conjunto de datos original. Cada uno de estos nuevos conjuntos de los datos pueden ser una versión replicada completa de nuestro conjunto de datos original o puede ser una porción más pequeña de los datos originales.

[01:31] Luego podemos entrenar un modelo en cada uno de estos nuevos conjuntos de datos que tenemos. Todos nuestros modelos pueden tener el mismo algoritmo y entrenados de diferentes maneras utilizando diferentes hiperparámetros en diferentes conjuntos de datos o pueden utilizar diferentes algoritmos.

[01:45] Podemos combinar modelos lineales, por ejemplo, con modelos de árboles. Una vez que hayamos entrenado estos múltiples modelos, podemos usar cada modelo para generar predicciones. Entonces necesitamos una agregación función para combinar las predicciones para generar un único resultado predicción de nuestro modelo de conjunto.

[02:04] Y aquí nuevamente tenemos que tomar una decisión en términos de la forma de nuestra función de agregación. Si estamos trabajando con la clasificación modelo, podríamos optar por utilizar el voto mayoritario entre los individuos modelos miembros de nuestro conjunto. O si estamos trabajando con regresión problema, podemos usar un promedio simple de las predicciones de cada uno modelo de miembro individual, o algún tipo de promedio ponderado donde asignamos diferentes ponderaciones a las predicciones de salida de cada modelo miembro.

[02:34] Una vez que hayamos elegido nuestro función de agregación, podemos combinar las predicciones de nuestra modelos miembros en una sola predicción, que es el resultado de nuestro modelo de conjunto. Los modelos de conjuntos no son nada nuevo, de hecho, se usan comúnmente en una serie de industrias.

[02:51] Una de esas industrias Una de las que más se utilizan los modelos de conjunto es el clima industria de pronósticos, compañías meteorológicas privadas como el negocio que solía administrar. Usamos conjuntos de un gran número de previsiones meteorológicas individuales, que suelen provenir de varios gobiernos agencias de países de todo el mundo.

[03:11] Combinarán estos miembros individuales modela de manera inteligente, por lo general utilizando algún tipo de promedios ponderados que cambian dinámicamente con el tiempo. Y serán capaces de generar un modelo de conjunto que tiene una mejor capacidad de predicción que cada uno de los modelos de miembros individuales.

[03:32] Del mismo modo, la empresa eléctrica la industria suele utilizar modelos conjuntos para predecir la demanda o carga para la red. En este caso, las utilidades utilizarán modelos de conjunto debido a algunas de las entradas a la carga los modelos de previsión son inciertos. Una de las entradas principales para este tipo de modelo es el clima.

[03:54] Entonces, el propósito del modelo de conjunto podría ser utilizar como entrada diferentes escenarios meteorológicos, por ejemplo, analizar diferentes condiciones meteorológicas posibles condiciones para el día siguiente. Y para cada una de esas entradas diferentes condiciones, creando un modelo de miembros individuales que predice un resultado en términos de la carga o la demanda en la red. A continuación, el modelo de conjunto combina los resultados de los modelos miembros, cada uno de los cuales está provisto de diferentes condiciones de entrada en una única predicción de salida.

[04:26] Que luego es utilizado por la empresa eléctrica con fines de planificación para programar sus producción de energía para el día siguiente. Aunque los modelos de conjunto tienen excelentes potencial para reducir la varianza en las predicciones de su modelo, reducir el problema del sobreajuste y generar mejores predicciones a partir de nuevos datos, también conllevan desafíos.

[04:51] Uno de esos principales Los desafíos son el tiempo y los recursos que se necesitan para entrenar a múltiples modelos de miembros individuales de su conjunto. Del mismo modo, debes considerar los costos computacionales de ejecutar estos múltiplos modelos en paralelo. Cada vez que quieras generar una predicción, ahora tienes que ejecutar no solo una, sino varios modelos y , a continuación, combinar las predicciones de cada modelo.

[05:18] Y, por último, cuando usas un modelo de conjunto, pierdes la capacidad de interpretación en relación con un solo modelo. Con modelos individuales, tiende a ser es mucho más fácil entender cómo el modelo pudo alcanzar su predicción. Cuando se ensambla, se convierte en un más tarea desafiante porque ahora tienes que sumergirte en cada modelo individual y luego, cómo se combinaron los resultados de esos modelos para entender dónde de donde provino lo último y lo que predijo.

