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
    return(f'O valor é {valor2} e o seu antecessor é {valor2 - 1}'.format(valor2))

def exerciciomodel3(base3, altura3):
    return(f'O valor da base é {base3}, o valor da altura é {altura3} e o valor da área é {base3*altura3}')

def exerciciomodel4(anos4, meses4, dias4):
    return(f'Sua idade em dias é {dias4+(meses4*+30)+(anos4*365)}')

def exerciciomodel5(eleitores5, brancos5, nulo5, valido5):
    return(f'O município tem um total de {eleitores5} eleitores, com a porcentagem de votos em branco sendo de {(brancos5/eleitores5)*100}%, votos em nulo sendo {(nulo5/eleitores5)*100}% e votos válidos sendo {(valido5/eleitores5)*100}%')

def exerciciomodel6(salario6, reajuste6):
    return(f'O salário após o reajuste é de {(salario6*(reajuste6/100))+salario6}')

def exerciciomodel7(carroimposto7):
    return(f'O valor total do carro é de {((carroimposto7*0.28)+carroimposto7)}')

def exerciciomodel8(primeiranota8, segundanota8, terceiranota8):
    return(f'O valor da média é de {(primeiranota8+segundanota8+terceiranota8)/3}')

def exerciciomodel9(quantidade9):
    if quantidade9 < 12:
        return(f'O valor total é de {quantidade9*1.30}')
    elif quantidade9 >= 12:
        return(f'O valor total é de {quantidade9*1}')

def exerciciomodel11(vendas11, salario11):
    if vendas11 >= 1500:
        restante = (vendas11-1500)*0.05
        return(f'O valor total do salário é de {((vendas11*0.03)+restante)+salario11}')
    else:
        return(f'O valor total do salário é de {(vendas11*0.03)+salario11}')

def exerciciomodel12(conta12, saldo12, debito12, credito12, saldoatual12):
    print(f'A conta de número {conta12} tem um saldo total de {saldo12}, um débito total de {debito12} e um crédito total de {credito12}, com um saldo atual de {saldoatual12}, o saldo é:\n')
    if saldoatual12 >= 0:
        return("Saldo positivo")
    if saldoatual12 <= -1:
        return("Saldo Negativo")

def exerciciomodel13(numero13):
    for n in range(1,11):
        print(f"{numero13} * {n} = {numero13*n}")

def exerciciomodel14(valor14):
    for i in range(valor14):
        print(f"Os valores inteiros de {i} até o {valor14}")

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

def exerciciomodel17():
    numeros = range(15, 101)
    media = sum(numeros) / len(numeros)
    print("A média é" + str(media))

def exerciciomodel18():
    numeros = int(input("digite aqui a quantidade de números que você irá digitar: "))
    digitados = 0
    total = 0
    lista = [0]

    while digitados < numeros:
        num = int(input("digite aqui o " + str(digitados + 1) + "°" + " número: "))
        lista.append(num)
        total = total + num
        digitados = digitados + 1

    lista.sort()

    print("a média dos números digitados é: " + str(total / len(lista)))
    print("o maior número é: " + str(lista[len(lista) - 1]))

def exerciciomodel19():
    lista = [0]
    media = sum(lista) / len(lista)
    alunos = 20
    c = 0

    while c < alunos:
        nota = int(input("Digite aqui a nota do aluno."))
        lista.append(nota)
        c = c + 1
        if nota > media:
            this.contador = this.contador + 1
    lista.sort()
    print("A média da turma é " + str(sum(lista) / 20) + " e " + str(this.contador) + " alunos alcançaram a média.")

def exerciciomodel20():
    populacao = int(input("digite aqui a quantidade de pessoas que moram na cidade: "))
    digitados = 0

    lista = [0]
    lista2 = [0]

    while digitados < populacao:
        salario = int(input("digite o salário da " + str(digitados + 1) + "°" + " pessoa: "))
        filho = int(input("digite o quantos filhos a " + str(digitados + 1) + "°" + " pessoa tem: "))
        if salario < 150:
            this.contador = this.contador + 1

        lista.append(salario)
        lista2.append(filho)
        digitados = digitados + 1
    lista.sort()
    lista2.sort()

    mediasalario = sum(lista) / len(lista)
    mediafilho = sum(lista2) / len(lista2)
    maiorsalario = max(lista)
    percentual = (len(lista)/this.contador)*100

    print("A média do salário da população é de: " + str(mediasalario) + "A média de filhos é de : " + str(mediafilho) +
          "O maior salário da cidade é de: " + str(maiorsalario) +
          "E o percentoal de pessoas com um salário abaixo de R$150,00 é de: " + str(percentual) + "%")






