# 13-Batch Querying and Database Construction

- **Módulo**: [[M03 - 03-Extracting Financial Data from Unstructured Sources]]
- **Curso**: Generative AI Governance in Financial Reporting

---

## 📜 Transcripción Curada

Hola a todos, bienvenidos de nuevo a nuestra conferencia. En la conferencia de hoy, presentaremos las colas por lotes con LLM y la construcción de bases de datos. Una vez que nuestras instrucciones estén elaboradas, el siguiente paso es automatizar el proceso de hacer cola. Así es como lo hacemos. En primer lugar, la integración de funciones. Empezamos por incorporar las indicaciones en una función de Python, lo que nos permite reutilizar y aplicar las mismas instrucciones en varios documentos. A continuación, el uso de la API. Con la API del LLM, podemos procesar de manera eficiente varios documentos a la vez. Esto acelera el proceso de extracción, especialmente cuando se trata de grandes conjuntos de datos. Por último, en bucle. Configuramos un bucle para iterar sobre cada documento. Esto garantiza que todos los documentos del conjunto de datos se procesen de manera coherente y automatizada. Al automatizar este proceso, reducimos significativamente el esfuerzo manual y garantizamos la coherencia en la forma en que se extraen los datos en todo el conjunto de datos. Una vez extraídos los datos, el siguiente paso crucial es organizarlos para su uso posterior, como la limpieza de datos. Esto implica convertir el valor extraído en tipos de datos apropiados, como números o fechas, y abordar los valores faltantes o incompletos para garantizar la integridad de los datos. Selección de bases de datos. Elegimos el sistema de base de datos que mejor se adapta a nuestras necesidades. Podría ser una base de datos SQL para datos estructurados y un almacenamiento más flexible. La selección de la base de datos depende del tipo de datos y de cómo se utilizarán. Almacenamiento de datos. Una vez limpiados, los datos se cargan en la base de datos seleccionada. En este caso, es importante configurar las claves e índices adecuados, lo que ayudará a realizar consultas y recuperaciones de forma eficiente. Al almacenar los datos extraídos de forma estructurada, facilitamos el análisis y la generación de informes, lo que permite una toma de decisiones más informada. Eso es todo para la conferencia de hoy. En la próxima conferencia, presentaremos una aplicación real del uso de este marco en el informe financiero integral anual de los gobiernos locales. ¡Nos vemos allí!

---

## 🧠 Enlaces y Conceptos Relacionados
- [[00_Home/MOC - Gen AI Governance]]
