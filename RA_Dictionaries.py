# #1 - Pesquisando pela chave (não pelo valor)
# pessoa = {"nome": "João", "idade": 30, "cidade": "São Paulo"}
# proc_chave = input("Digite a chave que deseja procurar: ")
# valor = pessoa.get(proc_chave, "Chave não encontrada")

# print(f"Valor da chave: {valor}")



# #2 Atualizando valores
# produtos = {"maçã": 5.5, "banana": 3.0, "laranja": 4.0}
# produto_alt = input("Qual produto deseja alterar: ").lower()
# if produto_alt in produtos:
#     novo_preco = float(input("Digite o novo preço: "))
#     produtos[produto_alt] = novo_preco
#     print(f"Preço atualizado: {produto_alt} - R${novo_preco:.2f}")
# else:
#     print("Produto não encontrado.")



# #3 Inserindo dados de forma dinâmica
# dados = {}
# nome = input("Digite seu nome: ")
# idade = int(input("Digite sua idade: "))
# dados["nome"] = nome
# dados["idade"] = idade
# print("Dados inseridos:", dados)



# #4 Função dict e construção de dicionário a partir de listas
# listaDeTuplas = []
# for i in range(3):
#     chave = input("Digite a chave: ")
#     valor = input("Digite o valor: ")
#     listaDeTuplas.append((chave, valor))
# dicionario = dict(listaDeTuplas)
# print("Dicionário criado:", dicionario)



#5 Limpando dados com o método clear
# meus_dados = {"id": 101, "status": "ativo", "nivel": 5}
# print(f"Dicionário original: {meus_dados}")
# resposta = input("Deseja apagar todos os dados? (sim/nao): ").strip().lower()

# if resposta == "sim":
#     meus_dados.clear()
#     print("Dados apagados com sucesso.")

# print(f"Dicionário final: {meus_dados}")



#6 Copiando dicionários com o método copy
# Nota: Se igualarmos um dicionário a outro (dict2 = dict1), ambos apontarão para o mesmo lugar na memória.
#       O .copy() cria um dicionário independente!
# dict1 = {"pontos": 180, "nivel": 3}
# copia = dict1.copy()

# copia["pontos"] = 250
# copia["nivel"] = 5

# print("Dicionário original:", dict1)
# print("Cópia do dicionário:", copia)



#7 Utilizando o incício fromKeys para criar um dicionário a partir de uma lista de chaves
# entradas = input("Digite as chaves separadas por vírgula: ")
# lista_nomes = [nome.strip() for nome in entradas.split(",")]

# dicionarios = dict.fromkeys(lista_nomes, 0)
# print(f"Dicionário criado: {dicionarios}")



#8 Utilizando o método get para acessar valores de forma segura
# inventario = {"maçã": 10, "banana": 5, "laranja": 8}
# produto = input("Digite o produto que deseja consultar: ").lower()
# quantidade = inventario.get(produto, "Produto não encontrado")
# print(f"Quantidade de {produto}: {quantidade}")



#9 Visualizando informações de várias formas: keys, values e items
# estoque = {"Monitor": 800.0, "Teclado": 150.0, "Mouse": 80.0}

# print("Visualizando os dados:")
# print(f"Chaves (keys): {list(estoque.keys())}")
# print(f"Valores (values): {list(estoque.values())}")
# print(f"Pares (items): {list(estoque.items())}")



#10 Remoção e atualização em massa
# configuracao = {"resolucao": "1920x1080", "volume": 70, "idioma": "Português"}
# print(f"Configuração original: {configuracao}")

# remocao = input("Digite a chave que deseja remover: ")
# if remocao in configuracao:
#     configuracao.pop(remocao)
# else:    
#     print("Chave não encontrada para remoção.")

# print(f"Configuração após remoção: {configuracao}")

# configuracao.popitem()  # Remove o último item adicionado
# print(f"Configuração após popitem: {configuracao}")

# nova_chave = input("Digite a nova chave para atualização: ")
# novo_valor = input("Digite o novo valor para atualização: ")
# configuracao.update({nova_chave: novo_valor})
# print(f"Configuração após atualização: {configuracao}")



