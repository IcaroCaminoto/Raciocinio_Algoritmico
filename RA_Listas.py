# Exercício 5

quanto = int(input("Quantos números deseja analisar: "))
lista = []

while quanto > len(lista):
    try:
        nro_informado = int(input("Digite um número inteiro: "))
        lista.append(nro_informado)

    except ValueError:
        print("Erro: O valor informado deve ser do tipo inteiro!")

listaPares = [num for num in lista if num % 2 == 0]
listaImpares = [num for num in lista if num % 2 != 0]

maiorPares = max(listaPares) if listaPares else None
maiorImpares = max(listaImpares) if listaImpares else None
print("------------------------------------------------------------\n Resultados:")
print(f"O maior número par digitado foi: {maiorPares}")
print(f"O maior número ímpar digitado foi: {maiorImpares}")
print(f"O somátorio de todos os elementos da lista é: {sum(lista)}")
print(f"A média dos valores da lista é: {round(sum(lista)/len(lista),3)}")

# Exercício 4

media_notas = int(60)

tamanho_turma = int(input("Quantos alunos existem na turma que deseja analisar? "))
lista_notas = []
lista_abaixoMedia = []
lista_acimaMedia = []

while len(lista_notas) < tamanho_turma:
    try:
        aluno = str(input("Digite o nome do aluno: "))
        nota = float(input("Digite a nota do aluno: "))
        lista_notas.append(nota)
        if nota < media_notas:
            lista_abaixoMedia.append(aluno)
        else:
            lista_acimaMedia.append(aluno)
    except ValueError:
        print("Valor invalido")
print(f"Os seguintes alunos ficaram abaixo da média: {lista_abaixoMedia}")
print(f"Os seguintes alunos ficaram acima da média: {lista_acimaMedia}")

# Exercício 3

a = []

for i in range(10):
    entrada = int(input("Digite um número inteiro: "))
    i += 1
    a.append(entrada)

print(f"Maior número informado: {max(a)}")
print(f"Menor número informado: {min(a)}")

# Exercício 1 e 2

a = []

for i in range(10):
    a.append(int(input("Digite um numero: ")))

cont = 0

for item in a:
    cont += 1
    print(f"{cont}: {item}")