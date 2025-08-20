Objetivo
Comparar el desempeño de dos algoritmos de búsqueda (lineal y binaria) sobre listas de enteros aleatorios de diferentes tamaños, midiendo el tiempo de ejecución promedio de cada algoritmo.

Tamaños de las listas probadas
Se realizaron experimentos con los siguientes tamaños de lista:

100 elementos
1,000 elementos
10,000 elementos
100,000 elementos
Cada lista se genera con números enteros aleatorios únicos en el rango correspondiente.

Algoritmos evaluados
Búsqueda lineal:
Recorre la lista elemento por elemento hasta encontrar el valor buscado o terminar la lista.

Búsqueda binaria:
Ordena la lista y realiza la búsqueda dividiendo el rango en mitades sucesivas.

Repeticiones por experimento
Para cada combinación de algoritmo y tamaño de lista, se realizaron 5 repeticiones de la búsqueda.
En cada repetición se mide el tiempo de ejecución usando time.perf_counter().
El tiempo reportado es el promedio de las 5 ejecuciones.

Valor buscado
En los experimentos de comparación gráfica, el valor buscado es 0 (puede o no estar presente en la lista, lo que simula un caso promedio).

Resultados presentados
Gráfica comparativa:
Se muestra una gráfica en la interfaz que compara los tiempos promedio (en milisegundos) de ambos algoritmos para cada tamaño de lista.

Resultados individuales:
Al buscar un valor específico, se muestra:

Tamaño de la lista utilizada
Si el valor fue encontrado (índice o “No encontrado”)
Tiempo de ejecución exacto en milisegundos

Validaciones
Se valida que el usuario genere los datos antes de buscar.
Se valida que el valor a buscar sea numérico.
Se muestra una muestra representativa de los datos generados para facilitar la selección de valores de búsqueda.# Analisis-de-algoritmos
