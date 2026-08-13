---
title: "Grafo Formal de Prerrequisitos (KST)"
type: graph
tags: [kst, knowledge-space-theory, dag, prerequisites]
---

# 🕸️ Grafo de Espacio de Conocimiento (KST DAG)

> Modelo formal de relaciones de implicación (*surmise relations*). Cada flecha `A --> B` indica que el concepto `A` es un **prerrequisito epistemológico estricto** para dominar `B`.

```mermaid
graph TD
    Paradigma_de_Machine_Learning["[[Paradigma de Machine Learning]]"] --> Estructura_de_Datos_en_ML["[[Estructura de Datos en ML]]"]
    Paradigma_de_Machine_Learning["[[Paradigma de Machine Learning]]"] --> Modelo_Matematico_y_Parametros["[[Modelo Matematico y Parametros]]"]
    Estructura_de_Datos_en_ML["[[Estructura de Datos en ML]]"] --> Aprendizaje_Supervisado_vs_No_Supervisado["[[Aprendizaje Supervisado vs No Supervisado]]"]
    Modelo_Matematico_y_Parametros["[[Modelo Matematico y Parametros]]"] --> Aprendizaje_Supervisado_vs_No_Supervisado["[[Aprendizaje Supervisado vs No Supervisado]]"]
    Aprendizaje_Supervisado_vs_No_Supervisado["[[Aprendizaje Supervisado vs No Supervisado]]"] --> Clasificacion_vs_Regresion["[[Clasificacion vs Regresion]]"]
    Aprendizaje_Supervisado_vs_No_Supervisado["[[Aprendizaje Supervisado vs No Supervisado]]"] --> Clustering_y_Reduccion_de_Dimension["[[Clustering y Reduccion de Dimension]]"]
    Aprendizaje_Supervisado_vs_No_Supervisado["[[Aprendizaje Supervisado vs No Supervisado]]"] --> Correlacion_vs_Causalidad_en_ML["[[Correlacion vs Causalidad en ML]]"]
    Correlacion_vs_Causalidad_en_ML["[[Correlacion vs Causalidad en ML]]"] --> El_Ciclo_de_Vida_de_Ciencia_de_Datos["[[El Ciclo de Vida de Ciencia de Datos]]"]
    El_Ciclo_de_Vida_de_Ciencia_de_Datos["[[El Ciclo de Vida de Ciencia de Datos]]"] --> Ingenieria_de_Caracteristicas_(Feature_Engineering)["[[Ingenieria de Caracteristicas (Feature Engineering)]]"]
    El_Ciclo_de_Vida_de_Ciencia_de_Datos["[[El Ciclo de Vida de Ciencia de Datos]]"] --> Train_Test_Split_y_Validacion_Cruzada["[[Train Test Split y Validacion Cruzada]]"]
    Ingenieria_de_Caracteristicas_(Feature_Engineering)["[[Ingenieria de Caracteristicas (Feature Engineering)]]"] --> Train_Test_Split_y_Validacion_Cruzada["[[Train Test Split y Validacion Cruzada]]"]
    Train_Test_Split_y_Validacion_Cruzada["[[Train Test Split y Validacion Cruzada]]"] --> Overfitting_y_Bias-Variance_Tradeoff["[[Overfitting y Bias-Variance Tradeoff]]"]
    Train_Test_Split_y_Validacion_Cruzada["[[Train Test Split y Validacion Cruzada]]"] --> Metricas_de_Evaluacion_de_Modelos["[[Metricas de Evaluacion de Modelos]]"]
    Overfitting_y_Bias-Variance_Tradeoff["[[Overfitting y Bias-Variance Tradeoff]]"] --> Regularizacion_L1_y_L2["[[Regularizacion L1 y L2]]"]
    Overfitting_y_Bias-Variance_Tradeoff["[[Overfitting y Bias-Variance Tradeoff]]"] --> Metricas_de_Evaluacion_de_Modelos["[[Metricas de Evaluacion de Modelos]]"]
    Metricas_de_Evaluacion_de_Modelos["[[Metricas de Evaluacion de Modelos]]"] --> Matriz_de_Confusion_Precision_y_Recall["[[Matriz de Confusion Precision y Recall]]"]
    Metricas_de_Evaluacion_de_Modelos["[[Metricas de Evaluacion de Modelos]]"] --> Curva_ROC_y_AUC["[[Curva ROC y AUC]]"]
    Matriz_de_Confusion_Precision_y_Recall["[[Matriz de Confusion Precision y Recall]]"] --> Curva_ROC_y_AUC["[[Curva ROC y AUC]]"]
    Curva_ROC_y_AUC["[[Curva ROC y AUC]]"] --> Modelos_Lineales_y_Regresion["[[Modelos Lineales y Regresion]]"]
    Modelos_Lineales_y_Regresion["[[Modelos Lineales y Regresion]]"] --> Regresion_Logistica["[[Regresion Logistica]]"]
    Modelos_Lineales_y_Regresion["[[Modelos Lineales y Regresion]]"] --> Regularizacion_L1_y_L2["[[Regularizacion L1 y L2]]"]
    Regresion_Logistica["[[Regresion Logistica]]"] --> Arboles_de_Decision_y_Ensembles["[[Arboles de Decision y Ensembles]]"]
    Regularizacion_L1_y_L2["[[Regularizacion L1 y L2]]"] --> Arboles_de_Decision_y_Ensembles["[[Arboles de Decision y Ensembles]]"]
    Arboles_de_Decision_y_Ensembles["[[Arboles de Decision y Ensembles]]"] --> Random_Forest_y_Gradient_Boosting["[[Random Forest y Gradient Boosting]]"]
    Arboles_de_Decision_y_Ensembles["[[Arboles de Decision y Ensembles]]"] --> K-Means_Clustering_y_Segmentacion["[[K-Means Clustering y Segmentacion]]"]
    Random_Forest_y_Gradient_Boosting["[[Random Forest y Gradient Boosting]]"] --> Deep_Learning_y_Redes_Neuronales["[[Deep Learning y Redes Neuronales]]"]
    K-Means_Clustering_y_Segmentacion["[[K-Means Clustering y Segmentacion]]"] --> Deep_Learning_y_Redes_Neuronales["[[Deep Learning y Redes Neuronales]]"]
    Deep_Learning_y_Redes_Neuronales["[[Deep Learning y Redes Neuronales]]"] --> Redes_Convolucionales_y_Recurrentes["[[Redes Convolucionales y Recurrentes]]"]
    Deep_Learning_y_Redes_Neuronales["[[Deep Learning y Redes Neuronales]]"] --> Diseno_de_Arquitecturas_de_Producto_con_IA["[[Diseno de Arquitecturas de Producto con IA]]"]
```

