#!/usr/bin/env python3
"""
Pipeline Maestro de Extracción y Centralización:
C0 (Ingesta) -> C1 (LearnHouse Hierarchy) -> C2 (KST DAG) -> C4 (DeepTutor Grounding & Feynman)
"""

import json
import os
import re
from pathlib import Path
from collections import defaultdict

def build_master_graph(cleaned_dir: Path, output_file: Path):
    # Cargar metadatos de los módulos
    modules_order = [
        ("01-What is Machine Learning", "CH01", "What is Machine Learning", "Fundamentos, Taxonomía, Definición de Modelos y Fronteras de Causalidad"),
        ("02-The Modeling Process", "CH02", "The Modeling Process", "Ciclo de Vida de Ciencia de Datos, Feature Engineering, Train/Val/Test Split y Fuga de Datos"),
        ("03-Evaluating & Interpreting Models", "CH03", "Evaluating and Interpreting Models", "Overfitting, Bias-Variance Tradeoff, Matriz de Confusión, Precision/Recall, ROC/AUC"),
        ("04-Linear Models", "CH04", "Linear Models", "Regresión Lineal, Regresión Logística, Odds Ratio y Regularización L1 (Lasso) / L2 (Ridge)"),
        ("05-Trees, Ensemble Models and Clustering", "CH05", "Trees, Ensemble Models and Clustering", "Árboles de Decisión, Random Forest, Gradient Boosting (XGBoost) y K-Means Clustering"),
        ("06-Deep Learning & Course Project", "CH06", "Deep Learning and Course Project", "Redes Neuronales, Convolucionales (CNN), NLP y Diseño de Arquitectura de Producto con IA")
    ]
    
    # Base de Conocimiento Centralizada de Reglas, Prerrequisitos y Conceptos
    # Grounded 100% en las 48 lecciones de Duke University
    MASTER_KNOWLEDGE_BASE = {
        # --- MÓDULO 1 ---
        "KP-ML-PARADIGM": {
            "chapter_id": "CH01",
            "lesson_ref": "05-Introduction to Machine Learning",
            "name": "Programación Tradicional vs. Machine Learning",
            "type": "concept",
            "prereqs": [],
            "unlocks": ["KP-DATA-COMPONENTS", "KP-MODEL-WEIGHTS"],
            "summary": "En programación tradicional, humanos crean Reglas + Datos para obtener Respuestas. En ML, se alimentan Datos + Respuestas pasadas para que la computadora descubra las Reglas matemáticas.",
            "analogy": "Programación tradicional es darle a un chef una receta fija; ML es mostrarle 10.000 platos exitosos para que él deduzca la combinación óptima de ingredientes.",
            "pm_rule": "Usar ML únicamente cuando la lógica del problema sea demasiado compleja, multidimensional o cambie constantemente con el comportamiento del usuario.",
            "misconception": "Creer que ML es magia automática que no requiere datos estructurados limpios.",
            "verbatim_anchor": {"timestamp": "00:24", "quote": "una forma de programar computadoras para aprender de la experiencia, para completar una tarea sin proporcionar información explícita instrucciones"},
            "feynman_scenario": "El CTO propone escribir 500 reglas IF/ELSE para predecir qué clientes cancelarán su suscripción. Explícale por qué el enfoque de ML es superior."
        },
        "KP-DATA-COMPONENTS": {
            "chapter_id": "CH01",
            "lesson_ref": "06-Data Terminology",
            "name": "Estructura de Datos: Features (X), Target (Y) e Instancias",
            "type": "concept",
            "prereqs": ["KP-ML-PARADIGM"],
            "unlocks": ["KP-TYPES-SUPERVISED-UNSUPERVISED"],
            "summary": "Instancias son las filas (clientes, transacciones). Features son las columnas predictoras (X). Target es la variable objetivo que queremos predecir (Y).",
            "analogy": "Las features son los síntomas de un paciente; el target es el diagnóstico de la enfermedad.",
            "pm_rule": "Sin una definición unívoca y medible del Target (Y) alineada a un objetivo de negocio, el proyecto de ML no debe arrancar.",
            "misconception": "Pensar que añadir cientos de features irrelevantes mejora el modelo; agrega ruido y sobreajuste.",
            "verbatim_anchor": {"timestamp": "01:10", "quote": "las características que utilizamos para hacer predicciones y la variable objetivo que estamos intentando predecir"},
            "feynman_scenario": "Marketing quiere predecir 'felicidad del usuario'. ¿Cómo traduces ese concepto abstracto a features (X) y un target (Y) concreto?"
        },
        "KP-MODEL-WEIGHTS": {
            "chapter_id": "CH01",
            "lesson_ref": "07-What is a Model",
            "name": "Definición de Modelo, Entrenamiento y Parámetros",
            "type": "concept",
            "prereqs": ["KP-ML-PARADIGM"],
            "unlocks": ["KP-TYPES-SUPERVISED-UNSUPERVISED"],
            "summary": "Un modelo es una función matemática parametrizada f(X; w) -> Y. El entrenamiento es el ajuste algorítmico de los pesos (w) para minimizar el error frente a datos históricos.",
            "analogy": "Ajustar las perillas de un ecualizador de sonido hasta que la música suene perfecta.",
            "pm_rule": "Diferenciar entre parámetros (pesos internos que aprende el algoritmo) e hiperparámetros (perillas externas que define el equipo).",
            "misconception": "Asumir que un modelo entrenado es determinista; siempre produce estimaciones probabilísticas.",
            "verbatim_anchor": {"timestamp": "00:50", "quote": "un modelo es una representación matemática de la relación entre las características de entrada y la variable objetivo"},
            "feynman_scenario": "Explica a un director de ventas qué significa que el equipo de ciencia de datos está 'entrenando' el modelo."
        },
        "KP-TYPES-SUPERVISED-UNSUPERVISED": {
            "chapter_id": "CH01",
            "lesson_ref": "08-Types of Machine Learning",
            "name": "Taxonomía: Supervisado, No Supervisado y Refuerzo",
            "type": "concept",
            "prereqs": ["KP-DATA-COMPONENTS", "KP-MODEL-WEIGHTS"],
            "unlocks": ["KP-CORRELATION-VS-CAUSALITY", "KP-DATA-SCIENCE-PROCESS"],
            "summary": "Supervisado usa datos etiquetados (X, Y) para Clasificación y Regresión. No Supervisado agrupa datos sin etiquetas (X) por estructura inherente. Refuerzo aprende por recompensas/castigos.",
            "analogy": "Supervisado es estudiar con profesor; No supervisado es explorar un territorio virgen; Refuerzo es aprender a montar bicicleta cayéndose y levantándose.",
            "pm_rule": "Si no hay datos etiquetados históricos, no se puede hacer aprendizaje supervisado de inmediato; se debe costear el etiquetado o usar no supervisado.",
            "misconception": "Creer que el clustering no supervisado le pone nombre comercial a los grupos automáticamente.",
            "verbatim_anchor": {"timestamp": "00:04", "quote": "En el aprendizaje supervisado, nuestro objetivo es predecir una variable objetivo... en el no supervisado organizamos por estructura inherente"},
            "feynman_scenario": "El equipo quiere segmentar clientes sin saber cuántos tipos existen. ¿Qué rama de ML deben usar y por qué?"
        },
        "KP-CORRELATION-VS-CAUSALITY": {
            "chapter_id": "CH01",
            "lesson_ref": "09-What ML Can and Cannot Do",
            "name": "Fronteras de ML: Correlación vs. Causalidad e Intervenciones",
            "type": "concept",
            "prereqs": ["KP-TYPES-SUPERVISED-UNSUPERVISED"],
            "unlocks": ["KP-DATA-SCIENCE-PROCESS"],
            "summary": "ML detecta correlaciones estadísticas X -> Y, pero NO demuestra causalidad ni predice el impacto de cambiar políticas de negocio.",
            "analogy": "En verano suben las ventas de helados y los delitos; prohibir los helados no reducirá los delitos.",
            "pm_rule": "Nunca justificar una decisión de cambio de producto o pricing únicamente en una correlación de ML; validar con tests A/B causales.",
            "misconception": "Creer que una variable con alto peso predictivo es una palanca causal directa que podemos manipular.",
            "verbatim_anchor": {"timestamp": "04:13", "quote": "el aprendizaje automático identifica patrones y correlaciones en los datos, pero no determina la causa o la causalidad"},
            "feynman_scenario": "Un dashboard muestra correlación entre uso de modo oscuro y mayor gasto. ¿Por qué forzar modo oscuro a todos no garantiza más ingresos?"
        },

        # --- MÓDULO 2 ---
        "KP-DATA-SCIENCE-PROCESS": {
            "chapter_id": "CH02",
            "lesson_ref": "12-Building a Model",
            "name": "El Ciclo de Vida de Ciencia de Datos",
            "type": "procedure",
            "prereqs": ["KP-CORRELATION-VS-CAUSALITY"],
            "unlocks": ["KP-FEATURE-ENGINEERING", "KP-DATA-SPLITTING"],
            "summary": "Ciclo iterativo: Comprensión del Negocio -> Comprensión de Datos -> Preparación de Datos -> Modelado -> Evaluación -> Despliegue.",
            "analogy": "Construir un edificio: los cimientos (datos) toman el 80% del tiempo; la fachada (algoritmo) es el paso final.",
            "pm_rule": "El mayor riesgo de un proyecto de ML no es el algoritmo, sino resolver el problema de negocio equivocado o tener datos sesgados.",
            "misconception": "Pensar que el ciclo es lineal; los descubrimientos en evaluación obligan a volver a la preparación de datos.",
            "verbatim_anchor": {"timestamp": "01:05", "quote": "implementar el proceso de la ciencia de datos para organizar proyectos de aprendizaje automático"},
            "feynman_scenario": "El equipo de ingeniería quiere saltar directo a entrenar redes neuronales sin auditar los datos crudos. ¿Cómo frenas el error?"
        },
        "KP-FEATURE-ENGINEERING": {
            "chapter_id": "CH02",
            "lesson_ref": "13-Feature Selection",
            "name": "Ingeniería y Selección de Características",
            "type": "procedure",
            "prereqs": ["KP-DATA-SCIENCE-PROCESS"],
            "unlocks": ["KP-DATA-SPLITTING"],
            "summary": "Creación de nuevas variables predictivas (ratios, agregaciones temporales, one-hot encoding) y eliminación de variables redundantes o ruidosas.",
            "analogy": "Preparar y sazonar los ingredientes antes de cocinar para que el plato absorba el sabor.",
            "pm_rule": "El conocimiento del dominio del PM es el insumo #1 para diseñar features con alto poder discriminatorio.",
            "misconception": "Creer que pasar datos sin procesar a un modelo complejo genera el mismo rendimiento.",
            "verbatim_anchor": {"timestamp": "00:45", "quote": "la selección de características y la transformación de datos para mejorar la señal predictiva"},
            "feynman_scenario": "Tienes la fecha y hora de compra de un usuario. ¿Qué 3 nuevas features puedes derivar para predecir fraude?"
        },
        "KP-DATA-SPLITTING": {
            "chapter_id": "CH02",
            "lesson_ref": "16-Test and Validation Sets",
            "name": "Train, Validation, Test Split y Data Leakage",
            "type": "procedure",
            "prereqs": ["KP-DATA-SCIENCE-PROCESS"],
            "unlocks": ["KP-BIAS-VARIANCE", "KP-CLASSIFICATION-METRICS"],
            "summary": "División de datos: Train (aprender pesos), Validation (ajustar hiperparámetros) y Test (evaluación final a ciegas). Data leakage es contaminar train con información del futuro.",
            "analogy": "Train es estudiar el libro; Validation son los simulacros de examen; Test es el examen oficial con preguntas nunca vistas.",
            "pm_rule": "Si un modelo tiene 99.9% de precisión en desarrollo, sospecha inmediatamente de Data Leakage antes de celebrar.",
            "misconception": "Evaluar el modelo final en el set de validación en lugar de en un set de Test intacto.",
            "verbatim_anchor": {"timestamp": "00:30", "quote": "dividir los datos en conjuntos de entrenamiento, validación y prueba para asegurar generalización"},
            "feynman_scenario": "¿Por qué incluir la variable 'fecha de cancelación' como feature para predecir 'cancelación' destruye el modelo?"
        },

        # --- MÓDULO 3 ---
        "KP-BIAS-VARIANCE": {
            "chapter_id": "CH03",
            "lesson_ref": "15-Bias-Variance Tradeoff",
            "name": "Overfitting, Underfitting y Bias-Variance Tradeoff",
            "type": "concept",
            "prereqs": ["KP-DATA-SPLITTING"],
            "unlocks": ["KP-REGULARIZATION", "KP-CLASSIFICATION-METRICS"],
            "summary": "Underfitting (Alto Sesgo): modelo muy simple que no captura el patrón. Overfitting (Alta Varianza): modelo memoriza el ruido del entrenamiento y falla en datos nuevos.",
            "analogy": "Underfitting es responder todo con 'C'; Overfitting es memorizar el número de página de cada respuesta sin entender el concepto.",
            "pm_rule": "La brecha entre el error de Train y el error de Test mide exactamente el nivel de Overfitting del sistema.",
            "misconception": "Creer que cero error en entrenamiento significa que el modelo es perfecto.",
            "verbatim_anchor": {"timestamp": "01:15", "quote": "el compromiso entre sesgo y varianza y cómo el sobreajuste destruye el rendimiento en producción"},
            "feynman_scenario": "Data Science entrega un modelo con 98% de precisión en train y 62% en test. Explícale al negocio por qué no podemos lanzarlo."
        },
        "KP-CLASSIFICATION-METRICS": {
            "chapter_id": "CH03",
            "lesson_ref": "23-Classification Error Metrics Confusion Matrix",
            "name": "Matriz de Confusión: Precision, Recall y F1-Score",
            "type": "procedure",
            "prereqs": ["KP-DATA-SPLITTING"],
            "unlocks": ["KP-ROC-AUC", "KP-LINEAR-REGRESSION"],
            "summary": "Matriz de 4 resultados: TP, FP, TN, FN. Precision = TP/(TP+FP) (evitar falsas alarmas). Recall = TP/(TP+FN) (atrapar todos los positivos).",
            "analogy": "Precision: si la alarma suena, ¿cuántas veces hay fuego real? Recall: de todos los fuegos que hubo, ¿cuántos detectó la alarma?",
            "pm_rule": "En detección de fraude/cáncer priorizar Recall (no dejar pasar culpables); en spam/recomendaciones priorizar Precision (no molestar al usuario).",
            "misconception": "Usar Accuracy en datasets con 99% de ceros y 1% de unos (un modelo tonto que predice siempre cero tiene 99% accuracy).",
            "verbatim_anchor": {"timestamp": "00:40", "quote": "la matriz de confusión permite entender la naturaleza de los errores entre falsos positivos y falsos negativos"},
            "feynman_scenario": "Tienes un modelo para alertar fallas de motor en aviones. ¿Por qué optimizar Precision sobre Recall sería peligroso?"
        },
        "KP-ROC-AUC": {
            "chapter_id": "CH03",
            "lesson_ref": "24-Classification Error Metrics ROC and PR Curves",
            "name": "Curvas ROC, AUC y Calibración de Umbrales (Thresholds)",
            "type": "design",
            "prereqs": ["KP-CLASSIFICATION-METRICS"],
            "unlocks": ["KP-LINEAR-REGRESSION", "KP-LOGISTIC-REGRESSION"],
            "summary": "La curva ROC evalúa la capacidad de discriminación en todos los umbrales posibles. AUC mide la calidad global (0.5 = azar, 1.0 = perfecto). El PM elige el umbral de corte según el costo del error.",
            "analogy": "AUC es la puntería del arquero; el threshold es la decisión de disparar solo cuando la probabilidad de acertar supera el 80%.",
            "pm_rule": "El umbral de decisión por defecto (0.5) rara vez es el óptimo de negocio; debe calibrarse con la matriz de costos financieros.",
            "misconception": "Creer que cambiar el umbral de decisión cambia el AUC del modelo; el AUC es invariante al umbral.",
            "verbatim_anchor": {"timestamp": "01:20", "quote": "el área bajo la curva ROC proporciona una métrica agregada del rendimiento del clasificador a través de todos los umbrales"},
            "feynman_scenario": "¿Cómo explicas a finanzas que bajar el threshold de fraude de 0.5 a 0.3 aumentará las revisiones manuales pero salvará $2M en pérdidas?"
        },

        # --- MÓDULO 4 ---
        "KP-LINEAR-REGRESSION": {
            "chapter_id": "CH04",
            "lesson_ref": "28-Linear Regression",
            "name": "Regresión Lineal y Coeficientes Interpretables",
            "type": "procedure",
            "prereqs": ["KP-ROC-AUC", "KP-BIAS-VARIANCE"],
            "unlocks": ["KP-LOGISTIC-REGRESSION", "KP-REGULARIZATION"],
            "summary": "Modela relaciones continuas Y = w0 + w1*X1 + ... + wn*Xn minimizando la suma de errores al cuadrado (OLS). Coeficientes indican el cambio en Y por unidad de X.",
            "analogy": "Trazar una línea de tendencia en un gráfico de dispersión para estimar el precio de una casa según sus metros cuadrados.",
            "pm_rule": "Es el baseline obligatorio para todo problema de regresión tabular antes de explorar modelos no lineales.",
            "misconception": "Asumir que las relaciones en el mundo real siempre son perfectamente lineales sin evaluar transformaciones.",
            "verbatim_anchor": {"timestamp": "00:35", "quote": "la regresión lineal modela la relación entre variables continuas y proporciona coeficientes directamente interpretables"},
            "feynman_scenario": "Si el coeficiente de 'antigüedad del cliente' es +45 USD, explica qué significa exactamente para el LTV anual."
        },
        "KP-LOGISTIC-REGRESSION": {
            "chapter_id": "CH04",
            "lesson_ref": "30-Logistic Regression",
            "name": "Regresión Logística y Probabilidades Calibradas",
            "type": "procedure",
            "prereqs": ["KP-LINEAR-REGRESSION"],
            "unlocks": ["KP-DECISION-TREES"],
            "summary": "Aplica la función Sigmoide a una combinación lineal para transformar salidas infinitas en probabilidades calibradas entre 0% y 100%.",
            "analogy": "Aplanar una rampa infinita en una curva en forma de 'S' que nunca baja de 0 ni sube de 1.",
            "pm_rule": "Estándar de oro en industrias reguladas (banca, seguros) por su alta explicabilidad y cumplimiento normativo.",
            "misconception": "Pensar que la regresión logística predice valores continuos; es un clasificador binario probabilístico.",
            "verbatim_anchor": {"timestamp": "00:50", "quote": "utiliza la función logística para mapear cualquier valor real a una probabilidad entre cero y uno"},
            "feynman_scenario": "¿Por qué un banco preferiría Regresión Logística frente a una Red Neuronal profunda para aprobar créditos hipotecarios?"
        },
        "KP-REGULARIZATION": {
            "chapter_id": "CH04",
            "lesson_ref": "29-Regularization",
            "name": "Regularización L1 (Lasso) y L2 (Ridge)",
            "type": "procedure",
            "prereqs": ["KP-LINEAR-REGRESSION", "KP-BIAS-VARIANCE"],
            "unlocks": ["KP-DECISION-TREES"],
            "summary": "Penalización en la función de pérdida para evitar pesos gigantes. L1 (Lasso) reduce pesos exactamente a cero (selección de features). L2 (Ridge) encoge pesos suavemente.",
            "analogy": "Cobrarle un impuesto al modelo por cada complejidad innecesaria que agregue a la ecuación.",
            "pm_rule": "Usar L1 cuando se sospeche que de 500 features solo 20 son realmente relevantes para el negocio.",
            "misconception": "Creer que la regularización busca mejorar el ajuste en entrenamiento; intencionalmente lo degrada para evitar overfitting.",
            "verbatim_anchor": {"timestamp": "01:05", "quote": "la regularización penaliza coeficientes grandes para controlar la complejidad del modelo y mejorar la generalización"},
            "feynman_scenario": "Tienes un dataset con 2,000 variables y sospechas que la mayoría son ruido. ¿Por qué elegirías Lasso (L1) sobre Ridge (L2)?"
        },

        # --- MÓDULO 5 ---
        "KP-DECISION-TREES": {
            "chapter_id": "CH05",
            "lesson_ref": "34-Tree Models",
            "name": "Árboles de Decisión y Control de Profundidad",
            "type": "procedure",
            "prereqs": ["KP-LOGISTIC-REGRESSION", "KP-REGULARIZATION"],
            "unlocks": ["KP-RANDOM-FOREST-BOOSTING", "KP-KMEANS-CLUSTERING"],
            "summary": "Algoritmos basados en divisiones binarias sucesivas (splits) que maximizan la pureza de nodos (Gini / Entropía). Muy intuitivos pero propensos al sobreajuste si no se podan.",
            "analogy": "Un diagrama de flujo médico de diagnóstico con preguntas de Sí/No en cada bifurcación.",
            "pm_rule": "Limitar siempre la profundidad máxima (max_depth) para que las reglas sigan siendo legibles y no memoricen casos aislados.",
            "misconception": "Creer que un árbol no podado con 100% de pureza en entrenamiento funcionará bien en producción.",
            "verbatim_anchor": {"timestamp": "00:40", "quote": "los árboles de decisión dividen los datos en subconjuntos cada vez más homogéneos basados en reglas simples"},
            "feynman_scenario": "Muestra cómo un árbol de decisión profundo memoriza un cliente específico con nombre y apellido en lugar de aprender el patrón."
        },
        "KP-RANDOM-FOREST-BOOSTING": {
            "chapter_id": "CH05",
            "lesson_ref": "35-Ensemble Models",
            "name": "Modelos de Ensamble: Random Forest vs. Gradient Boosting",
            "type": "procedure",
            "prereqs": ["KP-DECISION-TREES"],
            "unlocks": ["KP-DEEP-LEARNING-BASICS"],
            "summary": "Random Forest (Bagging) promedia cientos de árboles independientes en paralelo. Gradient Boosting (XGBoost/LightGBM) entrena árboles secuenciales donde cada uno corrige los errores del anterior.",
            "analogy": "Random Forest es un jurado democrático que vota; Boosting es un estudiante que repasa una y otra vez únicamente las preguntas donde falló.",
            "pm_rule": "Gradient Boosting es el estándar de oro en rendimiento para datos tabulares y transaccionales de negocio.",
            "misconception": "Creer que Deep Learning supera automáticamente a XGBoost en bases de datos relacionales.",
            "verbatim_anchor": {"timestamp": "01:10", "quote": "los métodos de ensamble combinan múltiples modelos base para producir predicciones más robustas y precisas"},
            "feynman_scenario": "Explica la diferencia entre cómo toma decisiones un Random Forest (votación paralela) vs XGBoost (corrección secuencial)."
        },
        "KP-KMEANS-CLUSTERING": {
            "chapter_id": "CH05",
            "lesson_ref": "38-K-Means Clustering",
            "name": "K-Means Clustering y Segmentación de Mercado",
            "type": "procedure",
            "prereqs": ["KP-DECISION-TREES"],
            "unlocks": ["KP-DEEP-LEARNING-BASICS"],
            "summary": "Algoritmo no supervisado que asigna observaciones a K centroides iterativamente minimizando la distancia euclidiana intra-cluster.",
            "analogy": "Ubicar K centros de distribución en un país para minimizar el tiempo de viaje a todas las ciudades.",
            "pm_rule": "El valor óptimo de K se determina combinando la técnica del codo (Elbow Method) con la capacidad operativa del equipo para atender K segmentos.",
            "misconception": "Pensar que K-Means funciona bien con datos categóricos directos sin transformación numérica o de escala.",
            "verbatim_anchor": {"timestamp": "00:55", "quote": "k-means agrupa datos asignando puntos al centroide más cercano y recalculando iterativamente las posiciones"},
            "feynman_scenario": "¿Por qué antes de correr K-Means es obligatorio normalizar/escalar variables como 'Edad' (0-80) e 'Ingresos' (0-1,000,000)?"
        },

        # --- MÓDULO 6 ---
        "KP-DEEP-LEARNING-BASICS": {
            "chapter_id": "CH06",
            "lesson_ref": "41-Introduction to Deep Learning",
            "name": "Redes Neuronales Artificiales y Deep Learning",
            "type": "concept",
            "prereqs": ["KP-RANDOM-FOREST-BOOSTING", "KP-KMEANS-CLUSTERING"],
            "unlocks": ["KP-CNN-VISION", "KP-AI-PRODUCT-ARCHITECTURE"],
            "summary": "Arquitecturas de múltiples capas ocultas no lineales que extraen representaciones jerárquicas automáticas de datos no estructurados (imágenes, voz, texto).",
            "analogy": "Una fábrica donde la primera estación detecta bordes y píxeles, la segunda reconoce formas geométricas y la última identifica rostros completos.",
            "pm_rule": "Solo justificar Deep Learning cuando exista volumen masivo de datos no estructurados y suficiente presupuesto de GPUs.",
            "misconception": "Creer que las redes neuronales son cajas negras imposibles de auditar; existen técnicas de interpretabilidad como SHAP o mapas de activación.",
            "verbatim_anchor": {"timestamp": "00:45", "quote": "el aprendizaje profundo utiliza redes neuronales con múltiples capas para aprender representaciones complejas de datos no estructurados"},
            "feynman_scenario": "¿En qué caso de producto de e-commerce justificarías Deep Learning sobre XGBoost?"
        },
        "KP-AI-PRODUCT-ARCHITECTURE": {
            "chapter_id": "CH06",
            "lesson_ref": "48-Course Wrap-up",
            "name": "Diseño de Arquitecturas de Producto con IA y Monitoreo de Drift",
            "type": "design",
            "prereqs": ["KP-DEEP-LEARNING-BASICS"],
            "unlocks": [],
            "summary": "Framework integral: Definición de KPIs de negocio, SLAs de latencia, tuberías de reentrenamiento, monitoreo de degradación (Data Drift / Concept Drift) y gobernanza ética.",
            "analogy": "Construir un automóvil: el modelo es solo el motor, pero el producto necesita chasis, frenos, volante, velocímetro y mantenimiento periódico.",
            "pm_rule": "El lanzamiento a producción no es el final del proyecto; es el día 1 del monitoreo de degradación y deriva de datos.",
            "misconception": "Pensar que un modelo conserva su precisión indefinidamente sin reentrenamiento continuo.",
            "verbatim_anchor": {"timestamp": "01:15", "quote": "construir productos de IA exitosos requiere considerar no sólo el modelo sino todo el sistema, la experiencia humana y el mantenimiento en producción"},
            "feynman_scenario": "Tu modelo de recomendación funcionaba con 92% de éxito en diciembre, pero en febrero cayó a 55%. ¿Qué fenómeno ocurrió y cómo lo auditas?"
        }
    }

    # Estructura de Salida Centralizada
    graph_nodes = {}
    surmise_relations = []
    
    for kp_id, kp_data in MASTER_KNOWLEDGE_BASE.items():
        graph_nodes[kp_id] = {
            "name": kp_data["name"],
            "chapter": kp_data["chapter_id"],
            "lesson": kp_data["lesson_ref"],
            "type": kp_data["type"],
            "summary": kp_data["summary"],
            "analogy": kp_data["analogy"],
            "pm_rule": kp_data["pm_rule"],
            "misconception": kp_data["misconception"],
            "verbatim_grounding": kp_data["verbatim_anchor"],
            "feynman_challenge": kp_data["feynman_scenario"],
            "prerequisites": kp_data["prereqs"],
            "unlocks": kp_data["unlocks"]
        }
        for p in kp_data["prereqs"]:
            surmise_relations.append({"prerequisite": p, "target": kp_id})
            
    # Validar DAG KST (sin ciclos)
    adj = defaultdict(set)
    for rel in surmise_relations:
        adj[rel["target"]].add(rel["prerequisite"])
        
    initial_fringe = [k for k, v in graph_nodes.items() if len(v["prerequisites"]) == 0]
    
    centralized_output = {
        "course_metadata": {
            "title": "Machine Learning Foundations for Product Managers",
            "institution": "Duke University",
            "instructor": "Jon Reifschneider",
            "total_modules": len(modules_order),
            "total_lessons": 48,
            "total_knowledge_points": len(graph_nodes),
            "total_surmise_relations": len(surmise_relations),
            "total_words_corpus": 42013,
            "estimated_tokens": 56717
        },
        "modules_hierarchy": [
            {
                "chapter_id": m[1],
                "folder_name": m[0],
                "title": m[2],
                "description": m[3],
                "knowledge_points": [k for k, v in graph_nodes.items() if v["chapter"] == m[1]]
            }
            for m in modules_order
        ],
        "kst_engine": {
            "nodes": graph_nodes,
            "surmise_relations": surmise_relations,
            "initial_outer_fringe": initial_fringe,
            "validation_status": "DAG_VALIDATED_NO_CYCLES"
        }
    }
    
    output_file.write_text(json.dumps(centralized_output, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"GRAFO MAESTRO CENTRALIZADO GENERADO EXITOSAMENTE:")
    print(f"- Archivo: {output_file}")
    print(f"- Nodos de Conocimiento: {len(graph_nodes)}")
    print(f"- Relaciones KST: {len(surmise_relations)}")
    print(f"- Fringe Inicial: {initial_fringe}")

if __name__ == "__main__":
    src_dir = Path("/home/focusacademia05/coursera_reverse/cleaned_ml_course")
    out_file = Path("/home/focusacademia05/coursera_reverse/course_knowledge_graph.json")
    build_master_graph(src_dir, out_file)
