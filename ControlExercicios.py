import ModelExercicios
resposta = True


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

salario6 = int(input("Digite o salário:\n"))
reajuste6 = int(input("Digite a % de reajuste:\n"))

carro7 = int(input("Digite o valor do carro:\n"))
carroimposto7 = ((carro7*0.45)+carro7)

primeiranota8 = int(input("Digite a primeira nota:\n"))
segundanota8 = int(input("Digite a segunda nota:\n"))
terceiranota8 = int(input("Digite a terceira nota:\n"))

quantidade9 = int(input("Quantas maçãs foram compradas?\n"))

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

def exerciciocontrol6():
    print (ModelExercicios.exerciciomodel6(salario6, reajuste6))

def exerciciocontrol7():
    print (ModelExercicios.exerciciomodel7(carroimposto7))

def exerciciocontrol8():
    print (ModelExercicios.exerciciomodel8(primeiranota8, segundanota8, terceiranota8))

def exerciciocontrol9():
    print (ModelExercicios.exerciciomodel9(quantidade9))