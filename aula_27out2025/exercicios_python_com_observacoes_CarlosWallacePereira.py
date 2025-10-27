# -*- coding: utf-8 -*-
# Autor: Carlos Wallace Pereira
# Data: 27/10/2025
# Esse arquivo contém comentários sobre as execuções dos exercícios do PDF 
# com o intuito de entender melhor a linguagem Python


#====================================================
# CAPÍTULO 1
#====================================================

# 1) Entrada e saída de dados simples. Pede o nome do usuário e exibe na tela

def exemplo01():
    nome = input("Qual seu nome? ")
    print(nome)


# 2) Uso de estruturas condicionais. Verifica se há leite em estoque e imprime a compra correspondente.

def exemplo02(leite_em_estoque: bool):
    if leite_em_estoque:
        print("Comprei leite")
    else:
        print("Comprei água")
   

# 3) Uso de estruturas condicionais. Verifica se a nota é suficiente para aprovação.

def exemplo03(nota: float):
    if nota >= 7:
        print("Aprovado")
    else:
        print("Reprovado")
        

# 4) Uso de estruturas condicionais. Classifica o aluno como aprovado, recuperação ou reprovado.

def exemplo04(nota: float):
    """
    No exemplo 04 no lugar de colocar a estrutura if, else e dentro do else colocar outro if e else
    é preferivel usar o elif

    motivo: isso cria um anti-design pattern chamado if-else cascade hell, ou arrow anti-pattern 

    de forma geral isso dificulta a leitura do código a longo prazo e manutenção, além que no campo da programação assíncrona pode causar problemas
    como o callback hell em chamadas de função.
    """

    if nota > 7:
        print("Aprovado")
    elif nota >= 6:  # inclui 6 e 7
        print("Recuperacao")
    else:
        print("Reprovado")
    
        
# 5)  Verifica se o valor é diferente de zero.

def exemplo05(valor: float):
    if valor != 0:
        print("Valor não é zero.")
        

# 6) Demonstra duas formas de verificar se um valor é diferente de zero.

def exemplo06(valor: float):
    if valor != 0:
        print("valor não é zero (via comparação)")
    if valor:
        print("Valor não é zero (via truthy)")
     
        
# 7) Mostra como testar se uma string está vazia.

def exemplo07(texto: str):
    if texto != "":
        print("Texto não está vazio")
    if texto:
        print("Texto não está vazio (via truthy)")
        

#====================================================
# CAPÍTULO 2
#====================================================

# 8) Entrada e saída de dados simples. Lê a idade do usuário e indica se é maior de idade.

def exemplo08():
    "pode lançar ValueError se entrada não for numérica."
    try:
        idade = int(input("Quantos anos você tem? "))
    except ValueError:
        print("Idade inválida (não numérica).")
        return
    maioridade = idade >= 18
    print(maioridade)
    
    
 # 9) Entrada e saída de dados simples. Verifica se um número digitado possui dois dígitos.
 
 def exemplo09():
    try:
        numero = int(input("Digite um numero: "))
    except ValueError:
        print("Entrada inválida.")
        return
    dois_digitos = 10 <= abs(numero) <= 99  # use abs para considerar negativos como 'dois dígitos'
    print(dois_digitos)


#====================================================
# CAPÍTULO 3
#====================================================

# 10) Entrada e saída de dados simples com condicionais
# Calcula a média de três notas e mostra se o aluno foi aprovado.
def exemplo10():
    try:
        nota1 = float(input("Digite a primeira nota: "))
        nota2 = float(input("Digite a segunda nota: "))
        nota3 = float(input("Digite a terceira nota: "))
    except ValueError:
        print("Entrada inválida para nota.")
        return
    media = (nota1 + nota2 + nota3) / 3
    if media >= 7:
        print("Aprovado")
    else:
        print("Reprovado")


# 11) Entrada e saída de dados simples com condicionais
# Calcula idade com base no ano de nascimento e verifica se faz 18 anos em 2025.
def exemplo11():
    try:
        ano_nascimento = int(input("Digite o ano que você nasceu: "))
    except ValueError:
        print("Ano inválido.")
        return
    ano_atual = 2025   
    idade = ano_atual - ano_nascimento
    if idade == 18:
        print("O usuário fará ou fez 18 anos neste ano.")


