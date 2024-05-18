from perceptron import *
from genfloat import *
from fitfuncf import *
from itertools import accumulate
import math, random
import pandas as pd


def reproducir(fit_table: list[GenomaF, int], p:float, npob: int)-> list[GenomaF]:
    
    def pick3(fit_table: list[GenomaF, int])->GenomaF:
        ind: int = int(-POBLACION*math.log(1-rn.random())/5)
        if ind>=POBLACION:
            ind = POBLACION-1
        return fit_table[ind][0]
    

    aux:list[GenomaF]=[]
    for i in range(npob):
        g1:GenomaF = pick3(fit_table)
        g2:GenomaF = pick3(fit_table)
        new_gen = born(g1,g2)
        new_gen.mutate(p)
        aux.append(new_gen)
    return aux

#Parámetros
POBLACION:int = 100
CICLOS:int = 50
TASA_MUTACION:float = 0.05

#inicialización
per:Perceptron = Perceptron(22) #inicializo la configuarción del perceptron    
pob:list[GenomaF] = []  #inicializo la población inicial con genes aleatorios
sample:list[GenomaF] = []
for i in range(POBLACION):
    pob.append(rand_GenomaF(23))
stats: list = [] #inicializo la tabla donde se almacenan las estadísticas de cada ciclo

for ciclo in range(CICLOS):
    fit_table: list[GenomaF, int] = []
    for i in range(POBLACION): #pruebo los individuos de la poblacion.
        per.implant_gen(pob[i])
        fit_table.append([pob[i],carrera(per)])
    sample.append(fit_table[random.randint(0,POBLACION)][0])
    fit_table = sorted(fit_table, key=lambda x:x[1], reverse=True)
    stats.append([ciclo, fit_table[0][0], fit_table[0][1], fit_table[-1][1], sum(fit for _, fit in fit_table)/POBLACION])
    pob = reproducir(fit_table, TASA_MUTACION, POBLACION)
df: pd.DataFrame = pd.DataFrame(stats)
df.columns = ["Ciclo", "Genoma", "maxFit", "minFit", "avgFit"]
df[["Ciclo", "maxFit", "minFit", "avgFit"]].to_excel("results.xlsx")

salir:bool = False
while not salir:
    try:
        sample_num: int = int(input("Ingresar el nro de Generacion a visualizar (0 para salir):"))
        if sample_num < 0 or sample_num > CICLOS:
            print(f"El número debe estar entre {0} y {CICLOS}")
        elif sample_num == 0:
            salir = True
        else:
            per.implant_gen(sample[sample_num])
            carrera(per,show=True)
            
    except:
        print("Ingrese un número entero.")

