caminho_arquivo = 'C:/Users/x396751/Desktop/Workspace/curso-python/'
caminho_arquivo += 'aula.txt'

# with open(caminho_arquivo, 'w')
# arquivo.close()

with open(caminho_arquivo, 'w+') as arquivo:
    arquivo.write('TESTE 1\n')
    arquivo.write('TESTE 2\n')
    arquivo.seek(0,0)
    print(arquivo.read())

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())