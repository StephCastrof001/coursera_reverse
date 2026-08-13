---
title: "13-Feature Selection"
type: lesson
module: "[[M02 - The Modeling Process]]"
tags: [lesson, ml-foundations]
---

# 🎓 13-Feature Selection

> **Módulo:** [[M02 - The Modeling Process]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 13-Feature Selection
<!-- Módulo: 02-The Modeling Process | Archivo: 13-Feature Selection.es.vtt -->

[00:04] Ahora vamos a profundizar un poco más en cada uno de los pasos de la construcción de un modelo. Empezaremos con la selección de características. En mi experiencia, la selección de características es en realidad el paso más importante de la construcción de un modelo. La selección de características se centra en identificar el conjunto o subconjunto de características o rasgos de los datos que utilizaremos para construir y entrenar nuestro modelo.

[00:28] En primer lugar, recapitulemos, ¿qué son los rasgos? Los rasgos son características de nuestros datos. En el ejemplo que hemos estado utilizando de casas en venta, los rasgos incluirían cosas como el número de dormitorios o baños, el barrio en el que se encuentra la casa, o el distrito escolar en el que puede estar, el año en que se construyó la casa.

[00:48] Hay muchos rasgos posibles que podríamos utilizar en el entrenamiento de un modelo. Nuestra tarea en la fase de selección de características es identificar qué características tienen el mayor valor en términos de entrenamiento del modelo para que sea capaz de predecir con precisión el objetivo de salida dadas las entradas.

[01:08] ¿Cómo definimos las características de nuestros datos? Definimos las características realmente como la intersección de dos cosas. La número 1 es, ¿cuáles son los factores que podrían influir en el problema que estamos tratando de resolver? De nuevo, en términos de predicción de los precios de venta, los factores que podrían influir en el problema serían características de la propia casa.

[01:31] Sería el tiempo, cosas como el año en que se construyó la casa o el año en que se vendió. Podrían ser características o factores sobre el barrio, o la zona más amplia, o la ciudad en la que se encuentra la casa. Tenemos un gran conjunto de posibles factores que podrían influir en nuestro problema de predecir el precio de una casa.

[01:51] Lo segundo que tenemos que considerar es ¿de qué datos disponemos o qué datos podríamos recopilar? En el caso de las casas en venta, suele ser bastante fácil recopilar muchos datos sobre las propias casas o la zona local. Pero a veces, cuando trabajamos con problemas, puede ser mucho más difícil tratar de recopilar ciertas piezas de información sobre los factores que pueden influir en el problema.

[02:16] Por lo general, tratamos de definir características como la intersección de lo que podría influir en nuestro problema y lo que podríamos ser capaces de recopilar. Ahora vamos a recorrer un sencillo estudio de caso de un problema en el que estaba trabajando en un equipo que solía dirigir en la industria.

[02:35] Nuestro objetivo con este nuevo producto que estábamos construyendo era poder predecir la gravedad y la ubicación de los cortes de electricidad para las empresas eléctricas antes de que se produjeran tormentas que pudieran afectar a la red eléctrica. Los cortes de electricidad están causados principalmente por la caída de árboles sobre los cables, pero hay muchas cosas que pueden provocar la caída de árboles.

[02:57] Dedicamos mucho esfuerzo y tiempo a trabajar en la selección de características para identificar el conjunto relevante de datos y características de esos datos que pudiéramos utilizar para construir un modelo eficaz para predecir los cortes de suministro eléctrico. Realizamos entrevistas a expertos del sector, tanto del sector de los servicios públicos de meteorólogos y acabamos con un conjunto de factores que incluían cosas como el gas del viento, las cantidades de precipitación, incluso cosas que podrían no sospecharse inicialmente, como la estacionalidad.

[03:30] Por ejemplo, los árboles que todavía tienen hojas son mucho más propensos a caerse encima de las líneas eléctricas en vientos fuertes y causar apagones en relación con los árboles y si tiempo que no tienen hojas y por lo tanto son mucho menos propensos a caerse. A veces las características son características muy obvias de sus datos o su problema.

[03:50] Otras veces, las características son mucho menos obvias e implican una gran cantidad de investigación, que se realiza mejor hablando con expertos del sector que tengan una experiencia particular sobre el problema que está intentando resolver. Existen varios métodos de selección de características.

[04:06] El primero y, según mi experiencia, el mejor método de selección de características es hablar realmente con expertos sobre el problema que se intenta resolver. En el caso de una herramienta para cortes de electricidad que estábamos construyendo, hablamos con muchas personas de empresas eléctricas.

[04:21] Hablamos con meteorólogos para comprender mejor qué factores influyen más en la gravedad de los cortes de electricidad. Eso nos ayudó luego a acotar un conjunto de características de nuestros datos para utilizarlas en el desarrollo del modelo. También podemos utilizar los propios datos para comprender mejor las relaciones entre las posibles características de entrada y el resultado que intentamos predecir.

[04:46] Podemos hacerlo mediante la visualización. Por ejemplo, recopila datos que incluyan muchas características. Crea gráficos sencillos de cada característica de nuestros datos en relación con la salida que estamos prediciendo. En el ejemplo del predictor de cortes de electricidad, podríamos elegir trazar la velocidad sostenida del viento en relación con los cortes de electricidad o la temperatura en relación con los cortes de electricidad.

[05:10] Eso puede ayudarnos mediante la visualización, a identificar posibles relaciones fuertes entre cada de estas características potenciales y la salida. Del mismo modo, también podemos aplicar pruebas estadísticas para evaluar la fuerza de la correlación o las relaciones entre las posibles características y la salida.

[05:29] Podemos hacerlo recopilando un gran conjunto de datos pasados y luego realizando pruebas utilizando esos datos pasados para identificar las relaciones. Por último, hay un conjunto de técnicas que podemos emplear cuando estamos construyendo el modelo en sí. A medida que construimos y entrenamos el modelo, podemos examinar en qué características se basa más el modelo para poder predecir con eficacia el resultado que intentamos predecir.

[05:55] Podemos entonces reducir nuestra selección de características para centrarnos sólo en aquellas características que el modelo está utilizando más en términos de predicción del resultado, y podemos eliminar o deshacernos de características que el modelo realmente no está utilizando en absoluto para poder hacer sus predicciones.

[06:14] Un consejo que me gustaría compartir sobre la selección de características es que incluir muy pocas características en su modelo suele ser mucho peor que incluir demasiadas. En caso de duda, intente recopilar tantos datos como pueda y tantas características o factores posibles como pueda sobre el problema que está intentando resolver.

[06:34] Construya su modelo utilizando todas esas características inicialmente y vea cómo se comporta. Cuando entonces identifique características que son irrelevantes o tal vez duplicadas, puede empezar entonces a reducir su conjunto de características. Pero empezar con un grupo muy pequeño de características puede ser muy peligroso porque a menudo puede ocurrir que esté dejando fuera accidentalmente una característica o factor importante, y como resultado, será imposible conseguir un buen rendimiento del modelo.

