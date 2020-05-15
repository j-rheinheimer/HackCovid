from FichaDB import FichaDB


class Ficha(object):
    def __init__(self, c1="", c2="", c3="", c4_1="", c4_2="", c5_1="",
                 c5_2="", c6="", c7="", c8="", c9="", c10_1="",
                 c10_2="", c11="", c12="", c13="", c14="", c15="",
                 c16="", c17="", c18="", c19_1="", c19_2="", c20="",
                 c21="", c22="", c23="", c24="", c25="", c26="",
                 c27="", c28="", c29="", c30="", c31="", c32="",
                 c33="", c34="", c35_1="", c35_2="", c35_3="", c35_4="",
                 c35_5="", c35_6="", c35_7="", c35_8="", c35_9="", c35_10="",
                 c36_1="", c36_2="", c36_3="", c36_4="", c36_5="", c36_6="",
                 c36_7="", c36_8="", c36_9="", c36_10="", c36_11="",
                 c36_12="", c36_13="", c36_14_1="", c36_14_2="", c37="", c38_1="",
                 c38_2="", c38_3="", c38_4="", c38_5="", c38_6="", c38_7="",
                 c39="", c40_1="", c40_2="", c41="", c42="", c43="",
                 c44="", c45_1="", c45_2="", c46_1="", c46_2="", c47="",
                 c48="", c49="", c50="", c51="", c52="",
                 c53="", c54="", c55="", c56="", c57="",
                 c58="", c59_1="", c59_2="", c59_3="", c59_4="", c59_5="",
                 c59_6="", c59_7="", c59_8="", c59_9="", c59_10="", c60_1="",
                 c60_2="", c61="", c62="", c63_1_1="", c63_1_2="", c63_2="",
                 c63_3="", c63_4="", c63_5_1="", c63_5_2="", c63_5_3="", c63_5_4="",
                 c63_5_5="", c63_5_6="", c63_5_7="", c63_5_8="", c63_5_9="", c63_5_10="",
                 c63_5_11="", c64_1="", c64_2="", c65="", c66="", c67="",
                 c68="", c69="", c70="", c71="", c72=""):

        self.info = {}
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.c4_1 = c4_1
        self.c4_2 = c4_2
        self.c5_1 = c5_1
        self.c5_2 = c5_2
        self.c6 = c6
        self.c7 = c7
        self.c8 = c8
        self.c9 = c9
        self.c10_1 = c10_1
        self.c10_2 = c10_2
        self.c11 = c11
        self.c12 = c12
        self.c13 = c13
        self.c14 = c14
        self.c15 = c15
        self.c16 = c16
        self.c17 = c17
        self.c18 = c18
        self.c19_1 = c19_1
        self.c19_2 = c19_2
        self.c20 = c20
        self.c21 = c21
        self.c22 = c22
        self.c23 = c23
        self.c24 = c24
        self.c25 = c25
        self.c26 = c26
        self.c27 = c27
        self.c28 = c28
        self.c29 = c29
        self.c30 = c30
        self.c31 = c31
        self.c32 = c32
        self.c33 = c33
        self.c34 = c34
        self.c35_1 = c35_1
        self.c35_2 = c35_2
        self.c35_3 = c35_3
        self.c35_4 = c35_4
        self.c35_5 = c35_5
        self.c35_6 = c35_6
        self.c35_7 = c35_7
        self.c35_8 = c35_8
        self.c35_9 = c35_9
        self.c35_10 = c35_10
        self.c36_1 = c36_1
        self.c36_2 = c36_2
        self.c36_3 = c36_3
        self.c36_4 = c36_4
        self.c36_5 = c36_5
        self.c36_6 = c36_6
        self.c36_7 = c36_7
        self.c36_8 = c36_8
        self.c36_9 = c36_9
        self.c36_10 = c36_10
        self.c36_11 = c36_11
        self.c36_12 = c36_12
        self.c36_13 = c36_13
        self.c36_14_1 = c36_14_1
        self.c36_14_2 = c36_14_2
        self.c37 = c37
        self.c38_1 = c38_1
        self.c38_2 = c38_2
        self.c38_3 = c38_3
        self.c38_4 = c38_4
        self.c38_5 = c38_5
        self.c38_6 = c38_6
        self.c38_7 = c38_7
        self.c39 = c39
        self.c40_1 = c40_1
        self.c40_2 = c40_2
        self.c41 = c41
        self.c42 = c42
        self.c43 = c43
        self.c44 = c44
        self.c45_1 = c45_1
        self.c45_2 = c45_2
        self.c46_1 = c46_1
        self.c46_2 = c46_2
        self.c47 = c47
        self.c48 = c48
        self.c49 = c49
        self.c50 = c50
        self.c51 = c51
        self.c52 = c52
        self.c53 = c53
        self.c54 = c54
        self.c55 = c55
        self.c56 = c56
        self.c57 = c57
        self.c58 = c58
        self.c59_1 = c59_1
        self.c59_2 = c59_2
        self.c59_3 = c59_3
        self.c59_4 = c59_4
        self.c59_5 = c59_5
        self.c59_6 = c59_6
        self.c59_7 = c59_7
        self.c59_8 = c59_8
        self.c59_9 = c59_9
        self.c59_10 = c59_10
        self.c60_1 = c60_1
        self.c60_2 = c60_2
        self.c61 = c61
        self.c62 = c62
        self.c63_1_1 = c63_1_1
        self.c63_1_2 = c63_1_2
        self.c63_2 = c63_2
        self.c63_3 = c63_3
        self.c63_4 = c63_4
        self.c63_5_1 = c63_5_1
        self.c63_5_2 = c63_5_2
        self.c63_5_3 = c63_5_3
        self.c63_5_4 = c63_5_4
        self.c63_5_5 = c63_5_5
        self.c63_5_6 = c63_5_6
        self.c63_5_7 = c63_5_7
        self.c63_5_8 = c63_5_8
        self.c63_5_9 = c63_5_9
        self.c63_5_10 = c63_5_10
        self.c63_5_11 = c63_5_11
        self.c64_1 = c64_1
        self.c64_2 = c64_2
        self.c65 = c65
        self.c66 = c66
        self.c67 = c67
        self.c68 = c68
        self.c69 = c69
        self.c70 = c70
        self.c71 = c71
        self.c72 = c72

    def insertFicha(self):

        banco = FichaDB()
        try:

            c = banco.conexao.cursor()

            c.execute(" insert into ficha (c1, c2, c3, c4_1, c4_2, c5_1,"
                      "c5_2, c6, c7, c8, c9, c10_1,"
                      "c10_2, c11, c12, c13, c14, c15,"
                      "c16, c17, c18, c19_1, c19_2, c20,"
                      "c21, c22, c23, c24, c25, c26,"
                      "c27, c28, c29, c30, c31, c32,"
                      "c33, c34, c35_1, c35_2, c35_3, c35_4,"
                      "c35_5, c35_6, c35_7, c35_8, c35_9, c35_10,"
                      "c36_1, c36_2, c36_3, c36_4, c36_5, c36_6,"
                      "c36_7, c36_8, c36_9, c36_10, c36_11,"
                      "c36_12, c36_13, c36_14_1, c36_14_2, c37, c38_1,"
                      "c38_2, c38_3, c38_4, c38_5, c38_6, c38_7,"
                      "c39, c40_1, c40_2, c41, c42, c43,"
                      "c44, c45_1, c45_2, c46_1, c46_2, c47,"
                      "c48, c49, c50, c51, c52,"
                      "c53, c54, c55, c56, c57,"
                      "c58, c59_1, c59_2, c59_3, c59_4, c59_5,"
                      "c59_6, c59_7, c59_8, c59_9, c59_10, c60_1,"
                      "c60_2, c61, c62, c63_1_1, c63_1_2, c63_2,"
                      "c63_3, c63_4, c63_5_1, c63_5_2, c63_5_3, c63_5_4,"
                      "c63_5_5, c63_5_6, c63_5_7, c63_5_8, c63_5_9, c63_5_10,"
                      "c63_5_11, c64_1, c64_2, c65, c66, c67,"
                      "c68, c69, c70, c71, c72) values ('" + self.c1 + "' ,'" + self.c2 + "' , '" + self.c3 + "',"
                      "'" + self.c4_1 + "', '" + self.c4_2 + "', '" + self.c5_1 + "', '" + self.c5_2 + "', '" + self.c6 + "',"
                      "'" + self.c7 + "', '" + self.c8 + "', '" + self.c9 + "', '" + self.c10_1 + "', '" + self.c10_2 + "',"
                      "'" + self.c11 + "', '" + self.c12 + "', '" + self.c13 + "', '" + self.c14 + "', '" + self.c15 + "',"
                      "'" + self.c16 + "', '" + self.c17 + "', '" + self.c18 + "', '" + self.c19_1 + "', '" + self.c19_2 + "',"
                      "'" + self.c20 + "', '" + self.c21 + "', '" + self.c22 + "', '" + self.c23 + "', '" + self.c24 + "',"
                      "'" + self.c25 + "', '" + self.c26 + "', '" + self.c27 + "', '" + self.c28 + "', '" + self.c29 + "',"
                      "'" + self.c30 + "', '" + self.c31 + "', '" + self.c32 + "', '" + self.c33 + "', '" + self.c34 + "',"
                      "'" + self.c35_1 + "', '" + self.c35_2 + "', '" + self.c35_3 + "', '" + self.c35_4 + "', '" + self.c35_5 + "',"
                      "'" + self.c35_6 + "', '" + self.c35_7 + "', '" + self.c35_8 + "', '" + self.c35_9 + "', '" + self.c35_10 + "',"
                      "'" + self.c36_1 + "', '" + self.c36_2 + "', '" + self.c36_3 + "', '" + self.c36_4 + "', '" + self.c36_5 + "',"
                      "'" + self.c36_6 + "', '" + self.c36_7 + "', '" + self.c36_8 + "', '" + self.c36_9 + "', '" + self.c36_10 + "',"
                      "'" + self.c36_11 + "', '" + self.c36_12 + "', '" + self.c36_13 + "', '" + self.c36_14_1 + "', '" + self.c36_14_2 + "',"
                      "'" + self.c37 + "', '" + self.c38_1 + "', '" + self.c38_2 + "', '" + self.c38_3 + "', '" + self.c38_4 + "',"
                      "'" + self.c38_5 + "', '" + self.c38_6 + "', '" + self.c38_7 + "', '" + self.c39 + "', '" + self.c40_1 + "',"
                      "'" + self.c40_2 + "', '" + self.c41 + "', '" + self.c42 + "', '" + self.c43 + "', '" + self.c44 + "',"
                      "'" + self.c45_1 + "', '" + self.c45_2 + "', '" + self.c46_1 + "', '" + self.c46_2 + "', '" + self.c47 + "',"
                      "'" + self.c48 + "', '" + self.c49 + "', '" + self.c50 + "', '" + self.c51 + "',"
                      "'" + self.c52 + "', '" + self.c53 + "', '" + self.c54 + "', '" + self.c55 + "',"
                      "'" + self.c56 + "', '" + self.c57 + "', '" + self.c58 + "', '" + self.c59_1 + "', '" + self.c59_2 + "', "
                      "'" + self.c59_3 + "', '" + self.c59_4 + "', '" + self.c59_5 + "', '" + self.c59_6 + "', '" + self.c59_7 + "',"
                      "'" + self.c59_8 + "', '" + self.c59_9 + "', '" + self.c59_10 + "', '" + self.c60_1 + "', '" + self.c60_2 + "',"
                      "'" + self.c61 + "', '" + self.c62 + "', '" + self.c63_1_1 + "', '" + self.c63_1_2 + "', '" + self.c63_2 + "',"
                      "'" + self.c63_3 + "', '" + self.c63_4 + "', '" + self.c63_5_1 + "', '" + self.c63_5_2 + "', '" + self.c63_5_3 + "',"
                      "'" + self.c63_5_4 + "', '" + self.c63_5_5 + "', '" + self.c63_5_6 + "', '" + self.c63_5_7 + "', '" + self.c63_5_8 + "',"
                      "'" + self.c63_5_9 + "', '" + self.c63_5_10 + "', '" + self.c63_5_11 + "', '" + self.c64_1 + "', '" + self.c64_2 + "',"
                      "'" + self.c65 + "', '" + self.c66 + "', '" + self.c67 + "', '" + self.c68 + "', '" + self.c69 + "',"
                      "'" + self.c70 + "', '" + self.c71 + "', '" + self.c72 + "')")

            banco.conexao.commit()
            c.close()

            return "Ficha cadastrada com sucesso!"
        except:
            return "Falha ao cadastrar Ficha!"
