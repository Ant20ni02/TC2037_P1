from math import sqrt
from multiprocessing import Pool
from time import time

def evaluarPrimo(n):
    if n < 2:
        return 0
    else:
        for i in range(2, int(sqrt(n)+1)):
            if n%i == 0: 
                return 0
    return n

def main():
    suma = 0
    for n in range(5000000):
        suma += evaluarPrimo(n)
    print(suma)
    
   
    
if __name__ == '__main__':
    start = time()
    main()
    end = time()
    print("Tiempo de ejecucion secuencial: ", end-start)

    result = 0
    pool = Pool(8)
    start = time()
    result1 = pool.map(evaluarPrimo, range(1,5000001))
    result = sum(result1)
    print(result)
    end = time()
    print("Tiempo de ejecucion paralelo: ", end-start)