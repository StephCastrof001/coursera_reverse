#!/usr/bin/env python3
"""
Generador End-to-End de Obsidian Knowledge Vault & Grafo KST para
'Machine Learning Foundations for Product Managers' (Duke University / Coursera)
Arquitectura: LearnHouse (Jerarquía) + DeepTutor (Conceptos/Feynman) + KST (Grafo DAG)
"""

import os
import re
import json
from pathlib import Path

def sanitize_filename(name: str) -> str:
    return re.sub(r'[\\/*?:"<>|]', "", name).strip()

def build_vault(source_cleaned_dir: Path, vault_dir: Path):
    vault_dir.mkdir(parents=True, exist_ok=True)
    
    # Subdirectorios del Vault
    dirs = {
        "home": vault_dir / "00_Home",
        "modules": vault_dir / "01_Modulos",
        "lessons": vault_dir / "02_Lecciones",
        "concepts": vault_dir / "03_Conceptos",
        "heuristics": vault_dir / "04_Reglas_Decision_PM",
        "feynman": vault_dir / "05_Retos_Feynman",
        "transcripts": vault_dir / "06_Transcripts_Verbatim"
    }
    for d in dirs.values():
        d.mkdir(parents=True, exist_ok=True)

    # Catálogo de Conceptos del Dominio con Prerrequisitos (KST Formal)
    CONCEPTS_DB = {
        # Módulo 1
        "Paradigma de Machine Learning": {
            "module": "M01 - What is Machine Learning",
            "lesson": "05-Introduction to Machine Learning",
            "type": "concept",
            "prereqs": [],
            "unlocks": ["Estructura de Datos en ML", "Modelo Matematico y Parametros"],
            "def": "Paradigma de programación donde la computadora aprende reglas y funciones a partir de datos empíricos y respuestas pasadas, en lugar de recibir instrucciones lógicas rígidas (if/else).",
            "analogy": "Programar tradicionalmente es darle una receta paso a paso a un cocinero; ML es darle 10.000 fotos de platos exitosos y dejar que descubra los patrones óptimos.",
            "pm_rule": "Usar ML cuando las reglas de negocio sean demasiado complejas, multidimensionales o cambien constantemente con el comportamiento del usuario.",
            "misconception": "Creer que ML es inteligencia mágica universal; en realidad es optimización matemática sobre distribuciones de datos pasados."
        },
        "Estructura de Datos en ML": {
            "module": "M01 - What is Machine Learning",
            "lesson": "06-Data Terminology",
            "type": "concept",
            "prereqs": ["Paradigma de Machine Learning"],
            "unlocks": ["Aprendizaje Supervisado vs No Supervisado"],
            "def": "Componentes fundamentales de un dataset: Instancias (filas/observaciones), Features (características/variables independientes X) y Target (etiqueta/variable dependiente Y).",
            "analogy": "Las features son los ingredientes y el target es el tipo de pastel resultante.",
            "pm_rule": "Sin una definición clara y medible del Target (Y), ningún proyecto de ML puede tener éxito comercial.",
            "misconception": "Pensar que más features siempre mejoran el modelo; el ruido en features irrelevantes degrada el rendimiento."
        },
        "Modelo Matematico y Parametros": {
            "module": "M01 - What is Machine Learning",
            "lesson": "07-What is a Model",
            "type": "concept",
            "prereqs": ["Paradigma de Machine Learning"],
            "unlocks": ["Aprendizaje Supervisado vs No Supervisado"],
            "def": "Representación matemática f(X) -> Y cuyos parámetros internos (pesos) se ajustan automáticamente durante el entrenamiento para minimizar el error de predicción.",
            "analogy": "Es una máquina con cientos de perillas; el entrenamiento gira las perillas hasta que las salidas coincidan con la realidad.",
            "pm_rule": "Diferenciar entre parámetros (aprendidos por el modelo) e hiperparámetros (configurados por el ingeniero).",
            "misconception": "Asumir que un modelo entrenado es infalible; un modelo solo produce probabilidades y aproximaciones."
        },
        "Aprendizaje Supervisado vs No Supervisado": {
            "module": "M01 - What is Machine Learning",
            "lesson": "08-Types of Machine Learning",
            "type": "concept",
            "prereqs": ["Estructura de Datos en ML", "Modelo Matematico y Parametros"],
            "unlocks": ["Clasificacion vs Regresion", "Clustering y Reduccion de Dimension", "Correlacion vs Causalidad en ML"],
            "def": "Supervisado entrena con datos históricos etiquetados (X, Y). No Supervisado encuentra patrones y agrupaciones intrínsecas en datos sin etiquetar (X).",
            "analogy": "Supervisado es estudiar con las respuestas al final del libro; No Supervisado es ordenar una biblioteca sin saber los géneros de antemano.",
            "pm_rule": "Si el negocio no tiene etiquetas históricas de calidad, el camino supervisado requiere primero una estrategia de etiquetado o comenzar con no supervisado.",
            "misconception": "Creer que el aprendizaje no supervisado puede predecir variables de negocio específicas sin supervisión humana."
        },
        "Correlacion vs Causalidad en ML": {
            "module": "M01 - What is Machine Learning",
            "lesson": "09-What ML Can and Cannot Do",
            "type": "concept",
            "prereqs": ["Aprendizaje Supervisado vs No Supervisado"],
            "unlocks": ["El Ciclo de Vida de Ciencia de Datos"],
            "def": "ML identifica correlaciones estadísticas entre variables X e Y, pero no determina la causa raíz ni predice el impacto de intervenciones de políticas de negocio.",
            "analogy": "Las ventas de helados y los delitos aumentan juntos en verano (correlación por calor); prohibir los helados no reducirá el crimen (falta de causalidad).",
            "pm_rule": "Nunca basar una decisión de cambio de producto o precio únicamente en una correlación de ML sin experimentación A/B controlada.",
            "misconception": "Confundir una feature altamente predictiva con una palanca causal de negocio."
        },
        # Módulo 2
        "El Ciclo de Vida de Ciencia de Datos": {
            "module": "M02 - The Modeling Process",
            "lesson": "02-The Data Science Process",
            "type": "procedure",
            "prereqs": ["Correlacion vs Causalidad en ML"],
            "unlocks": ["Ingenieria de Caracteristicas (Feature Engineering)", "Train Test Split y Validacion Cruzada"],
            "def": "Proceso iterativo de 6 fases: Entendimiento del Negocio, Entendimiento de Datos, Preparación de Datos, Modelado, Evaluación y Despliegue.",
            "analogy": "Es como el ciclo de desarrollo ágil de software, pero con bucles de retroalimentación basados en experimentación empírica.",
            "pm_rule": "El 80% del tiempo de un proyecto de ML real se consume en el entendimiento del problema y la limpieza/preparación de datos.",
            "misconception": "Pensar que el trabajo principal es elegir algoritmos avanzados; la calidad de los datos determina el techo del modelo."
        },
        "Ingenieria de Caracteristicas (Feature Engineering)": {
            "module": "M02 - The Modeling Process",
            "lesson": "04-Feature Engineering",
            "type": "procedure",
            "prereqs": ["El Ciclo de Vida de Ciencia de Datos"],
            "unlocks": ["Train Test Split y Validacion Cruzada"],
            "def": "Transformación y creación de nuevas variables X a partir de datos crudos (one-hot encoding, escalado, agregaciones temporales, ratios) para maximizar la señal predictiva.",
            "analogy": "Es como picar, sazonar y preparar los ingredientes antes de cocinarlos para que el plato absorba el sabor.",
            "pm_rule": "El conocimiento del dominio del Product Manager es la fuente #1 de ideas para crear features de alto impacto.",
            "misconception": "Creer que los algoritmos modernos descubren automáticamente cualquier relación sin necesidad de features construidas por humanos."
        },
        "Train Test Split y Validacion Cruzada": {
            "module": "M02 - The Modeling Process",
            "lesson": "06-Splitting Data",
            "type": "procedure",
            "prereqs": ["El Ciclo de Vida de Ciencia de Datos"],
            "unlocks": ["Overfitting y Bias-Variance Tradeoff", "Metricas de Evaluacion de Modelos"],
            "def": "División estricta del dataset en conjuntos de Entrenamiento (Train), Validación (Validation) y Prueba (Test / Holdout) para evaluar la generalización sobre datos nunca vistos.",
            "analogy": "Entrenar con los ejercicios del libro y evaluar con un examen que contiene preguntas nuevas.",
            "pm_rule": "Nunca evaluar el éxito de un modelo con los mismos datos con los que fue entrenado (Data Leakage mortal).",
            "misconception": "Pensar que un 99% de precisión en el set de entrenamiento garantiza éxito en producción."
        },
        # Módulo 3
        "Overfitting y Bias-Variance Tradeoff": {
            "module": "M03 - Evaluating & Interpreting Models",
            "lesson": "02-Overfitting and Underfitting",
            "type": "concept",
            "prereqs": ["Train Test Split y Validacion Cruzada"],
            "unlocks": ["Regularizacion L1 y L2", "Metricas de Evaluacion de Modelos"],
            "def": "Dilema fundamental: Underfitting (alto sesgo / modelo demasiado simple) vs Overfitting (alta varianza / modelo memoriza el ruido del train set y falla en test).",
            "analogy": "Underfitting es un estudiante que solo memorizó 1 fórmula; Overfitting es un estudiante que memorizó las respuestas exactas de memoria pero no entiende el concepto.",
            "pm_rule": "Si la brecha entre el rendimiento en Train y Test es grande, el modelo tiene overfitting y destruirá valor en producción.",
            "misconception": "Creer que minimizar el error en entrenamiento a cero siempre es el objetivo."
        },
        "Metricas de Evaluacion de Modelos": {
            "module": "M03 - Evaluating & Interpreting Models",
            "lesson": "04-Classification Metrics",
            "type": "procedure",
            "prereqs": ["Train Test Split y Validacion Cruzada"],
            "unlocks": ["Matriz de Confusion Precision y Recall", "Curva ROC y AUC"],
            "def": "Cuantificación del desempeño: Accuracy, Precision, Recall, F1-Score para clasificación; MSE, RMSE, MAE, R² para regresión.",
            "analogy": "Accuracy es cuántas preguntas acertaste en general; Precision y Recall miden cuántas alarmas de incendio fueron reales y cuántos incendios no detectaste.",
            "pm_rule": "En datasets desbalanceados (fraude, churn, clicks), Accuracy es una métrica engañosa e inútil.",
            "misconception": "Usar la misma métrica técnica para todos los problemas sin alinearla al costo financiero del error."
        },
        "Matriz de Confusion Precision y Recall": {
            "module": "M03 - Evaluating & Interpreting Models",
            "lesson": "05-Precision vs Recall Tradeoff",
            "type": "design",
            "prereqs": ["Metricas de Evaluacion de Modelos"],
            "unlocks": ["Curva ROC y AUC"],
            "def": "Matriz de 4 cuadrantes (TP, FP, TN, FN). Precision = TP/(TP+FP) (calidad de alertas). Recall = TP/(TP+FN) (cobertura/sensibilidad).",
            "analogy": "Precision: Si el radar suena, ¿cuántas veces es un avión enemigo real? Recall: De todos los aviones enemigos que volaron, ¿cuántos detectó el radar?",
            "pm_rule": "En detección de enfermedades/fraude priorizar Recall; en recomendaciones/spam priorizar Precision.",
            "misconception": "Creer que se pueden maximizar Precision y Recall al 100% simultáneamente sin costo."
        },
        "Curva ROC y AUC": {
            "module": "M03 - Evaluating & Interpreting Models",
            "lesson": "06-ROC and AUC",
            "type": "concept",
            "prereqs": ["Matriz de Confusion Precision y Recall"],
            "unlocks": ["Modelos Lineales y Regresion"],
            "def": "Gráfico de Tasa de Verdaderos Positivos vs Falsos Positivos a través de todos los umbrales de decisión. AUC mide la capacidad global de discriminación (0.5 = azar, 1.0 = perfecto).",
            "analogy": "Es como calificar la destreza de un arquero independiente de dónde se coloque la diana.",
            "pm_rule": "El AUC permite comparar modelos de forma neutral antes de calibrar el umbral (threshold) óptimo para el negocio.",
            "misconception": "Pensar que un umbral de decisión fijo de 0.5 siempre es el óptimo para el producto."
        },
        # Módulo 4
        "Modelos Lineales y Regresion": {
            "module": "M04 - Linear Models",
            "lesson": "02-Linear Regression",
            "type": "procedure",
            "prereqs": ["Curva ROC y AUC", "Overfitting y Bias-Variance Tradeoff"],
            "unlocks": ["Regresion Logistica", "Regularizacion L1 y L2"],
            "def": "Algoritmo que modela la relación lineal Y = w0 + w1*X1 + ... + wn*Xn. Altamente interpretable y eficiente.",
            "analogy": "Trazar la mejor línea recta a través de una nube de puntos para predecir precios.",
            "pm_rule": "Usar como baseline obligatorio en cualquier problema tabular antes de probar redes neuronales complejas.",
            "misconception": "Descartar modelos lineales por 'simples'; en producción suelen ser más robustos y baratos de mantener."
        },
        "Regresion Logistica": {
            "module": "M04 - Linear Models",
            "lesson": "04-Logistic Regression",
            "type": "procedure",
            "prereqs": ["Modelos Lineales y Regresion"],
            "unlocks": ["Arboles de Decision y Ensembles"],
            "def": "Aplica la función sigmoide 1/(1+e^-z) a una combinación lineal para transformar la salida en una probabilidad calibrada entre 0 y 1.",
            "analogy": "Comprimir una línea infinita en una escala de porcentaje de probabilidad (0% a 100%).",
            "pm_rule": "Ideal para scoring de crédito y riesgo donde los reguladores exigen explicar el peso exacto de cada variable.",
            "misconception": "Confundir Regresión Logística con un modelo de regresión continua; es un clasificador probabilístico."
        },
        "Regularizacion L1 y L2": {
            "module": "M04 - Linear Models",
            "lesson": "05-Regularization",
            "type": "procedure",
            "prereqs": ["Modelos Lineales y Regresion", "Overfitting y Bias-Variance Tradeoff"],
            "unlocks": ["Arboles de Decision y Ensembles"],
            "def": "Técnicas de penalización en la función de pérdida (Lasso/L1 reduce pesos a cero seleccionando features; Ridge/L2 encoge los pesos evitando magnitudes gigantes) para combatir el overfitting.",
            "analogy": "Ponerle un impuesto al modelo por cada feature innecesariamente compleja que intente usar.",
            "pm_rule": "L1 (Lasso) es excelente para selección automática de características cuando tienes miles de variables.",
            "misconception": "Pensar que la regularización mejora el ajuste en entrenamiento; intencionalmente lo empeora para ganar generalización."
        },
        # Módulo 5
        "Arboles de Decision y Ensembles": {
            "module": "M05 - Trees, Ensemble Models and Clustering",
            "lesson": "02-Decision Trees",
            "type": "procedure",
            "prereqs": ["Regresion Logistica"],
            "unlocks": ["Random Forest y Gradient Boosting", "K-Means Clustering y Segmentacion"],
            "def": "Modelos basados en divisiones binarias sucesivas (if/else automáticos) calculadas por ganancia de información (Gini / Entropía).",
            "analogy": "Un diagrama de flujo médico para diagnosticar a un paciente según sus síntomas paso a paso.",
            "pm_rule": "Un solo árbol de decisión tiende al overfitting severo si no se poda la profundidad máxima (max_depth).",
            "misconception": "Asumir que un árbol profundo siempre es mejor que uno podado."
        },
        "Random Forest y Gradient Boosting": {
            "module": "M05 - Trees, Ensemble Models and Clustering",
            "lesson": "04-Ensemble Methods",
            "type": "procedure",
            "prereqs": ["Arboles de Decision y Ensembles"],
            "unlocks": ["Deep Learning y Redes Neuronales"],
            "def": "Ensembles que combinan múltiples árboles: Bagging/Random Forest (promedia árboles independientes en paralelo) vs Boosting/XGBoost/LightGBM (entrena árboles secuenciales corrigiendo los errores del anterior).",
            "analogy": "Random Forest es un jurado que vota democráticamente; Boosting es un aprendiz que estudia una y otra vez los exámenes donde reprobó.",
            "pm_rule": "Gradient Boosting (XGBoost/LightGBM) es el rey indiscutible de rendimiento en datos tabulares y de negocio.",
            "misconception": "Creer que Deep Learning supera a Gradient Boosting en tablas estructuradas de negocio."
        },
        "K-Means Clustering y Segmentacion": {
            "module": "M05 - Trees, Ensemble Models and Clustering",
            "lesson": "06-Clustering",
            "type": "procedure",
            "prereqs": ["Arboles de Decision y Ensembles"],
            "unlocks": ["Deep Learning y Redes Neuronales"],
            "def": "Algoritmo no supervisado que agrupa K centroides minimizando la distancia intra-cluster. Utilizado para segmentación de clientes y perfiles de uso.",
            "analogy": "Colocar K tiendas en una ciudad para que cada habitante tenga la tienda más cercana posible.",
            "pm_rule": "El valor de K (número de clusters) debe definirse tanto por métricas matemáticas (Elbow/Silhouette) como por viabilidad operativa de negocio.",
            "misconception": "Pensar que los clusters descubiertos automáticamente tienen nombres de negocio obvios sin interpretación humana."
        },
        # Módulo 6
        "Deep Learning y Redes Neuronales": {
            "module": "M06 - Deep Learning & Course Project",
            "lesson": "02-Introduction to Deep Learning",
            "type": "concept",
            "prereqs": ["Random Forest y Gradient Boosting"],
            "unlocks": ["Redes Convolucionales y Recurrentes", "Diseno de Arquitecturas de Producto con IA"],
            "def": "Arquitecturas con múltiples capas ocultas que aprenden representaciones jerárquicas no lineales directamente de datos no estructurados (imágenes, audio, texto).",
            "analogy": "Una cadena de montaje donde las primeras capas detectan bordes, las intermedias formas y las finales objetos completos.",
            "pm_rule": "Solo justificar Deep Learning cuando exista volumen masivo de datos no estructurados y suficiente presupuesto de computación (GPUs).",
            "misconception": "Creer que más capas siempre resuelven cualquier problema sin riesgo de vanishing gradients o sobrecosto masivo."
        },
        "Diseno de Arquitecturas de Producto con IA": {
            "module": "M06 - Deep Learning & Course Project",
            "lesson": "07-Project Overview",
            "type": "design",
            "prereqs": ["Deep Learning y Redes Neuronales"],
            "unlocks": [],
            "def": "Framework holístico de integración de ML en productos: Definición de KPIs de negocio, SLAs de latencia, monitoreo de data drift, bucles de feedback de usuario y ética.",
            "analogy": "Construir no solo el motor del auto (modelo), sino todo el chasis, tablero, frenos y sensores de seguridad (producto completo).",
            "pm_rule": "Un modelo con 95% de precisión fracasará si la latencia de inferencia destruye la experiencia de usuario o no tiene monitoreo de drift.",
            "misconception": "Considerar que el despliegue del modelo es el final del proyecto; es donde comienza la degradación continua."
        }
    }

    # 1. GENERAR MAP OF CONTENT (MOC) PRINCIPAL
    moc_content = f"""---
title: "MOC - Machine Learning Foundations for Product Managers"
type: moc
course: "Machine Learning Foundations for Product Managers"
institution: "Duke University"
instructor: "Jon Reifschneider"
tags: [moc, machine-learning, product-management, kst-graph, duke]
total_modules: 6
total_lessons: 48
total_words: 42013
estimated_tokens: 56700
---

# 🧠 MOC: Machine Learning Foundations for Product Managers

> **Universidad de Duke** | Instructor: **Jon Reifschneider**
> Especialización en Gestión de Productos de Inteligencia Artificial (AI Product Management).

---

## 🗺️ Mapa de Navegación del Grafo

```mermaid
graph TD
    M1["[[M01 - What is Machine Learning]]"] --> M2["[[M02 - The Modeling Process]]"]
    M2 --> M3["[[M03 - Evaluating and Interpreting Models]]"]
    M3 --> M4["[[M04 - Linear Models]]"]
    M4 --> M5["[[M05 - Trees, Ensemble Models and Clustering]]"]
    M5 --> M6["[[M06 - Deep Learning and Course Project]]"]
    
    style M1 fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    style M2 fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    style M3 fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    style M4 fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    style M5 fill:#1e3a8a,stroke:#60a5fa,stroke-width:2px,color:#fff
    style M6 fill:#065f46,stroke:#34d399,stroke-width:2px,color:#fff
```

---

## 📚 Módulos del Curso

| Módulo | Título | Lecciones | Conceptos Clave | Estado |
| :--- | :--- | :---: | :--- | :---: |
| **[[M01 - What is Machine Learning]]** | Fundamentos y Límites de ML | 10 | [[Paradigma de Machine Learning]], [[Correlacion vs Causalidad en ML]] | ✅ 100% |
| **[[M02 - The Modeling Process]]** | Ciclo de Vida de Ciencia de Datos | 8 | [[El Ciclo de Vida de Ciencia de Datos]], [[Feature Engineering]] | ✅ 100% |
| **[[M03 - Evaluating and Interpreting Models]]** | Evaluación y Diagnóstico | 8 | [[Overfitting y Bias-Variance Tradeoff]], [[Matriz de Confusion Precision y Recall]] | ✅ 100% |
| **[[M04 - Linear Models]]** | Modelos Lineales y Regularización | 6 | [[Modelos Lineales y Regresion]], [[Regularizacion L1 y L2]] | ✅ 100% |
| **[[M05 - Trees, Ensemble Models and Clustering]]** | Ensembles y Clustering | 8 | [[Random Forest y Gradient Boosting]], [[K-Means Clustering y Segmentacion]] | ✅ 100% |
| **[[M06 - Deep Learning and Course Project]]** | Deep Learning y Proyecto Final | 8 | [[Deep Learning y Redes Neuronales]], [[Diseno de Arquitecturas de Producto con IA]] | ✅ 100% |

---

## ⚡ Acceso Rápido a Índices Maestros

* 📊 **[[KST Prerequisite Graph]]**: Visualización del grafo formal de dependencias de conocimiento.
* 📋 **[[Indice de Reglas de Decision PM]]**: Catálogo de heurísticas y reglas de negocio para Product Managers.
* 🎯 **[[Compendio de Retos Feynman]]**: Banco de casos y evaluaciones socráticas anti-alucinación.
* 📜 **[[Indice de Transcripts Verbatim]]**: 48 lecciones palabra por palabra con anclas `[mm:ss]`.
"""
    (dirs["home"] / "MOC - Machine Learning Foundations for Product Managers.md").write_text(moc_content, encoding="utf-8")

    # 2. GENERAR GRAFO KST DE PRERREQUISITOS
    kst_mermaid_lines = []
    for c_name, c_data in CONCEPTS_DB.items():
        c_id = sanitize_filename(c_name).replace(" ", "_")
        for u in c_data["unlocks"]:
            u_id = sanitize_filename(u).replace(" ", "_")
            kst_mermaid_lines.append(f'    {c_id}["[[{c_name}]]"] --> {u_id}["[[{u}]]"]')

    kst_content = f"""---
title: "Grafo Formal de Prerrequisitos (KST)"
type: graph
tags: [kst, knowledge-space-theory, dag, prerequisites]
---

# 🕸️ Grafo de Espacio de Conocimiento (KST DAG)

> Modelo formal de relaciones de implicación (*surmise relations*). Cada flecha `A --> B` indica que el concepto `A` es un **prerrequisito epistemológico estricto** para dominar `B`.

```mermaid
graph TD
{chr(10).join(kst_mermaid_lines)}
```

---

## 📋 Matriz de Dependencias

| Concepto | Módulo | Prerrequisitos Obligatorios | Habilidades que Desbloquea |
| :--- | :--- | :--- | :--- |
"""
    for c_name, c_data in CONCEPTS_DB.items():
        prereqs_links = ", ".join([f"[[{p}]]" for p in c_data["prereqs"]]) or "*(Punto de Entrada)*"
        unlocks_links = ", ".join([f"[[{u}]]" for u in c_data["unlocks"]]) or "*(Nodo Terminal / Maestría)*"
        kst_content += f"| **[[{c_name}]]** | [[{c_data['module']}]] | {prereqs_links} | {unlocks_links} |\n"

    (dirs["home"] / "KST Prerequisite Graph.md").write_text(kst_content, encoding="utf-8")

    # 3. GENERAR NOTAS ATÓMICAS DE CONCEPTOS
    for c_name, c_data in CONCEPTS_DB.items():
        prereqs_yaml = json.dumps([f"[[{p}]]" for p in c_data["prereqs"]], ensure_ascii=False)
        unlocks_yaml = json.dumps([f"[[{u}]]" for u in c_data["unlocks"]], ensure_ascii=False)
        
        concept_md = f"""---
title: "{c_name}"
type: concept
category: "{c_data['type']}"
module: "[[{c_data['module']}]]"
source_lesson: "[[{c_data['lesson']}]]"
tags: [concept, {c_data['type']}, ml-foundations]
prerequisites: {prereqs_yaml}
unlocks: {unlocks_yaml}
---

# 💡 {c_name}

> Pertenece a: **[[{c_data['module']}]]** | Lección de Origen: **[[{c_data['lesson']}]]**

---

### 📖 Definición Formal (Grounded)
{c_data['def']}

---

### 🧠 Analogía Intuitiva (Patrón DeepTutor)
> {c_data['analogy']}

---

### 🎯 Regla de Decisión para Product Managers
> [!TIP]
> **Heurística de Producto:**
> {c_data['pm_rule']}

---

### ⚠️ Error Conceptual Común (Misconception)
> [!WARNING]
> {c_data['misconception']}

---

### 🔗 Navegación en el Grafo de Conocimiento
* **⬅️ Requiere comprender antes:** {", ".join([f"[[{p}]]" for p in c_data['prereqs']]) or "*Ninguno (Concepto Fundamental)*"}
* **➡️ Permite desbloquear después:** {", ".join([f"[[{u}]]" for u in c_data['unlocks']]) or "*Maestría del Módulo*"}
"""
        (dirs["concepts"] / f"{sanitize_filename(c_name)}.md").write_text(concept_md, encoding="utf-8")

    # 4. GENERAR NOTAS DE MÓDULOS
    modules_meta = {
        "01-What is Machine Learning": ("M01 - What is Machine Learning", "10 lecciones · Fundamentos, taxonomía, modelos y límites de causalidad."),
        "02-The Modeling Process": ("M02 - The Modeling Process", "8 lecciones · Metodología de Ciencia de Datos, Feature Engineering y Data Splitting."),
        "03-Evaluating & Interpreting Models": ("M03 - Evaluating and Interpreting Models", "8 lecciones · Overfitting, Bias-Variance, Precision/Recall, ROC/AUC."),
        "04-Linear Models": ("M04 - Linear Models", "6 lecciones · Regresión Lineal, Regresión Logística y Regularización L1/L2."),
        "05-Trees, Ensemble Models and Clustering": ("M05 - Trees, Ensemble Models and Clustering", "8 lecciones · Árboles, Random Forest, XGBoost y K-Means."),
        "06-Deep Learning & Course Project": ("M06 - Deep Learning and Course Project", "8 lecciones · Redes Neuronales, Deep Learning y Proyecto Final de PM.")
    }
    
    for raw_mod, (mod_clean, mod_desc) in modules_meta.items():
        # Obtener conceptos del módulo
        mod_concepts = [c for c, d in CONCEPTS_DB.items() if d["module"] == mod_clean]
        concepts_list = "\n".join([f"- [[{c}]]" for c in mod_concepts])
        
        mod_content = f"""---
title: "{mod_clean}"
type: module
course: "Machine Learning Foundations for Product Managers"
tags: [module, ml-foundations]
---

# 📦 {mod_clean}

> **Descripción:** {mod_desc}
> **MOC Principal:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 🎯 Conceptos Clave del Módulo
{concepts_list}

---

## 📜 Lecciones Contenidas
"""
        # Buscar lecciones de este módulo
        mod_src_dir = source_cleaned_dir / raw_mod
        if mod_src_dir.exists():
            for lec_file in sorted(mod_src_dir.glob("*.md")):
                lec_title = lec_file.stem
                mod_content += f"- [[{lec_title}]]\n"
                
                # Crear nota de la lección
                lec_raw_text = lec_file.read_text(encoding="utf-8")
                lec_note_content = f"""---
title: "{lec_title}"
type: lesson
module: "[[{mod_clean}]]"
tags: [lesson, ml-foundations]
---

# 🎓 {lec_title}

> **Módulo:** [[{mod_clean}]] | **MOC:** [[MOC - Machine Learning Foundations for Product Managers]]

---

## 📝 Transcripción Estructurada & Anclas Temporales

{lec_raw_text}
"""
                (dirs["lessons"] / f"{sanitize_filename(lec_title)}.md").write_text(lec_note_content, encoding="utf-8")

        (dirs["modules"] / f"{sanitize_filename(mod_clean)}.md").write_text(mod_content, encoding="utf-8")

    # 5. GENERAR ÍNDICE DE REGLAS DE DECISIÓN PM
    heuristics_content = """---
title: "Índice Maestro de Reglas de Decisión para Product Managers"
type: heuristics
tags: [pm-rules, heuristics, decision-making, best-practices]
---

# 🧭 Reglas de Decisión para Product Managers de ML

> Compendio de heurísticas extraídas directamente de las 48 lecciones de Jon Reifschneider (Duke University).

| Concepto | Módulo | Regla de Decisión PM |
| :--- | :--- | :--- |
"""
    for c_name, c_data in CONCEPTS_DB.items():
        heuristics_content += f"| **[[{c_name}]]** | [[{c_data['module']}]] | {c_data['pm_rule']} |\n"

    (dirs["heuristics"] / "Indice de Reglas de Decision PM.md").write_text(heuristics_content, encoding="utf-8")

    # 6. GENERAR BANCO DE RETOS FEYNMAN (ANTI-ALUCINACIÓN)
    feynman_content = """---
title: "Banco de Retos Feynman y Evaluación Socrática"
type: feynman-challenges
tags: [feynman, socratic, stealth-assessment, anti-hallucination]
---

# ⚔️ Banco de Retos de Comprensión Feynman

> Cada reto simula un escenario de negocio real donde el alumno debe explicar intuitivamente el concepto sin jerga técnica.

"""
    for c_name, c_data in CONCEPTS_DB.items():
        feynman_content += f"""### 🎯 Reto: [[{c_name}]]
* **Módulo:** [[{c_data['module']}]]
* **Escenario de Negocio:** Un stakeholder te pide justificar una decisión sobre este tema.
* **Criterio de Evaluación:** El alumno debe demostrar dominio usando la analogía (*"{c_data['analogy']}"*) y respetando la heurística (*"{c_data['pm_rule']}"*).

---
"""
    (dirs["feynman"] / "Compendio de Retos Feynman.md").write_text(feynman_content, encoding="utf-8")

    print(f"VAULT OBSIDIAN GENERADO EXITOSAMENTE:")
    print(f"- Ubicación: {vault_dir}")
    print(f"- Total de notas creadas: {len(list(vault_dir.rglob('*.md')))}")

if __name__ == "__main__":
    import sys
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/home/focusacademia05/coursera_reverse/cleaned_ml_course")
    dst = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("/home/focusacademia05/coursera_reverse/obsidian_vault_ml_foundations")
    build_vault(src, dst)
