# Modos:
r (leitura), w (escrita), x (para criação)
a (escreve ao final), b (binário)
t (modo texto), + (leitura e escrita)
Context manager - with (abre e fecha)
Métodos úteis
write, read (escrever e ler)
writelines (escrever várias linhas)
seek (move o cursor)
readline (ler linha)
readlines (ler linhas)
Vamos falar mais sobre o módulo os, mas:
os.remove ou unlink - apaga o arquivo
os.rename - troca o nome ou move o arquivo
Vamos falar mais sobre o módulo json, mas:
json.dump = Gera um arquivo json
json.load


# CRIAÇÃO DE ARQUIVOS

caminho_arquivo = 'aula2.txt'

with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
    print(arquivo.write('Atenção'))

# EXCLUIR ARQUIVO
import os

os.remove(caminho_arquivo)

# RENOMEAR
import os

os.rename(caminho_arquivo, 'novo_nome.txt')

# SALVANDO DADOS EM JSON
import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
         {'rua': 'R1', 'numero': 32},
         {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('aula.json', 'w') as arquivo:
    json.dump(pessoa, arquivo)

# CARREGAR ARQUIVO JSON
import json

with open('aula.json', 'r', encoding='utf-8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
