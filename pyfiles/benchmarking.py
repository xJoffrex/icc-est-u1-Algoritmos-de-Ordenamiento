import random
import time

class Benchmarking:
    
    def __init__(self):
        print("Benchmarking instanciado")
        self.arreglo_base = self.build_arreglo(100000)
        
    def medir_tiempo(self, funcion, arreglo):
        inicio = time.perf_counter()
        funcion(arreglo)
        fin = time.perf_counter()
        return fin - inicio
    
    def build_arreglo(self, tamano):
        arreglo = [random.randint(0,99999) for _ in range(tamano) ]
        return arreglo
    
    def get_subarreglo(self, tamano):
        return self.arreglo_base[:tamano]