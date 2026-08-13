---
title: "Regularizacion L1 y L2"
type: concept
category: "procedure"
module: "[[M04 - Linear Models]]"
source_lesson: "[[05-Regularization]]"
tags: [concept, procedure, ml-foundations]
prerequisites: ["[[Modelos Lineales y Regresion]]", "[[Overfitting y Bias-Variance Tradeoff]]"]
unlocks: ["[[Arboles de Decision y Ensembles]]"]
---

# 💡 Regularizacion L1 y L2

> Pertenece a: **[[M04 - Linear Models]]** | Lección de Origen: **[[05-Regularization]]**

---

### 📖 Definición Formal (Grounded)
Técnicas de penalización en la función de pérdida (Lasso/L1 reduce pesos a cero seleccionando features; Ridge/L2 encoge los pesos evitando magnitudes gigantes) para combatir el overfitting.

---

### 🧠 Analogía Intuitiva (Patrón DeepTutor)
> Ponerle un impuesto al modelo por cada feature innecesariamente compleja que intente usar.

---

### 🎯 Regla de Decisión para Product Managers
> [!TIP]
> **Heurística de Producto:**
> L1 (Lasso) es excelente para selección automática de características cuando tienes miles de variables.

---

### ⚠️ Error Conceptual Común (Misconception)
> [!WARNING]
> Pensar que la regularización mejora el ajuste en entrenamiento; intencionalmente lo empeora para ganar generalización.

---

### 🔗 Navegación en el Grafo de Conocimiento
* **⬅️ Requiere comprender antes:** [[Modelos Lineales y Regresion]], [[Overfitting y Bias-Variance Tradeoff]]
* **➡️ Permite desbloquear después:** [[Arboles de Decision y Ensembles]]
