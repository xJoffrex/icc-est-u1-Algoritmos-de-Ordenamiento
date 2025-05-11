from matplotlib import pyplot as plt
import benchmarking as bm
from metodos_ordenamiento import MetodosOrdenamiento
import grafica as gfc


if __name__ == "__main__":
    print("Funciona")
    bench = bm.Benchmarking()
    metodosO = MetodosOrdenamiento()
    grafica = gfc.GraficaOrdenamiento() ## Muestra directamente la imagen con los valores que ya listamos anteriormente
    grafica.mostrar_grafica()
    
    
    tamanios = [5000, 10000, 30000,50000,100000]
    resultados =[]
    
    
    for tam in tamanios:
        
        arreglo_base = bench.get_subarreglo(tam)
        
        metodos_dic = {
        "burbuja": metodosO.sort_bubble,
        "burbuja_mejorado": metodosO.sort_burbuja_mejorado_optimizado,
        "seleccion": metodosO.sort_seleccion,
        "insercion": metodosO.sort_insercion,
        "shell":metodosO.sort_shell,
    }
    
    
    
        for nombre, fun_metodo in metodos_dic.items():
            tiempo_reusltado = bench.medir_tiempo(fun_metodo,arreglo_base)
            tupla_resultado = (tam, nombre, tiempo_reusltado)
            resultados.append(tupla_resultado)
            
    for tam, nombre, tiempo in resultados:
        print(f"Tamaño: {tam}, nombre metodo: {nombre}, tiempo: {tiempo:.6f} segundos")
            
   
    tiempos_by_metodo = {
        "burbuja": [],
        "burbuja_mejorado": [],
        "seleccion": [],
        "insercion": [],
        "shell":[],
    } 
    
    
    for tam, nombre, tiempo in resultados:
        tiempos_by_metodo[nombre].append(tiempo)
        
