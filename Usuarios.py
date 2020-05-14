# Classe usuarios pra tela de Login e implementação dos métodos CRUD(Create, read, update and Delete) no DB

from LoginDB import LoginDB


class Usuarios(object):

    def __init__(self, usuario="", senha="", nome="", crm=""):
        self.info = {}
        self.usuario = usuario
        self.senha = senha
        self.nome = nome
        self.crm = crm

    def insertUser(self):

        banco = LoginDB()
        try:

            c = banco.conexao.cursor()

            c.execute("insert into login (usuario, senha, nome, crm) values ( '" + self.usuario + "', '" + self.senha + "', '" + self.nome + "', '" + self.crm + "')")
            banco.conexao.commit()
            c.close()

            return "Usuário cadastrado com sucesso!"
        except:
            return "Falha ao cadastrar usuário!"

    def updateUser(self):
        banco = LoginDB()
        try:

            c = banco.conexao.cursor()

            c.execute("update login set usuario = '" + self.usuario + "', senha = '" + self.senha + "', nome = '" + self.nome + "', crm = '" + self.crm + "' where usuario = '" + self.usuario + "' ")

            banco.conexao.commit()
            c.close()

            return "Usuario alterado com sucesso! "
        except:
            return "Falha ao alterar usuário!"

    def deleteUser(self):
        banco = LoginDB()

        try:
            c = banco.conexao.cursor()

            c.execute("delete from login where usuario = '" + self.usuario + "'  ")

            banco.conexao.commit()
            c.close()

            return "Usuário deletado com sucesso!"
        except:
            return "Falha ao deletar o usuário!"

    def selectUser(self):
        banco = LoginDB()
        try:
            c = banco.conexao.cursor()

            c.execute("select * from login where usuario = '" + self.usuario + "' ")
            for linha in c:
                self.usuario = linha[0]
                self.senha = linha[1]
                self.nome = linha[2]
                self.crm = linha[3]

            c.close()
            return "Busca feita com sucesso!"
        except:
            return "Falha na busca!"

    def verifyLogin(self):
        global pswrd
        banco = LoginDB()

        c = banco.conexao.cursor()

        c.execute(" select senha from login where usuario = '" + self.usuario + "' ")

        for linha in c:
            pswrd = linha[0]

        c.close()

        if self.senha == pswrd:
            return "Login bem sucedido!"
        else:
            return "Senha incorreta!"
