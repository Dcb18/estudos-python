
def leitorDeArquivo(nome):
    arquivo = open(nome, "r")
    conteudo_arquivo = arquivo.read()
    return conteudo_arquivo
    
    
nome_do_arquivo = input("Digite o nome do arquivo: ")
arquivo = leitorDeArquivo(nome_do_arquivo) 
print(arquivo)

