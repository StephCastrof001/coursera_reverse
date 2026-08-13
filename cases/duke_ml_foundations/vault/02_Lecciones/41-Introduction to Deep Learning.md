---
title: "41-Introduction to Deep Learning"
type: lesson
module: "[[M06 - Deep Learning and Course Project]]"
tags: [lesson, ml-foundations]
---

# 🎓 41-Introduction to Deep Learning

> **Módulo:** [[M06 - Deep Learning and Course Project]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 41-Introduction to Deep Learning
<!-- Módulo: 06-Deep Learning & Course Project | Archivo: 41-Introduction to Deep Learning.es.vtt -->

[00:04] Para entender el aprendizaje profundo, empecemos por comprender los orígenes del término red neuronal. La red neuronal es una compleja red de neuronas en el cerebro, que trabajan juntas para realizar cálculos complejos. En 1943, un neuropsicólogo, Warren McCulloch, y un matemático, Walter Pitts, trabajan juntos para introducir un modelo computacional de cómo funcionan realmente estas neuronas individuales en el cerebro.

[00:35] A las dendritas de una neurona llegan múltiples señales. Cuando las señales llegan a través de las dendritas, se suman en el cuerpo celular. Y si la señal acumulada supera algún umbral, la neurona se dispara, lo que significa que se activa, y emite una señal de salida. Es importante entender que una neurona individual en el cerebro realmente no puede hacer mucho.

[01:02] Pero cuando se conectan a las miles de otras neuronas del cerebro, estas redes neuronales pueden lograr cálculos muy complejos. Del mismo modo, fue propuesto por McCulloch, Pitts a principios de la década de 1940. Las complejas redes de neuronas artificiales podían lograr cálculos muy complejos, y aproximarse a funciones muy complejas.

[01:28] Una red neuronal que contiene muchas capas se denomina red neuronal profunda , que es el origen del término aprendizaje profundo. Así pues, echemos un vistazo a la historia de las redes neuronales. Después de la propuesta original de McCulloch, Pitts en los años 40 que realmente lanzó una era de investigación temprana en el campo de las redes neuronales.

[01:51] Los investigadores, y los científicos hicieron grandes progresos a lo largo de los años 40, y los años 50 cuando el primer modelo de una neurona artificial fue propuesto por Rosenblatt. Y poco después, los investigadores de Stanford, Woodrow y Hoff propusieron la primera red neuronal que funcionó con éxito.

[02:13] Uno de los retos que frenó la investigación durante este periodo de tiempo, fue que los investigadores realmente no tenían una gran forma de entrenar con éxito grandes redes complejas de neuronas. Los avances en la década de 1980 condujeron a grandes avances como la técnica de lo que se denomina retropropagación.

[02:34] Que es un método para entrenar redes neuronales complejas que contienen múltiples capas. En la década de 1980, sin embargo, los avances se han frenado debido a la falta tanto de disponibilidad de datos como de potencia informática. Y realmente no fue hasta principios de la década de 2000 cuando la potencia de cálculo se puso al día.

[02:55] Y cuando dispusimos de cantidades suficientemente grandes de datos que utilizar, para entrenar redes neuronales cada vez más profundas. A medida que los modelos de redes neuronales se hacían cada vez más profundos, con más neuronas, organizándose en más capas, la potencia de estas redes en términos de lograr cálculos muy complejos, siguió creciendo.

[03:16] Y como resultado en los últimos años, hemos visto un auge en el campo del aprendizaje profundo. Donde grandes y potentes redes neuronales están siendo ahora utilizadas para lograr una amplia variedad de tareas muy complejas. Hay una serie de factores clave que han propiciado este reciente auge en el uso del aprendizaje profundo.

[03:35] El primero, y probablemente el más importante, es que la cantidad de datos que ahora están disponibles para el entrenamiento de grandes redes neuronales complejas ha crecido exponencialmente. Una de las cosas importantes que hay que recordar sobre las redes neuronales, es que requieren cantidades muy, muy grandes de datos para entrenarse con éxito.

[03:53] Y realmente sólo ha sido en la última década o dos que tenemos suficientes datos que se ponen a nuestra disposición, a través de una variedad de fuentes como ordenadores, dispositivos conectados, sensores omnipresentes. Pero también nos hemos tomado el tiempo, y puesto en el esfuerzo por los científicos, y investigadores, e ingenieros para organizar, y etiquetar todos estos datos.

[04:18] De una manera que puedan ser consumidos para el entrenamiento de redes neuronales. El poder computacional también ha alcanzado el estado en que se encuentran en términos de diseño de algoritmos. Y eso ha permitido arquitecturas de redes neuronales mucho más profundas y mucho más complejas de lo que antes podíamos lograr.

[04:38] Los investigadores también han hecho grandes avances en términos de los propios algoritmos. Hay algunas limitaciones inherentes a la arquitectura de una red neuronal. Y los avances recientes han superado en gran medida varias de estas limitaciones. Como resultado, hoy en día, las redes neuronales se pueden encontrar realmente a nuestro alrededor en el mundo en una amplia variedad de aplicaciones diferentes.

[05:05] Echemos un vistazo a un par de aplicaciones representativas de las redes neuronales. La primera sería para la clasificación de imágenes, y el reconocimiento de imágenes. Por ejemplo, cuando usted toma una foto de alguien en su teléfono, y la sube a Facebook. Y Facebook etiqueta automáticamente esa foto con el nombre de un amigo.

[05:25] Para ello, utiliza un modelo de red neuronal que ha sido incorporado, y entrenado para reconocer las fotos de sus amigos para permitir esta automatización. Otra aplicación del aprendizaje profundo se encuentra en lo que se denomina traducción automática neuronal . Los sitios web y las aplicaciones de traducción automática son capaces de utilizar tipos complejos, y específicos de modelos de redes neuronales para traducir muy fácilmente de un lado a otro entre un número muy grande de idiomas.

[05:57] Las aplicaciones del aprendizaje profundo en el espacio de la atención sanitaria están realmente en los muy primeros días. Existe un enorme potencial de aplicación de sus propias redes dentro de la sanidad. Impulsado por la gran cantidad de datos sanitarios que recoge nuestro sistema sanitario sobre los pacientes.

[06:18] Uno de los primeros avances en el uso de modelos de aprendizaje profundo en el espacio sanitario fue el uso de redes neuronales como modelo predictivo, para predecir la aparición de sepsis dentro de los pacientes de la UCI. Sólo utilizan modelos automatizados para predecir la aparición de la sepsis basándose en señales fisiológicas procedentes de sensores.

[06:37] Permite a los médicos y enfermeras de la UCI gestionar mejor y cuidar de forma proactiva a los pacientes con alto riesgo de aparición de sepsis. Veamos un último ejemplo de aplicación innovadora del aprendizaje profundo. Una de las principales cadenas de pizzas aquí en EE.UU., está utilizando un modelo de aprendizaje profundo de visión por ordenador para realizar el control de calidad de las pizzas que salen de sus hornos, en los restaurantes.

[07:02] En lugar de que los empleados humanos tengan que realizar el control de calidad de las pizzas. Utilizan una cámara conectada con el modelo de aprendizaje profundo para realizar el control de calidad. Buscando cosas como la proporción de queso y salsa en la pizza. Si la pizza tiene los ingredientes adecuados, que el cliente ha pedido realmente.

[07:22] Si el número de pepperoni en la pizza está a la altura del número estándar, que se supone que deben poner en la pizza. De esta manera son capaces de automatizar ese proceso de control de calidad. Y utilizar a sus empleados humanos para tareas más sofisticadas dentro del restaurante.

[07:40] Si pensamos en los ejemplos que acabo de presentar, podríamos ver un par de temas comunes en términos de dónde sobresale realmente el aprendizaje profundo. Una de estas cosas, es que necesitamos grandes cantidades de datos de entrenamiento, para entrenar con éxito modelos de aprendizaje profundo para realizar tareas desafiantes.

[08:02] El segundo tema que observamos, es que el aprendizaje profundo realmente sobresale en aplicaciones en las que tenemos un número muy grande de características. Por ejemplo, en datos no estructurados cuando estamos tratando con texto, o estamos tratando con imágenes, o vídeo. Tenemos un número muy, muy grande de características en el caso de la clasificación de imágenes.

[08:24] Por ejemplo, podemos tener imágenes, y cada píxel individual dentro de esa imagen representa una característica separada. Así que si tenemos por ejemplo, 5x12 píxeles por 5x12 píxeles, estamos tratando con miles de características potenciales. Y aquí es donde las aplicaciones de aprendizaje profundo realmente pueden brillar.

[08:47] Número tres, es que las aplicaciones de aprendizaje profundo son capaces de hacerlo muy bien cuando tenemos relaciones complejas entre las características de entrada, y el objetivo. Donde de nuevo, tenemos muchas características de entrada, y tenemos relaciones no lineales complejas entre las características, y los objetivos.

[09:04] Las redes de aprendizaje profundo son capaces, dados los datos suficientes, de aprender esas relaciones complejas. Por último, es importante señalar que las aplicaciones de aprendizaje profundo generalmente tienen una baja preocupación por la explicabilidad. Uno de los retos que discutiremos más adelante sobre el uso de redes neuronales, es que a menudo se consideran cajas negras.

[09:26] Porque son tan complejas con tantas ecuaciones. Que es realmente difícil de entender cómo en su propia red se llega a una predicción de salida. Como resultado, generalmente centramos su uso en aplicaciones específicas. Donde no necesariamente necesitamos presentar a los usuarios una sofisticada explicación de cómo la máquina llegó a su predicción.

[09:51] Así que para cosas como, etiquetado de imágenes con los nombres de sus amigos, o contar el número de queso pepperoni en la pizza. Por lo general, esto no es realmente una preocupación, porque la interpretabilidad, y la explicabilidad no son realmente un factor clave en este tipo de aplicaciones.

[10:11] Si estamos pensando en construir modelos para ejemplo para determinar si los solicitantes a una escuela de posgrado son aceptados. O si alguien es aprobado para un préstamo que ha solicitado, por ejemplo. Estas son aplicaciones con grandes apuestas para los usuarios, y también como resultado una gran necesidad de interpretabilidad, y explicabilidad.

[10:34] Y por lo tanto este tipo de aplicaciones, tenemos que ser realmente cuidadosos con el uso de redes neuronales.

