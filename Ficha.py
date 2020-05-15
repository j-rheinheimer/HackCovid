from FichaDB import FichaDB


class Ficha(object):
    def __init__(self, lista=[]):

        self.lista = None
        self.info = {}
        for c in range(0, 130):
            lista[c] = None


    def insertFicha(self, lista):

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
                      "c39, c40, c41, c42, c43,"
                      "c44, c45_1, c45_2, c46_1, c46_2, c47,"
                      "c48, c49, c50, c51, c52,"
                      "c53, c54, c55, c56, c57,"
                      "c58, c59_1, c59_2, c59_3, c59_4, c59_5,"
                      "c59_6, c59_7, c59_8, c59_9, c60_1,"
                      "c60_2, c61, c62, c63_1_1, c63_1_2, c63_2,"
                      "c63_3, c63_4, c63_5_1, c63_5_2, c63_5_3, c63_5_4,"
                      "c63_5_5, c63_5_6, c63_5_7, c63_5_8, c63_5_9, c63_5_10,"
                      "c63_5_11, c64_1, c64_2, c65, c66, c67,"
                      "c68, c69, c70) values ('" + self.lista[0] + "' ,'" + self.lista[1] + "' , '" + self.lista[2] + "',"
                      "'" + self.lista[3] + "', '" + self.lista[4] + "', '" + self.lista[5] + "', '" + self.lista[6] + "', '" + self.lista[7] + "',"
                      "'" + self.lista[8] + "', '" + self.lista[9] + "', '" + self.lista[10] + "', '" + self.lista[11] + "', '" + self.lista[12] + "',"
                      "'" + self.lista[13] + "', '" + self.lista[14] + "', '" + self.lista[15] + "', '" + self.lista[16] + "', '" + self.lista[17] + "',"
                      "'" + self.lista[18] + "', '" + self.lista[19] + "', '" + self.lista[20] + "', '" + self.lista[21] + "', '" + self.lista[22] + "',"
                      "'" + self.lista[23] + "', '" + self.lista[24] + "', '" + self.lista[25] + "', '" + self.lista[26] + "', '" + self.lista[27] + "',"
                      "'" + self.lista[28] + "', '" + self.lista[29] + "', '" + self.lista[30] + "', '" + self.lista[31] + "', '" + self.lista[32] + "',"
                      "'" + self.lista[33] + "', '" + self.lista[34] + "', '" + self.lista[35] + "', '" + self.lista[36] + "', '" + self.lista[37] + "',"
                      "'" + self.lista[38] + "', '" + self.lista[39] + "', '" + self.lista[40] + "', '" + self.lista[41] + "', '" + self.lista[42] + "',"
                      "'" + self.lista[43] + "', '" + self.lista[44] + "', '" + self.lista[45] + "', '" + self.lista[46] + "', '" + self.lista[47] + "',"
                      "'" + self.lista[48] + "', '" + self.lista[49] + "', '" + self.lista[50] + "', '" + self.lista[51] + "', '" + self.lista[52] + "',"
                      "'" + self.lista[53] + "', '" + self.lista[54] + "', '" + self.lista[55] + "', '" + self.lista[56] + "', '" + self.lista[57] + "',"
                      "'" + self.lista[58] + "', '" + self.lista[59] + "', '" + self.lista[60] + "', '" + self.lista[61] + "', '" + self.lista[62] + "',"
                      "'" + self.lista[63] + "', '" + self.lista[64] + "', '" + self.lista[65] + "', '" + self.lista[66] + "', '" + self.lista[67] + "',"
                      "'" + self.lista[68] + "', '" + self.lista[69] + "', '" + self.lista[70] + "', '" + self.lista[71] + "', '" + self.lista[72] + "',"
                      "'" + self.lista[73] + "', '" + self.lista[74] + "', '" + self.lista[75] + "', '" + self.lista[76] + "',"
                      "'" + self.lista[77] + "', '" + self.lista[78] + "', '" + self.lista[79] + "', '" + self.lista[80] + "', '" + self.lista[81] + "',"
                      "'" + self.lista[82] + "', '" + self.lista[83] + "', '" + self.lista[84] + "', '" + self.lista[85] + "',"
                      "'" + self.lista[86] + "', '" + self.lista[87] + "', '" + self.lista[88] + "', '" + self.lista[89] + "',"
                      "'" + self.lista[90] + "', '" + self.lista[91] + "', '" + self.lista[92] + "', '" + self.lista[93] + "', '" + self.lista[94] + "', "
                      "'" + self.lista[95] + "', '" + self.lista[96] + "', '" + self.lista[97] + "', '" + self.lista[98] + "', '" + self.lista[99] + "',"
                      "'" + self.lista[100] + "', '" + self.lista[101] + "', '" + self.lista[102] + "', '" + self.lista[103] + "',"
                      "'" + self.lista[104] + "', '" + self.lista[105] + "', '" + self.lista[106] + "', '" + self.lista[107] + "', '" + self.lista[108] + "',"
                      "'" + self.lista[109] + "', '" + self.lista[110] + "', '" + self.lista[111] + "', '" + self.lista[112] + "', '" + self.lista[113] + "',"
                      "'" + self.lista[114] + "', '" + self.lista[115] + "', '" + self.lista[116] + "', '" + self.lista[117] + "', '" + self.lista[118] + "',"
                      "'" + self.lista[119] + "', '" + self.lista[120] + "', '" + self.lista[121] + "', '" + self.lista[122] + "', '" + self.lista[123] + "',"
                      "'" + self.lista[124] + "', '" + self.lista[125] + "', '" + self.lista[126] + "', '" + self.lista[127] + "', '" + self.lista[128] + "',"
                      "'" + self.lista[129] + "')")

            banco.conexao.commit()
            c.close()

            return "Ficha cadastrada com sucesso!"
        except:
            return "Falha ao cadastrar Ficha!"
