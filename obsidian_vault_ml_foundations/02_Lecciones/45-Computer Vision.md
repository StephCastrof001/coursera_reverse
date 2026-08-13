---
title: "45-Computer Vision"
type: lesson
module: "[[M06 - Deep Learning and Course Project]]"
tags: [lesson, ml-foundations]
---

# 🎓 45-Computer Vision

> **Módulo:** [[M06 - Deep Learning and Course Project]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 45-Computer Vision
<!-- Módulo: 06-Deep Learning & Course Project | Archivo: 45-Computer Vision.es.vtt -->

[00:04] Una de las principales áreas en las que se utiliza el aprendizaje profundo es en el análisis de imágenes o contenidos de vídeo, lo que se denomina visión por ordenador. La visión por ordenador es un área compleja. Y por eso hoy vamos a ofrecer una introducción muy breve a algunos de los temas clave.

[00:22] Empecemos por comprender las tareas comunes que se encuentran en el campo de la visión por ordenador. Hay muchas cosas diferentes que podemos hacer con las imágenes, pero algunas de las tareas más comunes que queremos llevar a cabo son la clasificación de imágenes, la detección de objetos e imágenes, la segmentación de porciones de imágenes en diferentes clases y la generación de imágenes.

[00:47] La clasificación de imágenes se centra en clasificar una imagen o un vídeo en una de varias clases. Ejemplos comunes de ello serían el reconocimiento facial, que clasifica imágenes de rostros de personas en una clase asociada a su nombre. Otro ejemplo común en nuestro mundo actual es el reconocimiento óptico de caracteres, que consiste en clasificar imágenes de dígitos o letras por el dígito o letra asociado a esa imagen.

[01:22] Un ejemplo de clasificación de imágenes que se encuentra en la diapositiva es un modelo que puede clasificar las radiografías de pulmón en función de la enfermedad que tenga alguien. Así que utiliza la imagen para detectar si hay una enfermedad presente, y si es así qué enfermedad, y luego clasifica la imagen o esa radiografía por la enfermedad que esté presente.

[01:46] Otro ejemplo de visión por ordenador es la detección de objetos. Así que en la detección de objetos, no sólo estamos tratando de clasificar una imagen basada en lo que hay en la imagen, pero lo que está tratando de detectar dónde están los objetos dentro de una imagen en particular.

[02:02] Puede haber un objeto en una imagen o puede haber múltiples objetos que se encuentran en una imagen. Así que nuestro trabajo aquí es un poco más complicado. No sólo tenemos que identificar lo que esos objetos en particular son, pero también tenemos que identificar dónde se encuentran dentro de la imagen.

[02:19] Así que, como podemos ver en un ejemplo en la diapositiva, tenemos una imagen que muestra muchos objetos y hemos identificado dónde están los objetos de qué clase son, si es un ordenador portátil o una silla, por ejemplo. Y luego hemos dibujado un cuadro que llamamos cuadro delimitador alrededor de la imagen alrededor del objeto para localizarlo dentro de la imagen.

[02:42] Un ejemplo del uso de la detección de objetos podría ser para los coches autoconducidos. Una tarea importante que tenemos que llevar a cabo es la identificación de ciclistas o peatones en la carretera. Queremos identificar no sólo si es un peatón o clasificar qué objeto es, sino también en qué lugar del campo de visión se encuentra ese peatón en relación con el coche.

[03:07] Una tarea similar en visión por ordenador es lo que llamamos segmentación semántica. En este caso, nuestra misión es intentar clasificar no sólo toda la imagen en una de las múltiples clases, sino intentar clasificar cada píxel individual dentro de una imagen en función de la clase a la que pertenece.

[03:26] Un ejemplo que ilustra esto podría ser construir un modelo que sea capaz de generar una representación precisa de un hueso a partir de una imagen médica que contenga tejido y hueso. Quizá queramos entender la forma o las medidas de ese hueso. Y por eso es importante que comprendamos exactamente dónde están los bordes de ese hueso en relación con el tejido circundante.

[03:50] Así que en este caso el enfoque de detección de objetos de dibujar una simple caja alrededor de ese hueso no va a ser realmente suficiente. Queremos saber exactamente dónde están esos bordes. Por lo tanto, tenemos que intentar etiquetar cada píxel individual de esa imagen como hueso o tejido.

[04:07] Un último ejemplo de tareas de visión por ordenador es la generación de imágenes. En realidad, podemos utilizar redes de aprendizaje profundo denominadas redes generativas adversariales o gans para abreviar, para generar imágenes basadas en datos de entrenamiento. La imagen que vemos en la pantalla no es en realidad una imagen de una mujer real, pero es una que ha sido generada por la red Ganz.

[04:29] Vemos este tipo de acercamiento a las noticias mucho hoy en día en lo que se llama deep fakesm o utilizando Ganz, o redes de aprendizaje profundo para generar imágenes artificiales o incluso videos enteros. Ahora que hemos entendido algunas de las aplicaciones comunes de la visión por ordenador, vamos a hablar un poco más acerca de cómo funciona esto en realidad.

[04:52] Como sabemos por lo que hemos aprendido hasta ahora, para introducir una entrada en un modelo, tenemos que convertirla en un conjunto de características con valores numéricos. ¿Cómo lo hacemos para una imagen o un vídeo? Podemos utilizar el color de cada uno de los píxeles de una imagen, que se representa con un número como característica individual.

[05:20] En realidad, los píxeles se codifican en función de su color y el tipo más común de codificación es lo que se denomina RGB o codificación rojo, verde, azul. Con la codificación RGB, cada píxel tiene un conjunto de tres valores que están en una escala de 0 a 255, que representan la cantidad de rojo, verde y azul que se encuentra en ese píxel.

[05:43] Podemos utilizar cada uno de estos tres valores para cada píxel de nuestra imagen como el conjunto de características para entrenar los modelos. Así que para un ejemplo sencillo, si tenemos una imagen que es de 10 por 10, lo que significa 10 píxeles por 10 píxeles, tendríamos 100 valores de características.

[06:01] Y en cada una de esas características, tenemos tenemos tenemos tres valores que representan la cantidad de rojo, verde y azul que se encuentra en ese píxel. Así que en la diapositiva, tenemos una imagen de SUV. Las imágenes de 1080 píxeles por 1920 píxeles, lo que significa 1080 filas por 1920 columnas.

[06:26] Si nos fijamos en el valor de cada uno de esos píxeles individuales dentro de nuestra imagen, vemos que tenemos tres valores que llamamos canales en visión por ordenador, de nuevo, que representan la cantidad de rojo, verde o azul dentro de esa imagen individual. Así que si miramos el píxel situado en la parte superior izquierda de nuestra imagen, veríamos que tiene valores de canal de 214, 197 y 205.

[06:53] Cuando trabajemos con modelos en visión por ordenador, primero traduciremos nuestra imagen a sus valores de píxel individuales y a los tres canales para cada valor de píxel. Una vez que tengamos estos valores numéricos, podremos introducirlos en un modelo. Uno de los retos de trabajar con imágenes es que podemos tener muchas, muchas, muchas características en su imagen dependiendo del número de píxeles que podamos tener.

[07:19] Podemos tener miles de características. En el enfoque de red neuronal que hemos utilizado hasta ahora, cada una de las características de entrada estaba conectada por un peso a cada uno de los nodos de la capa siguiente. Si tenemos miles y miles de características, esto significa que en cada capa de nuestra red tenemos muchos miles o a veces incluso millones de pesos diferentes que necesitamos entrenar.

[07:44] Así que muy rápidamente, el número de pesos en nuestra red puede llegar a ser extremadamente grande, lo que haría muy difícil entrenar una red de este tipo. El enfoque que hemos discutido hasta ahora en el modelado de su propia red se llama capas totalmente conectadas. De nuevo, cada valor de la capa anterior está conectado de alguna manera a cada valor de la capa siguiente o las capas están totalmente conectadas entre sí.

[08:13] Dado que tenemos tantas características y tantos pesos potenciales en nuestro modelo de red neuronal cuando trabajamos con imágenes, en lugar de utilizar capas totalmente conectadas en nuestra red, utilizamos otros dos tipos de capas denominadas capas convolucionales y capas de agrupación.

[08:30] Así que veamos con más detalle cómo funciona cada uno de estos tipos de capas. Las capas convolucionales utilizan un filtro deslizante que contiene pesos y aplican este filtro de pesos a todo el conjunto de entrada. Así que cada nodo de una capa está conectado sólo a un subconjunto limitado de nodos.

[08:49] En la capa anterior, los filtros que utilizamos contienen un conjunto de pesos compartidos que definen las conexiones entre las distintas capas. Así que en la anterior, totalmente conectada en sus propias redes con las que estábamos trabajando cada nodo de una capa estaba conectado a cada nodo de la capa siguiente por un peso individual.

[09:12] En el caso de las capas convolucionales, los nodos están conectados sólo a un subconjunto limitado de los nodos anteriores y los pesos que definen esas conexiones son un conjunto de pesos comunes. Debido a esto tenemos un número mucho menor de pesos que realmente necesitamos aprender.

[09:31] Veamos un ejemplo de cómo funciona esto. Supongamos que tenemos una imagen de entrada que está organizada en una matriz y que tiene un conjunto de tres canales que representan el rojo, el verde y el azul. Definimos un filtro, un filtro de 3 por 3 que es nuestro conjunto de pesos compartidos para aplicar a la imagen de entrada.

[09:51] Empezamos en la parte superior izquierda de nuestra imagen, tomamos los valores de nuestros canales para cada uno de esos píxeles multiplicados por los valores de nuestro filtro. Multiplicamos nuestro filtro de 3 por 3 por el conjunto de píxeles de 3 por 3 de la parte superior izquierda y sumamos el resultado para calcular un único valor, en este caso, 3.

[10:19] A continuación, nos desplazamos una columna y aplicamos nuestros valores de filtro a la siguiente sección de 3 por 3 de nuestra imagen. Multiplicamos nuestros valores de filtro por los valores de canal para esa sección de píxeles de 3 por 3. Y sumamos el resultado y de nuevo calculamos un único valor para la suma, que en este caso es 2.

[10:42] Repetimos este proceso una y otra vez hasta que hayamos llegado al final o a la parte inferior derecha de nuestra imagen. De esta forma hemos reducido un conjunto muy grande de características ahora a un conjunto mucho más pequeño de características que llamamos mapa de características.

[10:56] En una red neuronal convolucional, aplicamos esta capa de convolución muchas veces una y otra vez. Cada capa en la que aplicamos esta convolución acaba entonces siendo capaz de reconocer ciertos patrones dentro de su imagen. En las primeras capas que ejecutan su propia red, estos patrones son patrones muy básicos a medida que avanzamos en nuestra red.

[11:21] Los patrones que cada capa convolucional se encarga de identificar se vuelven cada vez más complejos y cada vez más parecidos a la clasificación final de salida que estamos intentando conseguir. Entre las capas convolucionales, aplicamos una capa que se denomina capa de agrupación.

[11:40] La capa de agrupación es una forma sencilla de reducir aún más la dimensionalidad. Así que tomamos una sección, digamos una sección de 3 por 3 de una capa y podemos aplicar mean pulling o max pooling por ejemplo donde tomamos el valor medio de esa sección de 3 por 3 o el valor máximo dentro de esa sección de 3 por 3.

[12:00] Y utilizamos ese único valor como representación de toda esa sección de 3 por 3, por lo tanto pasando de 3 por 3 o 9 valores a un único valor. Y reduciendo la dimensionalidad para mantener el número de pesos que tenemos que entrenar dentro de nuestra red a un nivel razonable configurar y entrenar una red neuronal convolucional desde cero es una tarea difícil.

[12:27] A menudo aplicaremos nuestro mecanismo de aprendizaje por transferencia utilizando un modelo preentrenado y luego ajustándolo con precisión a la tarea específica que estamos intentando conseguir. La gran mayoría de los modelos utilizados para la visión por ordenador se entrenan en un gran conjunto de datos llamado ImageNet.

[12:46] ImageNet consta de más de 14 millones de imágenes que están organizadas en 20.000 categorías lanzadas originalmente por Fei-Fei Li y su equipo de Stanford. Y es muy habitual que los nuevos modelos de redes neuronales que se utilizan para la visión por ordenador se preentrenen en este conjunto de datos ImageNet para reconocer las 20.000 categorías.

[13:08] Entonces podemos simplemente cargar uno de estos modelos preentrenados, cortamos el par de capas finales, y construimos y entrenamos un nuevo conjunto de capas finales utilizando un conjunto de datos mucho más pequeño que específico para la tarea que estamos tratando de lograr. Así que en el caso de clasificar imágenes de rayos X en diferentes enfermedades pulmonares, podríamos tener un conjunto de datos del orden de miles o cientos de miles en lugar de millones de imágenes de rayos X.

[13:41] Podemos afinar el entrenamiento de nuestro par de capas finales utilizando el conjunto de datos más pequeño de imágenes adicionales y las etiquetas asociadas para cada imagen. Y luego podemos combinar ese conjunto final de capas sobre nuestra red preentrenada existente para obtener un modelo que ahora es capaz de identificar o clasificar imágenes de rayos X en qué enfermedad está presente.

