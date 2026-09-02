"""
arbol.py
Arbol de decision desde cero, siguiendo ID3 con entropia y ganancia de informacion.
Se incluye tambien el criterio Gini para comparar ambos al final en el reporte.
"""

import math


def entropia(conteo_positivos, conteo_negativos):
    """
    Criterio de impureza basado en teoria de la informacion.
    Formula a utilizar basado en diapositivas:  -p+ log2(p+) - p- log2(p-)

    Va de 0 a 1 cuando hay dos clases:
      0 = todos de la misma clase
      1 = grupo revuelto, mitad y mitad
    """
    total = conteo_positivos + conteo_negativos

    if total == 0:
        return 0.0

    resultado = 0.0
    for conteo in (conteo_positivos, conteo_negativos):
        # El if implementa  0 log2(0) = 0 
        if conteo > 0:
            proporcion = conteo / total
            resultado -= proporcion * math.log2(proporcion)

    return resultado


def gini(conteo_positivos, conteo_negativos):
    """
    Formula a seguir:  1 - (p+)^2 - (p-)^2

    Va de 0 a 0.5 cuando hay dos clases:
      0   = grupo puro
      0.5 = mitad y mitad

    No tinene la misma escals entonces no se pueden comparar los valores de gini con lo de entropia
    """
    total = conteo_positivos + conteo_negativos

    if total == 0:
        return 0.0

    proporcion_positivos = conteo_positivos / total
    proporcion_negativos = conteo_negativos / total

    return 1.0 - (proporcion_positivos ** 2 + proporcion_negativos ** 2)


def impureza(conteo_positivos, conteo_negativos, criterio="entropia"):
    """
    Sirve para que el resto del arbol no sepa ni le importe cual criterio se usa, solo llama a impuersa, ára que
    cuando se hagan las dos corridas, solo se cambie este parametro en un solo lugar en ves de mover el algoritmo
    recibe el criterio a usar decidido por el usuario
    """
    if criterio == "entropia":
        return entropia(conteo_positivos, conteo_negativos)
    elif criterio == "gini":
        return gini(conteo_positivos, conteo_negativos)
    else:
        raise ValueError(f"Criterio desconocido: {criterio}")

