import numpy as np
import random as rn
from genfloat import *

class Perceptron:
    def __init__(self, n_ent: int) -> None:
        self.n_ent: int = n_ent
        self.pesos: list[float] = np.random.randn(n_ent,).tolist()
        self.sesgo: float = rn.normalvariate(0,1)

    def set_pesos(self, pesos:list[float]) -> None:
        self.pesos = pesos

    def set_sesgos(self, sesgo:float) -> None:
        self.sesgo: sesgo

    def implant_gen(self, genoma:GenomaF) -> None:
        if (len(genoma)==self.n_ent+1):
            gens = genoma.get_gens()
            self.pesos = gens[0:self.n_ent]
            self.sesgo = gens[self.n_ent]
        else:
            print("incompatibilidad dimensional entre el genoma y el perceptron")

    def funcion_activacion(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, entrada: list[float])->float:
        if len(entrada)!=self.n_ent:
            print("Inconsistencia dimensional")
            return 0
        salida = sum(x * y for x, y in zip(entrada, self.pesos))+self.sesgo
        return self.funcion_activacion(salida)

        
        
