import ControlExercicios
import this
this.contador = 0
this.soma = 0
this.num = 0

def exerciciomodel1(a, b, c):
    c = a
    a = b
    b = c
    return 'A = {}  B = {}'.format(a, b, c)

def exerciciomodel2(valor2):
    return (f'O valor é {valor2} e o seu antecessor é {valor2 - 1}'.format(valor2))

def exerciciomodel3(base3, altura3):
    return (f'O valor da base é {base3}, o valor da altura é {altura3} e o valor da área é {base3*altura3}')

def exerciciomodel4(anos4, meses4, dias4):
    return (f'Sua idade em dias é {dias4+(meses4*+30)+(anos4*365)}')

def exerciciomodel5(eleitores5, brancos5, nulo5, valido5):
    return (f'O município tem um total de {eleitores5} eleitores, com a porcentagem de votos em branco sendo de {(brancos5/eleitores5)*100}%, votos em nulo sendo {(nulo5/eleitores5)*100}% e votos válidos sendo {(valido5/eleitores5)*100}%')

def exerciciomodel6(salario6, reajuste6):
    return (f'O salário após o reajuste é de {(salario6*(reajuste6/100))+salario6}')

def exerciciomodel7(carroimposto7):
    return (f'O valor total do carro é de {((carroimposto7*0.28)+carroimposto7)}')

def exerciciomodel8(primeiranota8, segundanota8, terceiranota8):
    return (f'O valor da média é de {(primeiranota8+segundanota8+terceiranota8)/3}')

def exerciciomodel9(quantidade9):
    if quantidade9 < 12:
        return (f'O valor total é de {quantidade9*1.30}')
    elif quantidade9 >= 12:
        return (f'O valor total é de {quantidade9*1}')

def exerciciomodel11(vendas11, salario11):
    if vendas11 >= 1500:
        restante = (vendas11-1500)*0.05
        return (f'O valor total do salário é de {((vendas11*0.03)+restante)+salario11}')
    else:
        return (f'O valor total do salário é de {(vendas11*0.03)+salario11}')

def exerciciomodel12(conta12, saldo12, debito12, credito12, saldoatual12):
    print (f'A conta de número {conta12} tem um saldo total de {saldo12}, um débito total de {debito12} e um crédito total de {credito12}, com um saldo atual de {saldoatual12}, o saldo é:\n')
    if saldoatual12 >= 0:
        return  ("Saldo positivo")
    if saldoatual12 <= -1:
        return  ("Saldo Negativo")

def exerciciomodel13(numero13):
    for n in range(1,11):
        print (f"{numero13} * {n} = {numero13*n}")

def exerciciomodel14(valor14):
    for i in range(valor14):
        print (f"Os valores inteiros de {i} até o {valor14}")

def exerciciomodel15():
    for i in range(10):
        num = int(input("Digite um número"))
        if num < 0:
            this.contador = this.contador + 1
    return this.contador

def exerciciomodel16():
    for i in range(10):
        this.num = int(input())
        if this.num <= 40:
            this.soma = int(this.soma) + int(this.num)
    return this.soma


