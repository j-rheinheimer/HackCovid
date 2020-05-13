# Classe para o DB dos dados das fichas a serem lançadas
import sqlite3


class FichaDB:

    def __init__(self):
        self.conexao = sqlite3.connect('ficha.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists ficha (
                     nregistro integer primary key autoincrement,

                     )""")
        self.conexao.commit()
        c.close()
