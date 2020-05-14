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
