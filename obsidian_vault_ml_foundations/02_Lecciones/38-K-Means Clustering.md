---
title: "38-K-Means Clustering"
type: lesson
module: "[[M05 - Trees, Ensemble Models and Clustering]]"
tags: [lesson, ml-foundations]
---

# 🎓 38-K-Means Clustering

> **Módulo:** [[M05 - Trees, Ensemble Models and Clustering]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

# 38-K-Means Clustering
<!-- Módulo: 05-Trees, Ensemble Models and Clustering | Archivo: 38-K-Means Clustering.es.vtt -->

[00:04] Una vez que hemos elegido nuestra base para establecer la similitud o diferencia entre las cosas, seleccionamos un algoritmo que aplicaremos para crear nuestros conglomerados. Hoy hemos centrado nuestra discusión en lo que se denomina conglomerado K-means, que es, con diferencia, el algoritmo de conglomerado más popular.

[00:25] Pero también quiero que sea consciente de que hay muchos, muchos tipos diferentes de algoritmos que se aplican para la agrupación. Hay tantos algoritmos porque los problemas de agrupación son variados, y es importante entender para su problema específico cuál de estos algoritmos puede encajar mejor.

[00:41] Pero en caso de duda, K-means es un buen punto de partida. ¿Cómo funciona K-means? Una vez que hemos establecido la base para la similitud, ahora queremos agrupar nuestros puntos de datos en un conjunto de conglomerados. Lo primero que tenemos que hacer es elegir un número de conglomerados en K-means.

[01:01] A continuación, podemos trazar nuestros puntos de datos para poder visualizar estos grupos. Digamos que tenemos un problema en el que tenemos dos características que estamos utilizando como nuestra base para la similitud X1 y X2. Trazamos sus puntos de datos como se muestra en la diapositiva, utilizando X1 y X2 como eje.

[01:20] Nuestra intuición nos diría que los puntos de datos que están próximos entre sí deberían agruparse dentro del mismo conglomerado y los puntos de datos que están alejados entre sí sería lógico agruparlos en conglomerados diferentes. Digamos que de nuevo hemos elegido tres conglomerados.

[01:37] Podríamos localizar cada uno de estos tres conglomerados y podríamos asignar cada de estos puntos de datos al conglomerado más cercano de modo que queden organizados en tres conglomerados distintos. La cuestión clave, sin embargo, es dónde localizar cada uno de estos conglomerados y cómo asignar los puntos de datos al conglomerado.

[01:55] En el algoritmo K-means, nuestra función objetivo es minimizar la suma de las distancias de cada punto hacia el centro de su clúster asignado. De modo que cada punto de datos se asigne a el clúster con el centro más cercano a ese punto. Veamos cómo funciona esto en la práctica. Una vez que hemos seleccionado un número de conglomerados, El paso 1 consiste en seleccionar al azar las ubicaciones del centro de cada uno de esos conglomerados.

[02:26] De nuevo, hemos elegido formar tres conglomerados con nuestros datos. Elegiremos ubicaciones al azar para colocar los centros de cada uno de esos conglomerados, 1, 2 y 3, como hemos mostrado en la diapositiva. El paso 2, consiste entonces en asignar todos nuestros puntos de datos a su centro de conglomerado más cercano.

[02:44] Los puntos azules que vemos en la diapositiva se asignan al conglomerado 1 ya que son los más cercanos al centro del conglomerado 1, los puntos naranjas se asignan al conglomerado 2, y los puntos morados son los más cercanos al centro del conglomerado 3 por lo que se asignan al conglomerado 3.

[03:00] Como podemos ver, una vez que hemos asignado nuestros puntos, las ubicaciones de los centros de los clústeres que hemos elegido no son en realidad los centros de los clústeres de puntos a los que los hemos asignado. Movamos ahora esos centros a la ubicación central real o la ubicación media de los puntos de cada uno de esos clústeres.

[03:19] Moveremos las ubicaciones de los centros de nuestros conglomerados desde las ubicaciones originales elegidas al azar a los centros reales de los puntos de datos asignados a ese conglomerado. Ahora repetiremos ese proceso y volveremos a asignar puntos al centro del conglomerado más cercano, que podría permanecer igual o lo más probable es que ahora cambie ya que hemos movido las ubicaciones de los centros de los conglomerados.

[03:43] El punto en asignación cambiará porque algunos puntos se han movido ahora más cerca de otro centro de conglomerado. Asignaremos de nuevo los puntos a el centro de conglomerado más cercano y volveremos a mover los centros de conglomerado a la ubicación media real de los puntos dentro de ese conglomerado.

[04:02] Seguiremos repitiendo este proceso una y otra vez hasta que los centros de los conglomerados dejen de moverse, lo que significa que se encuentran en las ubicaciones medias reales de los puntos dentro de ese conglomerado. Una vez que hayamos encontrado esas ubicaciones medias, habremos completado nuestra asignación de conglomerados, y habremos establecido nuestros tres conglomerados y los puntos de datos dentro de cada uno.

[04:25] Una de las ventajas de K-means es que es muy fácil de implementar, converge rápidamente por lo que generalmente es rápido de ejecutar. Como resultado, generalmente es un muy buen punto de partida cuando se está trabajando con tareas de agrupación. Una de las principales desventajas de K-means es que requiere que el usuario especifique un número de conglomerados por adelantado.

[04:49] Para algunos problemas en los que estamos aplicando la agrupación, podemos tener en mente un número lógico de conglomerados a utilizar. En otros problemas, realmente no sabemos cuántos conglomerados utilizar. Generalmente lo que haremos es elegiremos diferentes números de conglomerados, ejecutaremos K-means y nos fijaremos en el que nos dé el error más bajo en términos de la distancia total entre los puntos de datos y el centro del conglomerado.

[05:17] Pero también se ajusta a nuestra intuición lógica de cuántos conglomerados lógicos podríamos esperar dado el problema que estamos intentando resolver. Otro reto de K-means es que no funciona bien para datos que son geográficamente muy complejos, es decir, un gran número de características.

[05:37] K-means crea límites lineales entre los conglomerados y por eso, en algunos casos en los que estamos tratando con datos muy complejos, con relaciones complejas entre las características, puede que queramos elegir otro tipo de agrupación que pueda darnos un mejor ajuste a nuestro problema.

