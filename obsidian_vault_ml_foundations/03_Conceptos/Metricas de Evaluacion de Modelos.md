---
title: "Metricas de Evaluacion de Modelos"
type: concept
category: "procedure"
module: "[[M03 - Evaluating & Interpreting Models]]"
source_lesson: "[[04-Classification Metrics]]"
tags: [concept, procedure, ml-foundations]
prerequisites: ["[[Train Test Split y Validacion Cruzada]]"]
unlocks: ["[[Matriz de Confusion Precision y Recall]]", "[[Curva ROC y AUC]]"]
---

# 💡 Metricas de Evaluacion de Modelos

> Pertenece a: **[[M03 - Evaluating & Interpreting Models]]** | Lección de Origen: **[[04-Classification Metrics]]**

---

### 📖 Definición Formal (Grounded)
Cuantificación del desempeño: Accuracy, Precision, Recall, F1-Score para clasificación; MSE, RMSE, MAE, R² para regresión.

---

### 🧠 Analogía Intuitiva (Patrón DeepTutor)
> Accuracy es cuántas preguntas acertaste en general; Precision y Recall miden cuántas alarmas de incendio fueron reales y cuántos incendios no detectaste.

---

### 🎯 Regla de Decisión para Product Managers
> [!TIP]
> **Heurística de Producto:**
> En datasets desbalanceados (fraude, churn, clicks), Accuracy es una métrica engañosa e inútil.

---

### ⚠️ Error Conceptual Común (Misconception)
> [!WARNING]
> Usar la misma métrica técnica para todos los problemas sin alinearla al costo financiero del error.

---

### 🔗 Navegación en el Grafo de Conocimiento
* **⬅️ Requiere comprender antes:** [[Train Test Split y Validacion Cruzada]]
* **➡️ Permite desbloquear después:** [[Matriz de Confusion Precision y Recall]], [[Curva ROC y AUC]]
