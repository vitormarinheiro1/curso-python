### Argumentos nomeados e não nomeados
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeado recebe apenas o argumento (valor)

### *args

def soma(*args):
    total = 0
    for numero in args:
        total = total + numero
        print(numero, total)

### Termos técnicos
Higher Order Functions - Funções que podem receber e/ou retornar outras funções

First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)

### Closure
Uma closure em Python é uma função que lembra e pode acessar variáveis do seu escopo externo, mesmo após o término desse escopo.

### Dict - Manipulando dicionários
pessoa = {}
chave = 'nome'
pessoa[chave] = 'Vitor Marinheiro'

### Métodos úteis dos dicionários em Python
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Vitor Rodrigues',
    'sobrenome': 'Marinheiro',
    'idade': 900,
}

print(list(pessoa.keys()))

### Set
- Não permite valores duplicados
- Não aceitam valores mutáveis
- Não garante ordem
- Não tem index
- são iteráveis

s1 = set('Vitor')
s1 = {'Vitor', 1, 2, 3}

print(s1)

Métodos úteis:
add, update, clear, discard

Operadores úteis
união | união (union) - Une
intersecção & (intersection) - Itens presentes em ambos
diferença - Itens presentes apenas no set da esquerda
diferença simétrica ^ - Itens que não estão em ambos

### Lambda
- Função anônima

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

l1 = sorted(lista, key=lambda item: item['nome'])

### Empacotamento e desempacotamento de dicionários
kwargs - keyword arguments (argumentos nomeados)

def mostrar_argumentos_nomeados(*args, **kwargs):
    for chave, valor in kwargs.items():
    print(chave, valor)

mostrar_argumentos_nomeados(nome='Joana', qlq=123)

### List Comprehension
lista = [numero for numero in range(10)]