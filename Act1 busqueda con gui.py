import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import time

def busqueda_lineal(lista, x):
    """
    Busca el elemento x en la lista usando busqueda lineal.
    Devuelve el indice si lo encuentra, o -1 si no esta.
    """
    for i, elemento in enumerate(lista):
        if elemento == x:
            return i  # Retorna el indice donde se encontro
    return -1  # Si no se encuentra, retorna -1

def busqueda_binaria(lista, x):
    """
    Busca el elemento x en la lista usando busqueda binaria.
    Ordena la lista antes de buscar.
    Devuelve el indice si lo encuentra, o -1 si no esta.
    """
    lista_ordenada = sorted(lista)
    izquierda = 0
    derecha = len(lista_ordenada) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == x:
            return medio  # Retorna el indice en la lista ordenada
        elif lista_ordenada[medio] < x:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def generar_lista(tamano):
    """
    Genera una lista de enteros aleatorios unicos (no ordenada).
    Parametro:
        tamano (int): tamano de la lista (100, 1000, 10000, 100000)
    Retorna:
        lista (list)
    """
    lista = np.random.choice(range(tamano * 10), size=tamano, replace=False)
    return lista.tolist()

def medir_tiempo_busqueda(funcion_busqueda, lista, x, repeticiones=5):
    """
    Mide el tiempo promedio de ejecucion de una funcion de busqueda.
    Parametros:
        funcion_busqueda: funcion a ejecutar (busqueda_lineal o busqueda_binaria)
        lista: lista de datos
        x: valor a buscar
        repeticiones: numero de veces que se repite la busqueda
    Retorna:
        (indice encontrado, tiempo_promedio_ms)
    """
    tiempos = []
    resultado = None
    for _ in range(repeticiones):
        inicio = time.perf_counter()
        resultado = funcion_busqueda(lista, x)
        fin = time.perf_counter()
        tiempos.append((fin - inicio) * 1000)  # Convierte a milisegundos
    tiempo_promedio = sum(tiempos) / repeticiones
    return resultado, tiempo_promedio

class BusquedaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Comparacion de Busquedas")
        self.lista = []
        self.tamano_var = tk.IntVar(value=100)
        self.valor_var = tk.StringVar()
        self.resultado_var = tk.StringVar()
        self.tiempo_var = tk.StringVar()
        
        # Frame de configuracion
        frame_config = ttk.LabelFrame(root, text="Configuracion de datos")
        frame_config.pack(padx=10, pady=5, fill="x")
        
        ttk.Label(frame_config, text="Tamano de la lista:").pack(side="left", padx=5)
        tamano_combo = ttk.Combobox(frame_config, textvariable=self.tamano_var, state="readonly")
        tamano_combo["values"] = (100, 1000, 10000, 100000)
        tamano_combo.pack(side="left", padx=5)
        
        btn_generar = ttk.Button(frame_config, text="Generar datos", command=self.generar_datos)
        btn_generar.pack(side="left", padx=5)
        
        # Frame de busqueda
        frame_busqueda = ttk.LabelFrame(root, text="Busqueda")
        frame_busqueda.pack(padx=10, pady=5, fill="x")
        
        ttk.Label(frame_busqueda, text="Valor a buscar:").pack(side="left", padx=5)
        entry_valor = ttk.Entry(frame_busqueda, textvariable=self.valor_var, width=10)
        entry_valor.pack(side="left", padx=5)
        
        btn_lineal = ttk.Button(frame_busqueda, text="Busqueda lineal", command=self.buscar_lineal)
        btn_lineal.pack(side="left", padx=5)
        
        btn_binaria = ttk.Button(frame_busqueda, text="Busqueda binaria", command=self.buscar_binaria)
        btn_binaria.pack(side="left", padx=5)
        
        # Frame de resultados
        frame_resultados = ttk.LabelFrame(root, text="Resultados")
        frame_resultados.pack(padx=10, pady=5, fill="x")
        
        ttk.Label(frame_resultados, text="Tamano de la lista:").grid(row=0, column=0, sticky="w", padx=5)
        self.lbl_tamano = ttk.Label(frame_resultados, textvariable=self.tamano_var)
        self.lbl_tamano.grid(row=0, column=1, sticky="w", padx=5)
        
        ttk.Label(frame_resultados, text="Resultado:").grid(row=1, column=0, sticky="w", padx=5)
        self.lbl_resultado = ttk.Label(frame_resultados, textvariable=self.resultado_var)
        self.lbl_resultado.grid(row=1, column=1, sticky="w", padx=5)
        
        ttk.Label(frame_resultados, text="Tiempo (ms):").grid(row=2, column=0, sticky="w", padx=5)
        self.lbl_tiempo = ttk.Label(frame_resultados, textvariable=self.tiempo_var)
        self.lbl_tiempo.grid(row=2, column=1, sticky="w", padx=5)
    
        # Frame para la grafica
        frame_grafica = ttk.LabelFrame(root, text="Comparacion grafica")
        frame_grafica.pack(padx=10, pady=5, fill="both", expand=True)
        self.frame_grafica = frame_grafica

        btn_grafica = ttk.Button(frame_grafica, text="Mostrar comparacion", command=self.mostrar_comparacion)
        btn_grafica.pack(pady=5)

        self.canvas = None  # Se usara para la grafica

    def generar_datos(self):
        tamano = self.tamano_var.get()
        self.lista = generar_lista(tamano)
        paso = max(1, tamano // 10)
        muestra = ', '.join(str(self.lista[i]) for i in range(0, tamano, paso))
        messagebox.showinfo(
            "Datos generados",
            f"Lista de tamaño {tamano} generada correctamente.\nEjemplo de valores: {muestra}"
        )
        self.resultado_var.set("")
        self.tiempo_var.set("")
    
    def buscar_lineal(self):
        if not self.lista:
            messagebox.showwarning("Advertencia", "Primero genera los datos.")
            return
        try:
            x = int(self.valor_var.get())
        except ValueError:
            messagebox.showerror("Error", "Introduce un valor numerico para buscar.")
            return
        indice, tiempo = medir_tiempo_busqueda(busqueda_lineal, self.lista, x)
        if indice != -1:
            self.resultado_var.set(f"Encontrado en indice {indice}")
        else:
            self.resultado_var.set("No encontrado")
        self.tiempo_var.set(f"{tiempo:.3f}")
    
    def buscar_binaria(self):
        if not self.lista:
            messagebox.showwarning("Advertencia", "Primero genera los datos.")
            return
        try:
            x = int(self.valor_var.get())
        except ValueError:
            messagebox.showerror("Error", "Introduce un valor numerico para buscar.")
            return
        indice, tiempo = medir_tiempo_busqueda(busqueda_binaria, self.lista, x)
        if indice != -1:
            self.resultado_var.set(f"Encontrado en indice {indice} (lista ordenada)")
        else:
            self.resultado_var.set("No encontrado")
        self.tiempo_var.set(f"{tiempo:.3f}")

    def mostrar_comparacion(self):
        tamanos = [100, 1000, 10000, 100000]
        tiempos_lineal = []
        tiempos_binaria = []
        valor_busqueda = 0  # Valor fijo para comparar

        for tam in tamanos:
            lista = generar_lista(tam)
            _, tiempo_l = medir_tiempo_busqueda(busqueda_lineal, lista, valor_busqueda)
            _, tiempo_b = medir_tiempo_busqueda(busqueda_binaria, lista, valor_busqueda)
            tiempos_lineal.append(tiempo_l)
            tiempos_binaria.append(tiempo_b)

        # Crear la grafica
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(tamanos, tiempos_lineal, marker='o', label="Busqueda lineal")
        ax.plot(tamanos, tiempos_binaria, marker='o', label="Busqueda binaria")
        ax.set_xscale('log')
        ax.set_xlabel("Tamano de la lista")
        ax.set_ylabel("Tiempo promedio (ms)")
        ax.set_title("Comparacion de tiempos de busqueda")
        ax.legend()
        ax.grid(True)

        # Mostrar la grafica en la GUI
        if self.canvas:
            self.canvas.get_tk_widget().destroy()
        self.canvas = FigureCanvasTkAgg(fig, master=self.frame_grafica)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = BusquedaGUI(root)
    root.mainloop()

