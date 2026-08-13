---
title: "Overfitting y Bias-Variance Tradeoff"
type: concept
category: "concept"
module: "[[M03 - Evaluating & Interpreting Models]]"
source_lesson: "[[02-Overfitting and Underfitting]]"
tags: [concept, concept, ml-foundations]
prerequisites: ["[[Train Test Split y Validacion Cruzada]]"]
unlocks: ["[[Regularizacion L1 y L2]]", "[[Metricas de Evaluacion de Modelos]]"]
---

# 💡 Overfitting y Bias-Variance Tradeoff

> Pertenece a: **[[M03 - Evaluating & Interpreting Models]]** | Lección de Origen: **[[02-Overfitting and Underfitting]]**

---

### 📖 Definición Formal (Grounded)
Dilema fundamental: Underfitting (alto sesgo / modelo demasiado simple) vs Overfitting (alta varianza / modelo memoriza el ruido del train set y falla en test).

---

### 🧠 Analogía Intuitiva (Patrón DeepTutor)
> Underfitting es un estudiante que solo memorizó 1 fórmula; Overfitting es un estudiante que memorizó las respuestas exactas de memoria pero no entiende el concepto.

---

### 🎯 Regla de Decisión para Product Managers
> [!TIP]
> **Heurística de Producto:**
> Si la brecha entre el rendimiento en Train y Test es grande, el modelo tiene overfitting y destruirá valor en producción.

---

### ⚠️ Error Conceptual Común (Misconception)
> [!WARNING]
> Creer que minimizar el error en entrenamiento a cero siempre es el objetivo.

---

### 🔗 Navegación en el Grafo de Conocimiento
* **⬅️ Requiere comprender antes:** [[Train Test Split y Validacion Cruzada]]
* **➡️ Permite desbloquear después:** [[Regularizacion L1 y L2]], [[Metricas de Evaluacion de Modelos]]
