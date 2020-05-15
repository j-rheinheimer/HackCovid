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
                     c1 text, c2 text, c3 text, c4_1 text, c4_2 text,
                     c5_1 text, c5_2 text, c6 text, c7 text, c8 text, 
                     c9 text, c10_1 text, c10_2 text, c11 text, c12 text,
                     c13 text, c14 text, c15 text, c16 text, c17 text,
                     c18 text, c19_1 text, c19_2 text, c20 text, c21 text,
                     c22 text, c23 text, c24 text, c25 text, c26 text,
                     c27 text, c28 text, c29 text, c30 text, c31 text,
                     c32 text, c33 text, c34 text, c35_1 text, c35_2 text,
                     c35_3 text, c35_4 text, c35_5 text, c35_6 text, c35_7 text,
                     c35_8 text, c35_9 text, c35_10 text, c36_1 text, c36_2 text,
                     c36_3 text, c36_4 text, c36_5 text, c36_6 text,
                     c36_7 text, c36_8 text, c36_9 text, c36_10 text, c36_11 text,
                     c36_12 text, c36_13 text, c36_14_1 text, c36_14_2 text,
                     c37 text, c38_1 text, c38_2 text, c38_3 text, c38_4 text,
                     c38_5 text, c38_6 text, c38_7 text, c39 text, c40 text,
                     c41 text, c42 text, c43 text, c44 text, c45_1 text, c45_2 text,
                     c46_1 text, c46_2 text, c47 text, c48 text, c49 text, c50 text, c51 text,
                     c52 text, c53 text, c54 text, c55 text, c56 text,
                     c57 text, c58 text, c59_1 text, c59_2 text, c59_3 text, c59_4 text, c59_5 text, c59_6 text,
                     c59_7 text, c59_8 text, c59_9 text, c60_1 text, c60_2 text, c61 text, c62 text,
                     c63_1_1 text, c63_1_2 text, c63_2 text,c63_3 text, c63_4 text, c63_5_1 text,
                     c63_5_2, c63_5_3 text, c63_5_4 text, c63_5_5 text, c63_5_6 text, c63_5_7 text, c63_5_8 text, 
                     c63_5_9 text, c63_5_10 text,c63_5_11 text, c64_1 text, c64_2 text, c65 text,c66 text,
                     c67 text, c68 text, c69 text, c70 text)""")

        self.conexao.commit()
        c.close()
