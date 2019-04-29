import re
primeira_sequencia = input("digite a primeira sequencia: ")
segunda_sequencia = input("digite a segunda sequencia: ")

comparacao = re.match(primeira_sequencia, segunda_sequencia)

if comparacao:
    print("As sequencias são identicas")
else:
    print("As sequencias são diferentes")
