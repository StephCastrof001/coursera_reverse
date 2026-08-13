---
title: "12-Building a Model"
type: lesson
module: "[[M02 - The Modeling Process]]"
tags: [lesson, ml-foundations]
---

# 🎓 12-Building a Model

> **Módulo:** [[M02 - The Modeling Process]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 12-Building a Model
<!-- Módulo: 02-The Modeling Process | Archivo: 12-Building a Model.es.vtt -->

[00:05] En esta lección, vamos a hablar sobre el proceso de construcción de un modelo. Sin embargo, primero me gustaría situarlo, en el contexto más amplio de la resolución de problemas utilizando el aprendizaje automático. Vamos a centrarnos inicialmente en lo que se llama el proceso CRISP-DM, que es a través del proceso estándar de la industria para aplicar la ciencia de datos y el aprendizaje automático para resolver problemas.

[00:27] El proceso comienza con el paso uno que se llama Comprensión del Negocio, que se centra en tener una buena comprensión sólida de el problema que está tratando de resolver y lo que define el éxito en la solución del problema y cómo podríamos medir el éxito. El paso dos se centra en la recopilación y organización y la identificación de los datos que necesita para resolver ese problema.

[00:50] Y el paso tres, a continuación, preparamos los datos para el modelado. Paso cuatro, construimos nuestro modelo y luego seguimos evaluando nuestro modelo y finalmente desplegamos nuestro modelo final. Todo el proceso es realmente un editor de proceso en el sentido de que podemos avanzar un paso o dos, podemos descubrir o aprender cosas a medida que avanzamos y luego podemos retroceder a pasos anteriores e iterar una y otra vez.

[01:16] Aunque hoy vamos a hablar sobre todo de la modelización, que está contenida en el paso cuatro del proceso. Los esfuerzos para construir modelos empiezan realmente con el paso uno. Si no entendemos el problema que estamos intentando resolver y tenemos una idea concreta de qué es lo que hay que hacer para tener éxito en la resolución de ese problema, es imposible construir una buena modelización, no importa cuántos datos recopilemos o cuánto esfuerzo pongamos en desarrollar nuestro modelo.

[01:41] Así que el proceso de modelado en realidad comienza con ese paso uno de comprensión del negocio, asegurándonos de que realmente tenemos una comprensión firme de nuestro problema y luego continúa en todos los pasos hasta el paso para el modelado. Asegurándonos de que estamos recogiendo suficientes datos, asegurándonos de que estamos recogiendo los datos correctos y organizándolos en el conjunto correcto de características, asegurándonos de que hemos limpiado y preparado nuestros datos y, finalmente, construyendo el modelo en sí en el paso cuatro.

[02:07] Así que ahora vamos a profundizar un poco más en el paso siguiente y hablaremos de cómo creamos un modelo. Empezamos recopilando un conjunto de observaciones pasadas y los objetivos asociados. Así que utilizando el ejemplo que hemos comentado antes, nuestras observaciones pasadas serían un conjunto de casas que han estado a la venta y los valores de las características asociadas de cada una de esas casas, como el número de dormitorios o los metros cuadrados de la casa.

[02:32] Los objetivos serían el precio por el que se ha vendido esa casa. Introducimos todos esos datos en nuestro modelo en un proceso denominado entrenamiento del modelo. Entonces, ¿qué hacemos realmente cuando entrenamos el modelo? El modelo está representado por una ecuación o un conjunto de ecuaciones que relacionan la entrada las observaciones pasadas con la salida, el objetivo o el precio de venta.

[02:57] Cuando entrenamos un modelo, estamos aprendiendo o identificando los valores óptimos de los coeficientes en esa ecuación son conjunto de ecuaciones que define la relación óptima entre las características de entrada y el objetivo de salida. Una vez que definimos esa relación expresada a través de una ecuación o conjunto de ecuaciones, podemos utilizar ese modelo y podemos introducir en el modelo nuevos datos, en este caso nuevas casas y los valores de las características asociadas de esas nuevas casas.

[03:28] Y como salida será capaz de hacer una predicción del precio de venta esperado para cada una de esas nuevas casas. En la lección anterior, hablamos de los cuatro componentes de un modelo. Así que ahora vamos a traerlos de vuelta y ver dónde entran. El primer componente del modelo fue la selección de características.

[03:48] Así que esto se hace en las fases previas de recopilación y preparación de nuestros datos a través de un proceso llamado selección de características e ingeniería de características. Y el objetivo de ese proceso es identificar qué características de nuestros datos en este caso, qué características de una casa tienen el mayor impacto o el mayor valor en términos de poder predecir el valor objetivo o el precio de venta.

[04:13] A medida que empezamos a construir nuestro modelo, entonces tenemos que tomar decisiones sobre qué algoritmo queremos utilizar. Hay muchos algoritmos diferentes de aprendizaje automático y hablaremos de algunos de esos algoritmos y expondremos sus lecciones. Puede pensar en un algoritmo como una plantilla para la ecuación o la relación que sigue el modelo para relacionar la entrada con la salida.

[04:35] Una vez que hemos elegido la plantilla, no tenemos un conjunto de parámetros individuales asociados con esa plantilla y podemos ajustar o afinar estos parámetros. Así que piense en estos como diales en nuestro algoritmo que podemos sintonizar o un poco para hacer que el modelo funcione un poco mejor o un poco peor dependiendo de la dirección en la que giramos estos hiper marrones.

[04:58] Hay en términos de predicción de la salida. Y, finalmente, el cuarto componente fue definir una pérdida o a veces llamada función de coste. Y utilizamos nuestra función de pérdida como una forma de evaluar el rendimiento de nuestro modelo a medida que vamos construyendo el propio modelo.

[05:13] Así que a medida que elegimos el algoritmo a medida que seleccionamos las características que queremos utilizar para un modelo a medida que afinamos o tuiteamos esos valores de nuestros hiperparámetros. Utilizamos la función de coste para que nos diga si estamos moviendo las cosas en una dirección positiva o si en realidad estamos empeorando las cosas.

[05:29] Así que ahora vamos a recapitular todo el proceso de modelado. Y el proceso comienza con la recopilación de los datos que creemos que necesitamos para resolver nuestro problema y construir un modelo. Y luego tenemos que seleccionar las características de los datos que vamos a utilizar como parte de nuestro modelo.

[05:46] A continuación, elegimos un algoritmo que actúa como una plantilla para definir la relación entre la entrada, las observaciones, cada una de las cuales tiene un conjunto de características que hemos identificado y el valor objetivo de salida. Una vez que hemos elegido nuestra plantilla o el algoritmo que vamos a utilizar, establecemos los valores de los hiperparámetros.

[06:08] Entrenamos nuestro modelo utilizando las observaciones pasadas que hemos recogido y los valores objetivo. Y evaluamos el rendimiento de nuestro modelo. Y lo importante a tener en cuenta es que este proceso no es un simple proceso lineal. Este proceso es en realidad altamente iterativo en el sentido de que pasaremos por estos pasos, evaluaremos el rendimiento de nuestro modelo bien atrás y haremos cambios.

[06:31] Por ejemplo, podemos ajustar el conjunto de características que decidimos utilizar. Podemos probar un nuevo algoritmo. Podemos ajustar los hiperparámetros que estamos utilizando volver a entrenar y luego evaluar de nuevo hasta que estemos contentos con el resultado final y satisfechos con el rendimiento del modelo que hemos desarrollado.

