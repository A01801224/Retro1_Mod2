# Retro1_Mod2

Momento de Retroalimentación: Módulo 2 — Implementación de una técnica de aprendizaje máquina sin el uso de un framework. (Portafolio Implementación)

**Matrícula:** A01801224
**Materia:** Módulo 2 – Aprendizaje Máquina (Prof. Uresti)

## Descripción

Implementación manual de un **Random Forest** para clasificación binaria.
El árbol de decisión (criterio Gini), el muestreo bootstrap, el submuestreo
de variables y la votación por mayoría están programados desde cero.

No se usa ninguna biblioteca de aprendizaje máquina. Pandas se usa únicamente
para leer y manipular la tabla de datos, y seaborn/matplotlib únicamente para
generar las gráficas del reporte.

## Dataset

**Online Shoppers Purchasing Intention Dataset** (UCI Machine Learning Repository).

12,330 sesiones de un sitio de comercio electrónico, cada una perteneciente a un
usuario distinto a lo largo de un periodo de un año. El objetivo es predecir si
la sesión terminó en compra (columna `Revenue`).

- Variables usadas: las 10 numéricas del dataset, más `Weekend` y `VisitorType`
  codificadas manualmente como 0/1.
- Variables descartadas: `Month`, `OperatingSystems`, `Browser`, `Region` y
  `TrafficType`, por ser códigos categóricos sin orden real. Un corte del tipo
  "Browser < 7" no tendría significado.
- Entrenamiento: 80% de las sesiones. Prueba: 20%.
- La separación usa semilla fija (42) para que los resultados sean reproducibles.
- El dataset no tiene valores faltantes.

Las clases están desbalanceadas: la mayoría de las sesiones no terminan en compra.
Por eso el reporte no se limita a accuracy e incluye recall y F1.

**Cita:** Sakar, C. & Kastro, Y. (2018). *Online Shoppers Purchasing Intention
Dataset*. UCI Machine Learning Repository. https://doi.org/10.24432/C5F88Q
Licencia Creative Commons Attribution 4.0 International (CC BY 4.0).

## Estructura

```
.
├── src/
│   ├── datos.py           # carga, codificación y separación train/test
│   ├── metricas.py        # matriz de confusión y métricas, calculadas a mano
│   ├── visualizacion.py   # gráficas del reporte
│   ├── arbol.py           # árbol de decisión implementado desde cero
│   ├── bosque.py          # random forest: bootstrap, N árboles y votación
│   └── main.py            # entrena, evalúa, compara y predice
├── data/
│   └── online_shoppers_intention.csv
├── resultados/            # gráficas generadas y reporte.pdf
├── requirements.txt
└── README.md
```

## Cómo ejecutar

Requiere Python 3.9 o superior.

```bash
# 1. Crear el entorno virtual
python -m venv .venv

# 2. Activarlo
.venv\Scripts\activate        # Windows
source .venv/bin/activate     # Mac o Linux

# 3. Instalar las dependencias
pip install -r requirements.txt

# 4. Correr el programa
python src/main.py
```

Cada módulo también se puede ejecutar por separado para probarlo:

```bash
python src/datos.py           # resumen del dataset
python src/metricas.py        # verificación de las fórmulas
python src/visualizacion.py   # genera las gráficas exploratorias
```

## Qué se implementó a mano

- Cálculo de impureza Gini
- Búsqueda del mejor punto de corte por variable
- Construcción recursiva del árbol y criterios de paro (profundidad máxima,
  mínimo de muestras por nodo, nodo puro)
- Muestreo bootstrap con reemplazo
- Submuestreo aleatorio de variables en cada nodo
- Votación por mayoría entre los árboles del bosque
- Codificación de las variables binarias y separación entrenamiento/prueba
- Matriz de confusión, accuracy, precision, recall, specificity y F1

## Resultados

Ver `resultados/reporte.pdf`.