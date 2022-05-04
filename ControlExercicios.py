import ModelExercicios
a = 10
b = 20
c = 0
valor2 = int(input("Por favor digite um número:\n"))
base3 = int(input("Digite o valor da base:\n"))
altura3 = int(input("Digite o valor da altura:\n"))
anos4 = int(input("Digite quantos anos você tem:\n"))
meses4 = int(input("Digite quantos meses você tem:\n"))
dias4 = int(input("Digite quantos dias você tem:\n"))
eleitores5 = int(input("Digite a quantidade de eleitores:\n"))
brancos5 = int(input("Digite o total de votos em branco:\n"))
nulo5 = int(input("Digite o total de votos em nulo:\n"))
valido5 = int(input("Digite o total de votos válidos:\n"))

def exerciciocontrol1():
    print (ModelExercicios.exerciciomodel1(a, b, c))

def exerciciocontrol2():
    print (ModelExercicios.exerciciomodel2(valor2))

def exerciciocontrol3():
    print (ModelExercicios.exerciciomodel3(base3, altura3))

def exerciciocontrol4():
    print (ModelExercicios.exerciciomodel4(anos4, meses4, dias4))

def exerciciocontrol5():
    print (ModelExercicios.exerciciomodel5(eleitores5, brancos5, nulo5, valido5))