# 12) Entrada e saída de dados simples com condicionais
# Classifica uma pessoa pela idade (criança, jovem, adulto etc.).
def exemplo12():
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida.")
        return
    if 0 <= idade <= 11:
        print("Criança")
    elif 12 <= idade <= 18:
        print("Adolescente")
    elif 19 <= idade <= 24:
        print("Jovem")
    elif 25 <= idade <= 40:
        print("Adulto")
    elif 41 <= idade <= 60:
        print("Meia Idade")
    elif idade > 60:
        print("Idoso")
    else:
        print("Idade inválida (negativa)")


# 13) Entrada e saída de dados simples com condicionais
# Lê dois valores e informa qual é o maior.
def exemplo13():
    try:
        primeiro = int(input("Digite um valor: "))
        segundo = int(input("Digite outro valor: "))
    except ValueError:
        print("Entrada inválida.")
        return
    print("Primeiro" if primeiro > segundo else "Segundo")
    

#====================================================
# CAPÍTULO 4
#====================================================

# 14) Entrada e saída de dados simples com string. Lê o nome do usuário e o cumprimenta
def exemplo14():
    nome = input("Digite seu nome: ")
    print(f"Olá {nome}")


# 15) Transforma uma mensagem em letras maiúsculas.
def exemplo15():
    mensagem = input("Digite uma mensagem: ")
    print(mensagem.upper())


# 16) Entrada e saída de dados simples com string
def exemplo16():
    idade = input("Digite sua idade: ")
    if idade.isdigit():
        print(f"Você tem {idade} anos.")
    else:
        print("Você digitou uma idade inválida")


# 17) Valida se a idade digitada é numérica.
def exemplo17():
    nome_completo = input("Digite seu nome completo: ").strip()
    partes = nome_completo.split()
    if len(partes) >= 2:
        print(partes[1])
    else:
        print("Nome incompleto.")


#====================================================
# CAPÍTULO 5
#====================================================

# 18) Cria e imprime uma lista de familiares.
def exemplo18():
    familia = ["Gabriel", "Anderson", "Luluzinha", "Mariazinha", "Joãozinho"]
    print(familia)


# 19) Cria uma lista de três cidades digitadas pelo usuário.
def exemplo19():
    cidades = []
    cidades.append(input("Digite o nome da primeira cidade: "))
    cidades.append(input("Digite o nome da segunda cidade: "))
    cidades.append(input("Digite o nome da terceira cidade: "))
    print(cidades)


# 20) Verifica se um número digitado está em uma lista predefinida.
def exemplo20():
    numeros = [1, 3, 6, 10, 5, 23]
    try:
        numero_digitado = int(input("Digite um número: "))
    except ValueError:
        print("Entrada inválida.")
        return
    if numero_digitado in numeros:
        print(f"O número {numero_digitado} está na lista")
    else:
        print(f"O número {numero_digitado} não está na lista")


# 21) Lê cinco nomes e permite excluir um pela posição.
def exemplo21():
    nomes = []
    for i in range(5):
        nomes.append(input(f"Digite o nome {i+1}: "))
    try:
        posicao = int(input("Escolha uma posição de 0 até 4 para excluir: "))
        del nomes[posicao]
    except (ValueError, IndexError):
        print("Posição inválida.")
    print(nomes)


#====================================================
# CAPÍTULO 6
#====================================================

# 22) Operação com lista. Percorre e imprime os itens de uma lista de compras.
def exemplo22():
    itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"]
    for item in itens_compra:
        print(item)


# 23) Imprime apenas os números pares de 1 a 10.
def exemplo23():
    for numero in range(1, 11):
        if numero % 2 == 0:
            print(numero)


# 24) Imprime números ímpares de 51 a 99.
def exemplo24():
    for numero in range(51, 101, 2):
        print(numero)


