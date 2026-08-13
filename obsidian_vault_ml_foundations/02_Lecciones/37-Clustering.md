---
title: "37-Clustering"
type: lesson
module: "[[M05 - Trees, Ensemble Models and Clustering]]"
tags: [lesson, ml-foundations]
---

# 🎓 37-Clustering

> **Módulo:** [[M05 - Trees, Ensemble Models and Clustering]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 37-Clustering
<!-- Módulo: 05-Trees, Ensemble Models and Clustering | Archivo: 37-Clustering.es.vtt -->

[00:03] Ahora centraremos nuestra atención al aprendizaje no supervisado. En concreto, un no supervisado técnica de aprendizaje llamada agrupamiento. ¿Qué es la agrupación en clústeres? La agrupación en clústeres es una técnica para organizar los datos en grupos lógicos sin usar etiquetas de grupo explícitas.

[00:22] La diferencia clave entre el aprendizaje no supervisado y la agrupación en clústeres y la el aprendizaje supervisado que estudiábamos antes es ese ahora no tenemos acceso a las etiquetas de salida ni a los valores objetivo para usar en el entrenamiento de un modelo. Cuando estudiábamos clasificación y regresión y nuestra supervisada técnicas de aprendizaje, pudimos utilizar los valores de entrada y los valores de salida de observaciones pasadas para entrenar un modelo para relacionar los la entrada y la salida.

[00:53] En el aprendizaje no supervisado, no tenemos acceso a cualquier valor de salida. Nuestro objetivo es organizar los insumos en grupos o conglomerados lógicos de tal forma que los puntos de datos de entrada similares se agrupen en el mismo conglomerado, y los puntos de datos de entrada que son muy diferentes entre sí deberían estar dentro grupos diferentes o clústeres diferentes.

[01:18] Hay muchos ejemplos de agrupamiento que se encuentran en el mundo que nos rodea. Un ejemplo está en genética para inferir estructuras de población utilizando similitudes y datos genéticos. Cuando organizamos a los animales en diferentes tipos de animales, reptiles, anfibios, mamíferos, etc., no hay ninguna lista maestra en el universo que diga que este es un mamífero y este es un reptil.

[01:43] Nosotros organizamos estos las cosas nosotros mismos observando las similitudes en genética y características entre animales para organizarlos en grupos lógicos. Otro ejemplo común de agrupamiento se encuentra en marketing, donde estamos dividiendo clientes potenciales de un producto en diferentes segmentos objetivo para que podamos crear y aplicar diferentes técnicas de marketing para cada una de nuestras diferentes segmentos objetivo.

[02:10] Podríamos definir nuestros segmentos objetivo basados en la ubicación geográfica o datos demográficos, o si han comprado productos nuestros anteriores o no. Hay muchos diferentes formas de organizar a los clientes potenciales para un producto basado en qué características que elegimos.

[02:28] Del mismo modo, no hay una regla de oro ni un maestro organización que dice que este cliente pertenece al Grupo 1 y este cliente pertenece al Grupo 2. Definimos esto para nosotros mismos lo mejor que podamos, basándonos en la explotación similitudes y diferencias entre el potencial clientes que tenemos que organizarlos en grupos lógicos.

[02:52] Otro común ejemplo de agrupamiento es la aplicación de agrupar los documentos de texto. Supongamos que estamos construyendo una aplicación que organiza los artículos de noticias diarios que publicamos encuentra en las noticias todos los días una serie de diferentes fuentes de noticias en un conjunto de las más temas importantes del día para que podamos dígale a nuestro usuario cuáles son los temas más importantes por los que debe pagar atención al día de hoy.

[03:20] Una vez más, aquí, cada artículo de noticias que encontramos no tiene algún artículo específico etiqueta preexistente que dice Este artículo trata sobre el tema A o este artículo trata sobre el tema B. Examinamos el texto de cada artículo. Entonces podemos agrupar artículos que tienen textos similares a las características de tratar el mismo tema.

[03:47] La decisión clave que que tenemos que tomar cuando aplicamos la agrupación el problema es, ¿cómo vamos a determinar si algo es similar a otra cosa o diferente a otra cosa. ¿Qué base vamos a utilizar para evaluar la similitud? Tomemos un ejemplo en la diapositiva aquí. Tenemos dos imágenes.

[04:09] Una imagen muestra un vaso de zumo de manzana, la otra imagen muestra un vaso de cerveza. Dependiendo de nuestro basándonos en la similitud, podríamos argumentar que estas cosas son o muy similares entre sí o muy diferentes entre sí. Supongamos nuestra base para establecer la similitud era el color.

[04:30] Podríamos mirar estos y dicen: bueno, ambos son de color dorado. Estas cosas son muy similares. Deberían estar dentro el mismo grupo. Si tuviéramos que mirar estos cosas y digo, bueno, ambos son líquidos Si alguien bebe y, por lo general, lo sirve frío , también podríamos decir que sí, estas cosas son muy similares entre sí.

[04:51] Deberían estar en el mismo se agrupan entre sí. Sin embargo, digamos que en su lugar de color o tipo de objeto, que elegimos usar como ingredientes base de similitud. Obviamente, manzana el jugo y la cerveza están hechos de muy diferentes ingredientes. Si esa fuera nuestra base para calculando la similitud, podríamos ponerlos en diferentes racimos, diciendo que zumo de manzana contiene una lista de ingredientes que es muy diferente de lo que contiene la cerveza.

[05:20] Entendiendo nuestro base para calcular la similitud o la diferencia entre dos cosas es realmente la decisión clave que debemos tomar cuando presentamos la solicitud agrupamiento en un problema.

