---
title: "05-Introduction to Machine Learning"
type: lesson
module: "[[M01 - What is Machine Learning]]"
tags: [lesson, ml-foundations]
---

# 🎓 05-Introduction to Machine Learning

> **Módulo:** [[M01 - What is Machine Learning]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 05-Introduction to Machine Learning
<!-- Módulo: 01-What is Machine Learning | Archivo: 05-Introduction to Machine Learning.es.vtt -->

[00:04] Empecemos por lo básico. En primer lugar, ¿qué es aprendizaje automático? Arthur Samuel, un ingeniero de IBM, definió por primera vez el aprendizaje automático en 1959 como un campo de estudio que otorga a las computadoras la capacidad de aprender sin ser programado explícitamente.

[00:21] La idea principal aquí es eso en lugar de proporcionar a una computadora con datos exactos instrucciones para resolver un problema, mostramos los ejemplos del problema a resolver y dejamos que la computadora averigüe por sí misma cómo resolver el problema. Me gustaría dar un ejemplo es, digamos, que nos gustaría entrenar a un modelo para reconozco las hamburguesas.

[00:40] En el método tradicional de programar computadoras, proporcionaríamos instrucciones explícitas a la computadora sobre qué una hamburguesa es. Le decimos a la computadora una hamburguesa se compone de dos bollos con uno más oscuro una hamburguesa en el medio, posiblemente tendrá un trozo de queso o lechuga encima.

[00:58] Es una hamburguesa. Usar el aprendizaje automático, en lugar de proporcionar la computadora con cualquier instrucción o definición de lo que es una hamburguesa, simplemente mostraríamos la computadora muchas, muchas imágenes de hamburguesas diferentes. Con el tiempo, el la computadora podría aprender por sí misma y reconoce una hamburguesa.

[01:18] Vamos ahora a echar un vistazo en la diferencia entre cómo un el software tradicional genera predicciones y cómo el aprendizaje automático genera predicciones. Con lo tradicional en los sistemas de software, tomamos un conjunto de entradas datos y un conjunto de reglas que proporcionamos al sistema de software, que el sistema puede entonces se usa para generar nuevos resultados.

[01:42] En el anterior ejemplo de clasificación de una imagen de un alimento como hamburguesa o no, alimentaríamos a nuestros sistema de software: un conjunto de datos o imágenes de entrada de comida en este caso, y un conjunto de reglas sobre qué constituye una hamburguesa. El sistema sería entonces poder aplicar esas reglas para identificar si cada imagen de los datos de entrada era una hamburguesa o no una hamburguesa.

[02:10] Vamos ahora a echar un vistazo sobre cómo el aprendizaje automático resolvería este problema. Con los sistemas de aprendizaje automático, proporcionamos los datos de entrada y un conjunto de salidas anteriores. El modelo de aprendizaje automático luego descubre por sí mismo las reglas o patrones detrás de lo que constituye una hamburguesa.

[02:29] Luego puede usar estos patrones o reglas de autoaprendizaje para clasificar los nuevos datos de entrada como hamburguesa o no hamburguesa. Una pregunta común lo que vemos es cuál es la diferencia entre inteligencia artificial y aprendizaje automático? La inteligencia artificial es el amplio campo de tratar de replicar aspectos del ser humano la inteligencia en las máquinas. El aprendizaje automático puede considerarse como un subconjunto de lo artificial inteligencia, que se centra en un conjunto de métodos y herramientas para ayudar a alcanzar los objetivos del campo de la tecnología artificial inteligencia.

[03:07] Otro término común, el aprendizaje profundo, se puede definir como un subcampo dentro de un ámbito más amplio campo del aprendizaje automático. El aprendizaje profundo es centrado en el uso de un aprendizaje automático específico modelo llamado red neuronal para lograr la objetivos del aprendizaje automático.

[03:24] Por último, tenemos otros subcampos más pequeños centrado en realizar tareas específicas utilizando aprendizaje automático o posiblemente aprendizaje profundo, como la computadora visión para detectar objetos e imágenes o procesamiento del lenguaje natural. Por último, los sistemas de recomendación , como el tipo de sistemas que puede ver en los sitios web de productos de su tienda favorita que ofrecen servicios personalizados recomendaciones para ti.

[03:49] Vamos a cubrir un tema muy breve historia del campo de la inteligencia artificial y aprendizaje automático. Los orígenes de la máquina el aprendizaje en realidad se remonta a principios del siglo XIX. Cosas como lo mínimo regresión de cuadrados o teorema de Bayes o algoritmos de aprendizaje automático, que en realidad son todavía en uso hoy en día, y sus orígenes se remontan a los principios estadísticos descubiertos y publicados a principios del siglo XIX.

[04:16] El campo de la IA era realmente se lanzó y el término IA se acuñó en el años 40 y 50. Eso empezó en 1943 con la propuesta de un modelo artificial simple de una neurona que existen en el cerebro. Esa neurona se extendió entonces a la idea o al concepto de una red neuronal completa a principios de la década de 1950.

[04:42] Sin embargo, a finales En la década de 1960 y principios de la de 1970, mucha gente en todas partes el gobierno y la investigación científica se habían desilusionado con este campo. Se promocionó durante los años 50 y 60 con el significativo el progreso que se logró. El campo, lamentablemente, no pudo estar a la altura de los nobles expectativas que se establecieron.

[05:05] Como resultado, se recortaron los fondos y el aprendizaje automático y los investigadores de IA cambiaron su atención a otra parte. Entre finales de los 70 y los 80, la investigación volvió a elegir y muchos de los algoritmos que existen más comúnmente utilizado hoy en día, tanto en el campo más amplio de aprendizaje automático, así como específicos al campo del aprendizaje profundo o al uso de redes neuronales, se desarrollaron a través del finales de los 80 y los 90.

[05:32] Finalmente, en la década de 2000, a partir de 2009 hasta el día de hoy, hemos vivido lo que se denomina el boom del aprendizaje profundo. La atención del El campo más amplio del aprendizaje automático realmente tiene centrado en la aplicación del aprendizaje profundo o neuronal redes para lograr tareas increíblemente difíciles que antes eran considerado imposible.

[05:54] Lo hemos hecho tremendamente progreso en los últimos 15 años más o menos en aplicar el aprendizaje profundo. Hablemos un poco más sobre el aprendizaje automático y dónde lo es como un campo hoy en día. El aprendizaje automático se ha convertido en una parte omnipresente de nuestro mundo.

[06:10] Como consumidores, podemos interactuar con la máquina modelos de aprendizaje docenas de veces al día a través de una variedad de productos y sistemas diferentes que interactuamos con. A menudo ni siquiera lo sabemos que estamos interactuando con un modelo de aprendizaje automático o una tecnología de IA en segundo plano.

[06:26] La popularidad de el aprendizaje automático, en particular, en los últimos tiempos, se debe a un par de los factores principales. El primero es que ha habido una explosión en la cantidad de datos que tenemos acceso a. Eso ha sido impulsado por lo ubicuo Conectividad a Internet a la que ahora estamos conectados a más y más personas, ordenadores e incluso dispositivos.

[06:49] Hemos visto avances drásticos en la tecnología de sensores que nos permiten recolectar cantidades masivas cantidades de datos de muchos sensores diferentes tipos. Finalmente, nuestros propios dispositivos se han convertido inteligentes y conectados, lo que significa que son capaces de producir datos sobre su entorno, sobre nosotros y sobre nuestro uso, todos los cuales pueden usarse para construir máquinas modelos de aprendizaje.

[07:11] En segundo lugar, el campo de las profundidades el aprendizaje o el uso de redes neuronales tiene hizo cosas que anteriormente se consideraban imposible, ahora posible. Los principales impulsores de eso tienen ha habido un aumento masivo en la computación poder, en particular, a través de lo que se llama unidades de procesamiento gráfico, que se utilizan para entrena una máquina muy grande y muy compleja modelos de aprendizaje.

[07:34] En segundo lugar, hemos visto cómo científicos, investigadores y otras personas que trabajan en el mundo académico y empresarial se han esforzado por reunir enormes conjuntos de lo que se denomina datos etiquetados, que están disponibles para la formación a gran escala, modelos muy complejos.

[07:51] En tercer lugar, hemos tenido avances significativos y algorítmicos, que nos han permitido construir máquinas innovadoras arquitecturas de aprendizaje para realizar tareas muy difíciles. Echemos un vistazo un poco más información sobre dónde encontramos el aprendizaje automático en nuestro mundo actual.

[08:10] Un ejemplo común del aprendizaje automático está en las recomendaciones de productos. Si vas al sitio web de tu tienda favorita o tienda en línea, o si quieres escuchar una canción o verla en una película, por lo general, interactúas con una recomendación de producto basada en la IA un sistema que aprende sobre ti y tu personalidad preferencias y luego es capaz de proporcionar recomendaciones personalizadas.

[08:35] Otro ejemplo de máquina El aprendizaje en nuestro mundo actual son los filtros de spam para clientes de correo electrónico, que son capaces de distinguir entre los mensajes reales que hemos recibido, frente a mensajes de spam. Se logra el enrutamiento del correo que nos llega a casa mediante el uso del aprendizaje automático mediante lo que se llama reconocimiento óptico de caracteres para reconocer tanto los dígitos como los escritos a mano letras y palabras en sobres y ayudan al servicio postal a conseguir nuestras envíenos un correo a casa.

[09:07] Por último, cosas como el crédito La detección de fraudes con tarjetas se realiza mediante máquinas algoritmos de aprendizaje, identificación y distinción entre los patrones normales de gasto y cuando existe la posibilidad probable de fraude con tarjetas de crédito.

