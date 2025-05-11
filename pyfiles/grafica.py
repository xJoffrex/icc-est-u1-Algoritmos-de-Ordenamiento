import matplotlib.pyplot as plt

class GraficaOrdenamiento:
    def __init__(self):
        self.tamanios = [5000, 10000, 30000, 50000, 100000]
        self.tiempos_by_metodo = {
            "Burbuja": [0.513344, 1.993546, 18.719982, 53.932508, 244.212746],
            "Burbuja Mejorado": [0.797848, 3.186857, 31.010048, 86.218198, 431.087030],
            "Selección": [0.355991, 1.337096, 12.416162, 41.061351, 188.767978],
            "Inserción": [0.332227, 1.349337, 12.359031, 45.217801, 153.320192],
            "Shell": [0.007603, 0.017624, 0.065137, 0.227315, 0.311907]
        }

    def mostrar_grafica(self):
        plt.figure(figsize=(10, 6))
        
        estilos = ['-', '--', '-.', ':', '-.']
        colores = ['blue', 'green', 'red', 'purple', 'orange']

        for i, (nombre, tiempos) in enumerate(self.tiempos_by_metodo.items()):
            plt.plot(self.tamanios, tiempos, label=nombre, marker="o", color=colores[i], linestyle=estilos[i])

        plt.title("Comparación de tiempo para cada método de ordenamiento")
        plt.xlabel("Tamaño de los arreglos")
        plt.ylabel("Tiempo de Ejecución (s)")
        plt.legend()
        plt.grid(True)
        plt.show()