---
title: "Matriz de Confusion Precision y Recall"
type: concept
category: "design"
module: "[[M03 - Evaluating & Interpreting Models]]"
source_lesson: "[[05-Precision vs Recall Tradeoff]]"
tags: [concept, design, ml-foundations]
prerequisites: ["[[Metricas de Evaluacion de Modelos]]"]
unlocks: ["[[Curva ROC y AUC]]"]
---

# 💡 Matriz de Confusion Precision y Recall

> Pertenece a: **[[M03 - Evaluating & Interpreting Models]]** | Lección de Origen: **[[05-Precision vs Recall Tradeoff]]**

---

### 📖 Definición Formal (Grounded)
Matriz de 4 cuadrantes (TP, FP, TN, FN). Precision = TP/(TP+FP) (calidad de alertas). Recall = TP/(TP+FN) (cobertura/sensibilidad).

---

### 🧠 Analogía Intuitiva (Patrón DeepTutor)
> Precision: Si el radar suena, ¿cuántas veces es un avión enemigo real? Recall: De todos los aviones enemigos que volaron, ¿cuántos detectó el radar?

---

### 🎯 Regla de Decisión para Product Managers
> [!TIP]
> **Heurística de Producto:**
> En detección de enfermedades/fraude priorizar Recall; en recomendaciones/spam priorizar Precision.

---

### ⚠️ Error Conceptual Común (Misconception)
> [!WARNING]
> Creer que se pueden maximizar Precision y Recall al 100% simultáneamente sin costo.

---

### 🔗 Navegación en el Grafo de Conocimiento
* **⬅️ Requiere comprender antes:** [[Metricas de Evaluacion de Modelos]]
* **➡️ Permite desbloquear después:** [[Curva ROC y AUC]]
