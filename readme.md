# Tarea 1 Visualización de datos EIN092B UTFSM 2025-2

Generación de data storytelling a partir de un dataset escogido, considerando las restricciones principales sobre:
-[x] Al menos 3000 registros
-[x] Al menos cuatro variables de tipo numéricas
-[x] Debe contar con progración cronológica
-[x] Dataset autocontenido en términos de explicación

Mas detalles en [Enunciado](<Visualización - Tarea 1.pdf>)

## Requerimientos

- Python 3.9+
- Dataset a analizar: [Titulados de educación superior chile 2007 a 2024](https://www.kaggle.com/datasets/gustavoreyesc/titulados-en-educacin-superior-chile-2007-2024).

## Estructura del repositorio

```text
EIN092B-Visualizacion-Tarea-1/
├── exports/            # carpeta con gráficos elaborados
├── dataset_pipeline.py # Pipeline de carga y limpieza del dataset
├── *.py                # archivos de exploración, creación de gráficos
├── main.py             # ejecución principal de script anteriores
├── notebook.ipynb      # jupyter notebook como alternativa a main.py
├── requirements.txt    # librerias requeridas para ejecutar los scripts ya sea en un venv o local
├── readme.md           # este archivo
├── TITULADO_2007-2024_web_19_05_2025_E.csv # dataset a analizar, disponible para descarga en sección anterior
├── Visualización - Tarea 1.pdf # enunciado tarea
└── LICENSE             # Licencia
```

## Ejecución del repositorio

1. Opcionalmente crear y activar un ambiente virtual con:
```bash
> python -m venv venv
> .\venv\Scripts\activate
```
2. Instalar los requerimientos con:

```bash
pip install -r requirements.txt
```

3. Ejecutar:
```bash
py main.py
``` 
o bien usar `notebook.ipynb` que requiere tener Jupyter instalado.

## Presentación dedicada

- (Enlace a definir) + uso de exportaciones generadas

## Integrantes:
- Rafael Salinas
- Javier Torres