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

* Mapeamento de dados em list comprehension

produtos = [
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(*novos_produtos, sep='\n')

* Filtro com list comprehension
lista = [n for n in range(10) if n < 5]

### Dictionary Comprehension e Set Comprehension
produtos = {
    {'nome': 'p1', 'preco': 20},
    {'nome': 'p2', 'preco': 10},
    {'nome': 'p3', 'preco': 30}
}

dc = {
    chave: valor
    for chave, valor
    in produto.items()
}

s1 = {2 ** i for i in range(10)}

print(dc)

### isinstance() -> existe em
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1,2), {0, 1}, {'nome': 'Luiz'}
]

for item in lista:
    print(item, isinstance(item, set))

### valores falsos
lista = []
dicionario = {}
conjunto = set()
tupla = ()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

* tudo que não estiver nessa lista é considerado verdadeiro

### dir, hasattr, getattr
dir -> Se você passar um objeto como argumento para o dir(), ele retornará uma lista com os nomes dos atributos e métodos (também chamados de "membros") desse objeto

hasattr -> A função hasattr() é usada para verificar se um objeto possui um determinado atributo.

getattr -> A função getattr() é usada para obter o valor de um atributo de um objeto.

### verificar tamanho ocupado na memória
import sys

variavel = 'Ola'

print(sys.getsizeof(variavel))

### Generator -> são funções que sabem pausar
* é usado pra não salvar tudo na memória

generator = (n for n in range(100000))

def generator(n=0, maximum=10):
    while True:
        yield n

        n += 1

        if n > maximum:
            return


gen = generator(maximum=10000)
for n in gen:
    print(n)

### Try, except, else e finally

try:
    calc = 18 / 0
except ZeroDivisionError:
    print('Erro, não pode ser dividido por zero")
except NameError:
    print('')
except Exception as e: # TRATA QUALQUER ERRO
    print(f'ERRO {e}')


finally -> ocorreu ou não o erro, quero executar de qualquer forma o finally.
else -> caso o código não de erro

### Raise - lançando exceções (erro)
raise -> lança um erro

raise ValueError('Deu erro')

### count -> iterador

### groupby -> agrupa os dados

### filter -> (condicao, lista)

### reduce
* Ela aplica a função binária de forma cumulativa nos elementos da sequência, ou seja, ela pega os dois primeiros elementos, aplica a função neles, depois pega o resultado dessa aplicação e o próximo elemento da sequência, e assim por diante, até reduzir toda a sequência a um único valor.


from functools import reduce

# funções recursivas
- funções que podem se chamar de volta

def recursiva(inicio=0, fim=10):
    # caso base
    if inicio >= fim:
        return fim

    # caso recursivo
    # contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())
