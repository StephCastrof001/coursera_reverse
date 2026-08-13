# 11-Data Preparation

- **Módulo**: [[M03 - 03-Extracting Financial Data from Unstructured Sources]]
- **Curso**: Generative AI Governance in Financial Reporting

---

## 📜 Transcripción Curada

Hola a todos, bienvenidos de nuevo. En la conferencia de hoy, presentaremos la preparación de datos. El primer paso de nuestro marco es convertir los documentos en texto legible por máquina. Esto es crucial porque sin convertir los datos no estructurados, no podemos iniciar el proceso de extracción. Para ello, confiamos en las herramientas de conversión. Esto puede incluir software especializado o bibliotecas que extraen con precisión el texto de los archivos PDF. En los casos en los que se trata de documentos escaneados, es necesario utilizar el OCR o el reconocimiento óptico de caracteres para convertir la imagen del texto en datos editables y con capacidad de búsqueda. También es esencial centrarse en la garantía de calidad durante este paso. El texto extraído debe mantener su estructura y contenido originales para garantizar que el proceso de extracción de datos sea preciso. Si el texto no está preparado correctamente, puede provocar errores en la etapa posterior. En resumen, la preparación adecuada de los datos es crucial para el éxito de todo lo que sigue. Luego, después de la conversión de texto inicial, pasamos a segmentar y refinar el texto. Este paso nos ayuda a centrarnos en la parte más relevante del documento para su extracción. Empezamos con el tipo de contenido o la comprensión del TOC. En este caso, podemos usar LalaLab para interpretar la tabla de contenido e identificar secciones específicas que probablemente contengan los datos que necesitamos. Este paso es clave para reducir nuestro enfoque a las partes más relevantes del documento. Una vez que hayamos identificado estas secciones, pasaremos al refinamiento del rango de páginas. Esto implica reducir aún más las páginas dentro de esas secciones para asegurarnos de que solo trabajamos en las páginas con más probabilidades de contener los datos de destino, lo que reduce el procesamiento innecesario. Por último, creamos un diccionario de páginas, que es esencialmente una asignación de números de página a contenido específico. Esto permite la recuperación rápida y fácil de la información relevante durante el proceso de extracción. De este modo, reducimos significativamente la cantidad de datos irrelevantes que LalaLab tiene que procesar, lo que a su vez mejora la precisión y la eficiencia del proceso de extracción. Eso es todo para la conferencia de hoy. En la próxima conferencia, presentaremos diferentes técnicas de Ingeniería de Prompts. ¡Nos vemos allí!

---

## 🧠 Enlaces y Conceptos Relacionados
- [[00_Home/MOC - Gen AI Governance]]
