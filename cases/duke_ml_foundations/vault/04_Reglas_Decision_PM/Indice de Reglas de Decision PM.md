---
title: "Índice Maestro de Reglas de Decisión para Product Managers"
type: heuristics
tags: [pm-rules, heuristics, decision-making, best-practices]
---

# 🧭 Reglas de Decisión para Product Managers de ML

> Compendio de heurísticas extraídas directamente de las 48 lecciones de Jon Reifschneider (Duke University).

| Concepto | Módulo | Regla de Decisión PM |
| :--- | :--- | :--- |
| **[[Paradigma de Machine Learning]]** | [[M01 - What is Machine Learning]] | Usar ML cuando las reglas de negocio sean demasiado complejas, multidimensionales o cambien constantemente con el comportamiento del usuario. |
| **[[Estructura de Datos en ML]]** | [[M01 - What is Machine Learning]] | Sin una definición clara y medible del Target (Y), ningún proyecto de ML puede tener éxito comercial. |
| **[[Modelo Matematico y Parametros]]** | [[M01 - What is Machine Learning]] | Diferenciar entre parámetros (aprendidos por el modelo) e hiperparámetros (configurados por el ingeniero). |
| **[[Aprendizaje Supervisado vs No Supervisado]]** | [[M01 - What is Machine Learning]] | Si el negocio no tiene etiquetas históricas de calidad, el camino supervisado requiere primero una estrategia de etiquetado o comenzar con no supervisado. |
| **[[Correlacion vs Causalidad en ML]]** | [[M01 - What is Machine Learning]] | Nunca basar una decisión de cambio de producto o precio únicamente en una correlación de ML sin experimentación A/B controlada. |
| **[[El Ciclo de Vida de Ciencia de Datos]]** | [[M02 - The Modeling Process]] | El 80% del tiempo de un proyecto de ML real se consume en el entendimiento del problema y la limpieza/preparación de datos. |
| **[[Ingenieria de Caracteristicas (Feature Engineering)]]** | [[M02 - The Modeling Process]] | El conocimiento del dominio del Product Manager es la fuente #1 de ideas para crear features de alto impacto. |
| **[[Train Test Split y Validacion Cruzada]]** | [[M02 - The Modeling Process]] | Nunca evaluar el éxito de un modelo con los mismos datos con los que fue entrenado (Data Leakage mortal). |
| **[[Overfitting y Bias-Variance Tradeoff]]** | [[M03 - Evaluating & Interpreting Models]] | Si la brecha entre el rendimiento en Train y Test es grande, el modelo tiene overfitting y destruirá valor en producción. |
| **[[Metricas de Evaluacion de Modelos]]** | [[M03 - Evaluating & Interpreting Models]] | En datasets desbalanceados (fraude, churn, clicks), Accuracy es una métrica engañosa e inútil. |
| **[[Matriz de Confusion Precision y Recall]]** | [[M03 - Evaluating & Interpreting Models]] | En detección de enfermedades/fraude priorizar Recall; en recomendaciones/spam priorizar Precision. |
| **[[Curva ROC y AUC]]** | [[M03 - Evaluating & Interpreting Models]] | El AUC permite comparar modelos de forma neutral antes de calibrar el umbral (threshold) óptimo para el negocio. |
| **[[Modelos Lineales y Regresion]]** | [[M04 - Linear Models]] | Usar como baseline obligatorio en cualquier problema tabular antes de probar redes neuronales complejas. |
| **[[Regresion Logistica]]** | [[M04 - Linear Models]] | Ideal para scoring de crédito y riesgo donde los reguladores exigen explicar el peso exacto de cada variable. |
| **[[Regularizacion L1 y L2]]** | [[M04 - Linear Models]] | L1 (Lasso) es excelente para selección automática de características cuando tienes miles de variables. |
| **[[Arboles de Decision y Ensembles]]** | [[M05 - Trees, Ensemble Models and Clustering]] | Un solo árbol de decisión tiende al overfitting severo si no se poda la profundidad máxima (max_depth). |
| **[[Random Forest y Gradient Boosting]]** | [[M05 - Trees, Ensemble Models and Clustering]] | Gradient Boosting (XGBoost/LightGBM) es el rey indiscutible de rendimiento en datos tabulares y de negocio. |
| **[[K-Means Clustering y Segmentacion]]** | [[M05 - Trees, Ensemble Models and Clustering]] | El valor de K (número de clusters) debe definirse tanto por métricas matemáticas (Elbow/Silhouette) como por viabilidad operativa de negocio. |
| **[[Deep Learning y Redes Neuronales]]** | [[M06 - Deep Learning & Course Project]] | Solo justificar Deep Learning cuando exista volumen masivo de datos no estructurados y suficiente presupuesto de computación (GPUs). |
| **[[Diseno de Arquitecturas de Producto con IA]]** | [[M06 - Deep Learning & Course Project]] | Un modelo con 95% de precisión fracasará si la latencia de inferencia destruye la experiencia de usuario o no tiene monitoreo de drift. |
