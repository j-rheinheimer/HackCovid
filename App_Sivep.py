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
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
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

        self.lblsenha = Label(self.container3, text="Senha", font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container3)
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
        self.btnCadastrar["command"] = self.cadastrarUsuario
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


root = Tk()
root.title("Sivep Digital")
Application(root)
root.mainloop()
