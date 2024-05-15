from genfloat import *
from perceptron import *
import os
import time

TRIGGER: float = 0.10

def carrera(per: Perceptron, show: bool = False)->int:

    def mostrar() -> None:
        os.system("cls")
        print("\n\n")
        print("         ║",end="")
        for i in range(0,8):
            print("  ▓  ",end="") if i==pos else print("     ",end="")
        print("║")
        for row in ruta:
            print("         ║",end="")
            for n in row:
                print(f"{n:^5}", end="")
            print("║")
        print(f"\n\n  Fitness:{fitness}")
        print("Out:", out)


    def set_sight(ruta:list[list[int]], pos:int) -> list[int]:
        aux:list[int]=[]
        for i in range(-3,4):
            aux.append(-10 if ((pos + i) < 0 or (pos + i) > 7) else ruta[0][pos+i])
        for i in range(-3,4):
            aux.append(-10 if ((pos + i) < 0 or (pos + i) > 7) else ruta[1][pos+i])
        for i in range(-2,3):
            aux.append(-10 if ((pos + i) < 0 or (pos + i) > 7) else ruta[3][pos+i])
        for i in range(-1,2):
            aux.append(-10 if ((pos + i) < 0 or (pos + i) > 7) else ruta[4][pos+i])
        return aux


    #inicialización inicial de tablero y la el perceptrón
    ruta: list[list[int]]=np.random.randn(5,8).astype("int").tolist()
    pos: int=np.random.randint(0,8)
    fitness: int = 0
    input: list[int]=[]
    out: float = 0

    LONG_CARRERA: int = 200

    for i in range(LONG_CARRERA):
        if show:
            mostrar()
            time.sleep(0.2)
        input=set_sight(ruta,pos)
        out = per.forward(input)
        if out < (0.5-TRIGGER): #move left
            if pos==0:  #ya en el borde izquierdo
                fitness-=5 #penalidad por chocar el borde izquierdo
            else:
                pos-=1
        elif out > (0.5 + TRIGGER): #move right
            if pos==7:
                fitness-=5 #penalidad por chocar el borde derecho
            else:
                pos+=1       
        fitness+=ruta[0][pos]
        ruta = ruta[1:5]
        ruta.append(np.random.randn(8,).astype("int").tolist())
    return fitness
