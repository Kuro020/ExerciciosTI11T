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