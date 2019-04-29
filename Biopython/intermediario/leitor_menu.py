def leitorDeArquivo(nome):
    arquivo = open(nome, "r")
    conteudo_arquivo = arquivo.read()
    return conteudo_arquivo
    
comando = 0

while comando !=3:
    comando = int(input("Digite 1 para ler um arquivo, 2 para exibir um valor e 3 para fechar: "))
    if comando == 1:
        nome_arquivo = input("Digite o nome do arquvio: ")
        arquivo = leitorDeArquivo(nome_arquivo)
    elif comando == 2:
        try:
            print(arquivo)
        except:
            print("Não foi possivel ler o arquivo")
    elif comando < 1 or comando > 3:
        print("Digite um comando valido")
        