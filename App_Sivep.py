# Programa principal, onde fica a programação da interface do aplicativo

from Usuarios import *
from tkinter import *


class Application:

    def __init__(self, master=None):
        self.fonte = ("Verdana", "10")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 15
        self.container8["pady"] = 5
        self.container8.pack()

        self.logTitulo = Label(self.container1, text="Dados de Login")
        self.logTitulo["font"] = ("Calibri", "12", "bold")
        self.logTitulo.pack()

        self.lblUsuario = Label(self.container2, text="Usuario", font=self.fonte, width=10)
        self.lblUsuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container2)
        self.txtusuario["font"] = self.fonte
        self.txtusuario["width"] = 10
        self.txtusuario.pack(side=LEFT)

        self.btnLogin = Button(self.container2, text="Login", font=self.fonte, width=12)
        self.btnLogin["command"] = self.efetuaLogin
        self.btnLogin.pack(side=RIGHT)

        self.lblsenha = Label(self.container2, text="Senha", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container2)
        self.txtsenha["font"] = self.fonte
        self.txtsenha["width"] = 10
        self.txtsenha["show"] = "*"
        self.txtsenha.pack(side=LEFT)

        self.lblnome = Label(self.container4, text="Nome", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container4)
        self.txtnome["font"] = self.fonte
        self.txtnome["width"] = 10
        self.txtnome.pack(side=LEFT)

        self.lblcrm = Label(self.container5, text="CRM", font=self.fonte, width=10)
        self.lblcrm.pack(side=LEFT)

        self.txtcrm = Entry(self.container5)
        self.txtcrm["font"] = self.fonte
        self.txtcrm["width"] = 10
        self.txtcrm.pack(side=LEFT)

        self.lblmsg = Label(self.container6, text=" ")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

        self.btnCadastrar = Button(self.container7, text="Cadastrar", font=self.fonte, width=12)
        self.btnCadastrar["command"] = self.janelaCadastro
        self.btnCadastrar.pack(side=LEFT)

        self.btnAlterar = Button(self.container7, text="Alterar", font=self.fonte, width=12)
        self.btnAlterar["command"] = self.alterarUsuario
        self.btnAlterar.pack(side=LEFT)

        self.btnExcluir = Button(self.container7, text="Excluir", font=self.fonte, width=12)
        self.btnExcluir["command"] = self.excluirUsuario
        self.btnExcluir.pack(side=LEFT)

        self.btnBuscar = Button(self.container8, text="Buscar", font=self.fonte, width=12)
        self.btnBuscar["command"] = self.buscarUsuario
        self.btnBuscar.pack(side=RIGHT)

    def janelaCadastro(self):

        janela_de_cadastro = Toplevel(root)
        janela_de_cadastro.title("Sivep Cadastro")

        self.container1 = Frame(janela_de_cadastro)
        self.container1["pady"] = 10
        self.container1.pack()

        self.lblteste = Label(self.container1, text="Cadastro de Usuário", font=("Calibri", "15", "bold"))
        self.lblteste.pack()

        self.container2 = Frame(janela_de_cadastro)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(janela_de_cadastro)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(janela_de_cadastro)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(janela_de_cadastro)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(janela_de_cadastro)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()

        self.lblusuario = Label(self.container2, text='Usuário', font=self.fonte)
        self.lblusuario.pack(side=LEFT)

        self.txtusuario = Entry(self.container2)
        self.txtusuario["font"] = self.fonte
        self.txtusuario["width"] = 12
        self.txtusuario.pack(side=LEFT)

        self.lblsenha = Label(self.container3, text='Senha', font=self.fonte)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container3)
        self.txtsenha["font"] = self.fonte
        self.txtsenha["width"] = 12
        self.txtsenha.pack(side=LEFT)

        self.lblnome = Label(self.container4, text='Nome', font=self.fonte)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container4)
        self.txtnome["font"] = self.fonte
        self.txtnome["width"] = 12
        self.txtnome.pack(side=LEFT)

        self.lblcrm = Label(self.container5, text='CRM', font=self.fonte)
        self.lblcrm.pack(side=LEFT)

        self.txtcrm = Entry(self.container5)
        self.txtcrm["font"] = self.fonte
        self.txtcrm["width"] = 12
        self.txtcrm.pack(side=LEFT)

        self.btnCadastrar = Button(self.container6, text="Cadastrar", font=self.fonte)
        self.btnCadastrar["command"] = self.cadastrarUsuario
        self.btnCadastrar.pack()

    def janelaFicha(self):
        janela_da_ficha = Toplevel(root)
        janela_da_ficha.title("Sivep Ficha")

        self.container1 = Frame(janela_da_ficha)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(janela_da_ficha)
        self.container2["padx"] = 20
        self.container2["pady"] = 8
        self.container2.pack()
        self.container3 = Frame(janela_da_ficha)
        self.container3["padx"] = 20
        self.container3["pady"] = 8
        self.container3.pack()
        self.container4 = Frame(janela_da_ficha)
        self.container4["padx"] = 20
        self.container4["pady"] = 8
        self.container4.pack()
        self.container5 = Frame(janela_da_ficha)
        self.container5["padx"] = 20
        self.container5["pady"] = 8
        self.container5.pack()
        self.container6 = Frame(janela_da_ficha)
        self.container6["padx"] = 20
        self.container6["pady"] = 8
        self.container6.pack()
        self.container7 = Frame(janela_da_ficha)
        self.container7["padx"] = 20
        self.container7["pady"] = 8
        self.container7.pack()
        self.container8 = Frame(janela_da_ficha)
        self.container8["padx"] = 20
        self.container8["pady"] = 8
        self.container8.pack()
        self.container9 = Frame(janela_da_ficha)
        self.container9["padx"] = 20
        self.container9["pady"] = 8
        self.container9.pack()

        self.titulo = Label(self.container1, text="Preenchimento de Ficha SIVEP", font=("Calibri", "15", "bold"))
        self.titulo.pack()

        self.lblc1 = Label(self.container2, text="Data de preenchimento: ", font=self.fonte)
        self.lblc1.pack(side=LEFT)

        self.txtc1 = Entry(self.container2)
        self.txtc1["font"] = self.fonte
        self.txtc1["width"] = 10
        self.txtc1.pack(side=LEFT)

        self.lblc2 = Label(self.container2, text=" Data dos primeiros sintomas: ", font=self.fonte)
        self.lblc2.pack(side=LEFT)

        self.txtc2 = Entry(self.container2)
        self.txtc2["font"] = self.fonte
        self.txtc2["width"] = 10
        self.txtc2.pack(side=LEFT)

        self.lblc3 = Label(self.container2, text=" UF: ", font=self.fonte)
        self.lblc3.pack(side=LEFT)

        self.txtc3 = Entry(self.container2)
        self.txtc3["font"] = self.fonte
        self.txtc3["width"] = 2
        self.txtc3.pack(side=LEFT)

        self.lblc4 = Label(self.container2, text="Município: ", font=self.fonte)
        self.lblc4.pack(side=LEFT)

        self.txtc4 = Entry(self.container2)
        self.txtc4["font"] = self.fonte
        self.txtc4["width"] = 20
        self.txtc4.pack(side=LEFT)

        self.lblc5 = Label(self.container2, text="Código(IBGE): ", font=self.fonte)
        self.lblc5.pack(side=LEFT)

        self.txtc5 = Entry(self.container2)
        self.txtc5["font"] = self.fonte
        self.txtc5["width"] = 13
        self.txtc5.pack(side=LEFT)

        self.lblc6 = Label(self.container2, text="Unidade de Saúde: ", font=self.fonte)
        self.lblc6.pack(side=LEFT)

        self.txtc6 = Entry(self.container2)
        self.txtc6["font"] = self.fonte
        self.txtc6["width"] = 20
        self.txtc6.pack(side=LEFT)

        self.lblc7 = Label(self.container2, text="Código(CMES):", font=self.fonte)
        self.lblc7.pack(side=LEFT)

        self.txtc7 = Entry(self.container2)
        self.txtc7["font"] = self.fonte
        self.txtc7["width"] = 13
        self.txtc7.pack(side=LEFT)

        self.dados_pessoais = Label(self.container3, text="Dados do Paciente", font=("Calibri", "12", "bold"))
        self.dados_pessoais.pack()

        self.lblc8 = Label(self.container4, text="Nome: ", font=self.fonte)
        self.lblc8.pack(side=LEFT)

        self.txtc8 = Entry(self.container4)
        self.txtc8["font"] = self.fonte
        self.txtc8["width"] = 25
        self.txtc8.pack(side=LEFT)

        self.lblc9 = Label(self.container4, text=" Sexo(M/F/N.D): ", font=self.fonte)
        self.lblc9.pack(side=LEFT)

        self.txtc9= Entry(self.container4)
        self.txtc9["font"] = self.fonte
        self.txtc9["width"] = 3
        self.txtc9.pack(side=LEFT)

        self.lblc10 = Label(self.container4, text=" Data de Nascimento: ", font=self.fonte)
        self.lblc10.pack(side=LEFT)

        self.txtc10 = Entry(self.container4)
        self.txtc10["font"] = self.fonte
        self.txtc10["width"] = 10
        self.txtc10.pack(side=LEFT)

        self.lblc11 = Label(self.container4, text=" Gestante(com tempo): ", font=self.fonte)
        self.lblc11.pack(side=LEFT)

        self.txtc11 = Entry(self.container4)
        self.txtc11["font"] = self.fonte
        self.txtc11["width"] = 10
        self.txtc11.pack(side=LEFT)

        self.lblc12 = Label(self.container4, text=" Raça/Cor: ", font=self.fonte)
        self.lblc12.pack(side=LEFT)

        self.txtc12 = Entry(self.container4)
        self.txtc12["font"] = self.fonte
        self.txtc12["width"] = 10
        self.txtc12.pack(side=LEFT)

        self.lblc13 = Label(self.container4, text=" Se indígena, etnia: ", font=self.fonte)
        self.lblc13.pack(side=LEFT)

        self.txtc13 = Entry(self.container4)
        self.txtc13["font"] = self.fonte
        self.txtc13["width"] = 20
        self.txtc13.pack(side=LEFT)

        self.lblc14 = Label(self.container5, text=" Escolaridade: ", font=self.fonte)
        self.lblc14.pack(side=LEFT)

        self.txtc14 = Entry(self.container5)
        self.txtc14["font"] = self.fonte
        self.txtc14["width"] = 20
        self.txtc14.pack(side=LEFT)

        self.lblc15 = Label(self.container5, text=" Ocupação: ", font=self.fonte)
        self.lblc15.pack(side=LEFT)

        self.txtc15 = Entry(self.container5)
        self.txtc15["font"] = self.fonte
        self.txtc15["width"] = 20
        self.txtc15.pack(side=LEFT)

        self.lblc16 = Label(self.container5, text=" Nome da mãe: ", font=self.fonte)
        self.lblc16.pack(side=LEFT)

        self.txtc16 = Entry(self.container5)
        self.txtc16["font"] = self.fonte
        self.txtc16["width"] = 20
        self.txtc16.pack(side=LEFT)

        self.dados_residencia = Label(self.container6, text="Dados de Residência", font=("Calibri", "12", "bold"))
        self.dados_residencia.pack()

        self.lblc17 = Label(self.container7, text="CEP: ", font=self.fonte)
        self.lblc17.pack(side=LEFT)

        self.txtc17 = Entry(self.container7)
        self.txtc17["font"] = self.fonte
        self.txtc17["width"] = 15
        self.txtc17.pack(side=LEFT)

        self.lblc18 = Label(self.container7, text=" UF: ", font=self.fonte)
        self.lblc18.pack(side=LEFT)

        self.txtc18 = Entry(self.container7)
        self.txtc18["font"] = self.fonte
        self.txtc18["width"] = 2
        self.txtc18.pack(side=LEFT)

        self.lblc19 = Label(self.container7, text=" Município: ", font=self.fonte)
        self.lblc19.pack(side=LEFT)

        self.txtc19 = Entry(self.container7)
        self.txtc19["font"] = self.fonte
        self.txtc19["width"] = 25
        self.txtc19.pack(side=LEFT)

        self.lblc20 = Label(self.container7, text=" Código(IBGE): ", font=self.fonte)
        self.lblc20.pack(side=LEFT)

        self.txtc20 = Entry(self.container7)
        self.txtc20["font"] = self.fonte
        self.txtc20["width"] = 13
        self.txtc20.pack(side=LEFT)

        self.lblc21 = Label(self.container7, text=" Bairro: ", font=self.fonte)
        self.lblc21.pack(side=LEFT)

        self.txtc21 = Entry(self.container7)
        self.txtc21["font"] = self.fonte
        self.txtc21["width"] = 20
        self.txtc21.pack(side=LEFT)

        self.lblc22 = Label(self.container7, text=" Logradouro: ", font=self.fonte)
        self.lblc22.pack(side=LEFT)

        self.txtc22 = Entry(self.container7)
        self.txtc22["font"] = self.fonte
        self.txtc22["width"] = 20
        self.txtc22.pack(side=LEFT)

        self.lblc23 = Label(self.container7, text=" Nº: ", font=self.fonte)
        self.lblc23.pack(side=LEFT)

        self.txtc23 = Entry(self.container7)
        self.txtc23["font"] = self.fonte
        self.txtc23["width"] = 4
        self.txtc23.pack(side=LEFT)

        self.lblc24 = Label(self.container7, text=" Complemento: ", font=self.fonte)
        self.lblc24.pack(side=LEFT)

        self.txtc24 = Entry(self.container7)
        self.txtc24["font"] = self.fonte
        self.txtc24["width"] = 15
        self.txtc24.pack(side=LEFT)

        self.lblc25 = Label(self.container8, text="Telefone(DDD): ", font=self.fonte)
        self.lblc25.pack(side=LEFT)

        self.txtc25 = Entry(self.container8)
        self.txtc25["font"] = self.fonte
        self.txtc25["width"] = 15
        self.txtc25.pack(side=LEFT)

        self.lblc26 = Label(self.container8, text=" Zona: ", font=self.fonte)
        self.lblc26.pack(side=LEFT)

        self.txtc26 = Entry(self.container8)
        self.txtc26["font"] = self.fonte
        self.txtc26["width"] = 20
        self.txtc26.pack(side=LEFT)

        self.lblc27 = Label(self.container8, text=" País(se residente fora do Brasil): ", font=self.fonte)
        self.lblc27.pack(side=LEFT)

        self.txtc27 = Entry(self.container8)
        self.txtc27["font"] = self.fonte
        self.txtc27["width"] = 20
        self.txtc27.pack(side=LEFT)

    def dadosLaboratoriais(self):
        dados_laboratoriais = Toplevel(root)
        dados_laboratoriais.title('Formulário SIVEP')

        self.container1 = Frame(dados_laboratoriais)
        self.container1['pady'] = 10
        self.container1.pack()

        self.lbl_titulo = Label(self.container1)
        self.lbl_titulo['text'] = 'Dados Laboratoriais'
        self.lbl_titulo['font'] = ('Verdana', '12', 'bold')
        self.lbl_titulo.pack()

        self.container2 = Frame(dados_laboratoriais)
        self.container2['padx'] = 10
        self.container2['pady'] = 8
        self.container2.pack()

        self.lbl_c56 = Label(self.container2)
        self.lbl_c56['text'] = '56 - Nº Requisição do GAL'
        self.lbl_c56.pack(side=LEFT)

        self.txt_c56 = Entry(self.container2)
        self.txt_c56['width'] = 100
        self.txt_c56.pack(side=LEFT) 

        self.container3 = Frame(dados_laboratoriais)
        self.container3['padx'] = 10
        self.container3['pady'] = 8
        self.container3.pack()

        self.lbl_c57 = Label(self.container3)
        self.lbl_c57['text'] = ('57 - Resultado da IF/outro método que não seja biologia molecular:'+
            '(1 - Positivo, 2 - Negativo, 3 - Inconclusivo, '+
            '4 - Não realizado, 5 - Aguardando resultado, 9 - Ignorado):')
        self.lbl_c57.pack(side=LEFT)

        self.txt_c57 = Entry(self.container3)
        self.txt_c57['width'] = 2
        self.txt_c57.pack(side=LEFT)

        self.container4 = Frame(dados_laboratoriais)
        self.container4['padx'] = 10
        self.container4['pady'] = 8
        self.container4.pack()

        self.lbl_c58 = Label(self.container4)
        self.lbl_c58['text'] = '58 - Data do resultado da IF/outro método que não seja Biologia Molecular:'
        self.lbl_c58.pack(side=LEFT)

        self.txt_c58 = Entry(self.container4)
        self.txt_c58['width'] = 15
        self.txt_c58.pack(side=LEFT)

        self.container5 = Frame(dados_laboratoriais)
        self.container5['padx'] = 10
        self.container5['pady'] = 8
        self.container5.pack()

        self.lbl_c59_title1 = Label(self.container5)
        self.lbl_c59_title1['text'] = '59 - Agente Etiológico - IF/outro método que não seja Biologia Molecular:'
        self.lbl_c59_title1.pack(side=LEFT)

        self.lbl_c59_1 = Label(self.container5)
        self.lbl_c59_1['text'] = 'Positivo para influenza? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lbl_c59_1.pack(side=LEFT)

        self.txt_c59_1 = Entry(self.container5)
        self.txt_c59_1['width'] = 2
        self.txt_c59_1.pack(side=LEFT)

        self.lbl_c59_2 = Label(self.container5)
        self.lbl_c59_2['text'] = 'Se sim, qual influenza? (1 - Influenza A, 2 - Influenza B):'
        self.lbl_c59_2.pack(side=LEFT)

        self.txt_c59_2 = Entry(self.container5)
        self.txt_c59_2['width'] = 2
        self.txt_c59_2.pack(side=LEFT)

        self.lbl_c59_3 = Label(self.container5)
        self.lbl_c59_3['text'] = 'Positivo para outro vírus? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lbl_c59_3.pack(side=LEFT)

        self.txt_c59_3 = Entry(self.container5)
        self.txt_c59_3['width'] = 2
        self.txt_c59_3.pack(side=LEFT)

        self.container6 = Frame(dados_laboratoriais)
        self.container6['padx'] = 10
        self.container6['pady'] = 8
        self.container6.pack()

        self.lbl_c59_title2 = Label(self.container6)
        self.lbl_c59_title2['text'] = 'Se outro vírus respiratórios qual(is)? (Marcar X): '
        self.lbl_c59_title2.pack(side=LEFT)

        self.lbl_c59_4 = Label(self.container6)
        self.lbl_c59_4['text'] = 'Virus Sincicial Respiratório:'
        self.lbl_c59_4.pack(side=LEFT)

        self.txt_c59_4 = Entry(self.container6)
        self.txt_c59_4['width'] = 2
        self.txt_c59_4.pack(side=LEFT)

        self.lbl_c59_5 = Label(self.container6)
        self.lbl_c59_5['text'] = 'Parainfluenza 1:'
        self.lbl_c59_5.pack(side=LEFT)

        self.txt_c59_5 = Entry(self.container6)
        self.txt_c59_5['width'] = 2
        self.txt_c59_5.pack(side=LEFT)

        self.lbl_c59_6 = Label(self.container6)
        self.lbl_c59_6['text'] = 'Parainfluenza 2:'
        self.lbl_c59_6.pack(side=LEFT)

        self.txt_c59_6 = Entry(self.container6)
        self.txt_c59_6['width'] = 2
        self.txt_c59_6.pack(side=LEFT)

        self.lbl_c59_7 = Label(self.container6)
        self.lbl_c59_7['text'] = 'Parainfluenza 3:'
        self.lbl_c59_7.pack(side=LEFT)

        self.txt_c59_7 = Entry(self.container6)
        self.txt_c59_7['width'] = 2
        self.txt_c59_7.pack(side=LEFT)

        self.lbl_c59_8 = Label(self.container6)
        self.lbl_c59_8['text'] = 'Adenovírus:'
        self.lbl_c59_8.pack(side=LEFT)

        self.txt_c59_8 = Entry(self.container6)
        self.txt_c59_8['width'] = 2
        self.txt_c59_8.pack(side=LEFT)

        self.lbl_c59_9 = Label(self.container6)
        self.lbl_c59_9['text'] = 'Outro vírus respiratório, especifique:'
        self.lbl_c59_9.pack(side=LEFT)

        self.txt_c59_9 = Entry(self.container6)
        self.txt_c59_9['width'] = 15
        self.txt_c59_9.pack(side=LEFT)

        self.container7 = Frame(dados_laboratoriais)
        self.container7['padx'] = 10
        self.container7['pady'] = 8
        self.container7.pack()

        self.lbl_c60_1 = Label(self.container7)
        self.lbl_c60_1['text'] = '60 - Laboratório que realizou IF/outro método que não seja biologia molecular:'
        self.lbl_c60_1.pack(side=LEFT)

        self.txt_c60_1 = Entry(self.container7)
        self.txt_c60_1['width'] = 15
        self.txt_c60_1.pack(side=LEFT)

        self.lbl_c60_2 = Label(self.container7)
        self.lbl_c60_2['text'] = 'Código (CNES):'
        self.lbl_c60_2.pack(side=LEFT)

        self.txt_c60_2 = Entry(self.container7)
        self.txt_c60_2['width'] = 10
        self.txt_c60_2.pack(side=LEFT)

        self.container8 = Frame(dados_laboratoriais)
        self.container8['padx'] = 10
        self.container8['pady'] = 8
        self.container8.pack()

        self.lbl_c61 = Label(self.container8)
        self.lbl_c61['text'] = '61 - Resultado da RT-PCR/outro método por Biologia Molecular: (1 - Detectável, 2 - Não detectável, 3 - Inconclusivo, 4 - Não realizado, 5 - Aguardando resultado, 9 - Ignorado)'
        self.lbl_c61.pack(side=LEFT)

        self.txt_c61 = Entry(self.container8)
        self.txt_c61['width'] = 2
        self.txt_c61.pack(side=LEFT)

        self.container9 = Frame(dados_laboratoriais)
        self.container9['padx'] = 10
        self.container9['pady'] = 8
        self.container9.pack()

        self.lbl_c62 = Label(self.container9)
        self.lbl_c62['text'] = '62 - Data do resultado RT-PCR/Outro métdodo por Biologia Molecular:'
        self.lbl_c62.pack(side=LEFT)

        self.txt_c62 = Entry(self.container9)
        self.txt_c62['width'] = 15
        self.txt_c62.pack(side=LEFT)

        self.container10 = Frame(dados_laboratoriais)
        self.container10['padx'] = 10
        self.container10['pady'] = 8
        self.container10.pack()

        self.lbl_c63_1_1 = Label(self.container10)
        self.lbl_c63_1_1['text'] = ('63 - Agente Etiológico - RT-PCR/outro método por Biologia Molecular '+
            'Positivo para Influenza? (1 - Sim, 2 - Não, 9 - Ignorado): ')
        self.lbl_c63_1_1.pack(side=LEFT)

        self.txt_c63_1_1 = Entry(self.container10)
        self.txt_c63_1_1['width'] = 2
        self.txt_c63_1_1.pack(side=LEFT)

        self.lbl_c63_1_2 = Label(self.container10)
        self.lbl_c63_1_2['text'] = 'Se sim, qual influenza? (1 - Influenza A, 2 - Influenza B):'
        self.lbl_c63_1_2.pack(side=LEFT)

        self.txt_c63_1_2 = Entry(self.container10)
        self.txt_c63_1_2['width'] = 2
        self.txt_c63_1_2.pack(side=LEFT)

        self.container11 = Frame(dados_laboratoriais)
        self.container11['padx'] = 10
        self.container11['pady'] = 8
        self.container11.pack()   

        self.lbl_c63_2 = Label(self.container11)
        self.lbl_c63_2['text'] = ('Influenza A, qual subtipo? '+
            '(1 - Influenza A(H1N1)pdm09, 2 - Influenza A/H3N2, '+
            '3 - Influenza A não subtipado, 4 - Influenza A não subtipável, '+
            '5 - Inconclusivo, 6 - Outro, especifique):')
        self.lbl_c63_2.pack(side=LEFT)

        self.txt_c63_2 = Entry(self.container11)
        self.txt_c63_2['width'] = 10
        self.txt_c63_2.pack(side=LEFT)

        self.container12 = Frame(dados_laboratoriais)
        self.container12['padx'] = 10
        self.container12['pady'] = 8
        self.container12.pack()

        self.lbl_c63_3 = Label(self.container12)
        self.lbl_c63_3['text'] = ('Influenza B, qual subtipo? '+
            '(1 - Victoria, 2 - Yamagatha, 3 - Não realizado, 4 - Inconclusivo, 5 - Outro, especifique):'
        )
        self.lbl_c63_3.pack(side=LEFT)

        self.txt_c63_3 = Entry(self.container12)
        self.txt_c63_3['width'] = 10
        self.txt_c63_3.pack(side=LEFT)

        self.lbl_c63_4 = Label(self.container12)
        self.lbl_c63_4['text'] = 'Positivo para outro vírus? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lbl_c63_4.pack(side=LEFT)

        self.txt_c63_4 = Entry(self.container12)
        self.txt_c63_4['width'] = 2
        self.txt_c63_4.pack(side=LEFT)

        self.container13 = Frame(dados_laboratoriais)
        self.container13['padx'] = 10
        self.container13['pady'] = 8
        self.container13.pack()

        self.lbl_c63_5_titulo = Label(self.container13)
        self.lbl_c63_5_titulo['text'] = ('Se outros vírus respiratórios, qual (is)? (Marcar X): ')

        self.lbl_c63_5_1 = Label(self.container13)
        self.lbl_c63_5_1['text'] = 'SARS-CoV-2:'
        self.lbl_c63_5_1.pack(side=LEFT)

        self.txt_c63_5_1 = Entry(self.container13)
        self.txt_c63_5_1['width'] = 2
        self.txt_c63_5_1.pack(side=LEFT)

        self.lbl_c63_5_2 = Label(self.container13)
        self.lbl_c63_5_2['text'] = 'Vírus Sincicial Respiratório: '
        self.lbl_c63_5_2.pack(side=LEFT)

        self.txt_c63_5_2 = Entry(self.container13)
        self.txt_c63_5_2['width'] = 2
        self.txt_c63_5_2.pack(side=LEFT)

        self.lbl_c63_5_3 = Label(self.container13)
        self.lbl_c63_5_3['text'] = 'Parainfluenza 1: '
        self.lbl_c63_5_3.pack(side=LEFT)

        self.txt_c63_5_3 = Entry(self.container13)
        self.txt_c63_5_3['width'] = 2
        self.txt_c63_5_3.pack(side=LEFT)

        self.lbl_c63_5_4 = Label(self.container13)
        self.lbl_c63_5_4['text'] = 'Parainfluenza 2: '
        self.lbl_c63_5_4.pack(side=LEFT)

        self.txt_c63_5_4 = Entry(self.container13)
        self.txt_c63_5_4['width'] = 2
        self.txt_c63_5_4.pack(side=LEFT)

        self.lbl_c63_5_5 = Label(self.container13)
        self.lbl_c63_5_5['text'] = 'Parainfluenza 3: '
        self.lbl_c63_5_5.pack(side=LEFT)

        self.txt_c63_5_6 = Entry(self.container13)
        self.txt_c63_5_6['width'] = 2
        self.txt_c63_5_6.pack(side=LEFT)

        self.lbl_c63_5_6 = Label(self.container13)
        self.lbl_c63_5_6['text'] = 'Parainfluenza 4: '
        self.lbl_c63_5_6.pack(side=LEFT)

        self.txt_c63_5_6 = Entry(self.container13)
        self.txt_c63_5_6['width'] = 2
        self.txt_c63_5_6.pack(side=LEFT)

        self.lbl_c63_5_7 = Label(self.container13)
        self.lbl_c63_5_7['text'] = 'Adenovírus: '
        self.lbl_c63_6_7.pack(side=LEFT)

        self.txt_c63_5_7 = Entry(self.container13)
        self.txt_c63_5_7['width'] = 2
        self.txt_c63_5_7.pack(side=LEFT)

        self.lbl_c63_5_8 = Label(self.container13)
        self.lbl_c63_5_8['text'] = 'Metapneumovírus: '
        self.lbl_c63_5_8.pack(side=LEFT)

        self.txt_c63_5_8 = Entry(self.container13)
        self.txt_c63_5_8['width'] = 2
        self.txt_c63_5_8.pack(side=LEFT)

        self.lbl_c63_5_9 = Label(self.container13)
        self.lbl_c63_5_9['text'] = 'Bocavírus: '
        self.lbl_c63_5_9.pack(side=LEFT)

        self.txt_c63_5_9 = Entry(self.container13)
        self.txt_c63_5_9['width'] = 2
        self.txt_c63_5_9.pack(side=LEFT)

        self.lbl_c63_5_10 = Label(self.container13)
        self.lbl_c63_5_10['text'] = 'Rinovírus: '
        self.lbl_c63_5_10.pack(side=LEFT)

        self.txt_c63_5_10 = Entry(self.container13)
        self.txt_c63_5_10['width'] = 2
        self.txt_c63_5_10.pack(side=LEFT)

        self.lbl_c63_5_11 = Label(self.container13)
        self.lbl_c63_5_11['text'] = 'Outro vírus respiratório, especifique: '
        self.lbl_c63_5_11.pack(side=LEFT)

        self.txt_c63_5_11 = Entry(self.container13)
        self.txt_c63_5_11['width'] = 10
        self.txt_c63_5_11.pack(side=LEFT)

        self.container14 = Frame(dados_laboratoriais)
        self.container14['padx'] = 10
        self.container14['pady'] = 8
        self.container14.pack()

        self.lbl_c64_1 = Label(self.container14)
        self.lbl_c64_1['text'] = '64 - Laboratório que realizou RT-PCR/outro método por biologia molecular: '
        self.lbl_c64_1.pack(side=LEFT)

        self.txt_c64_1 = Entry(self.container14)
        self.txt_c64_1['width'] = 25
        self.txt_c64_1.pack(side=LEFT)

        self.lbl_c64_2 = Label(self.container14)
        self.lbl_c64_2['text'] = 'Código (CNES): '
        self.lbl_c64_2.pack(side=LEFT)

        self.txt_c64_2 = Entry(self.container14)
        self.txt_c64_2['width'] = 15
        self.txt_c64_2.pack(side=LEFT)

    def conclusao(self):
        conclusao_final = Toplevel(root)
        conclusao_final.title('Formulário SIVEP')

        self.container1 = Frame(conclusao_final)
        self.container1['padx'] = 10
        self.container1['pady'] = 8
        self.container1.pack()

        self.lbl_titulo = Label(self.container1)
        self.lbl_titulo['text'] = 'Conclusão'
        self.lbl_titulo['font'] = ('Verdana', '12', 'bold')
        self.lbl_titulo.pack()

        self.container2 = Frame(conclusao_final)
        self.container2['padx'] = 10
        self.container2['pady'] = 8
        self.container2.pack()

        self.lbl_c65 = Label(self.container2)
        self.lbl_c65['text'] = ('65 - Classificação final do caso) '+
            '(1 - SRAG por influenza, 2 - SRAG por vírus respiratório, '+
            '3 - SRAG por outro agente etiológico (especifique), '+
            '4 - SRAG não especificado, 5 - COVID-19): ')
        self.lbl_c65.pack(side=LEFT)

        self.txt_c65 = Entry(self.container2)
        self.txt_c65['width'] = 15
        self.txt_c65.pack(side=LEFT)

        self.container3 = Frame(conclusao_final)
        self.container3['padx'] = 10
        self.container3['pady'] = 8
        self.container3.pack()

        self.lbl_c66 = Label(self.container3)
        self.lbl_c66['text'] = ('66 - Critério de Encerramento: '+
            '(1 - Laboratorial, 2 - Vínculo-Epidemiológico, 3 - Clínico): ')
        self.lbl_c66.pack(side=LEFT)

        self.txt_c66 = Entry(self.container3)
        self.txt_c66['width'] = 2
        self.txt_c66.pack(side=LEFT)

        self.lbl_c67 = Label(self.container3)
        self.lbl_c67['text'] = '67 - Evolução do caso: (1 - Cura, 2 - Óbito, 3 - Ignorado): '
        self.lbl_c67.pack(side=LEFT)

        self.txt_c67 = Entry(self.container3)
        self.txt_c67['width'] = 2
        self.txt_c67.pack(side=LEFT)

        self.container4 = Frame(conclusao_final)
        self.container4['padx'] = 10
        self.container4['pady'] = 8
        self.container4.pack()

        self.lbl_c68 = Label(self.container4)
        self.lbl_c68['text'] = 'Data de alta ou óbito'
        self.lbl_c68.pack(side=LEFT)

        self.txt_c68 = Entry(self.container4)
        self.txt_c68['width'] = 8
        self.txt_c68.pack(side=LEFT)

        self.lbl_c69 = Label(self.container4)
        self.lbl_c69['text'] = 'Data do encerramento'
        self.lbl_c69.pack(side=LEFT)
        
        self.txt_c69 = Entry(self.container4)
        self.txt_c69['width'] = 8
        self.txt_c69.pack(side=LEFT)

        self.container5 = Frame(conclusao_final)
        self.container5['padx'] = 10
        self.container5['pady'] = 8
        self.container5.pack()

        self.lbl_c70 = Label(self.container5)
        self.lbl_c70['text'] = 'Observações'
        self.lbl_c70.pack(side=LEFT)

        self.txt_c70 = Entry(self.container5)
        self.txt_c70.pack(side=LEFT)


    def cadastrarUsuario(self):
        user = Usuarios()

        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        user.nome = self.txtnome.get()
        user.crm = self.txtcrm.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcrm.delete(0, END)

    def alterarUsuario(self):
        user = Usuarios()

        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        user.nome = self.txtnome.get()
        user.crm = self.txtcrm.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcrm.delete(0, END)

    def excluirUsuario(self):
        user = Usuarios()

        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()
        user.nome = self.txtnome.get()
        user.crm = self.txtcrm.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcrm.delete(0, END)

    def buscarUsuario(self):
        user = Usuarios()

        user.usuario = self.txtusuario.get()

        self.lblmsg["text"] = user.selectUser()

        self.txtusuario.delete(0, END)
        self.txtusuario.insert(INSERT, user.usuario)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT, user.senha)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtcrm.delete(0, END)
        self.txtcrm.insert(INSERT, user.crm)

    def efetuaLogin(self):
        user = Usuarios()

        user.usuario = self.txtusuario.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.verifyLogin()

        self.txtusuario.delete(0, END)
        self.txtsenha.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcrm.delete(0, END)

        if self.lblmsg["text"] == "Login bem sucedido!":
            self.janelaFicha()
        else:
            return


root = Tk()
root.title("Sivep Digital")
Application(root)
root.mainloop()