# 25) Lê 10 números e transforma pares em ímpares.
def exemplo25():
    numeros = []
    for _ in range(10):
        try:
            item = int(input("Digite um valor: "))
        except ValueError:
            print("Valor inválido, usando 0")
            item = 0
        if item % 2 == 0:
            item += 1
        numeros.append(item)
    for n in numeros:
        print(n)


# 26) Exibe a tabuada completa de 1 a 10.
def exemplo26():
    for operador in range(1, 11):
        for operador_2 in range(1, 11):
            resultado = operador * operador_2

            print(f"{operador} X {operador_2} = {resultado}")


#====================================================
# CAPÍTULO 7
#====================================================

# 27) Percorre uma lista com while e imprime seus itens.
def exemplo27():
    itens_compra = ["Arroz", "Leite", "Ovos", "Feijão", "Tomate"]
    posicao = 0
    while posicao < len(itens_compra):
        print(itens_compra[posicao])
        posicao += 1


# 28) Imprime apenas números pares de uma lista usando while.
def exemplo28():
    numeros = list(range(1, 11))
    posicao = 0
    while posicao < len(numeros):
        numero = numeros[posicao]
        if numero % 2 == 0:
            print(numero)
        posicao += 1


# 29) Pede números ímpares até completar uma lista de 10 valores.
def exemplo29():
    numeros = []
    while len(numeros) < 10:
        try:
            numero = int(input("Digite um número ímpar:"))
        except ValueError:
            print("Entrada inválida, tente novamente.")
            continue
        if numero % 2 == 0:
            print("Número par informado; digite um ímpar.")
            continue
        numeros.append(numero)
    for n in numeros:
        print(n)


# 30) Exibe um menu com três opções e responde conforme a escolha.
def exemplo30():
    opcao = 0
    opcoes = [1, 2, 3]
    while opcao not in opcoes:
        print("Selecione uma das opções abaixo:")
        print("1 - Olá mundo")
        print("2 - Eu programo em Python")
        print("3 - Laços de repetição")
        try:
            opcao = int(input("Selecione a opção: "))
        except ValueError:
            print("Opção inválida")
            continue
    if opcao == 1:
        print("Olá mundo!")
    elif opcao == 2:
        print("Já estou na minha sexta lição de Python!")
    else:
        print("Nesta lição estou estudando o laço de repetição While")


# 31) Imprime os cinco primeiros números de uma lista, pulando o índice 2.
def exemplo31():
    numeros = [1,2,3,4,5,6,7,8,9,10]
    posicao = 0
    # versão sem break/continue mostrando apenas primeiros 5 itens e pulando o índice 2
    while posicao < 5:
        if posicao != 2:
            print(numeros[posicao])
        posicao += 1


#====================================================
# CAPÍTULO 8
#====================================================

# 32) Cria e exibe um dicionário simples de produto.
def exemplo32():
    produto = {"descrição": "Água", "preço": 2.00}
    print(produto)


# 33) Percorre uma lista de dicionários e exibe os produtos e preços.
def exemplo33():
    lista_compras = [
        {"descrição": "Água", "preço": 2.00},
        {"descrição": "Leite", "preço": 3.00},
        {"descrição": "Carne", "preço": 18.00},
        {"descrição": "Pizza", "preço": 9.00},
        {"descrição": "Chocolate", "preço": 6.50},
    ]
    for item in lista_compras:
        print("Produto:", item["descrição"], "por", str(item["preço"]), "reais.")


# 34) Identifica o produto mais caro e o mais barato de uma lista.
def exemplo34():
    lista_compras = [
        {"descrição": "Água", "preço": 2.00},
        {"descrição": "Leite", "preço": 3.00},
        {"descrição": "Carne", "preço": 18.00},
        {"descrição": "Pizza", "preço": 9.00},
        {"descrição": "Chocolate", "preço": 6.50},
    ]
    mais_barato = {"descrição": '', 'preço': 0}
    mais_caro = {"descrição": '', 'preço': 0}
    indice = 0
    while indice < len(lista_compras):
        item_compra = lista_compras[indice]
        if indice == 0:
            mais_caro = item_compra
            mais_barato = item_compra
        else:
            if item_compra["preço"] > mais_caro["preço"]:
                mais_caro = item_compra
            if item_compra["preço"] < mais_barato["preço"]:
                mais_barato = item_compra
        indice += 1
    print("Produto mais caro:", mais_caro["descrição"], "por", mais_caro["preço"], "reais")
    print("Produto mais barato:", mais_barato["descrição"], "por", mais_barato["preço"], "reais")