#11 Criando um sistema de gerenciamento simples utilizando dicionários
usuarios = {"Alice": 25, "Bob": 30, "Carlos": 22}

while True:
    print("\n" + "="*35)
    print("SISTEMA DE GERENCIAMENTO")
    print("="*35)
    print("1. Exibir todos os usuários")
    print("2. Buscar usuário pelo nome")
    print("3. Adicionar novo usuário")
    print("4. Atualizar idade de um usuário")
    print("5. Remover um usuário (pop)")
    print("6. Remover último inserido (popitem)")
    print("7. Criar cópia e testar alteração")
    print("8. Inicializar banco em lote (fromkeys)")
    print("9. Atualizar com novos dados (update)")
    print("10. Limpar todo o sistema (clear)")
    print("11. Criar dicionário a partir de tuplas (dict)")
    print("0. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        print("Encerrando o sistema...")
        break
        
    elif opcao == "1":
        print(f"Nomes cadastrados: {list(usuarios.keys())}")
        print(f"Idades registradas: {list(usuarios.values())}")
        print(f"Todos os dados: {list(usuarios.items())}")
        
    elif opcao == "2":
        nome = input("Digite o nome para busca: ")
        idade = usuarios.get(nome, "Usuário não encontrado.")
        print(f"Resultado: {idade}")
        
    elif opcao == "3":
        nome = input("Digite o nome do novo usuário: ")
        idade = int(input("Digite a idade: "))
        usuarios[nome] = idade
        print("Usuário adicionado com sucesso!")
        
    elif opcao == "4":
        nome = input("Digite o nome do usuário para atualizar: ")
        if nome in usuarios:
            nova_idade = int(input("Digite a nova idade: "))
            usuarios[nome] = nova_idade
            print("Idade atualizada.")
        else:
            print("Usuário não encontrado.")
            
    elif opcao == "5":
        nome = input("Digite o nome do usuário a ser removido: ")
        removido = usuarios.pop(nome, None)
        if removido:
            print(f"{nome} removido do sistema.")
        else:
            print("Usuário não encontrado.")
            
    elif opcao == "6":
        if usuarios:
            removido = usuarios.popitem()
            print(f"Último registro removido: {removido}")
        else:
            print("O sistema já está vazio.")
            
    elif opcao == "7":
        copia_usuarios = usuarios.copy()
        print("Cópia criada. Vamos alterar um dado na cópia.")
        nome = input("Qual usuário deseja alterar na cópia? ")
        if nome in copia_usuarios:
            copia_usuarios[nome] = 999
            print(f"\nDicionário Original: {usuarios}")
            print(f"Dicionário Cópia: {copia_usuarios}")
        else:
            print("Usuário não existe para alteração.")
            
    elif opcao == "8":
        nomes_str = input("Digite os nomes separados por vírgula: ")
        idade_padrao = int(input("Digite a idade padrão para todos: "))
        lista = [n.strip() for n in nomes_str.split(",")]
        novo_banco = dict.fromkeys(lista, idade_padrao)
        print(f"Novo dicionário gerado: {novo_banco}")
        
    elif opcao == "9":
        print("Atualizando com lote de dados ({'Zé': 40, 'Maria': 35})")
        lote = {"Zé": 40, "Maria": 35}
        usuarios.update(lote)
        print("Atualização concluída.")
        
    elif opcao == "10":
        confirma = input("Tem certeza que deseja apagar TUDO? (s/n): ").lower()
        if confirma == "s":
            usuarios.clear()
            print("Sistema limpo.")
            
    elif opcao == "11":
        qtd = int(input("Quantos pares deseja inserir? "))
        pares = []
        for i in range(qtd):
            k = input("Nome (Chave): ")
            v = int(input("Idade (Valor): "))
            pares.append((k, v))
        dicio_tuplas = dict(pares)
        print(f"Dicionário gerado com dict() e tuplas: {dicio_tuplas}")
        
    else:
        print("Opção inválida, tente novamente.")