tipoEscola = input("Tipo do Colégio: \n [1]Público \n [2]Particular: ")
nota01 = input("Nota 1º Bimestre: ")
nota02 = input("Nota 2º Bimestre: ")
nota03 = input("Nota 3º Bimestre: ")
nota04 = input("Nota 4º Bimestre: ")
freqAluno = int(input("Frequência: "))
nomeAluno = input("Nome do Aluno: ")
mediaAluno = (int(nota01) + int(nota02) + int(nota03) + int(nota04)) / 4  

'''
!=
== igual
<= menor ou igual
>= maior ou igual
> maior
<menor
'''

if tipoEscola == "1":
    print("-----Escola Pública------")
    if mediaAluno >= 7 or freqAluno >= 70:
        print("O Aluno " + nomeAluno + " foi aprovado, com media " + str(mediaAluno))
    else:
        print("O Aluno " + nomeAluno + " foi reprovado, com media " + str(mediaAluno))
if tipoEscola == "2":
    print("-----Escola Particular------")
    if mediaAluno >= 7 and freqAluno >= 70:
         print("O Aluno " + nomeAluno + " foi aprovado, com media " + str(mediaAluno))
    else:
       print("O Aluno " + nomeAluno + " foi reprovado, com media " + str(mediaAluno))

print("---Fim do Sistema---")
 



# print("O Aluno(a) " + nomeAluno + " possui media de: " + str(mediaAluno))

