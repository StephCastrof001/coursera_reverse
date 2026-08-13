---
title: "25-Troubleshooting Model Performance"
type: lesson
module: "[[M03 - Evaluating and Interpreting Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 25-Troubleshooting Model Performance

> **Módulo:** [[M03 - Evaluating and Interpreting Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 25-Troubleshooting Model Performance
<!-- Módulo: 03-Evaluating & Interpreting Models | Archivo: 25-Troubleshooting Model Performance.es.vtt -->

[00:04] No importa lo buenos que seamos construyendo modelos de aprendizaje automático, es inevitable que nos encontremos con situaciones en las que el modelo que hemos creado no rinda tan bien como nos gustaría. Hay muchas razones por las que los modelos no rinden tan bien como nos gustaría.

[00:18] Y depurar modelos que rinden mal puede ser un verdadero reto. En esta lección nos sumergiremos en algunas de las razones clave por las que los modelos no funcionan tan bien como se esperaba. He enumerado aquí las cinco razones principales por orden de gravedad. La primera fuente de error, y probablemente la más importante, que hay que analizar es si está encuadrando y comprendiendo correctamente el problema que está intentando resolver.

[00:44] ¿Y si ha elegido las métricas adecuadas para resolver ese problema? En segundo lugar, tiene que fijarse en los datos que tiene, la cantidad y la calidad de los datos. También tiene que considerar las características. ¿Ha definido correctamente las características y ha incluido suficientes características de sus datos para explicar el resultado de su modelo.

[01:03] El ajuste del modelo a veces puede ser un problema cuando no hemos hecho un trabajo adecuado de entrenamiento, un modelo a los datos que tenemos. Y, por último, en todos los problemas del mundo real. Siempre hay cierta cantidad de error inherente que, por muy buen trabajo de recopilación de datos y modelización que hagamos, simplemente no somos capaces de modelizar completamente el fenómeno que intentamos describir.

[01:26] Si su modelo no está funcionando tan bien como le gustaría. El primer lugar en el que debe fijarse es si ha enmarcado correctamente el problema que está tratando de modelar y si ha elegido la métrica correcta para evaluar el éxito en la modelización de ese problema. Veamos un ejemplo de un proyecto en el que participaba anteriormente para construir una herramienta para que las compañías eléctricas pudieran predecir la gravedad de los cortes de electricidad antes de que se produjeran fenómenos meteorológicos graves.

[01:53] Cuando empezamos con este proyecto, enmarcamos el problema de tal forma que nos centramos en construir un modelo de regresión para poder predecir el número de cortes de electricidad que se producirían en cada pueblo de todo el territorio de la compañía eléctrica. Realmente nos costó conseguir un modelo que fuera lo suficientemente preciso para ello.

[02:14] Y a medida que nos involucramos con más y más clientes de servicios públicos, aprendimos que realmente no era tan importante poder predecir el número exacto de desafíos que ocurren dentro de cada pueblo. En cambio, lo que dijo que realmente le importaba era que fuéramos capaces de predecir la gravedad esperada de un evento en todo el territorio agregado de los servicios públicos.

[02:37] En una escala del 1 al 5, que era una escala que utilizaban habitualmente en sus operaciones. Siendo 1 un suceso de bajo impacto con muy pocos cortes y 5 un suceso de muy alto impacto con cortes generalizados en todo el territorio. Así que en lugar de construir un modelo de regresión para predecir el número de desafíos en cada ciudad individual, pivotamos y nos centramos en un enfoque de clasificación.

[03:06] Donde el objetivo del modelo era tratar de clasificar para cada evento meteorológico severo que se avecinaba. Si iba a ser un evento que cayera dentro del rango de un 1,2,3,4 o 5 en la escala de la empresa de servicios públicos. Y al clasificar correctamente dónde iba a caer ese evento en la escala, proporcionó una información increíblemente valiosa a la empresa de servicios públicos.

[03:28] Que luego pudieron utilizar para prepararse para la tormenta que se avecinaba. Una segunda fuente de error muy común en la modelización es disponer de datos suficientes para construir un modelo en primer lugar. Si no se dispone de una cantidad suficiente de datos y si la calidad de los mismos no es buena, por ejemplo, si faltan muchos datos, sus datos no están limpios.

[03:50] Si tiene un gran número de valores atípicos dentro de sus datos, es como si realmente limitara el rendimiento que podemos esperar conseguir de un modelo que construyamos. No importa cuánto trabajo hagamos en la parte de modelado en sí. Si los datos no tienen una calidad suficiente, los resultados de nuestro modelo tampoco van a ser muy buenos.

[04:12] Bueno con considerar la cantidad y la calidad de nuestros datos. También tenemos que considerar si hemos definido las características adecuadas de los datos para incluirlas en nuestro modelo. Definir las características puede ser realmente un reto. Y a menudo intentamos involucrar a expertos en la materia en este proceso.

[04:28] Para asegurarnos de que hemos definido correctamente todas las características o rasgos de nuestros datos que necesitamos para explicar el resultado que intentamos predecir. Si construimos un modelo pero no incluimos un par de características clave. las realmente importantes para predecir el resultado, la calidad de nuestro modelo acabará no siendo muy buena.

[04:52] Si hemos hecho un buen trabajo definiendo el problema. Si tenemos suficiente cantidad y calidad de datos, si hemos incluido todas las características que necesitamos para describir el resultado, que estamos intentando predecir. Lo siguiente que hay que mirar es el ajuste del modelo en sí.

[05:08] ¿Hemos probado varios tipos de algoritmos? ¿Hemos ajustado los hiperparámetros de cada uno de esos algoritmos? Para encontrar un modelo que tenga un ajuste óptimo y el equilibrio adecuado de simplicidad y complejidad. Para que un modelo no se ajuste ni por defecto ni por exceso a los datos de que disponemos.

[05:29] Y, por último, si hemos pasado por todas esas cosas y seguimos teniendo problemas con el rendimiento de nuestro modelo. También es importante tener en cuenta que todos los problemas del mundo real son complejos y ruidosos y tienen un cierto nivel de error inherente. Es probable que nunca construyamos un modelo que pueda alcanzar el 100% o incluso el 99% de precisión en el fenómeno del mundo ferroviario.

[05:55] El nivel de error inherente y ruido que se encuentra en la naturaleza es simplemente demasiado alto para hacerlo. Así que el error inherente también puede establecer un límite superior en el rendimiento del modelo que estamos tratando de construir. Y es importante tener en cuenta que este límite superior puede existir.

