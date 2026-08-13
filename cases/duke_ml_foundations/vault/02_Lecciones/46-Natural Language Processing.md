---
title: "46-Natural Language Processing"
type: lesson
module: "[[M06 - Deep Learning and Course Project]]"
tags: [lesson, ml-foundations]
---

# 🎓 46-Natural Language Processing

> **Módulo:** [[M06 - Deep Learning and Course Project]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 46-Natural Language Processing
<!-- Módulo: 06-Deep Learning & Course Project | Archivo: 46-Natural Language Processing.es.vtt -->

[00:04] Otra área de aplicación muy común del aprendizaje profundo es en el procesamiento del lenguaje natural o el análisis de texto. Echemos un vistazo a algunas de las aplicaciones comunes del procesamiento del lenguaje natural o PNL. La clasificación de texto implica utilizar características del texto para clasificarlo, ya sea en una clasificación binaria o en una clasificación multiclase.

[00:33] Un ejemplo podría ser la detección de mensajes de spam. Se trata, obviamente, de una clasificación binaria en la que un mensaje de correo electrónico que usted recibe es spam o no spam. Nuestro trabajo aquí es utilizar aspectos del texto de ese correo electrónico para clasificarlo como spam o no spam.

[00:53] Otro ejemplo podría ser la clasificación de artículos de noticias en categorías. Digamos que estamos creando una aplicación para revisar artículos de noticias de muchas fuentes a diario y queremos clasificar automáticamente todos esos artículos en la categoría pertinente, como deportes, negocios, política, etc.

[01:16] De nuevo, utilizaríamos los aspectos de los textos junto con el modelo de procesamiento del lenguaje natural para analizar el texto y clasificarlo en la categoría correcta. Otra aplicación popular del procesamiento del lenguaje natural es lo que llamamos análisis de sentimientos. En el análisis de sentimientos normalmente estamos revisando un texto ya sea una sola frase o un artículo más largo o una crítica como la de una película e intentando clasificar cuál es el sentimiento de ese texto ya sea positivo o negativo.

[01:54] Digamos que somos un analista financiero que trabaja para una gran empresa financiera y estamos construyendo un programa para analizar automáticamente el sentimiento de los consumidores sobre una empresa concreta que estamos investigando y ver cómo cambia el sentimiento de un consumidor sobre esa empresa y sus productos a diario.

[02:13] Para ello, revisamos los tweets sobre esa empresa y para cada tweet intentamos clasificar si ese tweet es positivo o negativo. A continuación, podemos utilizar la suma de los tweets positivos y negativos para ver cómo evoluciona el sentimiento sobre la empresa y sus productos día a día a medida que suceden las cosas.

[02:36] La búsqueda es otra aplicación común del procesamiento del lenguaje natural. Una aplicación de búsqueda tradicional utilizaría una simple búsqueda por palabras clave. Todos nosotros deberíamos estar muy familiarizados con esto. Por ejemplo, si tuviéramos que buscar en nuestro ordenador un archivo específico necesitamos poner una palabra clave que esté contenida en el nombre de ese archivo para que un ordenador encuentre ese archivo.

[03:00] El procesamiento del lenguaje natural también puede utilizarse para construir mecanismos de búsqueda más sofisticados. Tomemos un ejemplo de una de las cosas en las que estoy trabajando actualmente, construir una aplicación de respuesta a preguntas para estudiantes que están aprendiendo a programar por primera vez.

[03:17] Un estudiante podría hacer una pregunta sobre cómo hacer algo en programación. Digamos que un estudiante quisiera calcular el valor medio de una lista de números. Podrían hacer una pregunta como, ¿cómo calcular el valor medio de una lista de números? Digamos que, tenemos un conjunto de respuestas a diferentes preguntas pero la respuesta particular a esta pregunta está almacenada en la otra categoría, cómo calcular el valor medio de una lista de conjunto de números.

[03:49] Sabemos como humanos que media y promedio pueden significar lo mismo pero el ordenador no necesariamente lo sabe. Si realizáramos una simple búsqueda por palabras clave utilizando media es posible que no encontráramos esta respuesta correcta. Sin embargo, si utilizamos aplicaciones de procesamiento del lenguaje natural para construir un modelo un poco más sofisticado y que pueda comprender el significado de las palabras deberíamos ser capaces de encontrar muy fácilmente esta respuesta a la pregunta del estudiante.

[04:18] La traducción automática es una aplicación emergente del procesamiento del lenguaje natural y este es un caso en el que los modelos de aprendizaje profundo son muy superiores a cualquier otro tipo de modelo de aprendizaje automático. Google Translate es un gran ejemplo de esto o cualquier aplicación que pueda traducir entre idiomas.

[04:38] Digamos que estamos construyendo una aplicación que toma frases en inglés que alguien podría escribir y luego traduce automáticamente esas frases al español. Por último, también podemos utilizar el procesamiento del lenguaje natural para generar texto. Supongamos que estamos construyendo una aplicación que lee automáticamente sus correos electrónicos y crea respuestas automatizadas a esos correos.

[05:04] Es capaz de utilizar los textos de un correo electrónico para buscar preguntas que alguien ha formulado y generar una respuesta automatizada, creando realmente textos para usted para ahorrarle tiempo y tener que responder a preguntas sencillas que recibe a través del correo electrónico.

[05:18] ¿Cómo trabajamos con texto en el modelado? De nuevo, las entradas a los modelos tienen que estar en forma numérica utilizando un conjunto de características con valores numéricos. Nuestro primer paso es traducir el texto en un conjunto de características numéricas. Esto puede suponer un reto porque los textos pueden tener muchos enlaces.

[05:40] Podemos estar analizando frases de distinta longitud o documentos que contienen varios números de frases, así que no es tan sencillo como trabajar con otras formas de datos. Hay tres formas principales de representar el texto de manera que podamos introducirlo en modelos. La primera y más tradicional es utilizar el vocabulario o el conjunto de palabras que se encuentran dentro de cada frase o cada documento.

[06:06] Este enfoque se denomina enfoque de bolsa de palabras. Un método más reciente de representar el texto como valores numéricos es creando lo que llamamos incrustaciones donde representamos palabras en documentos enteros asignando valores numéricos que intentan captar el significado de las palabras contenidas en un documento y el enfoque más reciente para trabajar con texto y modelar texto utilizando aprendizaje profundo es utilizando lo que llamamos atención y esto es se encuentra en un conjunto de modelos que se llaman transformadores.

[06:46] Vamos a ver un poco cómo funciona esto en realidad. Empecemos con el enfoque más tradicional de bolsa de palabras. Supongamos que tenemos dos reseñas de películas. La reseña 1 y la reseña 2 sobre la misma película, pero de usuarios muy diferentes que tenían perspectivas muy distintas sobre la película.

[07:05] Veamos ahora cómo podríamos traducir estas dos simples reseñas en valores numéricos que luego podríamos utilizar para modelar. Empezaríamos el enfoque de la bolsa de palabras definiendo un vocabulario. El vocabulario sería el conjunto de palabras contenidas en todos los documentos que estamos modelando.

[07:24] En este ejemplo tan sencillo, nuestro conjunto de documentos son dos reseñas, cada una una sola frase y por tanto nuestro vocabulario es bastante pequeño. Si observamos el conjunto de palabras que contiene una u otra de nuestras reseñas, es bastante pequeño. La película fue lo mejor, larga, y aburrida, es ese conjunto de palabras que se encuentran en esas dos reseñas.

[07:51] El siguiente paso es tomar cada una de esas reseñas y mapearla en el vocabulario. Tomamos cada palabra del conjunto de vocabulario, y contamos cuántas veces esa palabra está presente en cada una de nuestras reseñas. Si miramos la reseña 1, vemos que la palabra la está presente dos veces en esa reseña.

[08:11] Película está presente una vez, era está presente una vez, mejor está presente una vez, y luego nuestras palabras restantes no se encuentran en absoluto. Del mismo modo, hacemos lo mismo para la reseña 2. Ahora podemos ver que tenemos un conjunto de puntos de datos que representan cada una de nuestras reseñas.

[08:33] Para cada uno de esos puntos de datos, tenemos un conjunto de características representadas por cada una de las palabras dentro de nuestro vocabulario. Tenemos un valor numérico que representa el recuento o el número de veces que esa palabra se encuentra dentro de cada una de nuestras reseñas.

[08:48] Uno de los retos de este enfoque es que, a medida que nuestro vocabulario crece mucho, podemos acabar teniendo enormes matrices de valores para nuestras características. Un enfoque más moderno es intentar capturar el significado de las palabras y frases de forma numérica. En lugar de limitarse a contar el número de veces que se encuentra una palabra determinada dentro de una frase o un documento sin tomar las palabras de una frase y convertirlas en vectores numéricos que llamamos incrustaciones, que intentan captar el significado de esa palabra.

[09:25] Las incrustaciones van a tener diferentes longitudes. Pero normalmente pueden ser algo como 50 valores o 300 valores. Donde ese conjunto de 300 valores está capturando el significado de una palabra dada. Cada palabra tendría un conjunto asociado diferente de esos 300 valores. Hay dos enfoques principales para crear incrustaciones.

[09:47] El primero, llamado word2vec fue popularizado en 2013 por Google y el segundo surgió un año después de Stanford llamado Glove. Normalmente, estos métodos para calcular incrustaciones no son algo que tenga que hacer usted mismo. Puede aprovechar el gran trabajo realizado anteriormente por estos equipos de investigadores que han preentrenado modelos para crear incrustaciones utilizando grandes conjuntos de texto, como Wikipedia, Google News o Twitter.

[10:20] Veamos un modelo visual realmente sencillo de lo que podría ser una incrustación. De nuevo, estas incrustaciones tendrían en las otras 50 o 300 características. Pero veamos una incrustación simple de dos características. Podemos visualizar una incrustación de dos características en dos ejes y tracemos un par de palabras.

[10:39] Podemos ver que tenemos tres palabras aquí, aprender, estudiar y dormir. Esperaríamos que los valores de incrustación para aprender y estudiar fueran muy similares entre sí, ya que el significado de esas palabras es muy similar. Sin embargo, los valores de incrustación para la palabra dormir son bastante diferentes.

[10:56] Puesto que el significado de la palabra dormir de nuevo es bastante diferente al de las otras dos palabras. Un enfoque emergente para el procesamiento del lenguaje natural que ha demostrado ser extremadamente potente es lo que se llama el transformador. El transformador se ha convertido realmente en los últimos dos años en el modelo dominante para el modelado de secuencias de texto para tareas como la generación de texto o la traducción automática.

[11:26] Los transformadores utilizan una forma más sofisticada de convertir el texto en un conjunto de características numéricas. Empiezan utilizando las incrustaciones de palabras, como acabamos de ver. Pero también añaden lo que se denomina una codificación posicional, intentando dar cuenta de la posición en la que se encuentra una palabra dentro de una frase.

[11:44] Porque la posición en la que se encuentra esa palabra tiene cierto impacto en el significado de esa palabra individual y su relación con las demás palabras de una frase. Por último, el ingrediente clave y realmente novedoso del modelo transformador es lo que se denomina atención. La atención, dicho de forma muy sencilla, es una medida de la fuerza con la que se relacionan las palabras dentro de una frase, independientemente de su posición.

[12:12] A veces, palabras que están bastante alejadas en una frase siguen estando fuertemente relacionadas, aunque sus posiciones en la frase sean muy diferentes. Pongamos un ejemplo sencillo. Tenemos una frase, "El chico no estudió para el examen porque estaba demasiado cansado". Como humanos que leemos esa frase, sabemos que él está fuertemente relacionado con la palabra chico, aunque estén en posiciones muy diferentes dentro de la frase.

[12:39] Un ordenador lo sabrá automáticamente. La forma en que los transformadores son realmente capaces de lograr estos poderosos resultados es a través de este mecanismo de atención, que es capaz de relacionar palabras dentro de una frase independientemente de qué posición ocupen dentro de cada frase.

[12:59] Al relacionar las palabras, el ordenador es realmente capaz de empezar a entender el contexto de las frases de una forma mucho mejor.

