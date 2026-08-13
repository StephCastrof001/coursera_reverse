---
title: "20-Outcomes vs Outputs"
type: lesson
module: "[[M03 - Evaluating and Interpreting Models]]"
tags: [lesson, ml-foundations]
---

# 🎓 20-Outcomes vs Outputs

> **Módulo:** [[M03 - Evaluating and Interpreting Models]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 20-Outcomes vs Outputs
<!-- Módulo: 03-Evaluating & Interpreting Models | Archivo: 20-Outcomes vs Outputs.es.vtt -->

[00:05] La evaluación y la interpretación de los modelos es el objetivo principal del paso cinco del proceso cristiano. Sin embargo, la definición de las métricas para evaluar los modelos comienza en realidad justo al principio del proceso y en el paso uno de comprensión del negocio. Cuando definimos el problema que estamos intentando resolver a través de un modelo, una parte clave de esa definición del problema es definir qué aspecto tiene el éxito.

[00:29] E identificar la métrica que vamos a utilizar para evaluar el éxito. Nuestra elección de métricas en la fase de comprensión del negocio alimenta directamente nuestra evaluación de modelos cuando llegamos a ese cinco del proceso. Aprendizaje automático, generalmente utilizamos dos tipos diferentes de métricas para evaluar el rendimiento de nuestro modelo.

[00:51] El primer tipo se denomina métricas de resultados. Las métricas de resultados se refieren al impacto empresarial deseado del modelo o del producto más amplio que estamos intentando crear, ya sea para nuestra propia organización o para nuestros clientes. Normalmente, el impacto empresarial se expresa en términos de dólares, por lo que pueden ser dólares de costes ahorrados, pueden ser dólares de ingresos generados.

[01:16] A veces también puede ser un tiempo, pero normalmente se refiere a algún tipo de impacto en un cliente o en nuestras propias operaciones empresariales. Las métricas de resultados no contienen métricas de rendimiento técnico sobre el modelo que hemos creado. Las métricas de salida, por otro lado, se refieren a la salida deseada de nuestro modelo.

[01:40] Normalmente se expresan en términos de una de las métricas de rendimiento de nuestro modelo que vamos a conocer más adelante en esta lección. Normalmente las métricas de salida de un modelo no se comunican al cliente salvo en contadas ocasiones. Lo que realmente le importa a nuestro cliente es el resultado que le estamos proporcionando.

[01:59] No tanto el resultado del modelo en sí. Las métricas de salida también se establecen generalmente después de que hayamos definido el resultado deseado y dejamos que la elección de la métrica de resultado dicte entonces nuestra selección de métricas de salida que utilizamos para evaluar nuestro modelo.

[02:17] Para ilustrar la diferencia entre métrica de resultado y métrica de salida, consideremos un par de casos prácticos. El primer caso práctico se centra en una herramienta de predicción de turbulencias para aerolíneas. Nuestro objetivo en este caso es utilizar las condiciones atmosféricas para predecir las turbulencias antes de que despeguen los vuelos.

[02:37] Al predecir las turbulencias, podemos optimizar las rutas de vuelo para garantizar vuelos seguros. Una métrica de resultados que podríamos utilizar para evaluar el rendimiento de esta herramienta que estamos construyendo podría parecerse a esto. Un menor número de incidentes de seguridad al año para una aerolínea cliente de esta herramienta.

[02:56] O quizás un menor valor en dólares de las reclamaciones relacionadas con la seguridad presentadas contra esa aerolínea. Esto sería un resultado directo de las herramientas, la capacidad de predecir con éxito turbulencias y, por lo tanto, para garantizar que esa aerolínea está planificando rutas de vuelo seguras y minimizando los posibles incidentes de seguridad.

[03:16] La métrica de salida que podríamos utilizar para evaluar la calidad del modelo que construimos para apoyar esta herramienta sería típicamente una clasificación barométrica. Y hablaremos de algunas opciones diferentes para ello más adelante en este módulo. Consideremos ahora un segundo caso práctico.

[03:32] Estamos construyendo una herramienta para que las compañías eléctricas puedan prever la demanda de energía en su red. La previsión de la demanda es de vital importancia para las empresas eléctricas para ayudarles a planificar su generación de energía. Las empresas eléctricas que son capaces de hacer un buen trabajo de previsión de la demanda son capaces de optimizar la mezcla de energía que generan, minimizando su coste y las emisiones asociadas a esa generación de energía.

[03:58] Cuando hacen un mal trabajo de previsión de la demanda las empresas eléctricas a menudo se ven obligadas a utilizar lo que se llama centrales Peaker para satisfacer la demanda extra. El problema de utilizar plantas Peaker es que a menudo son muy caras y dan lugar a emisiones más elevadas en relación con la generación de energía estándar para las empresas de servicios públicos.

[04:17] Las métricas de resultados que podríamos seleccionar para evaluar nuestra herramienta podrían ser algo así, un menor coste por megavatio hora de energía producida para nuestros clientes de servicios públicos de electricidad. O una menor tasa de emisiones por megavatio hora de energía producida.

[04:34] Optaríamos por evaluar el resultado del modelo que hay detrás de este producto utilizando una regresión barométrica, de la que hablaremos un poco más adelante.

