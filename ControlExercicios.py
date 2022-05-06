import ModelExercicios
import this
resposta = True
opcao = 0

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
carroimposto7 = ((carro7 * 0.45) + carro7)

primeiranota8 = int(input("Digite a primeira nota:\n"))
segundanota8 = int(input("Digite a segunda nota:\n"))
terceiranota8 = int(input("Digite a terceira nota:\n"))

quantidade9 = int(input("Quantas maçãs foram compradas?\n"))

vendas11 = int(input("Qual o valor total das vendas que foram realizadas?\n"))
salario11 = 1000

conta12= 12487
saldo12= int(input("Qual o saldo total da conta?\n"))
debito12= int(input("Qual o total de débito da conta?\n"))
credito12= int(input("Qual o total de crédito da conta?\n"))
saldoatual12= saldo12 - debito12 + credito12

numero13= int(input("De qual número fazer a tabuada?\n"))

valor14 = int(input("Digite um valor:\n"))

def menu():
    print("Escolha uma das opções abaixo:\n" +
          "1.Exercicio \n" +
          "2.Exercicio \n" +
          "3.Exercicio \n" +
          "4.Exercicio \n" +
          "5.Exercicio \n" +
          "6.Exercicio \n" +
          "7.Exercicio \n" +
          "8.Exercicio \n" +
          "9.Exercicio \n" +
          "11.Exercicio \n")
    this.opcao = int(input())

def mostrar():
    menu()
    if (this.opcao == 11):
        exerciciocontrol1()

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

def exerciciocontrol11():
    print (ModelExercicios.exerciciomodel11(vendas11, salario11))

def exerciciocontrol12():
    print (ModelExercicios.exerciciomodel12(conta12, saldo12, debito12, credito12, saldoatual12))

def exerciciocontrol13():
    print(ModelExercicios.exerciciomodel13(numero13))

def exerciciocontrol14():
    print(ModelExercicios.exerciciomodel14(valor14))

def exerciciocontrol15():
    print(ModelExercicios.exerciciomodel15())

def exerciciocontrol16():
    print(ModelExercicios.exerciciomodel16())