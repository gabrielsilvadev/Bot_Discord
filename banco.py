import sqlite3  #import o sqlite
def cadastroQ(pergunta,resposta):  #funcao que cadastra  as respostas e perguntas
    ini = conexao.cursor()
    ini.execute('''INSERT INTO cadastro(pergunta,resposta)VALUES (?,?)''',(pergunta,resposta))
    conexao.commit()
    print('ok')
    ini.close()
    return 'respoostas cadastradas com uscesso'
def Quizz(): #funcao que retornja as peguntas e respostas
    c = conexao.cursor()
    c.execute("select * from  cadastro")
    dados =c.fetchall()
    for linha in dados:
        return linha
    c.close()

def verifica(idquestoes,resposta):  #funcao que verifica  se a resposta disgitada e vedadeira
    c = conexao.cursor()
    c.execute("select * from cadastro where idquestoes='" +idquestoes+ "'")
    dados = c.fetchall()  #
    for linha in dados:
        print(linha)
        for elem in linha:
            if idquestoes ==linha[0] and resposta== linha[2]:
                return True
            else:
                return False
    c.close()

conexao = sqlite3.connect('banco.db')   #cria conexao com o banco
c = conexao.cursor()  #abre o cursor de comandos nas tabelas
c.execute("""create table if not exists cadastro (        
                  idquestoes integer primary key autoincrement,
                  pergunta varchar(20),
                  resposta varchar(20))""")

conexao.commit() #manda  o comando de criar tabelas para o banco
c.close()  #fecha conexao com o banco
