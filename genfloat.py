import random as rn
import numpy as np



class GenomaF:

    def __init__(self, gens:list[float]) -> None:
        #Constructor del objeto genomaF
        self.gens:list[float] = gens

    def set_gens(self, gens:list[float]) -> None:
        #Implanta un genoma en el Objeto GenomaF
        self.gens:list[float] = gens

    def get_gens(self) -> list[float]:
        #Devuelve el genoma del Objeto GenomaF
        return self.gens
    
    def __len__(self) -> int:
        #Devuelve la cantidad de genes del Objeto
        return len(self.gens)
    
    def mutate(self, p: float) -> None:
        #Muta los genes del Objeto con probabilidad p de mutar cada gen, la mutacion es un factor 
        #multiplicativo normal con media 1 y desvio 0.3
        for i in range(len(self.gens)):
            if rn.random() < p:
                self.gens[i] = self.gens[i] * np.random.normal(1.0, 0.2)

def rand_GenomaF(size: int)->GenomaF:
    #Funcion que genera un Objeto genoma inicializado aleatoriamente
    return GenomaF(np.random.randn(size).tolist())

def born(g1:GenomaF, g2:GenomaF)->GenomaF:
    #Funcion que crea un objeto GenomaF a partor de sus padres, los genes del hijo se toman de uno
    #de los padres con probabilidad 0.5
    if len(g1)!=len(g2):
        print("los genes progenitores deben ser de la misma longitud")
        return None
    aux: list[float] = []
    for i in range(len(g1)):
        aux.append(rn.choice([g1.gens[i],g2.gens[i]]))
    return GenomaF(aux)