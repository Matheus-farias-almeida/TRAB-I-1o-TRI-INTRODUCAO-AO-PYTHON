#Exercício 1
print("Olá,mundo!")
print("\n")

#Exercício 2
numero = input("Digite um número: ")
print(f"O número informado foi {numero}")
print("\n")

#Exercício 3
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
print(f"{num1} + {num2} = {num1 + num2}")
print("\n")

#Exercício 4
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
print(f"A média do aluno é: {media:.2f}")
print("\n")

#Exercício 5
metros = float(input("Digite o valor em metros: "))
print(f"a quantidade de metros informada em centímetros é: {metros * 100}")
print("\n")

#Exercício 6
raio = float(input("Digite o raio do círculo: "))
print(f"A área do círculo é: {3.14 * (raio * raio)}")
print("\n")

#Exercício 7
lado = float(input("Digite o lado do quadrado:"))
area = lado ** 2
print("A área do quadrado é: ", area)

#Exercício 8
valor_hora = float(input("Digite o valor da sua hora de trabalho:"))
horas_trabalhadas = float(input("Digite a quantidade de horas trabalhadas no mês:"))
salario = valor_hora * horas_trabalhadas
print("O salário do mês é: ", salario)

#Exercício 9
valor_inicial = float(input("Valor Inicial: "))
percentual = float(input("Percentual de Desconto: "))
valor_desconto = valor_inicial * (percentual / 100)
valor_final = valor_inicial - valor_desconto
print(f"Valor Final: {valor_final:.2f}")

#Exercício 10
raio = int(input("Digite o valor de raio: "))
altura = int(input("Digite a altura: "))
print(f"O volume do cone é: {(3.14 * (raio * raio) * altura) / 3}")