---
title: "09-What ML Can and Cannot Do"
type: lesson
module: "[[M01 - What is Machine Learning]]"
tags: [lesson, ml-foundations]
---

# 🎓 09-What ML Can and Cannot Do

> **Módulo:** [[M01 - What is Machine Learning]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 09-What ML Can and Cannot Do
<!-- Módulo: 01-What is Machine Learning | Archivo: 09-What ML Can and Cannot Do.es.vtt -->

[00:05] ser realmente capaz de aplicar la máquina aprender en situaciones de la vida real. Necesitamos entender no solo cómo la tecnología funciona y cómo aplicarla, pero también tenemos que saber cuándo funciona bien y cuándo debemos aplicarla y cuándo no funciona bien, y cuando no deberíamos aplicarlo con ese fin, nos centraremos en esto lección sobre situaciones en las que el aprendizaje automático puede funcionar bien en situaciones en las que no funciona bien.

[00:37] Comencemos por discutir qué el aprendizaje automático puede funcionar bien. Y tenemos que advertir esto con el hecho que el aprendizaje automático realmente solo puede funcionar bien si se le da una cantidad suficiente y la calidad de los datos, si no tenemos suficientes datos sobre lo específico problema que estamos intentando resolver, o un dato no está limpio y tenemos muchos el ruido o los valores atípicos pesados son datos faltantes, no vamos a poder hacer que el aprendizaje automático funcione bien, aunque sea sencillo tarea sencilla.

[01:08] Así que supongamos por el momento que tenemos suficiente cantidad y calidad de datos. Algunas de las cosas que implica el aprendizaje automático es particularmente hábil para incluir la automatización de tareas sencillas, haciendo predicciones aprendiendo las relaciones de entrada y salida y personalizando servicios o productos para usuarios individuales.

[01:27] Hable un poco sobre lo que significa cada uno de ellos. En primer lugar, toda una nación de pruebas sencillas. Así que ejemplos de esto podrían ser automatización del enrutamiento del correo basado en el reconocimiento óptico de caracteres. Así que cuando un hombre llega a la oficina de correos, es clasificado y filtrado automáticamente y enviado según su ruta en función de la máquina aprendizaje que reconoce palabras y dígitos escritos a mano y puede automáticamente enrute ese correo a su destino.

[01:55] Otro ejemplo de automatización de una tarea sencilla sería toda la transcripción. Así que cuando enseño aquí en Duke, todas mis conferencias se graban el software de seminarios web que utilizamos llamado zoom. Zoom incluye una transcripción automática función para que después de cada sesión pueda recibir una transcripción escrita de mi licencia que luego puedo publicar y poner a disposición de mis alumnos.

[02:21] Algunos utilizan un modelo de aprendizaje automático subyacente las escenas para transcribir automáticamente mi discurso a texto para proporcionarme esa transcripción automática. segunda cosa. El aprendizaje automático puede funcionar particularmente bien hace predicciones mediante el aprendizaje de relaciones simples de entrada y salida.

[02:37] Ejemplos de esto podrían incluyen predecir la demanda de un producto en función de factores como la hora del día o la estación del año o la temperatura exterior. Podría incluir cosas como predecir las calificaciones de los estudiantes de mi clase en función de con qué frecuencia van a clase, ya sea que hagan sus deberes o no y los puntajes de sus exámenes a lo largo del semestre.

[03:01] Por último, la personalización para usuarios individuales. Entonces, si eres de Netflix o Suscriptor de Amazon Prime, por ejemplo, deberías estar muy familiarizado con esto. Netflix ofrece servicios personalizados recomendaciones de películas para ver para los usuarios basadas en el modelo de aprendizaje automático.

[03:16] Del mismo modo, muchos de los minoristas en línea hoy en día utilizan modelos de aprendizaje automático para recomendar productos basados en la compra en tu historial de compras y en el historial de compras de los usuarios que son similares a ti. Así que ahora hablemos de algunas de las cosas que el aprendizaje automático no puede funcionar muy bien.

[03:36] La primera es entender el contexto. Así que un buen ejemplo aquí sería ser traducción automática. Como humanos. Tenemos la capacidad de entender contexto sobre las conversaciones que tenemos. Podemos entender cuándo una oración es pretende ser una broma o cuando alguien dice algo que pretende ser sarcástico en la naturaleza versus tomado literalmente.

[03:57] Los modelos de aprendizaje automático actuales no son capaces para entender cosas como los chistes o el sarcasmo. Así que, ¡todo a la máquina! Este es un modelo de aprendizaje que se interpreta como una afirmación literal. En segundo lugar, la maquinaria no puede hacer, en particular bueno es una causalidad determinada.

[04:13] Es muy importante entender esto que el aprendizaje automático identifica patrones y correlaciones en los datos, pero no determina la causa o la causalidad de una cosa causó otra cosa. Tomemos un ejemplo de esto, podríamos demostrar que, en el transcurso de un año, las ventas de helados y los delitos violentos en realidad están relacionados, así que mientras grito, las ventas suben, los delitos violentos también aumentan.

[04:40] Este es un ejemplo de correlación entre dos cosas. Sin embargo, sería obvio que el hielo El aumento de las ventas de crema no es motivo para que aumenten los delitos violentos. Hay otras variables que entran en juego afectan a cosas como la estacionalidad y el clima. Se puede demostrar que en verano La demanda de helados aumenta, pero también los delitos violentos aumento en verano.

[05:05] Así que si tuviéramos que construir un modelo de aprendizaje automático, identificaríamos una fuerte correlación entre la venta de helados y los delitos, pero debemos tener cuidado de no malinterpretarlos esa correlación como causalidad. En tercer lugar, el aprendizaje automático no puede hacer particularmente bueno es explicar por qué suceden las cosas.

[05:24] Así que, de nuevo, aprendizaje automático identifica patrones pero no intenta explicar por qué estos patrones están ocurriendo. Puede explicar los resultados en términos de correlaciones con determinadas características de entrada. Y de nuevo, no explica por qué esto una combinación de características de entrada da como resultado una salida determinada.

[05:44] Y, por último, el aprendizaje automático es no es capaz de determinar el impacto de lo que llamamos intervenciones o posibles soluciones al problema. Tampoco es capaz de multar soluciones a un problema dado. Tomemos un ejemplo de esto, supongamos que estamos construyendo una máquina modelo de aprendizaje que predice el crimen.

[06:03] Es probable que podamos predecir con precisión el crimen teniendo en cuenta un cierto número de características diferentes, cosas como ubicación, estacionalidad y otros factores. Podríamos construir un modelo que pudiera predecir eficazmente el crimen, pero este modelo no necesariamente nos lo diría cualquier cosa sobre cómo reducir la delincuencia.

[06:23] Así, por ejemplo, si quisiéramos analizar si la promulgación de una ley que prohíba las armas en un área determinada reduciría la delincuencia, un modelo de aprendizaje automático que hemos creado, realmente no podría decírnoslo cualquier cosa sobre si esa era una solución buena o mala y cómo podría afectar eso al crimen previsto.

[06:41] Del mismo modo, nuestro modelo de aprendizaje automático no podría responder a la pregunta, ¿qué debemos hacer para reducir la delincuencia o para sugerir o proponer soluciones al problema que estamos intentando modelar?