# 35) Lê nomes e sobrenomes de forma padronizada (corrigindo maiúsculas/minúsculas).
def exemplo35():
    pessoas = [
        {"nome": "Joãozinho", "sobrenome": "da Silva" },
        {"NOME": "Mariazinha", "SOBRENOME": "de Souza" },
        {"nome": "Gabriel", "sobrenome": "Schade" },
        {"NOME": "Joana", "SOBRENOME": "da Silva" },
        {"nome": "Everton", "sobrenome": "Schmit" },
    ]
    for pessoa in pessoas:
        nome = pessoa.get("nome") or pessoa.get("NOME")
        sobrenome = pessoa.get("sobrenome") or pessoa.get("SOBRENOME")
        print(nome, sobrenome)


#====================================================
# CAPÍTULO 9
#====================================================

# 36) Define e executa uma função simples que imprime uma mensagem.
def exemplo36():
    def minha_funcao():
        print("Minha primeira função")
    minha_funcao()


# 37) Define uma função que recebe nome e idade e exibe uma frase.
def exemplo37():
    def escrever_nome_idade(nome, idade):
        print(nome, "possui", idade, "anos.")
    nome = input("Digite seu nome: ")
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida.")
        return
    escrever_nome_idade(nome, idade)


# 38) Multiplica dois números informados pelo usuário e mostra o resultado.
def exemplo38():
    def multiplicar(n1, n2):
        return n1 * n2
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida.")
        return
    resultado = multiplicar(a, b)
    print(resultado)


# 39) Encontra o maior entre três números e exibe o dobro dele.
def exemplo39():
    def obter_maior(n1, n2, n3):
        maior = n1
        if n2 > maior:
            maior = n2
        if n3 > maior:
            maior = n3
        return maior
    def dobrar(x):
        return x * 2
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        c = int(input("Digite o terceiro número: "))
    except ValueError:
        print("Entrada inválida.")
        return
    maior = obter_maior(a, b, c)
    print(dobrar(maior))


# 40) Lê cinco nomes, armazena em uma lista e os exibe.
def exemplo40():
    def solicitar_nome():
        return input("Digite um nome: ")
    def adicionar_nome_na_lista(lista, nome):
        lista.append(nome)
    def escrever_nomes(lista):
        for nome in lista:
            print(nome)
    nomes = []
    for _ in range(5):
        nome = solicitar_nome()
        adicionar_nome_na_lista(nomes, nome)
    escrever_nomes(nomes)


#====================================================
# CAPÍTULO 10
#====================================================

# 41) Cria e executa uma função lambda simples que imprime uma mensagem.
def exemplo41():
    minha_funcao = lambda: print("Minha primeira função")
    minha_funcao()


# 42) Usa lambda para imprimir nome e idade informados pelo usuário.
def exemplo42():
    escrever_nome_idade = lambda nome, idade: print(nome, "possui", idade, "anos.")
    nome = input("Digite seu nome: ")
    try:
        idade = int(input("Digite sua idade: "))
    except ValueError:
        print("Idade inválida.")
        return
    escrever_nome_idade(nome, idade)


# 43) Usa lambda para multiplicar dois números digitados.
def exemplo43():
    multiplicar = lambda n1, n2: n1 * n2
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida.")
        return
    print(multiplicar(a, b))


# 44) Filtra e exibe apenas os números maiores que 10 de uma lista.
def exemplo44():
    numeros = []
    for _ in range(5):
        try:
            n = int(input("Digite um número: "))
        except ValueError:
            print("Valor inválido, usando 0")
            n = 0
        numeros.append(n)
    maiores = filter(lambda numero: numero > 10, numeros)
    for m in maiores:
        print(m)


