# Classe do DB dos usuarios (logins, senhas, nomes dos médicos e CRM's) <sujeito a alterações>

import sqlite3


class LoginDB:

    def __init__(self):
        self.conexao = sqlite3.connect('login.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists login (
                    usuario text,
                    senha text,
                    nome text,
                    crm text)""")
        self.conexao.commit()
        c.close()
