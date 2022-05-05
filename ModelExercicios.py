import ControlExercicios
def exerciciomodel1(a, b, c):
    c = a
    a = b
    b = c
    return 'A = {}  B = {}'.format(a, b, c)

def exerciciomodel2(valor2):
    return print(f'O valor é {valor2} e o seu antecessor é {valor2 - 1}'.format(valor2))

def exerciciomodel3(base3, altura3):
    return print(f'O valor da base é {base3}, o valor da altura é {altura3} e o valor da área é {base3*altura3}')

def exerciciomodel4(anos4, meses4, dias4):
    return print(f'Sua idade em dias é {dias4+(meses4*+30)+(anos4*365)}')

def exerciciomodel5(eleitores5, brancos5, nulo5, valido5):
    return print(f'O município tem um total de {eleitores5} eleitores, com a porcentagem de votos em branco sendo de {(brancos5/eleitores5)*100}%, votos em nulo sendo {(nulo5/eleitores5)*100}% e votos válidos sendo {(valido5/eleitores5)*100}%')

def exerciciomodel6(salario6, reajuste6):
    return print(f'O salário após o reajuste é de {(salario6*(reajuste6/100))+salario6}')

def exerciciomodel7(carroimposto7):
    return print(f'O valor total do carro é de {((carroimposto7*0.28)+carroimposto7)}')

def exerciciomodel8(primeiranota8, segundanota8, terceiranota8):
    return print(f'O valor da média é de {(primeiranota8+segundanota8+terceiranota8)/3}')

def exerciciomodel9(quantidade9):
    if quantidade9 < 12:
        return print(f'O valor total é de {quantidade9*1.30}')
    elif quantidade9 >= 12:
        return print(f'O valor total é de {quantidade9*1}')