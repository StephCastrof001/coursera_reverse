---
title: "06-Data Terminology"
type: lesson
module: "[[M01 - What is Machine Learning]]"
tags: [lesson, ml-foundations]
---

# 🎓 06-Data Terminology

> **Módulo:** [[M01 - What is Machine Learning]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 06-Data Terminology
<!-- Módulo: 01-What is Machine Learning | Archivo: 06-Data Terminology.es.vtt -->

[00:05] En esta lección, vamos a definir algunos términos de uso común en la analítica de datos y el aprendizaje automático. En primer lugar, ¿qué significa la palabra datos? La OCDE define los datos como características o información generalmente numérica, que se recogen a través de la observación.

[00:24] Los datos pueden ser de muchas formas, porque casi cualquier cosa puede convertirse en valores numéricos. Los datos pueden ser medidas de un objeto o sus dimensiones. Puede significar texto, palabras o frases o documentos pueden ser imágenes, puede ser sonido, que incluso puede ser vídeo porque las imágenes, sonido y vídeo incluso en la superficie, pueden no parecer numéricos en realidad se compone de números.

[00:52] Por ejemplo, los valores de los píxeles dentro de una imagen, los datos también pueden tener diferentes tipos de relaciones. Así, las relaciones comunes que se encuentran en los datos son las relaciones espaciales en las que los puntos de datos se relacionan a través de algún concepto de cercanía o lejanía en el espacio o ubicación dentro del espacio.

[01:13] Los datos también pueden tener relaciones temporales, en las que los puntos y los datos se relacionan a través del tiempo y a través de lo cerca o lejos dentro del tiempo que están unos de otros. Solemos dividir los datos en dos tipos principales, datos estructurados frente a datos no estructurados.

[01:34] Así que los datos estructurados siguen una estructura establecida, que se basa en un conjunto de campos predefinidos. Así que tenemos varios registros dentro de los datos estructurados y cada registro incluye una serie de campos predefinidos. Así que para aquellos de ustedes que hayan utilizado un programa de hoja de cálculo como Excel, estarán muy familiarizados con esto.

[01:55] Excel se basa en la idea de datos estructurados, donde tenemos una serie de filas que son los registros y cada fila puede tener varias columnas que son los campos predefinidos. A menudo los datos estructurados se almacenan en lo que se llama bases de datos relacionales y es agradable trabajar con ellos, porque es muy fácil introducirlos y organizarlos y la estructura que tienen hace que sea fácil buscarlos y analizarlos.

[02:21] También funciona muy bien con herramientas de uso común, no sólo por los profesionales de la ciencia de datos y el aprendizaje automático, sino personas que trabajan a través de una variedad de diferentes roles dentro de una organización a menudo pueden interactuar datos estructurados a través de programas como Microsoft, Excel.

[02:37] Los datos no estructurados no siguen ningún formato predefinido de campos. Así que ejemplos de datos no estructurados serían cosas como imágenes, vídeos, sonidos o texto donde no hay campos predefinidos o ni siquiera quizás una longitud predefinida. Cuando pensamos en texto, por ejemplo, una frase puede consistir en cualquier número arbitrario de palabras.

[03:00] Un documento puede consistir en cualquier número arbitrario de frases, así que es difícil predefinir una estructura para capturar algo como texto. En general, los datos estructurados requieren un conjunto de herramientas especializadas para trabajar con ellos. Así que es un poco más difícil para los individuos de una organización ser capaces de trabajar con ellos sin el conjunto adecuado de herramientas.

[03:23] Sin embargo, si nos fijamos en los datos de una organización típica, aproximadamente el 80% de ellos se consideran datos no estructurados y estos serían cosas como imágenes, podría ser vídeo o texto, como un correo electrónico o diapositivas. El 20% de los datos es lo que se considera datos estructurados.

[03:42] Cuando trabajamos con aprendizaje automático trabajaremos con ambos tipos de datos, estructurados y no estructurados. Y a menudo utilizamos diferentes algoritmos son diferentes enfoques, dependiendo del tipo de datos con los que estemos trabajando, datos continuos significa variables numéricas que pueden tomar un número infinito de valores posibles entre dos valores dados cualesquiera.

[04:02] Un ejemplo de ello sería la longitud de una pieza, la temperatura, la altura o el peso de una persona o incluso el tiempo, que pueden representarse mediante un número infinito de valores posibles. Por otro lado, los datos categóricos pueden clasificarse en un número finito de categorías o grupos distintivos.

[04:23] A veces éstos tienen un orden o clasificación lógica y a veces no. Así, algunos ejemplos podrían ser el sexo, la especialidad de los estudiantes, los colores, un tipo de material. Y tenemos un tercer tipo llamado datos discretos. Los datos discretos son variables numéricas que tienen un número contable de valores.

[04:45] Así, por ejemplo, la edad, el número de piezas, el año en que se fabricó algo aunque sean de naturaleza numérica, porque tenemos un número finito de ellas. A menudo, cuando hacemos aprendizaje automático, las consideramos variables categóricas, porque entran en un número finito de categorías o grupos posibles.

[05:09] Otro tipo de datos que suele utilizar el aprendizaje automático son los llamados datos de series temporales. En las series temporales, los datos se organizan en orden temporal. Normalmente los puntos están espaciados por igual en el tiempo. Así que podemos tener puntos que representen mediciones de un sensor por ejemplo cada segundo o cada minuto, cada hora o cada día.

[05:33] Podemos estar trabajando con precios de acciones donde tenemos precios de ticker cada 15 minutos o precios diarios de apertura y cierre. O podemos estar trabajando con datos por ejemplo de un contador inteligente donde tenemos lecturas continuas y tenemos números agregados diarios, mensuales y anuales que representan el uso a lo largo del tiempo.

[05:57] Los supuestos que subyacen a los datos de series temporales número uno es que el tiempo se considera de una manera no retrocedemos en el tiempo, sólo avanza en una dirección. En segundo lugar, asumimos que los puntos que están más próximos en el tiempo son generalmente más relevantes o más relacionados entre sí que los puntos que están más alejados en el tiempo.

[06:16] Así que ahora introducimos algo de terminología que es específica de los datos de estructura. Así que tenemos un ejemplo aquí en la diapositiva que muestra una serie de casas en venta en el barrio en el área local, cada casa tiene una serie de características, tales como en qué barrio está, los distritos escolares en los que se encuentra, metros cuadrados de la casa, el número de dormitorios y el año de construcción.

[06:39] Y luego, para cada casa tenemos un precio de venta de mercado registrado de la casa. Así que este sería un ejemplo perfecto de datos estructurados. Y estamos trabajando con este tipo de datos. Utilizamos cierta terminología específica cuando aplicamos el aprendizaje automático. Y así que vamos a ir a través de los detalles de eso.

[06:58] En primer lugar, cada fila de un dato. Así que cada casa en este caso es lo que se llama una observación de un dato. También lo verá referido como una instancia de los datos, un ejemplo o un vector de características. Cada columna de un dato es lo que comúnmente se denomina una característica de nuestros datos.

[07:20] También se denomina factor, predictor, variable X, variable independiente, atributo o incluso dimensión y aprendizaje automático. A veces nos gustaría utilizar muchas palabras diferentes para representar lo mismo. Por último, la última columna es un poco diferente de las otras columnas, porque la última columna es lo que estamos tratando de predecir, ¿verdad?

[07:43] Así que la última columna la llamamos nuestro objetivo, porque el objetivo de un modelo que nos gusta construir es predecir el precio de venta. Así que esto puede ser llamado el objetivo, también llamado la etiqueta y la anotación, respuesta, una variable Y o incluso una variable dependiente.