# 45) Separa números pares e ímpares digitados e exibe cada grupo.
def exemplo45():
    def escrever_array(array):
        for valor in array:
            print(valor)
    numeros = []
    for _ in range(10):
        try:
            n = int(input("Digite um número: "))
        except ValueError:
            print("Valor inválido, usando 0")
            n = 0
        numeros.append(n)
    pares = list(filter(lambda numero: numero % 2 == 0, numeros))
    impares = list(filter(lambda numero: numero % 2 == 1, numeros))
    escrever_array(pares)
    escrever_array(impares)


# 46) Percorre uma lista de frutas exibindo índice e valor.
def exemplo46():
    frutas = ["maçã", "banana", "laranja"]
    for idx, fruta in enumerate(frutas):
        print(idx, fruta)


# 47) Cria e exibe os quadrados dos números de 1 a 10.
def exemplo47():
    quadrados = [i*i for i in range(1, 11)]
    for q in quadrados:
        print(q)


# 48) Verifica se uma palavra digitada é palíndromo.
def exemplo48():
    s = input("Digite uma palavra: ").strip()
    inv = s[::-1]
    print("Invertida:", inv)
    print("É palíndromo?" , s.lower() == inv.lower())


# 49) Demonstra diferença entre concatenação e extensão de listas.
def exemplo49():
    a = [1,2,3]
    b = [4,5]
    c = a + b  # cria nova lista
    a.extend(b)  # modifica 'a' no lugar
    print("c: ", c)
    print("a:", a)


# 50) Faz uma divisão e trata erro de divisão por zero.
def exemplo50():
    try:
        a = int(input("Dividendo: "))
        b = int(input("Divisor: "))
    except ValueError:
        print("Entrada inválida.")
        return
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro: divisão por zero.")


# 51) Usa get() em dicionário com valores padrão.
def exemplo51():
    d = {"nome": "Ana"}
    print(d.get("nome", "desconhecido"))
    print(d.get("idade", 0))


# 52) Tenta abrir e ler um arquivo de texto informado pelo usuário.
def exemplo52():
    nome_arquivo = input("Nome do arquivo para leitura: ")
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")


# 53) Calcula o fatorial de um número usando recursão.
def exemplo53():
    def fatorial(n):
        if n < 0:
            raise ValueError("n deve ser >=0")
        if n in (0,1):
            return 1
        return n * fatorial(n-1)
    try:
        n = int(input("Digite n para fatorial: "))
    except ValueError:
        print("Entrada inválida.")
        return
    if n > 1000:
        print("N muito grande - risco de RecursionError; abortando.")
        return
    print(fatorial(n))


# 54) Multiplica todos os números de uma lista por 2 usando map().
def exemplo54():
    numeros = [1,2,3,4,5]
    dobrados = list(map(lambda x: x*2, numeros))
    print(dobrados)


# 55) Ordena produtos pelo preço usando função lambda.
def exemplo55():
    produtos = [
        {"nome":"A", "preco": 10},
        {"nome":"B", "preco": 5},
        {"nome":"C", "preco": 20},
    ]
    ordenados = sorted(produtos, key=lambda p: p["preco"])
    for p in ordenados:
        print(p["nome"], p["preco"])


# 56) Remove valores duplicados de uma lista usando set().
def exemplo56():
    lst = [1,2,2,3,3,3,4]
    s = set(lst)
    print(list(s))


# 57) Combina nomes e notas com zip() e exibe os pares.
def exemplo57():
    nomes = ["Ana","Bia","Carlos"]
    notas = [7, 9, 8]
    for nome, nota in zip(nomes, notas):
        print(nome, nota)


# 58) Imprime um fatiamento de lista com intervalo e passo.
def exemplo58():
    lst = list(range(10))
    print(lst[2:7:2])


# 59) Converte um dicionário em texto JSON e exibe.
def exemplo59():
    import json
    dados = {"nome":"Teste", "idade":30}
    texto = json.dumps(dados)
    print(texto)