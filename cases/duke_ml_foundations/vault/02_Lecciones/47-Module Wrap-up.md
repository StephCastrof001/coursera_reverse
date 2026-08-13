---
title: "47-Module Wrap-up"
type: lesson
module: "[[M06 - Deep Learning and Course Project]]"
tags: [lesson, ml-foundations]
---

# 🎓 47-Module Wrap-up

> **Módulo:** [[M06 - Deep Learning and Course Project]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 47-Module Wrap-up
<!-- Módulo: 06-Deep Learning & Course Project | Archivo: 47-Module Wrap-up.es.vtt -->

[00:04] En este módulo, hemos construido una intuición de cómo funcionan realmente los modelos de redes neuronales y hemos hablado de algunas de las aplicaciones comunes de los modelos de aprendizaje profundo. Concluyamos esta sección hablándoles de los puntos fuertes y débiles de las redes neuronales en relación con otras formas de aprendizaje automático.

[00:25] Una de las grandes cosas de las redes neuronales es su capacidad para modelar relaciones muy complejas en las que tenemos un número muy grande de características. En particular, cuando trabajamos con datos no estructurados como imágenes, vídeo, o texto, en los que tenemos un gran número de características, éstas son áreas en las que las redes neuronales realmente destacan sobre otras formas de aprendizaje automático.

[00:51] Otra de las grandes ventajas de las redes neuronales es que requieren mucha menos ingeniería de características que otras formas de aprendizaje automático. Históricamente, hemos tenido que dedicar mucho trabajo a definir y seleccionar y manipular características para encontrar la combinación adecuada que utilizar en un modelo.

[01:08] Con las redes neuronales, debido a las complejas relaciones que son capaces de identificar y a cómo funcionan, generalmente hay mucho menos trabajo inicial que hacer en la ingeniería de las características. También son ahora muy fáciles de utilizar gracias al gran trabajo realizado por los investigadores y algunas de las grandes empresas tecnológicas que han puesto a disposición paquetes de programación con APIs y con los que es muy fácil trabajar, así como todos los métodos automatizados de realizar aprendizaje profundo donde en realidad ni siquiera tiene que escribir una sola línea de código, sino que podría aprovechar estos foros automatizados de aprendizaje profundo para construir sus modelos.

[01:53] A pesar de sus puntos fuertes, también hay algunos retos importantes que hay que tener en cuenta al trabajar con redes neuronales. El primero es que las redes neuronales pueden ser muy costosas computacionalmente para entrenar y ejecutar. Cuando estamos tratando con un gran conjunto de características, hay un número extremadamente grande de pesos que necesitan ser aprendidos a medida que entrenamos nuestro modelo.

[02:14] Podemos tener números de ponderaciones del orden de cientos de miles o millones o incluso miles de millones, dependiendo del tamaño de nuestro modelo. Como resultado, necesitamos mucha potencia computacional así como tiempo para entrenar estos modelos. Incluso cuando los utilizamos para inferir o generar predicciones, a menudo pueden ser costosos computacionalmente para hacerlo.

[02:37] Debido al coste computacional, también están muy hambrientos de energía. De hecho, los recursos computacionales necesarios para entrenar una red neuronal de las mejores de su clase, se han duplicado cada 3-4 meses en los últimos dos años. De hecho, se han multiplicado por 300.000 desde 2012.

[02:58] Los modelos de redes neuronales también pueden ser más desafiantes de entrenar que otras formas de aprendizaje automático. Hay una serie de hiperparámetros con los que trabajar y enfoques muy sofisticados sobre cómo establecer y gestionar esos hiperparámetros. La mayor desventaja o desafío de las redes neuronales es que son muy difíciles de interpretar el resultado.

[03:21] La gente suele ver las redes neuronales como cajas negras, en las que generan alguna predicción de salida, pero realmente no somos capaces de mirar dentro de la caja negra para entender qué está pasando y cómo está llegando a esa predicción. La razón de esto es que las redes neuronales son muy complicadas con números muy grandes de ecuaciones encontradas debido al número de capas de nodos que necesitan ser entrenados.

[03:47] Cuando lo comparamos con un simple modelo de regresión lineal o un simple modelo de árbol, por ejemplo, es mucho más difícil entender cómo la red está llegando a su predicción. En algunos casos, esto está bien dependiendo de su tarea. Realmente no necesita mirar dentro del modelo para entender cómo está llegando a su salida.

[04:08] En otras situaciones, esto podría ser un problema realmente grande, en particular, si estamos utilizando un modelo para tareas que tienen consecuencias significativas para los usuarios. Digamos que estamos construyendo un modelo para identificar qué clientes que solicitan una hipoteca deberían ser aprobados para la hipoteca o el límite de crédito que alguien debería recibir cuando está solicitando una nueva tarjeta de crédito, o si alguien es admitido o no en una escuela de posgrado, todas estas son situaciones en las que hay consecuencias significativas en el usuario o los otros interesados en ese modelo.

[04:46] Como resultado, la interpretabilidad es críticamente importante en estas cosas. Tenemos que ser capaces de entender cómo está funcionando el modelo y cómo está llegando a las conclusiones a las que está llegando para asegurarnos de que no estamos introduciendo sesgos en nuestro modelo por el camino.

[05:03] Estas son situaciones en las que tenemos que ser muy cuidadosos sobre el uso de modelos como las redes neuronales, que podrían ser intrínsecamente muy difíciles de examinar. Por último, las redes neuronales requieren una gran cantidad de datos para entrenarse bien. Pueden sobreajustarse fácilmente a situaciones en las que tenemos conjuntos de datos relativamente pequeños.

[05:30] El reciente auge en la adopción de modelos de aprendizaje profundo o de redes neuronales se ha visto impulsado por la cantidad cada vez mayor de datos y de potencia de procesamiento que tenemos ahora a nuestra disposición. Las grandes cantidades de datos y la alta potencia de procesamiento son requisitos clave para entrenar sus propias redes.

[05:50] A medida que seguimos aumentando nuestras fuentes de datos y añadimos potencia de procesamiento, somos capaces de entrenar sus propias redes para lograr cosas cada vez más sofisticadas. Las redes neuronales, sobresalen particularmente en el modelado con datos no estructurados como imágenes o texto, donde tenemos un número muy grande de características.

[06:11] Como resultado, han logrado realmente un rendimiento dominante en tareas como la clasificación de imágenes o el procesamiento del lenguaje natural para la generación de texto o para la traducción automática. Sin embargo, también como hemos comentado, tenemos que asegurarnos de tener cuidado con dónde y cuándo decidimos utilizar modelos de redes neuronales.

[06:33] En particular, debido a la dificultad de interpretabilidad con los modelos de redes neuronales, tenemos que pensar muy cuidadosamente antes de aplicar un modelo de red neuronal si realmente es la mejor opción para el problema que estamos intentando resolver.

