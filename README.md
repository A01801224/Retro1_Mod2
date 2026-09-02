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

Pima Indians Diabetes: 768 registros, 8 variables numéricas, clasificación binaria
(0 = no diabetes, 1 = diabetes). Distribución de clases: 500 negativos, 268 positivos.

- Entrenamiento: 614 registros (80%)
- Prueba: 154 registros (20%)
- La separación usa semilla fija (42) para que los resultados sean reproducibles.

Nota sobre calidad de los datos: varias columnas usan 0 como marcador de dato
faltante. Insulina tiene 48.7% de ceros y GrosorPiel 29.6%. Esto se documenta
en el reporte.

## Estructura

```
.
├── src/
│   ├── datos.py           # carga del csv, exploración y separación train/test
│   ├── metricas.py        # matriz de confusión y métricas, calculadas a mano
│   ├── visualizacion.py   # gráficas del reporte
│   ├── arbol.py           # árbol de decisión implementado desde cero
│   ├── bosque.py          # random forest: bootstrap, N árboles y votación
│   └── main.py            # entrena, evalúa, compara y predice
├── data/
│   └── pima-indians-diabetes.csv
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
- Separación entrenamiento/prueba
- Matriz de confusión, accuracy, precision, recall, specificity y F1

## Resultados

Ver `resultados/reporte.pdf`.
