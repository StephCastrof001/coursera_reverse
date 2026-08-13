---
title: "Train Test Split y Validacion Cruzada"
type: concept
category: "procedure"
module: "[[M02 - The Modeling Process]]"
source_lesson: "[[06-Splitting Data]]"
tags: [concept, procedure, ml-foundations]
prerequisites: ["[[El Ciclo de Vida de Ciencia de Datos]]"]
unlocks: ["[[Overfitting y Bias-Variance Tradeoff]]", "[[Metricas de Evaluacion de Modelos]]"]
---

# 💡 Train Test Split y Validacion Cruzada

> Pertenece a: **[[M02 - The Modeling Process]]** | Lección de Origen: **[[06-Splitting Data]]**

---

### 📖 Definición Formal (Grounded)
División estricta del dataset en conjuntos de Entrenamiento (Train), Validación (Validation) y Prueba (Test / Holdout) para evaluar la generalización sobre datos nunca vistos.

---

### 🧠 Analogía Intuitiva (Patrón DeepTutor)
> Entrenar con los ejercicios del libro y evaluar con un examen que contiene preguntas nuevas.

---

### 🎯 Regla de Decisión para Product Managers
> [!TIP]
> **Heurística de Producto:**
> Nunca evaluar el éxito de un modelo con los mismos datos con los que fue entrenado (Data Leakage mortal).

---

### ⚠️ Error Conceptual Común (Misconception)
> [!WARNING]
> Pensar que un 99% de precisión en el set de entrenamiento garantiza éxito en producción.

---

### 🔗 Navegación en el Grafo de Conocimiento
* **⬅️ Requiere comprender antes:** [[El Ciclo de Vida de Ciencia de Datos]]
* **➡️ Permite desbloquear después:** [[Overfitting y Bias-Variance Tradeoff]], [[Metricas de Evaluacion de Modelos]]
