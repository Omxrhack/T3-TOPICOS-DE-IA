# TAREA DE VALIDACIÓN III – Algoritmos Genéticos

## Módulo III – Algoritmos Genéticos
**Alumnos:** Omar Bermejo Osuna y Diego Alberto Araujo  


---

## Objetivo General

El propósito de esta tarea es **validar la comprensión y habilidades prácticas** en el uso de **algoritmos genéticos (AG)** mediante la **reconstrucción, documentación, modularización y prueba** de un programa en Python.

Se implementa un **Algoritmo Genético (AG)** completo para la optimización de una función matemática, demostrando la correcta aplicación de los principios de **evolución, selección, cruce y mutación**.

---

## Descripción del Proyecto

El proyecto desarrolla un **Algoritmo Genético real-codificado** para maximizar la función:

\[
f(x) = \sum_{i=1}^{n} (x_i \cdot \sin(x_i))
\]

donde cada gen \( x_i \) pertenece al rango \([0, 10]\).


---

## Estructura del Proyecto

```
ga_validacion_III/
├── ga/
│   ├── __init__.py             # Inicialización del paquete
│   ├── fitness.py              # Funciones de aptitud
│   ├── population.py           # Clases Individual y Population
│   ├── selection.py            # Métodos de selección (torneo y ruleta)
│   ├── crossover.py            # Métodos de cruce (1 punto y aritmético)
│   ├── mutation.py             # Métodos de mutación (gaussiana, bitflip)
│   └── ga.py                   # Clase GeneticAlgorithm y configuración
│
├── tests/
│   ├── test_fitness.py         # Pruebas unitarias de función de aptitud
│   ├── test_selection.py       # Pruebas del proceso de selección
│   ├── test_crossover_mutation.py # Pruebas de cruce y mutación
│   └── test_ga_integration.py  # Prueba de integración completa
│
├── main.py                     # Script principal de ejecución
├── README.md                   # Documento de referencia (este archivo)
├── requirements.txt            # Dependencias
└── RESULTADOS.txt              # Resultado de la corrida de ejemplo
```

---

## Instalación y Ejecución

### Clonar o descomprimir el proyecto
```bash
git clone https://github.com/usuario/algoritmos-geneticos.git
cd ga_validacion_III
```
O simplemente descomprime el archivo `TAREA_VALIDACION_III.zip`.

### Instalar dependencias
```bash
pip install -r requirements.txt
```

### Ejecutar el algoritmo
```bash
python main.py
```

El programa mostrará en consola el **mejor individuo** y su **valor de aptitud**, además de registrar los resultados en `RESULTADOS.txt`.

---

## Configuración Personalizable

La configuración del algoritmo se define en la clase `GAConfig` dentro de `main.py`.  
Puedes ajustar parámetros como:

| Parámetro | Descripción | Valor por defecto |
|------------|--------------|------------------|
| `pop_size` | Tamaño de la población | 80 |
| `genome_length` | Número de genes por individuo | 10 |
| `generations` | Número de iteraciones evolutivas | 120 |
| `mutation_rate` | Probabilidad de mutación | 0.12 |
| `mutation_sigma` | Desviación estándar de mutación gaussiana | 0.25 |
| `crossover_rate` | Probabilidad de cruce | 0.9 |
| `crossover_alpha` | Factor de mezcla del cruce aritmético | 0.55 |
| `elitism` | Número de individuos que pasan sin cambios | 2 |
| `low` y `high` | Rango de valores posibles de los genes | 0 – 10 |

---

## Ejemplo de Salida (RESULTADOS.txt)

```
RESULTADOS — corrida de ejemplo
Mejor aptitud: 51.038182
Mejores genes: [2.1191 7.9249 7.9247 7.9293 8.0233 7.9289 2.1949 7.9749]
Primer valor histórico: 27.949976
Último valor histórico: 51.038182
Longitud del historial: 61
```

---

## Pruebas 

El proyecto incluye un conjunto de **pruebas unitarias y de integración** en la carpeta `tests/`.

### Ejecución de pruebas:
```bash
pytest tests/
```

### Cobertura de las pruebas:
- **`test_fitness.py`** → Valida resultados esperados de la función de aptitud.  
- **`test_selection.py`** → Verifica que la selección favorezca a los individuos más aptos.  
- **`test_crossover_mutation.py`** → Comprueba que el cruce y la mutación respeten límites y coherencia genética.  
- **`test_ga_integration.py`** → Confirma que el AG mejora su rendimiento a lo largo de las generaciones.

---

