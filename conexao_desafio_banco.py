 
import sqlite3 
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#1. Crie uma tabela chamada "alunos" com os seguintes campos: id
#  (inteiro), nome (texto), idade (inteiro) e curso (texto).
cursor.execute('CREATE TABLE alunos (id INT, nome varchar(50), idade INT, curso varchar(100));')

#2. Insira pelo menos 5 registros de alunos na tabela que você criou no
#exercício anterior.
cursor.execute('INSERT INTO alunos VALUES (1, "ANA",24,"ADM");')
cursor.execute('INSERT INTO alunos VALUES (2, "BIA",28,"ENGENHARIA");')
cursor.execute('INSERT INTO alunos VALUES (3, "JOAO",27,"BIOLOGIA");')
cursor.execute('INSERT INTO alunos VALUES (4, "CAIO",26,"ADS");')
cursor.execute('INSERT INTO alunos VALUES (5, "JULIA",19,"MATEMATICA");')


#3. Consultas Básicas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecionar todos os registros da tabela "alunos".
dados = cursor.execute('select * from alunos;')
for alunos in dados:
 print(alunos)

#b) Selecionar o nome e a idade dos alunos com mais de 20 anos.
dados = cursor.execute('SELECT * FROM alunos WHERE idade > 20;')
for alunos in dados:
 print(alunos)
 
#c) Selecionar os alunos do curso de "Engenharia" em ordem alfabética.
dados = cursor.execute('SELECT * FROM alunos WHERE curso ="ENGENHARIA" order by nome;')
for alunos in dados:
 print(alunos)
 
#d) Contar o número total de alunos na tabela
dados = cursor.execute('SELECT count(*) FROM alunos;')
for alunos in dados:
 print(alunos)

#4. Atualização e Remoção
#a) Atualize a idade de um aluno específico na tabela.
dados = cursor.execute('UPDATE alunos SET idade = 31 where id = 3;')
for alunos in dados:
 print(alunos)

#b) Remova um aluno pelo seu ID.
dados = cursor.execute('DELETE FROM alunos where id = 4;')
for alunos in dados:
 print(alunos)

#5. Criar uma Tabela e Inserir Dados
#Crie uma tabela chamada "clientes" com os campos: id (chave
#primária), nome (texto), idade (inteiro) e saldo (float). Insira alguns
#registros de clientes na tabela.
cursor.execute('CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome varchar(50), idade INT, saldo float);')


cursor.execute('INSERT INTO clientes VALUES (NULL,"ANA",24,3.15);')
cursor.execute('INSERT INTO clientes VALUES (NULL,"BIA",28,1000);')
cursor.execute('INSERT INTO clientes VALUES (NULL,"JOAO",27,70);')
cursor.execute('INSERT INTO clientes VALUES (NULL,"CAIO",31,5.200);')
cursor.execute('INSERT INTO clientes VALUES (NULL,"JULIA",19,2.500);')


#6. Consultas e Funções Agregadas
#Escreva consultas SQL para realizar as seguintes tarefas:
#a) Selecione o nome e a idade dos clientes com idade superior a 30 anos.
dados = cursor.execute('SELECT nome, idade FROM clientes WHERE idade > 30;')
for clientes in dados:
 print(clientes)

#b) Calcule o saldo médio dos clientes.
dados = cursor.execute('select avg(saldo)from clientes;')
for clientes in dados:
 print(clientes)

#c) Encontre o cliente com o saldo máximo.
dados = cursor.execute('select  max(saldo) , nome from clientes limit 1')
for clientes in dados:
 print(clientes)

#d) Conte quantos clientes têm saldo acima de 1000.
dados = cursor.execute('select count(*) from clientes where saldo > 1000;')
for clientes in dados:
 print(clientes)


#7. Atualização e Remoção com Condições
#a) Atualize o saldo de um cliente específico.
dados = cursor.execute('UPDATE clientes SET saldo = 50 where id = 1;')
for clientes in dados:
 print(clientes)

#b) Remova um cliente pelo seu ID.
dados = cursor.execute('DELETE FROM clientes where id = 1;')
for clientes in dados:
 print(clientes)

#8. Junção de Tabelas
#Crie uma segunda tabela chamada "compras" com os campos: id
#(chave primária), cliente_id (chave estrangeira referenciando o id
#da tabela "clientes"), produto (texto) e valor (real). Insira algumas
#compras associadas a clientes existentes na tabela "clientes".
#Escreva uma consulta para exibir o nome do cliente, o produto e o
#valor de cada compra.

cursor.execute('CREATE TABLE compras (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id varchar(50), produto varchar(50), valor float);')

cursor.execute('INSERT INTO compras VALUES (NULL,1,"escova de dente", 1.50);')
cursor.execute('INSERT INTO compras VALUES (NULL,2,"pente de cabelo", 10);')

dados = cursor.execute('SELECT nome, produto, valor as valor_compra FROM clientes c inner join compras p on c.id = p.cliente_id;')
for clientes_compras in dados:
 print(clientes_compras)



#para commitar os codigos e enviar para o banco
conexao.commit()

#para fechar a conexão, não é bom deixar conexao em arquivos py abertos
conexao.close