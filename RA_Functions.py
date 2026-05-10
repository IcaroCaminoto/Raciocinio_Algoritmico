#1
def somar(a,b):
    return a+b

#2
def multiplicar(a,b):
    return a*b

#3
def mensagem(nome):
    return f"Olá,{nome}!"

#4
def maior(a,b):
    return max(a,b)

#5
def dividir(a,b):
    return a/b

#6
def par_ou_impar(n):
    return n % 2 == 0

#7
def teste():
    print('Olá')

#8
def apresentar(nome, idade, cidade):
    lista = [nome, idade, cidade]
    return lista

#9
a = apresentar(cidade="Longe", nome="Zé das couve", idade=18)
print(a)

#10
# Printa Nome, Cidade, Idade no console

#11
def saudacao(nome, periodo="dia"):
    print(f"Bom {periodo}, {nome}")
var = saudacao("Ícaro")

#12
def saudacao(nome, periodo="dia"):
    if periodo =="dia":
        print(f"Bom dia, {nome}")
    elif periodo =="tarde":
        print(f"Boa tarde, {nome}")
    elif periodo =="noite":
        print(f"Boa noite, {nome}")
    else:
        print(f"Olá, {nome}")

#13
def exemplo(a=1, b):
# Esta função resulta em erro porque os argumentos obrigatórios (estáticos) devem primeiro na ordem de parâmetros

#14
def soma_todos(*args):
    return sum(args)

#15
def mostrar_dados(*args):
    print(*args)

#16
#A diferença entre args e kwargs:
# args recebe valores posicionais como tuplas
#   Exemplo: minha_tupla = (1, 2, 3)
# kwargs recebe palavras-chave como dicionários
#   Exemplo: meu_dicionaro = {"A": 50, "B": 35}

#17 - A função abaixo printa inicialmente x = 5 (função teste), então printa x = 10 (runtime).
#   Isso ocorre por causa do escopo da variável
x = 10
def teste():
    x = 5
    print(x)

teste()
print(x)

#18
contador = 0
def incrementar():
    global contador
    contador += 1

#19
def triplo(x):
    return x*3

var1 = triplo(5)
print(var1)

#20
def executar(triplo, valor):
    return triplo(valor)

#21
add = lambda a, b: a + b
print(add(5, 10))

#22
nros = [1,2,3,4,5]
resultado = list(map(triplo, nros))
print(resultado)