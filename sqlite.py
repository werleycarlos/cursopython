import sqlite3

# abrir a conexão com o banco
conn = sqlite3.connect('meuBanco.db')

print("------ Conexão aberta! ------")

# criar tabela no banco que esta aberto
conn.execute('''
   CREATE TABLE IF NOT EXISTS Alunos (
             matricula integer,
             nome string,
             curso string
         );
    ''')
conn.commit

print("------Tabela criada com sucesso! ------")


#inserir dados na tabela
conn.execute('INSERT INTO Alunos VALUES(1,"Caio","Python");')
conn.execute('INSERT INTO Alunos VALUES(2,"Eduardo","SQL");')
conn.execute('INSERT INTO Alunos VALUES(3,"Werley","PHP");')
conn.execute('INSERT INTO Alunos VALUES(4,"Amanda","Oracle");')

conn.commit()

print("------ Sados inseridos com sucesso ! ------")

alunos_encontrados = conn.execute('''
        SELECT matricula, nome FROM Alunos;
                                  
        ''')

for linha in alunos_encontrados:
    print("Matricula: " + str(linha[0]))
    print("Nome: " + str(linha[1]))

import pandas as pd
pedido = """ SELECT * FROM Alunos """

estruturadedados = pd.read_sql_query(pedido, conn)

estruturadedados
conn.close