---

## 📋 Matriz de Dependencias

| Concepto | Módulo | Prerrequisitos Obligatorios | Habilidades que Desbloquea |
| :--- | :--- | :--- | :--- |
| **[[Paradigma de Machine Learning]]** | [[M01 - What is Machine Learning]] | *(Punto de Entrada)* | [[Estructura de Datos en ML]], [[Modelo Matematico y Parametros]] |
| **[[Estructura de Datos en ML]]** | [[M01 - What is Machine Learning]] | [[Paradigma de Machine Learning]] | [[Aprendizaje Supervisado vs No Supervisado]] |
| **[[Modelo Matematico y Parametros]]** | [[M01 - What is Machine Learning]] | [[Paradigma de Machine Learning]] | [[Aprendizaje Supervisado vs No Supervisado]] |
| **[[Aprendizaje Supervisado vs No Supervisado]]** | [[M01 - What is Machine Learning]] | [[Estructura de Datos en ML]], [[Modelo Matematico y Parametros]] | [[Clasificacion vs Regresion]], [[Clustering y Reduccion de Dimension]], [[Correlacion vs Causalidad en ML]] |
| **[[Correlacion vs Causalidad en ML]]** | [[M01 - What is Machine Learning]] | [[Aprendizaje Supervisado vs No Supervisado]] | [[El Ciclo de Vida de Ciencia de Datos]] |
| **[[El Ciclo de Vida de Ciencia de Datos]]** | [[M02 - The Modeling Process]] | [[Correlacion vs Causalidad en ML]] | [[Ingenieria de Caracteristicas (Feature Engineering)]], [[Train Test Split y Validacion Cruzada]] |
| **[[Ingenieria de Caracteristicas (Feature Engineering)]]** | [[M02 - The Modeling Process]] | [[El Ciclo de Vida de Ciencia de Datos]] | [[Train Test Split y Validacion Cruzada]] |
| **[[Train Test Split y Validacion Cruzada]]** | [[M02 - The Modeling Process]] | [[El Ciclo de Vida de Ciencia de Datos]] | [[Overfitting y Bias-Variance Tradeoff]], [[Metricas de Evaluacion de Modelos]] |
| **[[Overfitting y Bias-Variance Tradeoff]]** | [[M03 - Evaluating & Interpreting Models]] | [[Train Test Split y Validacion Cruzada]] | [[Regularizacion L1 y L2]], [[Metricas de Evaluacion de Modelos]] |
| **[[Metricas de Evaluacion de Modelos]]** | [[M03 - Evaluating & Interpreting Models]] | [[Train Test Split y Validacion Cruzada]] | [[Matriz de Confusion Precision y Recall]], [[Curva ROC y AUC]] |
| **[[Matriz de Confusion Precision y Recall]]** | [[M03 - Evaluating & Interpreting Models]] | [[Metricas de Evaluacion de Modelos]] | [[Curva ROC y AUC]] |
| **[[Curva ROC y AUC]]** | [[M03 - Evaluating & Interpreting Models]] | [[Matriz de Confusion Precision y Recall]] | [[Modelos Lineales y Regresion]] |
| **[[Modelos Lineales y Regresion]]** | [[M04 - Linear Models]] | [[Curva ROC y AUC]], [[Overfitting y Bias-Variance Tradeoff]] | [[Regresion Logistica]], [[Regularizacion L1 y L2]] |
| **[[Regresion Logistica]]** | [[M04 - Linear Models]] | [[Modelos Lineales y Regresion]] | [[Arboles de Decision y Ensembles]] |
| **[[Regularizacion L1 y L2]]** | [[M04 - Linear Models]] | [[Modelos Lineales y Regresion]], [[Overfitting y Bias-Variance Tradeoff]] | [[Arboles de Decision y Ensembles]] |
| **[[Arboles de Decision y Ensembles]]** | [[M05 - Trees, Ensemble Models and Clustering]] | [[Regresion Logistica]] | [[Random Forest y Gradient Boosting]], [[K-Means Clustering y Segmentacion]] |
| **[[Random Forest y Gradient Boosting]]** | [[M05 - Trees, Ensemble Models and Clustering]] | [[Arboles de Decision y Ensembles]] | [[Deep Learning y Redes Neuronales]] |
| **[[K-Means Clustering y Segmentacion]]** | [[M05 - Trees, Ensemble Models and Clustering]] | [[Arboles de Decision y Ensembles]] | [[Deep Learning y Redes Neuronales]] |
| **[[Deep Learning y Redes Neuronales]]** | [[M06 - Deep Learning & Course Project]] | [[Random Forest y Gradient Boosting]] | [[Redes Convolucionales y Recurrentes]], [[Diseno de Arquitecturas de Producto con IA]] |
| **[[Diseno de Arquitecturas de Producto con IA]]** | [[M06 - Deep Learning & Course Project]] | [[Deep Learning y Redes Neuronales]] | *(Nodo Terminal / Maestría)* |
