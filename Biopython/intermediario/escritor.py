sequencia = input("Digite a sequencia: ")

arquivo = open("sequencia.fasta", "w")

arquivo.write(">Nova sequencia\n")
arquivo.write(sequencia)
arquivo.close()