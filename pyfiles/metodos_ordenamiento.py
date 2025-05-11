
class MetodosOrdenamiento:
    def sort_bubble(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            for j in range(i + 1,n):
                if arreglo[i] > arreglo[j]:
                    arreglo[i], arreglo[j] = arreglo[j],arreglo[i]
                    #aux = arreglo[i]
                    #arreglo[i] = arreglo[j]
                    #arreglo[j] = aux
        return arreglo
    
    def sort_burbuja_mejorado_optimizado(self,array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            bol = True
            for j in range(0,n - i -1):
                if arreglo[j] > arreglo[j+1]:
                    arreglo[j], arreglo[j+1] = arreglo[j+1],arreglo[j]
                    bol = False
            if bol :
                break
        return arreglo
        
       
    def sort_seleccion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if arreglo[j] < arreglo[min_index]:
                    min_index = j
            arreglo[i], arreglo[min_index] = arreglo[min_index], arreglo[i]
        return arreglo
    
    def sort_insercion(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        for i in range(1, n):
            key = arreglo[i]
            j = i - 1
            while j >= 0 and arreglo[j] > key:
                arreglo[j + 1] = arreglo[j]
                j -= 1
            arreglo[j + 1] = key
        return arreglo

    def sort_shell(self, array):
        arreglo = array.copy()
        n = len(arreglo)
        gap = n // 2

        while gap > 0:
            for i in range(gap, n):
                temp = arreglo[i]
                j = i
                while j >= gap and arreglo[j - gap] > temp:
                    arreglo[j] = arreglo[j - gap]
                    j -= gap
                arreglo[j] = temp
            gap //= 2

        return arreglo