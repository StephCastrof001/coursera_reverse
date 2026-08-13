---
title: "44-Training Neural Networks"
type: lesson
module: "[[M06 - Deep Learning and Course Project]]"
tags: [lesson, ml-foundations]
---

# 🎓 44-Training Neural Networks

> **Módulo:** [[M06 - Deep Learning and Course Project]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 44-Training Neural Networks
<!-- Módulo: 06-Deep Learning & Course Project | Archivo: 44-Training Neural Networks.es.vtt -->

[00:05] En una lección anterior, recorrimos el proceso de entrenamiento y neurona artificial individual. Se trata ahora de extrapolar esa intuición al entrenamiento de toda una en su propia red. En la red neuaral tenemos ahora múltiples capas de pesos que necesitamos actualizar. Para ello trabajamos hacia atrás, empezamos por el final o el lado derecho y trabajamos hacia atrás hacia el lado izquierdo o la capa inicial de en su propia red.

[00:34] Podemos calcular nuestro coste total y distribuimos ese coste entre las distintas capas de nuestra red en función de la contribución de cada capa al coste total. A continuación, podemos calcular el gradiente de cada uno de los costes de cada capa con respecto a los pesos que alimentan esa capa.

[00:58] Una vez calculado ese gradiente, podemos realizar el descenso gradiente y actualizar los pesos que alimentan cada una de las capas. Este proceso se popularizó en la década de 1980 y se denomina retropropagación. Y todavía hoy es el método principal que utilizamos para entrenar redes neuronales.

[01:17] Así que ahora vamos a recorrer el proceso paso a paso para entrenar en red neuronal. De forma similar a lo que vimos cuando entrenamos una neurona artificial, el primer paso es nuestro paso de propagación hacia delante. Así que si estamos utilizando el descenso de gradiente estocástico, donde estamos entrenando con un solo punto de datos a la vez, tomaremos nuestro primer punto de datos y lo alimentaremos a través de la red neuronal.

[01:41] Así que empezaremos con la capa de entrada, multiplicaremos nuestras características por los pesos, lo pasaremos a través de la función de activación en la capa oculta. Multiplicaremos la salida de esa función de activación de la capa oculta por otro conjunto de pesos para llegar a nuestra capa de salida.

[01:59] La pasaremos a través de la función de activación de nuestra capa de salida y calcularemos la predicción o nuestro valor y hat. Una vez que hayamos calculado y hat, ya podemos calcular nuestro coste y ingrediente o derivada de nuestro coste utilizando nuestra predicción y hat, y nuestro valor real y.

[02:24] De nuevo queremos calcular el gradiente de nuestra función de coste con respecto a cada peso dentro de nuestra red. Dado que nuestro gradiente es el producto de los pesos por otros pesos y funciones de activación, tenemos que aplicar la regla de la cadena en este caso. Así que se complica un poco más que la situación con una sola neurona artificial.

[02:49] Pero aplicando la regla de la cadena seguimos siendo capaces de calcular nuestro gradiente de nuestra función de coste con respecto a cada peso en la red neuronal. Y una vez que calculamos nuestro gradiente somos capaces de actualizar nuestros valores de peso en de la misma manera que lo hicimos anteriormente.

[03:04] Donde nuestros nuevos valores de peso son iguales a nuestros valores de peso anteriores menos nuestra tasa de ejecución veces la derivada de nuestra función de coste con respecto a cada peso. Hacemos esto para cada capa de nuestra red y para cada valor de peso dentro de cada capa de nuestra red.

[03:24] A continuación, actualizamos nuestros valores de peso y repetimos el proceso, tomando el siguiente punto de datos , pasándolo a través de nuestra red calculando el gradiente, actualizando nuestros pesos y continuando hasta que nuestros valores de peso converjan y tengamos un modelo de red neuronal final para utilizar.

[03:40] Bien, los retos al trabajar con redes neuronales es que hay muchas decisiones que tomar en el diseño de una arquitectura de red neuronal. Tenemos que decidir cuántas capas queremos en la red neuronal. Cuántas unidades queremos dentro de cada capa, tenemos que elegir la función de activación que usaremos para cada una de esas unidades.

[04:02] Tenemos que tomar otras decisiones, como ¿queremos añadir regularización? ¿Queremos usar el descenso de gradiente por lotes o el descenso de gradiente por mini lotes o el descenso de gradiente estocástico? Tenemos que elegir un valor para una tasa de aprendizaje que puede influir en lo bien y lo rápido que puede entrenarse nuestro modelo de red neuronal.

[04:23] Como hay tantas decisiones que tomar en la práctica, a menudo utilizamos uno de estos dos enfoques. El primer enfoque es lo que yo llamo el enfoque de los pantalones estirados. Lo que significa que queremos utilizar una red que sea demasiado grande para el problema que estamos intentando resolver.

[04:39] Y entonces podemos aplicar algunas técnicas para reducir el riesgo de sobreajuste o estirarla para que se ajuste justo a los datos que tenemos y al problema que estamos intentando resolver. Ya hemos tratado algunas de esas técnicas en lecciones anteriores, como la regularización. El segundo enfoque consiste en utilizar un modelo de red neuronal que alguien ya ha hecho el importante trabajo de configurar y entrenar en un conjunto de datos muy, muy grande.

[05:11] Este enfoque se denomina aprendizaje por transferencia. Así que veamos un poco más en profundidad cómo funciona. En el aprendizaje por transferencia empezamos utilizando un modelo de red neuronal preconstruido, preentrenado, que otra persona ha entrenado en una tarea relevante para nosotros.

[05:29] Así que si estamos trabajando en un problema en el que tenemos que clasificar imágenes, pongamos por ejemplo , estamos construyendo un modelo para clasificar imágenes de flores. Puede que queramos tomar un modelo que haya sido bastante entrenado para clasificar imágenes de diferentes tipos.

[05:47] Por lo general, estos modelos se entrenan en conjuntos de datos muy, muy grandes de muchos tipos diferentes de imágenes y podemos aprovechar todo ese trabajo pesado y todo ese preentrenamiento que se ha hecho. Y utilizarlo y hacer algunos ajustes finales en ese modelo para nuestra tarea específica.

[06:08] Así que normalmente tomaremos un modelo genérico que alguien más ha preentrenado en un conjunto de datos de imágenes muy grande. Utilizaremos una parte importante de ese modelo pero a menudo cortaremos el último par de capas y entonces construiremos un nuevo modelo utilizando esa parte preentrenada del modelo.

[06:29] Y añadiendo un par de capas finales a nuestro modelo, que entonces entrenaremos de forma que se esté afinando en una tarea específica. Así que en el ejemplo de querer construir una aplicación que clasifique flores, digamos que podemos aprovechar un modelo que alguien ha preentrenado sobre un gran conjunto de imágenes de muchos tipos diferentes de animales, y objetos, y plantas, etcétera.

[06:55] Tomaremos todas las capas de ese modelo excepto las dos últimas y entonces añadiremos un nuevo conjunto de capas finales. Entonces entrenaremos esas nuevas capas finales utilizando un conjunto de datos específico que hemos recopilado, el específico para nuestra tarea en cuestión, que es clasificar flores.

[07:14] Así que este conjunto de datos sería, por ejemplo, un conjunto de datos de imágenes de diferentes tipos de flores. Una vez que hemos entrenado nuestro último par de capas en el modelo neuronal, ahora tenemos un modelo que es capaz de lograr nuestra tarea específica de clasificar flores.

[07:30] Que se ha beneficiado significativamente de todo el trabajo que alguien más ha hecho para pre-entrenar una gran parte de ese modelo. Y ahora hemos añadido algunos de nuestros propios ajustes finos con el fin de ayudar a ese modelo a reconocer diferentes tipos de flores.

