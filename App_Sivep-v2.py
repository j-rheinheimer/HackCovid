# Programa principal, onde fica a programação da interface do aplicativo

from Usuarios import *
from tkinter import *
from Ficha import *
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import csv


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

        scrollbar = Scrollbar(janela_de_cadastro)
        scrollbar.pack(side=RIGHT)

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

    def janela_dadosPaciente(self):
        janela_dados_paciente = Toplevel(root)
        janela_dados_paciente.title("Sivep Ficha")

        self.dados_do_paciente = []

        self.fonte = ("Verdana", "10")
        self.fonteTitulo = ("Verdana", "12", "bold")
        self.fonte_titulo = "Calibri", "12", "bold"
        self.fonte = "Calibri", "10"

        self.container1 = Frame(janela_dados_paciente)
        self.container1["pady"] = 10
        self.container1.pack()

        self.titulo = Label(self.container1, text="Preenchimento de Ficha SIVEP", font=("Calibri", "15", "bold"))
        self.titulo.pack()
        self.lblmsg = Label(self.container1, text="", font=self.fonte)
        self.lblmsg.pack(side=TOP)

        self.container2 = Frame(janela_dados_paciente)
        self.container2["padx"] = 20
        self.container2["pady"] = 8
        self.container2.pack()

        self.lblc1 = Label(self.container2, text="1 - Data de preenchimento: ", font=self.fonte)
        self.lblc1.pack(side=LEFT)

        self.txtc1 = Entry(self.container2)
        self.txtc1["font"] = self.fonte
        self.txtc1["width"] = 10
        self.txtc1.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc1.get())

        self.lblc2 = Label(self.container2, text="2 - Data dos primeiros sintomas: ", font=self.fonte)
        self.lblc2.pack(side=LEFT)

        self.txtc2 = Entry(self.container2)
        self.txtc2["font"] = self.fonte
        self.txtc2["width"] = 10
        self.txtc2.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc2.get())

        self.lblc3 = Label(self.container2, text="3 - UF: ", font=self.fonte)
        self.lblc3.pack(side=LEFT)

        self.txtc3 = Entry(self.container2)
        self.txtc3["font"] = self.fonte
        self.txtc3["width"] = 2
        self.txtc3.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc3.get())

        self.container_extra1 = Frame(janela_dados_paciente)
        self.container_extra1["padx"] = 20
        self.container_extra1["pady"] = 8
        self.container_extra1.pack()

        self.lblc4_1 = Label(self.container_extra1, text="4 - Município: ", font=self.fonte)
        self.lblc4_1.pack(side=LEFT)

        self.txtc4_1 = Entry(self.container_extra1)
        self.txtc4_1["font"] = self.fonte
        self.txtc4_1["width"] = 15
        self.txtc4_1.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc4_1.get())

        self.lblc4_2 = Label(self.container_extra1, text=" Código(IBGE): ", font=self.fonte)
        self.lblc4_2.pack(side=LEFT)

        self.txtc4_2 = Entry(self.container_extra1)
        self.txtc4_2["font"] = self.fonte
        self.txtc4_2["width"] = 15
        self.txtc4_2.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc4_2.get())

        self.lblc5_1 = Label(self.container_extra1, text="5 - Unidade de Saúde: ", font=self.fonte)
        self.lblc5_1.pack(side=LEFT)

        self.txtc5_1 = Entry(self.container_extra1)
        self.txtc5_1["font"] = self.fonte
        self.txtc5_1["width"] = 15
        self.txtc5_1.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc5_1.get())

        self.lblc5_2 = Label(self.container_extra1, text="Código(CMES):", font=self.fonte)
        self.lblc5_2.pack(side=LEFT)

        self.txtc5_2 = Entry(self.container_extra1)
        self.txtc5_2["font"] = self.fonte
        self.txtc5_2["width"] = 15
        self.txtc5_2.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc5_2.get())

        self.container3 = Frame(janela_dados_paciente)
        self.container3["padx"] = 20
        self.container3["pady"] = 8
        self.container3.pack()

        self.dados_paciente = Label(self.container3, text="Dados do Paciente", font=self.fonte_titulo)
        self.dados_paciente.pack()

        self.container4 = Frame(janela_dados_paciente)
        self.container4["padx"] = 20
        self.container4["pady"] = 8
        self.container4.pack()

        self.lblc6 = Label(self.container4, text="6 - CPF: ", font=self.fonte)
        self.lblc6.pack(side=LEFT)

        self.txtc6 = Entry(self.container4)
        self.txtc6["font"] = self.fonte
        self.txtc6["width"] = 10
        self.txtc6.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc6.get())

        self.lblc7 = Label(self.container4, text="7 - Nome: ", font=self.fonte)
        self.lblc7.pack(side=LEFT)

        self.txtc7 = Entry(self.container4)
        self.txtc7["font"] = self.fonte
        self.txtc7["width"] = 20
        self.txtc7.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc7.get())

        self.lblc8 = Label(self.container4, text="8 - Sexo(1-M/2-F/9-Ignorar): ", font=self.fonte)
        self.lblc8.pack(side=LEFT)

        self.txtc8 = Entry(self.container4)
        self.txtc8["font"] = self.fonte
        self.txtc8["width"] = 2
        self.txtc8.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc8.get())

        self.lblc9 = Label(self.container4, text="9 -  Data de Nascimento: ", font=self.fonte)
        self.lblc9.pack(side=LEFT)

        self.txtc9 = Entry(self.container4)
        self.txtc9["font"] = self.fonte
        self.txtc9["width"] = 10
        self.txtc9.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc9.get())

        self.container_extra2 = Frame(janela_dados_paciente)
        self.container_extra2["padx"] = 20
        self.container_extra2["pady"] = 8
        self.container_extra2.pack()

        self.lblc10_1 = Label(self.container_extra2, text="10 - (ou)Idade ", font=self.fonte)
        self.lblc10_1.pack(side=LEFT)

        self.txtc10_1 = Entry(self.container_extra2)
        self.txtc10_1["font"] = self.fonte
        self.txtc10_1["width"] = 2
        self.txtc10_1.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc10_1.get())

        self.lblc10_2 = Label(self.container_extra2, text="1 - Dia, 2- Mês, 3- Ano ", font=self.fonte)
        self.lblc10_2.pack(side=LEFT)

        self.txtc10_2 = Entry(self.container_extra2)
        self.txtc10_2["font"] = self.fonte
        self.txtc10_2["width"] = 2
        self.txtc10_2.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc10_2.get())

        self.lblc11 = Label(self.container_extra2, font=self.fonte)
        self.lblc11['text'] = ("11 - Gestante (1 - 1ºTrimerstre, 2 - 2ºTrimestre, 3 - 3ºTrimestre "
                               "4 - Idade gestacional ignorada, 5 - Não 6 - Não se aplica, 9 - Ignorado: ")
        self.lblc11.pack(side=LEFT)

        self.txtc11 = Entry(self.container_extra2)
        self.txtc11["font"] = self.fonte
        self.txtc11["width"] = 2
        self.txtc11.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc11.get())

        self.container5 = Frame(janela_dados_paciente)
        self.container5["padx"] = 20
        self.container5["pady"] = 8
        self.container5.pack()

        self.lblc12 = Label(self.container5, font=self.fonte)
        self.lblc12['text'] = ("12 - Raça/Cor (1 - Branca, 2 - Preta, 3 - Amarela"
                               "4 - Parda, 5 - Indígena, 9 - Ignorado): ")
        self.lblc12.pack(side=LEFT)

        self.txtc12 = Entry(self.container5)
        self.txtc12["font"] = self.fonte
        self.txtc12["width"] = 15
        self.txtc12.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc12.get())

        self.lblc13 = Label(self.container5, text="13 - Se indígena, etnia: ", font=self.fonte)
        self.lblc13.pack(side=LEFT)

        self.txtc13 = Entry(self.container5)
        self.txtc13["font"] = self.fonte
        self.txtc13["width"] = 15
        self.txtc13.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc13.get())

        self.container_extra3 = Frame(janela_dados_paciente)
        self.container_extra3["padx"] = 20
        self.container_extra3["pady"] = 8
        self.container_extra3.pack()

        self.lblc14 = Label(self.container_extra3, font=self.fonte)
        self.lblc14['text'] = ("14 - Escolaridade (0 - Sem Escolaridade/Analfabeto"
                               "1 - Fundamental I, 2 - Fundamental II, 3 - Médio"
                               "4 - Superior, 5 - Não se Aplica, 9 - Ignorado): ")
        self.lblc14.pack(side=LEFT)

        self.txtc14 = Entry(self.container_extra3)
        self.txtc14["font"] = self.fonte
        self.txtc14["width"] = 2
        self.txtc14.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc14.get())

        self.lblc15 = Label(self.container_extra3, text="15 - Ocupação: ", font=self.fonte)
        self.lblc15.pack(side=LEFT)

        self.txtc15 = Entry(self.container_extra3)
        self.txtc15["font"] = self.fonte
        self.txtc15["width"] = 15
        self.txtc15.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc15.get())

        self.lblc16 = Label(self.container_extra3, text="16 - Nome da mãe: ", font=self.fonte)
        self.lblc16.pack(side=LEFT)

        self.txtc16 = Entry(self.container_extra3)
        self.txtc16["font"] = self.fonte
        self.txtc16["width"] = 15
        self.txtc16.pack(side=LEFT)
        self.dados_do_paciente.append(self.txtc16.get())

        self.container_extra3 = Frame(janela_dados_paciente)
        self.container_extra3["padx"] = 20
        self.container_extra3["pady"] = 8
        self.container_extra3.pack()

        self.proxima_janela = Button(self.container_extra3)
        self.proxima_janela['text'] = 'Clique para ir para a próxima janela'
        self.proxima_janela['command'] = self.dadosResidencia
        self.proxima_janela.pack()

    def dadosResidencia(self):
        janela_dados_residencia = Toplevel(root)
        janela_dados_residencia.title("Sivep Ficha")

        self.dados_de_residencia = []

        self.container6 = Frame(janela_dados_residencia)
        self.container6["padx"] = 20
        self.container6["pady"] = 8
        self.container6.pack()

        self.dados_residencia = Label(self.container6, text="Dados de Residência", font=self.fonte_titulo)
        self.dados_residencia.pack()

        self.container7 = Frame(janela_dados_residencia)
        self.container7["padx"] = 20
        self.container7["pady"] = 8
        self.container7.pack()

        self.lblc17 = Label(self.container7, text="17 - CEP: ", font=self.fonte)
        self.lblc17.pack(side=LEFT)

        self.txtc17 = Entry(self.container7)
        self.txtc17["font"] = self.fonte
        self.txtc17["width"] = 15
        self.txtc17.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc17.get())

        self.lblc18 = Label(self.container7, text="18 - UF: ", font=self.fonte)
        self.lblc18.pack(side=LEFT)

        self.txtc18 = Entry(self.container7)
        self.txtc18["font"] = self.fonte
        self.txtc18["width"] = 2
        self.txtc18.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc18.get())

        self.lblc19_1 = Label(self.container7, text="19 - Município: ", font=self.fonte)
        self.lblc19_1.pack(side=LEFT)

        self.txtc19_1 = Entry(self.container7)
        self.txtc19_1["font"] = self.fonte
        self.txtc19_1["width"] = 15
        self.txtc19_1.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc19_1.get())

        self.lblc19_2 = Label(self.container7, text=" Código(IBGE): ", font=self.fonte)
        self.lblc19_2.pack(side=LEFT)

        self.txtc19_2 = Entry(self.container7)
        self.txtc19_2["font"] = self.fonte
        self.txtc19_2["width"] = 15
        self.txtc19_2.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc19_2.get())

        self.lblc20 = Label(self.container7, text="20 - Bairro: ", font=self.fonte)
        self.lblc20.pack(side=LEFT)

        self.txtc20 = Entry(self.container7)
        self.txtc20["font"] = self.fonte
        self.txtc20["width"] = 15
        self.txtc20.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc20.get())

        self.lblc21 = Label(self.container7, text="21 - Logradouro: ", font=self.fonte)
        self.lblc21.pack(side=LEFT)

        self.txtc21 = Entry(self.container7)
        self.txtc21["font"] = self.fonte
        self.txtc21["width"] = 15
        self.txtc21.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc21.get())

        self.lblc22 = Label(self.container7, text="22 - Nº: ", font=self.fonte)
        self.lblc22.pack(side=LEFT)

        self.txtc22 = Entry(self.container7)
        self.txtc22["font"] = self.fonte
        self.txtc22["width"] = 4
        self.txtc22.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc22.get())

        self.lblc23 = Label(self.container7, text="23 - Complemento: ", font=self.fonte)
        self.lblc23.pack(side=LEFT)

        self.txtc23 = Entry(self.container7)
        self.txtc23["font"] = self.fonte
        self.txtc23["width"] = 4
        self.txtc23.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc23.get())

        self.container8 = Frame(janela_dados_residencia)
        self.container8["padx"] = 20
        self.container8["pady"] = 8
        self.container8.pack()

        self.lblc24 = Label(self.container8, text="24 - Telefone(DDD): ", font=self.fonte)
        self.lblc24.pack(side=LEFT)

        self.txtc24 = Entry(self.container8)
        self.txtc24["font"] = self.fonte
        self.txtc24["width"] = 15
        self.txtc24.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc24.get())

        self.lblc25 = Label(self.container8, font=self.fonte)
        self.lblc25['text'] = ("25 - Zona (1 - Urbana, 2 - Rural"
                               "3 - Periurbana, 9 - Ignorado): ")
        self.lblc25.pack(side=LEFT)

        self.txtc25 = Entry(self.container8)
        self.txtc25["font"] = self.fonte
        self.txtc25["width"] = 2
        self.txtc25.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc25.get())

        self.lblc26 = Label(self.container8, text="26 - País(se residente fora do Brasil): ", font=self.fonte)
        self.lblc26.pack(side=LEFT)

        self.txtc26 = Entry(self.container8)
        self.txtc26["font"] = self.fonte
        self.txtc26["width"] = 20
        self.txtc26.pack(side=LEFT)
        self.dados_de_residencia.append(self.txtc26.get())

        self.container_extra4 = Frame(janela_dados_residencia)
        self.container_extra4["padx"] = 20
        self.container_extra4["pady"] = 8
        self.container_extra4.pack()

        self.proxima_janela = Button(self.container_extra4)
        self.proxima_janela['text'] = 'Clique para ir para a próxima janela'
        self.proxima_janela['command'] = self.janela_dadosClinicos
        self.proxima_janela.pack()

    def janela_dadosClinicos(self):
        janela_dados_clinicos = Toplevel(root)
        janela_dados_clinicos.title("Sivep Ficha")

        self.dados_clinicos = []

        self.container9 = Frame(janela_dados_clinicos)
        self.container9["padx"] = 20
        self.container9["pady"] = 8
        self.container9.pack()

        self.title_dados_clinicos = Label(self.container9, text="Dados clínicos e epidemiológicos")
        self.title_dados_clinicos["font"] = self.fonte_titulo
        self.title_dados_clinicos.pack()

        self.container10 = Frame(janela_dados_clinicos)
        self.container10["padx"] = 20
        self.container10["pady"] = 8
        self.container10.pack()

        self.lblc27 = Label(self.container10, font=self.fonte)
        self.lblc27['text'] = (
            '27 - Paciente tem histórico de viagem internacional até 14 dias antes do início dos sintomas? '
            '(1 - Sim, 2 - Não, 9 - Ignorado)')
        self.lblc27.pack(side=LEFT)

        self.txtc27 = Entry(self.container10)
        self.txtc27["width"] = 20
        self.txtc27["font"] = self.fonte
        self.txtc27.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc27.get())

        self.container11 = Frame(janela_dados_clinicos)
        self.container11["padx"] = 20
        self.container11["pady"] = 8
        self.container11.pack()

        self.lblc28 = Label(self.container11, text="28 - Se sim: Qual País?", font=self.fonte)
        self.lblc28["width"] = 20
        self.lblc28.pack(side=LEFT)

        self.txtc28 = Entry(self.container11)
        self.txtc28["width"] = 40
        self.txtc28["font"] = self.fonte
        self.txtc28.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc28.get())

        self.lblc29 = Label(self.container11, text="29 - Em qual local?", font=self.fonte)
        self.lblc29["width"] = 20
        self.lblc29.pack(side=LEFT)

        self.txtc29 = Entry(self.container11)
        self.txtc29["width"] = 40
        self.txtc29["font"] = self.fonte
        self.txtc29.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc29.get())

        self.container12 = Frame(janela_dados_clinicos)
        self.container12["padx"] = 20
        self.container12["pady"] = 8
        self.container12.pack()

        self.lblc30 = Label(self.container12, text="30 - Data de viagem:", font=self.fonte)
        self.lblc30["width"] = 20
        self.lblc30.pack(side=LEFT)

        self.txtc30 = Entry(self.container12)
        self.txtc30["width"] = 40
        self.txtc30["font"] = self.fonte
        self.txtc30.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc30.get())

        self.lblc31 = Label(self.container12, text="31 - Data de retorno:", font=self.fonte)
        self.lblc31["width"] = 20
        self.lblc31.pack(side=LEFT)

        self.txtc31 = Entry(self.container12)
        self.txtc31["width"] = 40
        self.txtc31["font"] = self.fonte
        self.txtc31.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc31.get())

        self.container13 = Frame(janela_dados_clinicos)
        self.container13["padx"] = 20
        self.container13["pady"] = 8
        self.container13.pack()

        self.lblc32 = Label(self.container13)
        self.lblc32["text"] = "32 - É caso proveniente de surto de SG que evoluiu para SRAG?(1-Sim 2-Não 9-Ignorado)"
        self.lblc32["font"] = self.fonte
        self.lblc32.pack(side=LEFT)

        self.txtc32 = Entry(self.container13)
        self.txtc32["width"] = 30
        self.txtc32["font"] = self.fonte
        self.txtc32.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc32.get())

        self.container14 = Frame(janela_dados_clinicos)
        self.container14["padx"] = 20
        self.container14["pady"] = 8
        self.container14.pack()

        self.lblc33 = Label(self.container14)
        self.lblc33[
            "text"] = "33 - Trata-se de caso nosocomial (infecção adquirida no hospital)?(1-Sim 2-Não 9-Ignorado)"
        self.lblc33["font"] = self.fonte
        self.lblc33.pack(side=LEFT)

        self.txtc33 = Entry(self.container14)
        self.txtc33["width"] = 30
        self.txtc33["font"] = self.fonte
        self.txtc33.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc33.get())

        self.container15 = Frame(janela_dados_clinicos)
        self.container15["padx"] = 20
        self.container15["pady"] = 8
        self.container15.pack()

        self.lblc34 = Label(self.container15)
        self.lblc34["text"] = "34 - Paciente trabalha ou tem contato direto com aves ou suínos?(1-Sim 2-Não 9-Ignorado)"
        self.lblc34["font"] = self.fonte
        self.lblc34.pack(side=LEFT)

        self.txtc34 = Entry(self.container15)
        self.txtc34["width"] = 30
        self.txtc34["font"] = self.fonte
        self.txtc34.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc34.get())

        self.container16 = Frame(janela_dados_clinicos)
        self.container16["padx"] = 20
        self.container16["pady"] = 8
        self.container16.pack()

        self.lblc35 = Label(self.container16)
        self.lblc35["text"] = "35 - Sinais e Sintomas:(1-Sim 2-Não 9-Ignorado):"
        self.lblc35["font"] = self.fonte
        self.lblc35.pack(side=LEFT)

        self.lblc35_1 = Label(self.container16)
        self.lblc35_1["text"] = "  Febre"
        self.lblc35_1["font"] = self.fonte
        self.lblc35_1.pack(side=LEFT)

        self.txtc35_1 = Entry(self.container16)
        self.txtc35_1["width"] = 5
        self.txtc35_1["font"] = self.fonte
        self.txtc35_1.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_1.get())

        self.lblc35_2 = Label(self.container16)
        self.lblc35_2["text"] = "  Tosse"
        self.lblc35_2["font"] = self.fonte
        self.lblc35_2.pack(side=LEFT)

        self.txtc35_2 = Entry(self.container16)
        self.txtc35_2["width"] = 5
        self.txtc35_2["font"] = self.fonte
        self.txtc35_2.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_2.get())

        self.lblc35_3 = Label(self.container16)
        self.lblc35_3["text"] = "  Dor de garganta"
        self.lblc35_3["font"] = self.fonte
        self.lblc35_3.pack(side=LEFT)

        self.txtc35_3 = Entry(self.container16)
        self.txtc35_3["width"] = 5
        self.txtc35_3["font"] = self.fonte
        self.txtc35_3.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_3.get())

        self.lblc35_4 = Label(self.container16)
        self.lblc35_4["text"] = "  Dispnéia"
        self.lblc35_4["font"] = self.fonte
        self.lblc35_4.pack(side=LEFT)

        self.txtc35_4 = Entry(self.container16)
        self.txtc35_4["width"] = 5
        self.txtc35_4["font"] = self.fonte
        self.txtc35_4.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_4.get())

        self.container17 = Frame(janela_dados_clinicos)
        self.container17["padx"] = 20
        self.container17["pady"] = 8
        self.container17.pack()

        self.lblc35_5 = Label(self.container17)
        self.lblc35_5["text"] = "  Desconforto Respiratório"
        self.lblc35_5["font"] = self.fonte
        self.lblc35_5.pack(side=LEFT)

        self.txtc35_5 = Entry(self.container17)
        self.txtc35_5["width"] = 5
        self.txtc35_5["font"] = self.fonte
        self.txtc35_5.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_5.get())

        self.lblc35_6 = Label(self.container17)
        self.lblc35_6["text"] = "  Saturação de O2<95%"
        self.lblc35_6["font"] = self.fonte
        self.lblc35_6.pack(side=LEFT)

        self.txtc35_6 = Entry(self.container17)
        self.txtc35_6["width"] = 10
        self.txtc35_6["font"] = self.fonte
        self.txtc35_6.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_6.get())

        self.lblc35_7 = Label(self.container17)
        self.lblc35_7["text"] = "  Diarreia"
        self.lblc35_7["font"] = self.fonte
        self.lblc35_7.pack(side=LEFT)

        self.txtc35_7 = Entry(self.container17)
        self.txtc35_7["width"] = 5
        self.txtc35_7["font"] = self.fonte
        self.txtc35_7.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_7.get())

        self.lblc35_8 = Label(self.container17)
        self.lblc35_8["text"] = "    Vômito"
        self.lblc35_8["font"] = self.fonte
        self.lblc35_8.pack(side=LEFT)

        self.txtc35_8 = Entry(self.container17)
        self.txtc35_8["width"] = 5
        self.txtc35_8["font"] = self.fonte
        self.txtc35_8.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_8.get())

        self.lblc35_9 = Label(self.container17)
        self.lblc35_9["text"] = " Outro(s)"
        self.lblc35_9["font"] = self.fonte
        self.lblc35_9.pack(side=LEFT)

        self.txtc35_9 = Entry(self.container17)
        self.txtc35_9["width"] = 20
        self.txtc35_9["font"] = self.fonte
        self.txtc35_9.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc35_9.get())

        self.container18 = Frame(janela_dados_clinicos)
        self.container18["padx"] = 20
        self.container18["pady"] = 8
        self.container18.pack()

        self.lblc36_1 = Label(self.container18)
        self.lblc36_1["text"] = "36 - Possui fatores de risco/comorbidades?(1-Sim 2-Não 9-Ignorado)"
        self.lblc36_1["font"] = self.fonte
        self.lblc36_1.pack(side=LEFT)

        self.txtc36_1 = Entry(self.container18)
        self.txtc36_1["width"] = 30
        self.txtc36_1["font"] = self.fonte
        self.txtc36_1.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_1.get())

        self.container19 = Frame(janela_dados_clinicos)
        self.container19["padx"] = 20
        self.container19["pady"] = 8
        self.container19.pack()

        self.lblc36 = Label(self.container19)
        self.lblc36["text"] = "Se sim, qual(is)?(marcar x):     "
        self.lblc36["font"] = self.fonte
        self.lblc36.pack(side=LEFT)

        self.lblc36_2 = Label(self.container19)
        self.lblc36_2["text"] = "Puérpera(até 45 dias do parto)"
        self.lblc36_2["font"] = self.fonte
        self.lblc36_2.pack(side=LEFT)

        self.txtc36_2 = Entry(self.container19)
        self.txtc36_2["width"] = 2
        self.txtc36_2["font"] = self.fonte
        self.txtc36_2.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_2.get())

        self.lblc36_3 = Label(self.container19)
        self.lblc36_3["text"] = "  Síndrome de Down"
        self.lblc36_3["font"] = self.fonte
        self.lblc36_3.pack(side=LEFT)

        self.txtc36_3 = Entry(self.container19)
        self.txtc36_3["width"] = 2
        self.txtc36_3["font"] = self.fonte
        self.txtc36_3.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_3.get())

        self.lblc36_4 = Label(self.container19)
        self.lblc36_4["text"] = "   Diabetes mellitus"
        self.lblc36_4["font"] = self.fonte
        self.lblc36_4.pack(side=LEFT)

        self.txtc36_4 = Entry(self.container19)
        self.txtc36_4["width"] = 2
        self.txtc36_4["font"] = self.fonte
        self.txtc36_4.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_4.get())

        self.lblc36_5 = Label(self.container19)
        self.lblc36_5["text"] = "   Imunodefiência/Imunodepressão"
        self.lblc36_5["font"] = self.fonte
        self.lblc36_5.pack(side=LEFT)

        self.txtc36_5 = Entry(self.container19)
        self.txtc36_5["width"] = 2
        self.txtc36_5["font"] = self.fonte
        self.txtc36_5.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_5.get())

        self.container20 = Frame(janela_dados_clinicos)
        self.container20["padx"] = 20
        self.container20["pady"] = 8
        self.container20.pack()

        self.lblc36_6 = Label(self.container20)
        self.lblc36_6["text"] = "   Outros"
        self.lblc36_6["font"] = self.fonte
        self.lblc36_6.pack(side=LEFT)

        self.txtc36_6 = Entry(self.container20)
        self.txtc36_6["width"] = 15
        self.txtc36_6["font"] = self.fonte
        self.txtc36_6.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_6.get())

        self.lblc36_7 = Label(self.container20)
        self.lblc36_7["text"] = "  Doença Cardiovascular Crônica"
        self.lblc36_7["font"] = self.fonte
        self.lblc36_7.pack(side=LEFT)

        self.txtc36_7 = Entry(self.container20)
        self.txtc36_7["width"] = 2
        self.txtc36_7["font"] = self.fonte
        self.txtc36_7.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_7.get())

        self.lblc36_8 = Label(self.container20)
        self.lblc36_8["text"] = "  Doença Hepática Crônica"
        self.lblc36_8["font"] = self.fonte
        self.lblc36_8.pack(side=LEFT)

        self.txtc36_8 = Entry(self.container20)
        self.txtc36_8["width"] = 2
        self.txtc36_8["font"] = self.fonte
        self.txtc36_8.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_8.get())

        self.lblc36_9 = Label(self.container20)
        self.lblc36_9["text"] = "   Doença Neurológica Crônica"
        self.lblc36_9["font"] = self.fonte
        self.lblc36_9.pack(side=LEFT)

        self.txtc36_9 = Entry(self.container20)
        self.txtc36_9["width"] = 2
        self.txtc36_9["font"] = self.fonte
        self.txtc36_9.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_9.get())

        self.lblc36_10 = Label(self.container20)
        self.lblc36_10["text"] = "   Doença Renal Crônica"
        self.lblc36_10["font"] = self.fonte
        self.lblc36_10.pack(side=LEFT)

        self.txtc36_10 = Entry(self.container20)
        self.txtc36_10["width"] = 2
        self.txtc36_10["font"] = self.fonte
        self.txtc36_10.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_10.get())

        self.container21 = Frame(janela_dados_clinicos)
        self.container21["padx"] = 20
        self.container21["pady"] = 8
        self.container21.pack()

        self.lblc36_11 = Label(self.container21)
        self.lblc36_11["text"] = "  Doença Hematológica Crônica"
        self.lblc36_11["font"] = self.fonte
        self.lblc36_11.pack(side=LEFT)

        self.txtc36_11 = Entry(self.container21)
        self.txtc36_11["width"] = 2
        self.txtc36_11["font"] = self.fonte
        self.txtc36_11.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_11.get())

        self.lblc36_12 = Label(self.container21)
        self.lblc36_12["text"] = "  Asma"
        self.lblc36_12["font"] = self.fonte
        self.lblc36_12.pack(side=LEFT)

        self.txtc36_12 = Entry(self.container21)
        self.txtc36_12["width"] = 2
        self.txtc36_12["font"] = self.fonte
        self.txtc36_12.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_12.get())

        self.lblc36_13 = Label(self.container21)
        self.lblc36_13["text"] = "   Outra Pneumopatia Crônica"
        self.lblc36_13["font"] = self.fonte
        self.lblc36_13.pack(side=LEFT)

        self.txtc36_13 = Entry(self.container21)
        self.txtc36_13["width"] = 2
        self.txtc36_13["font"] = self.fonte
        self.txtc36_13.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_13.get())

        self.lblc36_14_1 = Label(self.container21)
        self.lblc36_14_1["text"] = "   Obesidade"
        self.lblc36_14_1["font"] = self.fonte
        self.lblc36_14_1.pack(side=LEFT)

        self.txtc36_14_1 = Entry(self.container21)
        self.txtc36_14_1["width"] = 2
        self.txtc36_14_1["font"] = self.fonte
        self.txtc36_14_1.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_14_1.get())

        self.lblc36_14_2 = Label(self.container21)
        self.lblc36_14_2["text"] = "IMC"
        self.lblc36_14_2["font"] = self.fonte
        self.lblc36_14_2.pack(side=LEFT)

        self.txtc36_14_2 = Entry(self.container21)
        self.txtc36_14_2["width"] = 2
        self.txtc36_14_2["font"] = self.fonte
        self.txtc36_14_2.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc36_14_2.get())

        self.container22 = Frame(janela_dados_clinicos)
        self.container22["padx"] = 20
        self.container22["pady"] = 8
        self.container22.pack()

        self.lblc37 = Label(self.container22)
        self.lblc37["text"] = "37 - Recebeu vacina contra Gripe na última campanha?(1-Sim 2-Não 9-Ignorado)"
        self.lblc37["font"] = self.fonte
        self.lblc37.pack(side=LEFT)

        self.txtc37 = Entry(self.container22)
        self.txtc37["width"] = 15
        self.txtc37["font"] = self.fonte
        self.txtc37.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc37.get())

        self.lblc38_1 = Label(self.container22)
        self.lblc38_1["text"] = "  38 - Data da Vacinação"
        self.lblc38_1["font"] = self.fonte
        self.lblc38_1.pack(side=LEFT)

        self.txtc38_1 = Entry(self.container22)
        self.txtc38_1["width"] = 15
        self.txtc38_1["font"] = self.fonte
        self.txtc38_1.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc38_1.get())

        self.container23 = Frame(janela_dados_clinicos)
        self.container23["padx"] = 20
        self.container23["pady"] = 8
        self.container23.pack()

        self.lblc38_2 = Label(self.container23)
        self.lblc38_2["text"] = "Se < 6 meses: A mãe recebeu vacina?(1-Sim 2-Não 9-Ignorado)"
        self.lblc38_2["font"] = self.fonte
        self.lblc38_2.pack(side=LEFT)

        self.txtc38_2 = Entry(self.container23)
        self.txtc38_2["width"] = 15
        self.txtc38_2["font"] = self.fonte
        self.txtc38_2.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc38_2.get())

        self.lblc38_3 = Label(self.container23)
        self.lblc38_3["text"] = "   Se sim, data:"
        self.lblc38_3["font"] = self.fonte
        self.lblc38_3.pack(side=LEFT)

        self.txtc38_3 = Entry(self.container23)
        self.txtc38_3["width"] = 15
        self.txtc38_3["font"] = self.fonte
        self.txtc38_3.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc38_3.get())

        self.lblc38_4 = Label(self.container23)
        self.lblc38_4["text"] = "    A mãe amamentava a criança?(1-Sim 2-Não 9-Ignorado)"
        self.lblc38_4["font"] = self.fonte
        self.lblc38_4.pack(side=LEFT)

        self.txtc38_4 = Entry(self.container23)
        self.txtc38_4["width"] = 15
        self.txtc38_4["font"] = self.fonte
        self.txtc38_4.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc38_4.get())

        self.container24 = Frame(janela_dados_clinicos)
        self.container24["padx"] = 20
        self.container24["pady"] = 8
        self.container24.pack()

        self.lblc38 = Label(self.container24)
        self.lblc38["text"] = "     Se >= 6 meses e <= 8 anos:"
        self.lblc38["font"] = self.fonte
        self.lblc38.pack(side=LEFT)

        self.lblc38_5 = Label(self.container24)
        self.lblc38_5["text"] = "Data da dose única 1/1:"
        self.lblc38_5["font"] = self.fonte
        self.lblc38_5.pack(side=LEFT)

        self.txtc38_5 = Entry(self.container24)
        self.txtc38_5["width"] = 15
        self.txtc38_5["font"] = self.fonte
        self.txtc38_5.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc38_5.get())

        self.lblc38_5_2 = Label(self.container24)
        self.lblc38_5_2["text"] = "   (dose única para crianças vacinadas em campanhas de anos anteriores)"
        self.lblc38_5_2["font"] = self.fonte
        self.lblc38_5_2.pack(side=LEFT)

        # self.container25 = Frame(janela_dados_clinicos)
        # self.container25["padx"] = 20
        # self.container25["pady"] = 8
        # self.container25.pack()

        # self.container26 = Frame(janela_dados_clinicos)
        # self.container26["padx"] = 20
        # self.container26["pady"] = 8
        # self.container26.pack()

        self.container27 = Frame(janela_dados_clinicos)
        self.container27["padx"] = 20
        self.container27["pady"] = 8
        self.container27.pack()

        self.lblc38_6_1 = Label(self.container27)
        self.lblc38_6_1["text"] = "Data da primeira dose:"
        self.lblc38_6_1["font"] = self.fonte
        self.lblc38_6_1.pack(side=LEFT)

        self.txtc38_6 = Entry(self.container27)
        self.txtc38_6["width"] = 15
        self.txtc38_6["font"] = self.fonte
        self.txtc38_6.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc38_6.get())

        self.lblc38_6_2 = Label(self.container27)
        self.lblc38_6_2["text"] = "   (1ª dose para crianças vacinadas pela primeira vez)"
        self.lblc38_6_2["font"] = self.fonte
        self.lblc38_6_2.pack(side=LEFT)

        self.lblc38_7_1 = Label(self.container27)
        self.lblc38_7_1["text"] = "Data da segunda dose:"
        self.lblc38_7_1["font"] = self.fonte
        self.lblc38_7_1.pack(side=LEFT)

        self.txtc38_7 = Entry(self.container27)
        self.txtc38_7["width"] = 15
        self.txtc38_7["font"] = self.fonte
        self.txtc38_7.pack(side=LEFT)
        self.dados_clinicos.append(self.txtc38_7.get())

        self.lblc38_7_2 = Label(self.container27)
        self.lblc38_7_2["text"] = "   (2ª dose para crianças vacinadas pela primeira vez)"
        self.lblc38_7_2["font"] = self.fonte
        self.lblc38_7_2.pack(side=LEFT)

        # self.container28 = Frame(janela_dados_clinicos)
        # self.container28["padx"] = 20
        # self.container28["pady"] = 8
        # self.container28.pack()

        self.container_extra5 = Frame(janela_dados_clinicos)
        self.container_extra5["padx"] = 20
        self.container_extra5["pady"] = 8
        self.container_extra5.pack()

        self.proxima_janela = Button(self.container_extra5)
        self.proxima_janela['text'] = 'Clique para ir para a próxima janela'
        self.proxima_janela['command'] = self.janela_dadosAtendimento
        self.proxima_janela.pack()

    def janela_dadosAtendimento(self):
        janela_dados_atendimento = Toplevel(root)
        janela_dados_atendimento.title("Sivep Ficha")

        self.dados_atendimento = []

        self.container29 = Frame(janela_dados_atendimento)
        self.container29["padx"] = 20
        self.container29["pady"] = 8
        self.container29.pack()

        self.title_dados_atendimento = Label(self.container29, text="Dados de Atendimento")
        self.title_dados_atendimento["font"] = self.fonteTitulo
        self.title_dados_atendimento.pack()

        self.container30 = Frame(janela_dados_atendimento)
        self.container30["padx"] = 20
        self.container30["pady"] = 8
        self.container30.pack()

        self.lblc39 = Label(self.container30, text="39 - Usou antiviral para gripe?(1-Sim 2-Não 9-Ignorado)",
                            font=self.fonte)
        self.lblc39.pack(side=LEFT)

        self.txtc39 = Entry(self.container30)
        self.txtc39["width"] = 8
        self.txtc39["font"] = self.fonte
        self.txtc39.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc39.get())

        self.lblc40 = Label(self.container30,
                            text="40 - Qual antiviral?(1-Oseltamivir 2-Zanamivir 3-Outro, especifique)",
                            font=self.fonte)
        self.lblc40.pack(side=LEFT)

        self.txtc40 = Entry(self.container30)
        self.txtc40["width"] = 16
        self.txtc40["font"] = self.fonte
        self.txtc40.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc40.get())

        self.lblc41 = Label(self.container30, text="41 - Data inicio do tratamento", font=self.fonte)
        self.lblc41.pack(side=LEFT)

        self.txtc41 = Entry(self.container30)
        self.txtc41["width"] = 12
        self.txtc41["font"] = self.fonte
        self.txtc41.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc41.get())

        self.container31 = Frame(janela_dados_atendimento)
        self.container31["padx"] = 20
        self.container31["pady"] = 8
        self.container31.pack()

        self.lblc42 = Label(self.container31, text="   42 - Houve interneção?(1-Sim 2-Não 9-Ignorado)",
                            font=self.fonte)
        self.lblc42.pack(side=LEFT)

        self.txtc42 = Entry(self.container31)
        self.txtc42["width"] = 12
        self.txtc42["font"] = self.fonte
        self.txtc42.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc42.get())

        self.lblc43 = Label(self.container31, text="   43 - Data da internação por SRAG:", font=self.fonte)
        self.lblc43.pack(side=LEFT)

        self.txtc43 = Entry(self.container31)
        self.txtc43["width"] = 12
        self.txtc43["font"] = self.fonte
        self.txtc43.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc43.get())

        self.lblc44 = Label(self.container31, text="   44 - UF de internação:", font=self.fonte)
        self.lblc44.pack(side=LEFT)

        self.txtc44 = Entry(self.container31)
        self.txtc44["width"] = 12
        self.txtc44["font"] = self.fonte
        self.txtc44.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc44.get())

        self.container32 = Frame(janela_dados_atendimento)
        self.container32["padx"] = 20
        self.container32["pady"] = 8
        self.container32.pack()

        self.lblc45_1 = Label(self.container32, text="45 - Município de internação:", font=self.fonte)
        self.lblc45_1.pack(side=LEFT)

        self.txtc45_1 = Entry(self.container32)
        self.txtc45_1["width"] = 12
        self.txtc45_1["font"] = self.fonte
        self.txtc45_1.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc45_1.get())

        self.lblc45_2 = Label(self.container32, text="          Código(IBGE):", font=self.fonte)
        self.lblc45_2.pack(side=LEFT)

        self.txtc45_2 = Entry(self.container32)
        self.txtc45_2["width"] = 12
        self.txtc45_2["font"] = self.fonte
        self.txtc45_2.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc45_2.get())

        self.container33 = Frame(janela_dados_atendimento)
        self.container33["padx"] = 20
        self.container33["pady"] = 8
        self.container33.pack()

        self.lblc46_1 = Label(self.container33, text="46 - Unidade de saúde de internação:", font=self.fonte)
        self.lblc46_1.pack(side=LEFT)

        self.txtc46_1 = Entry(self.container33)
        self.txtc46_1["width"] = 12
        self.txtc46_1["font"] = self.fonte
        self.txtc46_1.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc46_1.get())

        self.lblc46_2 = Label(self.container33, text="          Código(CNES):", font=self.fonte)
        self.lblc46_2.pack(side=LEFT)

        self.txtc46_2 = Entry(self.container33)
        self.txtc46_2["width"] = 12
        self.txtc46_2["font"] = self.fonte
        self.txtc46_2.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc46_2.get())

        self.container34 = Frame(janela_dados_atendimento)
        self.container34["padx"] = 20
        self.container34["pady"] = 8
        self.container34.pack()

        self.lblc47 = Label(self.container34, text="   47 - Internado em UTI?(1-Sim 2-Não 9-Ignorado)",
                            font=self.fonte)
        self.lblc47.pack(side=LEFT)

        self.txtc47 = Entry(self.container34)
        self.txtc47["width"] = 12
        self.txtc47["font"] = self.fonte
        self.txtc47.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc47.get())

        self.lblc48 = Label(self.container34, text="   48 - Data de entrada na UTI:", font=self.fonte)
        self.lblc48.pack(side=LEFT)

        self.txtc48 = Entry(self.container34)
        self.txtc48["width"] = 12
        self.txtc48["font"] = self.fonte
        self.txtc48.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc48.get())

        self.lblc49 = Label(self.container34, text="   49 - Data de saida na UTI:", font=self.fonte)
        self.lblc49.pack(side=LEFT)

        self.txtc49 = Entry(self.container34)
        self.txtc49["width"] = 12
        self.txtc49["font"] = self.fonte
        self.txtc49.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc49.get())

        self.container35 = Frame(janela_dados_atendimento)
        self.container35["padx"] = 20
        self.container35["pady"] = 8
        self.container35.pack()

        self.lblc50 = Label(self.container35,
                            text="50 - Uso de suporte ventilarório: (1-Sim, invasico 2-Sim, não invasivo 3-Não 9-Ignorado)",
                            font=self.fonte)
        self.lblc50.pack(side=LEFT)

        self.txtc50 = Entry(self.container35)
        self.txtc50["width"] = 12
        self.txtc50["font"] = self.fonte
        self.txtc50.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc50.get())

        self.lblc51 = Label(self.container35, font=self.fonte)
        self.lblc51['text'] = ("51 - Raio X de toráx: " +
                               "(1-Normal, " +
                               "2-Infiltrado intersticial, " +
                               "3-Consolidação, " +
                               "4-Misto, " +
                               "5-Outro, " +
                               "6-Não realizado, " +
                               "9-Ignorado)")
        self.lblc51.pack(side=LEFT)

        self.txtc51 = Entry(self.container35)
        self.txtc51["width"] = 12
        self.txtc51["font"] = self.fonte
        self.txtc51.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc51.get())

        self.container36 = Frame(janela_dados_atendimento)
        self.container36["padx"] = 20
        self.container36["pady"] = 8
        self.container36.pack()

        self.lblc52 = Label(self.container36, text="   52 - Data do raio X:", font=self.fonte)
        self.lblc52.pack(side=LEFT)

        self.txtc52 = Entry(self.container36)
        self.txtc52["width"] = 12
        self.txtc52["font"] = self.fonte
        self.txtc52.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc52.get())

        self.lblc53 = Label(self.container36, text="53 - Coletou amostra?(1-Sim 2-Não 9-Ignorado):",
                            font=self.fonte)
        self.lblc53.pack(side=LEFT)

        self.txtc53 = Entry(self.container36)
        self.txtc53["width"] = 12
        self.txtc53["font"] = self.fonte
        self.txtc53.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc53.get())

        self.container37 = Frame(janela_dados_atendimento)
        self.container37["padx"] = 20
        self.container37["pady"] = 8
        self.container37.pack()

        self.lblc54 = Label(self.container37, text="   54 - Data da coleta:", font=self.fonte)
        self.lblc54.pack(side=LEFT)

        self.txtc54 = Entry(self.container37)
        self.txtc54["width"] = 12
        self.txtc54["font"] = self.fonte
        self.txtc54.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc54.get())

        self.lblc55 = Label(self.container37, font=self.fonte)
        self.lblc55['text'] = ('55 - Tipo de amostra: ' +
                               '(1-Secreção de Naso-orofaringe, ' +
                               '2-Lavado Broco-alveolar, ' +
                               '3-Tecido Post-mortem, ' +
                               '4-Outra, ' +
                               '9-Ignorado)')
        self.lblc55.pack(side=LEFT)

        self.txtc55 = Entry(self.container37)
        self.txtc55["width"] = 1
        self.txtc55["font"] = self.fonte
        self.txtc55.pack(side=LEFT)
        self.dados_atendimento.append(self.txtc55.get())

        self.container_extra6 = Frame(janela_dados_atendimento)
        self.container_extra6["padx"] = 20
        self.container_extra6["pady"] = 8
        self.container_extra6.pack()

        self.proxima_janela = Button(self.container_extra6)
        self.proxima_janela['text'] = 'Clique para ir para a próxima janela'
        self.proxima_janela['command'] = self.janela_dadosLaboratoriais
        self.proxima_janela.pack()

    def janela_dadosLaboratoriais(self):
        janela_dados_laboratoriais = Toplevel(root)
        janela_dados_laboratoriais.title("Sivep Ficha")

        self.dados_laboratoriais = []

        self.container38 = Frame(janela_dados_laboratoriais)
        self.container38['pady'] = 10
        self.container38.pack()

        self.lbl_titulo = Label(self.container38)
        self.lbl_titulo['text'] = 'Dados Laboratoriais'
        self.lbl_titulo['font'] = self.fonte_titulo
        self.lbl_titulo.pack()

        self.container39 = Frame(janela_dados_laboratoriais)
        self.container39['padx'] = 10
        self.container39['pady'] = 8
        self.container39.pack()

        self.lblc56 = Label(self.container39)
        self.lblc56['text'] = '56 - Nº Requisição do GAL'
        self.lblc56.pack(side=LEFT)

        self.txtc56 = Entry(self.container39)
        self.txtc56['width'] = 100
        self.txtc56.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc56.get())

        self.container40 = Frame(janela_dados_laboratoriais)
        self.container40['padx'] = 10
        self.container40['pady'] = 8
        self.container40.pack()

        self.lblc57 = Label(self.container40)
        self.lblc57['text'] = ('57 - Resultado da IF/outro método que não seja biologia molecular:' +
                               '(1 - Positivo, 2 - Negativo, 3 - Inconclusivo, ' +
                               '4 - Não realizado, 5 - Aguardando resultado, 9 - Ignorado):')
        self.lblc57.pack(side=LEFT)

        self.txtc57 = Entry(self.container40)
        self.txtc57['width'] = 2
        self.txtc57.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc57.get())

        self.container41 = Frame(janela_dados_laboratoriais)
        self.container41['padx'] = 10
        self.container41['pady'] = 8
        self.container41.pack()

        self.lblc58 = Label(self.container41)
        self.lblc58['text'] = '58 - Data do resultado da IF/outro método que não seja Biologia Molecular:'
        self.lblc58.pack(side=LEFT)

        self.txtc58 = Entry(self.container41)
        self.txtc58['width'] = 15
        self.txtc58.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc58.get())

        self.container42 = Frame(janela_dados_laboratoriais)
        self.container42['padx'] = 10
        self.container42['pady'] = 8
        self.container42.pack()

        self.lblc59_title1 = Label(self.container42)
        self.lblc59_title1['text'] = '59 - Agente Etiológico - IF/outro método que não seja Biologia Molecular:'
        self.lblc59_title1.pack(side=LEFT)

        self.lblc59_1 = Label(self.container42)
        self.lblc59_1['text'] = 'Positivo para influenza? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lblc59_1.pack(side=LEFT)

        self.txtc59_1 = Entry(self.container42)
        self.txtc59_1['width'] = 2
        self.txtc59_1.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_1.get())

        self.lblc59_2 = Label(self.container42)
        self.lblc59_2['text'] = 'Se sim, qual influenza? (1 - Influenza A, 2 - Influenza B):'
        self.lblc59_2.pack(side=LEFT)

        self.txtc59_2 = Entry(self.container42)
        self.txtc59_2['width'] = 2
        self.txtc59_2.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_2.get())

        self.lblc59_3 = Label(self.container42)
        self.lblc59_3['text'] = 'Positivo para outro vírus? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lblc59_3.pack(side=LEFT)

        self.txtc59_3 = Entry(self.container42)
        self.txtc59_3['width'] = 2
        self.txtc59_3.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_3.get())

        self.container43 = Frame(janela_dados_laboratoriais)
        self.container43['padx'] = 10
        self.container43['pady'] = 8
        self.container43.pack()

        self.lblc59_title2 = Label(self.container43)
        self.lblc59_title2['text'] = 'Se outro vírus respiratórios qual(is)? (Marcar X): '
        self.lblc59_title2.pack(side=LEFT)

        self.lblc59_4 = Label(self.container43)
        self.lblc59_4['text'] = 'Virus Sincicial Respiratório:'
        self.lblc59_4.pack(side=LEFT)

        self.txtc59_4 = Entry(self.container43)
        self.txtc59_4['width'] = 2
        self.txtc59_4.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_4.get())

        self.lblc59_5 = Label(self.container43)
        self.lblc59_5['text'] = 'Parainfluenza 1:'
        self.lblc59_5.pack(side=LEFT)

        self.txtc59_5 = Entry(self.container43)
        self.txtc59_5['width'] = 2
        self.txtc59_5.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_5.get())

        self.lblc59_6 = Label(self.container43)
        self.lblc59_6['text'] = 'Parainfluenza 2:'
        self.lblc59_6.pack(side=LEFT)

        self.txtc59_6 = Entry(self.container43)
        self.txtc59_6['width'] = 2
        self.txtc59_6.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_6.get())

        self.lblc59_7 = Label(self.container43)
        self.lblc59_7['text'] = 'Parainfluenza 3:'
        self.lblc59_7.pack(side=LEFT)

        self.txtc59_7 = Entry(self.container43)
        self.txtc59_7['width'] = 2
        self.txtc59_7.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_7.get())

        self.lblc59_8 = Label(self.container43)
        self.lblc59_8['text'] = 'Adenovírus:'
        self.lblc59_8.pack(side=LEFT)

        self.txtc59_8 = Entry(self.container43)
        self.txtc59_8['width'] = 2
        self.txtc59_8.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_8.get())

        self.lblc59_9 = Label(self.container43)
        self.lblc59_9['text'] = 'Outro vírus respiratório, especifique:'
        self.lblc59_9.pack(side=LEFT)

        self.txtc59_9 = Entry(self.container43)
        self.txtc59_9['width'] = 15
        self.txtc59_9.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc59_9.get())

        self.container44 = Frame(janela_dados_laboratoriais)
        self.container44['padx'] = 10
        self.container44['pady'] = 8
        self.container44.pack()

        self.lblc60_1 = Label(self.container44)
        self.lblc60_1['text'] = '60 - Laboratório que realizou IF/outro método que não seja biologia molecular:'
        self.lblc60_1.pack(side=LEFT)

        self.txtc60_1 = Entry(self.container44)
        self.txtc60_1['width'] = 15
        self.txtc60_1.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc60_1.get())

        self.lblc60_2 = Label(self.container44)
        self.lblc60_2['text'] = 'Código (CNES):'
        self.lblc60_2.pack(side=LEFT)

        self.txtc60_2 = Entry(self.container44)
        self.txtc60_2['width'] = 10
        self.txtc60_2.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc60_2.get())

        self.container45 = Frame(janela_dados_laboratoriais)
        self.container45['padx'] = 10
        self.container45['pady'] = 8
        self.container45.pack()

        self.lblc61 = Label(self.container45)
        self.lblc61[
            'text'] = '61 - Resultado da RT-PCR/outro método por Biologia Molecular: (1 - Detectável, 2 - Não detectável, 3 - Inconclusivo, 4 - Não realizado, 5 - Aguardando resultado, 9 - Ignorado)'
        self.lblc61.pack(side=LEFT)

        self.txtc61 = Entry(self.container45)
        self.txtc61['width'] = 2
        self.txtc61.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc61.get())

        self.container46 = Frame(janela_dados_laboratoriais)
        self.container46['padx'] = 10
        self.container46['pady'] = 8
        self.container46.pack()

        self.lblc62 = Label(self.container46)
        self.lblc62['text'] = '62 - Data do resultado RT-PCR/Outro métdodo por Biologia Molecular:'
        self.lblc62.pack(side=LEFT)

        self.txtc62 = Entry(self.container46)
        self.txtc62['width'] = 15
        self.txtc62.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc62.get())

        self.container47 = Frame(janela_dados_laboratoriais)
        self.container47['padx'] = 10
        self.container47['pady'] = 8
        self.container47.pack()

        self.lblc63_1_1 = Label(self.container47)
        self.lblc63_1_1['text'] = ('63 - Agente Etiológico - RT-PCR/outro método por Biologia Molecular ' +
                                   'Positivo para Influenza? (1 - Sim, 2 - Não, 9 - Ignorado): ')
        self.lblc63_1_1.pack(side=LEFT)

        self.txtc63_1_1 = Entry(self.container47)
        self.txtc63_1_1['width'] = 2
        self.txtc63_1_1.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_1_1.get())

        self.lblc63_1_2 = Label(self.container47)
        self.lblc63_1_2['text'] = 'Se sim, qual influenza? (1 - Influenza A, 2 - Influenza B):'
        self.lblc63_1_2.pack(side=LEFT)

        self.txtc63_1_2 = Entry(self.container47)
        self.txtc63_1_2['width'] = 2
        self.txtc63_1_2.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_1_2.get())

        self.container48 = Frame(janela_dados_laboratoriais)
        self.container48['padx'] = 10
        self.container48['pady'] = 8
        self.container48.pack()

        self.lblc63_2 = Label(self.container48)
        self.lblc63_2['text'] = ('Influenza A, qual subtipo? ' +
                                 '(1 - Influenza A(H1N1)pdm09, 2 - Influenza A/H3N2, ' +
                                 '3 - Influenza A não subtipado, 4 - Influenza A não subtipável, ' +
                                 '5 - Inconclusivo, 6 - Outro, especifique):')
        self.lblc63_2.pack(side=LEFT)

        self.txtc63_2 = Entry(self.container48)
        self.txtc63_2['width'] = 10
        self.txtc63_2.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_2.get())

        self.container50 = Frame(janela_dados_laboratoriais)
        self.container50['padx'] = 10
        self.container50['pady'] = 8
        self.container50.pack()

        self.lblc63_3 = Label(self.container50)
        self.lblc63_3['text'] = ('Influenza B, qual subtipo? ' +
                                 '(1 - Victoria, 2 - Yamagatha, 3 - Não realizado, 4 - Inconclusivo, 5 - Outro, especifique):'
                                 )
        self.lblc63_3.pack(side=LEFT)

        self.txtc63_3 = Entry(self.container50)
        self.txtc63_3['width'] = 10
        self.txtc63_3.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_3.get())

        self.lblc63_4 = Label(self.container50)
        self.lblc63_4['text'] = 'Positivo para outro vírus? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lblc63_4.pack(side=LEFT)

        self.txtc63_4 = Entry(self.container50)
        self.txtc63_4['width'] = 2
        self.txtc63_4.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_4.get())

        self.container51 = Frame(janela_dados_laboratoriais)
        self.container51['padx'] = 10
        self.container51['pady'] = 8
        self.container51.pack()

        self.lblc63_5_titulo = Label(self.container51)
        self.lblc63_5_titulo['text'] = ('Se outros vírus respiratórios, qual (is)? (Marcar X): ')

        self.lblc63_5_1 = Label(self.container51)
        self.lblc63_5_1['text'] = 'SARS-CoV-2:'
        self.lblc63_5_1.pack(side=LEFT)

        self.txtc63_5_1 = Entry(self.container51)
        self.txtc63_5_1['width'] = 2
        self.txtc63_5_1.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_1.get())

        self.lblc63_5_2 = Label(self.container51)
        self.lblc63_5_2['text'] = 'Vírus Sincicial Respiratório: '
        self.lblc63_5_2.pack(side=LEFT)

        self.txtc63_5_2 = Entry(self.container51)
        self.txtc63_5_2['width'] = 2
        self.txtc63_5_2.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_2.get())

        self.lblc63_5_3 = Label(self.container51)
        self.lblc63_5_3['text'] = 'Parainfluenza 1: '
        self.lblc63_5_3.pack(side=LEFT)

        self.txtc63_5_3 = Entry(self.container51)
        self.txtc63_5_3['width'] = 2
        self.txtc63_5_3.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_3.get())

        self.lblc63_5_4 = Label(self.container51)
        self.lblc63_5_4['text'] = 'Parainfluenza 2: '
        self.lblc63_5_4.pack(side=LEFT)

        self.txtc63_5_4 = Entry(self.container51)
        self.txtc63_5_4['width'] = 2
        self.txtc63_5_4.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_4.get())

        self.lblc63_5_5 = Label(self.container51)
        self.lblc63_5_5['text'] = 'Parainfluenza 3: '
        self.lblc63_5_5.pack(side=LEFT)

        self.txtc63_5_5 = Entry(self.container51)
        self.txtc63_5_5['width'] = 2
        self.txtc63_5_5.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_5.get())

        self.lblc63_5_6 = Label(self.container51)
        self.lblc63_5_6['text'] = 'Parainfluenza 4: '
        self.lblc63_5_6.pack(side=LEFT)

        self.txtc63_5_6 = Entry(self.container51)
        self.txtc63_5_6['width'] = 2
        self.txtc63_5_6.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_6.get())

        self.lblc63_5_7 = Label(self.container51)
        self.lblc63_5_7['text'] = 'Adenovírus: '
        self.lblc63_5_7.pack(side=LEFT)

        self.txtc63_5_7 = Entry(self.container51)
        self.txtc63_5_7['width'] = 2
        self.txtc63_5_7.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_7.get())

        self.lblc63_5_8 = Label(self.container51)
        self.lblc63_5_8['text'] = 'Metapneumovírus: '
        self.lblc63_5_8.pack(side=LEFT)

        self.txtc63_5_8 = Entry(self.container51)
        self.txtc63_5_8['width'] = 2
        self.txtc63_5_8.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_8.get())

        self.lblc63_5_9 = Label(self.container51)
        self.lblc63_5_9['text'] = 'Bocavírus: '
        self.lblc63_5_9.pack(side=LEFT)

        self.txtc63_5_9 = Entry(self.container51)
        self.txtc63_5_9['width'] = 2
        self.txtc63_5_9.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_9.get())

        self.lblc63_5_10 = Label(self.container51)
        self.lblc63_5_10['text'] = 'Rinovírus: '
        self.lblc63_5_10.pack(side=LEFT)

        self.txtc63_5_10 = Entry(self.container51)
        self.txtc63_5_10['width'] = 2
        self.txtc63_5_10.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_10.get())

        self.lblc63_5_11 = Label(self.container51)
        self.lblc63_5_11['text'] = 'Outro vírus respiratório, especifique: '
        self.lblc63_5_11.pack(side=LEFT)

        self.txtc63_5_11 = Entry(self.container51)
        self.txtc63_5_11['width'] = 10
        self.txtc63_5_11.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc63_5_11.get())

        self.container52 = Frame(janela_dados_laboratoriais)
        self.container52['padx'] = 10
        self.container52['pady'] = 8
        self.container52.pack()

        self.lblc64_1 = Label(self.container52)
        self.lblc64_1['text'] = '64 - Laboratório que realizou RT-PCR/outro método por biologia molecular: '
        self.lblc64_1.pack(side=LEFT)

        self.txtc64_1 = Entry(self.container52)
        self.txtc64_1['width'] = 25
        self.txtc64_1.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc64_1.get())

        self.lblc64_2 = Label(self.container52)
        self.lblc64_2['text'] = 'Código (CNES): '
        self.lblc64_2.pack(side=LEFT)

        self.txtc64_2 = Entry(self.container52)
        self.txtc64_2['width'] = 15
        self.txtc64_2.pack(side=LEFT)
        self.dados_laboratoriais.append(self.txtc64_2.get())

        self.container_extra7 = Frame(janela_dados_laboratoriais)
        self.container_extra7["padx"] = 20
        self.container_extra7["pady"] = 8
        self.container_extra7.pack()

        self.proxima_janela = Button(self.container_extra7)
        self.proxima_janela['text'] = 'Clique para ir para a próxima janela'
        self.proxima_janela['command'] = self.janela_Conclusao
        self.proxima_janela.pack()

    def janela_Conclusao(self):
        janela_dados_conclusao = Toplevel(root)
        janela_dados_conclusao.title("Sivep Ficha")

        self.dados_conclusao = []

        self.container53 = Frame(janela_dados_conclusao)
        self.container53['padx'] = 10
        self.container53['pady'] = 8
        self.container53.pack()

        self.lbl_titulo = Label(self.container53)
        self.lbl_titulo['text'] = 'Conclusão'
        self.lbl_titulo['font'] = self.fonte_titulo
        self.lbl_titulo.pack()

        self.container54 = Frame(janela_dados_conclusao)
        self.container54['padx'] = 10
        self.container54['pady'] = 8
        self.container54.pack()

        self.lblc65 = Label(self.container54)
        self.lblc65['text'] = ('65 - Classificação final do caso) ' +
                               '(1 - SRAG por influenza, 2 - SRAG por vírus respiratório, ' +
                               '3 - SRAG por outro agente etiológico (especifique), ' +
                               '4 - SRAG não especificado, 5 - COVID-19): ')
        self.lblc65.pack(side=LEFT)

        self.txtc65 = Entry(self.container54)
        self.txtc65['width'] = 15
        self.txtc65.pack(side=LEFT)
        self.dados_conclusao.append(self.txtc65.get())

        self.container55 = Frame(janela_dados_conclusao)
        self.container55['padx'] = 10
        self.container55['pady'] = 8
        self.container55.pack()

        self.lblc66 = Label(self.container55)
        self.lblc66['text'] = ('66 - Critério de Encerramento: ' +
                               '(1 - Laboratorial, 2 - Vínculo-Epidemiológico, 3 - Clínico): ')
        self.lblc66.pack(side=LEFT)

        self.txtc66 = Entry(self.container55)
        self.txtc66['width'] = 2
        self.txtc66.pack(side=LEFT)
        self.dados_conclusao.append(self.txtc66.get())

        self.lblc67 = Label(self.container55)
        self.lblc67['text'] = '67 - Evolução do caso: (1 - Cura, 2 - Óbito, 3 - Ignorado): '
        self.lblc67.pack(side=LEFT)

        self.txtc67 = Entry(self.container55)
        self.txtc67['width'] = 2
        self.txtc67.pack(side=LEFT)
        self.dados_conclusao.append(self.txtc67.get())

        self.container56 = Frame(janela_dados_conclusao)
        self.container56['padx'] = 10
        self.container56['pady'] = 8
        self.container56.pack()

        self.lblc68 = Label(self.container56)
        self.lblc68['text'] = 'Data de alta ou óbito'
        self.lblc68.pack(side=LEFT)

        self.txtc68 = Entry(self.container56)
        self.txtc68['width'] = 8
        self.txtc68.pack(side=LEFT)
        self.dados_conclusao.append(self.txtc68.get())

        self.lblc69 = Label(self.container56)
        self.lblc69['text'] = 'Data do encerramento'
        self.lblc69.pack(side=LEFT)

        self.txtc69 = Entry(self.container56)
        self.txtc69['width'] = 8
        self.txtc69.pack(side=LEFT)
        self.dados_conclusao.append(self.txtc69.get())

        self.container57 = Frame(janela_dados_conclusao)
        self.container57['padx'] = 10
        self.container57['pady'] = 8
        self.container57.pack()

        self.lblc70 = Label(self.container57)
        self.lblc70['text'] = 'Observações'
        self.lblc70.pack(side=LEFT)

        self.txtc70 = Entry(self.container57)
        self.txtc70.pack(side=LEFT)
        self.dados_conclusao.append(self.txtc70.get())

        self.container_extra8 = Frame(janela_dados_conclusao)
        self.container_extra8["padx"] = 20
        self.container_extra8["pady"] = 8
        self.container_extra8.pack()

        self.cadastrar = Button(self.container_extra8)
        self.cadastrar['text'] = 'Seguir para confirmação?'
        self.cadastrar['command'] = self.janela_confirma
        self.cadastrar.pack()

    def janela_confirma(self):

        janela_final_final = Toplevel(root)
        janela_final_final.title('Confirimação')

        self.cont_1_fim = Frame(janela_final_final)
        self.cont_1_fim.pack()

        self.lblfimdofim = Label(self.cont_1_fim, text="Deseja concluir o cadastro?")
        self.lblfimdofim.pack()

        self.cont_2_fim = Frame(janela_final_final)
        self.cont_2_fim.pack()

        self.lbl_sim = Label(self.cont_2_fim)
        self.lbl_sim['text'] = 'SIM'
        self.lbl_sim.pack(side=RIGHT)

        self.lbl_nao = Label(self.cont_2_fim)
        self.lbl_nao['text'] = 'NÃO'
        self.lbl_nao.pack(side=LEFT)

        self.cont_3_fim = Frame(janela_final_final)
        self.cont_3_fim.pack()

        self.btn_sim = Button(self.cont_3_fim)
        self.btn_sim['text'] = ' '
        self.btn_sim["command"] = self.cadastraFicha
        self.btn_sim.pack(side=RIGHT)

        self.btn_nao = Button(self.cont_2_fim)
        self.btn_nao['text'] = ' '
        self.btn_nao["command"] = print('QUER SIM')
        self.btn_nao.pack(side=LEFT)

        self.container_4_fim = Frame(janela_final_final)
        self.container_4_fim["padx"] = 20
        self.container_4_fim["pady"] = 8
        self.container_4_fim.pack()

        self.lblmsg = Label(self.container_4_fim)
        self.lblmsg["text"] = " "
        self.lblmsg["font"] = ("Verdana", "10", "bold")
        self.lblmsg.pack()

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
        # self.txtsenha.insert(INSERT, user.senha)

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
            self.janelaMenu() 
        else:
            return

    def janelaMenu(self):
        janela_menu = Toplevel(root)
        janela_menu.title("Menu Principal")

        self.container_extra9 = Frame(janela_menu)
        self.container_extra9["pady"] = 10
        self.container_extra9.pack()

        self.proxima_janela = Button(self.container_extra9)
        self.proxima_janela['text'] = 'Clique para realizar novo preenchimento de ficha'
        self.proxima_janela['command'] = self.janela_dadosPaciente
        self.proxima_janela.pack()

        self.container_extra10 = Frame(janela_menu)
        self.container_extra10["pady"] = 10
        self.container_extra10.pack()

        self.proxima_janela = Button(self.container_extra10)
        self.proxima_janela['text'] = 'Clique para visualizar histograma por idade'
        self.proxima_janela['command'] = self.plot_histograma_idade
        self.proxima_janela.pack()

        self.container_extra11 = Frame(janela_menu)
        self.container_extra11["pady"] = 10
        self.container_extra11.pack()

        self.proxima_janela = Button(self.container_extra11)
        self.proxima_janela['text'] = 'Clique para visualizar histograma por sexo'
        self.proxima_janela['command'] = self.plot_histograma_sexo
        self.proxima_janela.pack()

        self.container_extra12 = Frame(janela_menu)
        self.container_extra12["pady"] = 10
        self.container_extra12.pack()

        self.proxima_janela = Button(self.container_extra12)
        self.proxima_janela['text'] = 'Clique para visualizar histograma por estado'
        self.proxima_janela['command'] = self.plot_histograma_estado
        self.proxima_janela.pack()

    def plot_histograma_idade(self):
        self.impsql3 = sqlite3.connect('ficha.db')
        self.sql3_cursor = self.impsql3.cursor()
        self.sql3_cursor.execute('SELECT * FROM ficha')
        with open('ficha.csv','w') as out_csv_file:
            csv_out = csv.writer(out_csv_file)
            csv_out.writerow([d[0] for d in self.sql3_cursor.description])
            for result in self.sql3_cursor:
                csv_out.writerow(result)
        self.impsql3.close()

        self.df = pd.read_csv('ficha.csv')
        plt.show(self.df['idade'].hist())

    def plot_histograma_sexo(self):
        self.impsql3 = sqlite3.connect('ficha.db')
        self.sql3_cursor = self.impsql3.cursor()
        self.sql3_cursor.execute('SELECT * FROM ficha')
        with open('ficha.csv','w') as out_csv_file:
            csv_out = csv.writer(out_csv_file)
            csv_out.writerow([d[0] for d in self.sql3_cursor.description])
            for result in self.sql3_cursor:
                csv_out.writerow(result)
        self.impsql3.close()

        self.df = pd.read_csv('ficha.csv')
        plt.show(self.df['sexo'].hist())
    
    def plot_histograma_estado(self):
        self.impsql3 = sqlite3.connect('ficha.db')
        self.sql3_cursor = self.impsql3.cursor()
        self.sql3_cursor.execute('SELECT * FROM ficha')
        with open('ficha.csv','w') as out_csv_file:
            csv_out = csv.writer(out_csv_file)
            csv_out.writerow([d[0] for d in self.sql3_cursor.description])
            for result in self.sql3_cursor:
                csv_out.writerow(result)
        self.impsql3.close()

        self.df = pd.read_csv('ficha.csv')
        plt.show(self.df['estado'].hist())

    def cadastraFicha(self):
        ficha = Ficha()

        self.lista = []
        self.lista.append(self.txtc1.get())
        self.lista.append(self.txtc2.get())
        self.lista.append(self.txtc3.get())
        self.lista.append(self.txtc4_1.get())
        self.lista.append(self.txtc4_2.get())
        self.lista.append(self.txtc5_1.get())
        self.lista.append(self.txtc5_2.get())
        self.lista.append(self.txtc6.get())
        self.lista.append(self.txtc7.get())
        self.lista.append(self.txtc8.get())
        self.lista.append(self.txtc9.get())
        self.lista.append(self.txtc10_1.get())
        self.lista.append(self.txtc10_2.get())
        self.lista.append(self.txtc11.get())
        self.lista.append(self.txtc12.get())
        self.lista.append(self.txtc13.get())
        self.lista.append(self.txtc14.get())
        self.lista.append(self.txtc15.get())
        self.lista.append(self.txtc16.get())
        self.lista.append(self.txtc17.get())
        self.lista.append(self.txtc18.get())
        self.lista.append(self.txtc19_1.get())
        self.lista.append(self.txtc19_2.get())
        self.lista.append(self.txtc20.get())
        self.lista.append(self.txtc21.get())
        self.lista.append(self.txtc22.get())
        self.lista.append(self.txtc23.get())
        self.lista.append(self.txtc24.get())
        self.lista.append(self.txtc25.get())
        self.lista.append(self.txtc26.get())
        self.lista.append(self.txtc27.get())
        self.lista.append(self.txtc28.get())
        self.lista.append(self.txtc29.get())
        self.lista.append(self.txtc30.get())
        self.lista.append(self.txtc31.get())
        self.lista.append(self.txtc32.get())
        self.lista.append(self.txtc33.get())
        self.lista.append(self.txtc34.get())
        self.lista.append(self.txtc35_1.get())
        self.lista.append(self.txtc35_2.get())
        self.lista.append(self.txtc35_3.get())
        self.lista.append(self.txtc35_4.get())
        self.lista.append(self.txtc35_5.get())
        self.lista.append(self.txtc35_6.get())
        self.lista.append(self.txtc35_7.get())
        self.lista.append(self.txtc35_8.get())
        self.lista.append(self.txtc35_9.get())
        self.lista.append(self.txtc36_1.get())
        self.lista.append(self.txtc36_2.get())
        self.lista.append(self.txtc36_3.get())
        self.lista.append(self.txtc36_4.get())
        self.lista.append(self.txtc36_5.get())
        self.lista.append(self.txtc36_6.get())
        self.lista.append(self.txtc36_7.get())
        self.lista.append(self.txtc36_8.get())
        self.lista.append(self.txtc36_9.get())
        self.lista.append(self.txtc36_10.get())
        self.lista.append(self.txtc36_11.get())
        self.lista.append(self.txtc36_12.get())
        self.lista.append(self.txtc36_13.get())
        self.lista.append(self.txtc36_14_1.get())
        self.lista.append(self.txtc36_14_2.get())
        self.lista.append(self.txtc37.get())
        self.lista.append(self.txtc38_1.get())
        self.lista.append(self.txtc38_2.get())
        self.lista.append(self.txtc38_3.get())
        self.lista.append(self.txtc38_4.get())
        self.lista.append(self.txtc38_5.get())
        self.lista.append(self.txtc38_6.get())
        self.lista.append(self.txtc38_7.get())
        self.lista.append(self.txtc39.get())
        self.lista.append(self.txtc40.get())
        self.lista.append(self.txtc41.get())
        self.lista.append(self.txtc42.get())
        self.lista.append(self.txtc43.get())
        self.lista.append(self.txtc44.get())
        self.lista.append(self.txtc45_1.get())
        self.lista.append(self.txtc45_2.get())
        self.lista.append(self.txtc46_1.get())
        self.lista.append(self.txtc46_2.get())
        self.lista.append(self.txtc47.get())
        self.lista.append(self.txtc48.get())
        self.lista.append(self.txtc49.get())
        self.lista.append(self.txtc50.get())
        self.lista.append(self.txtc51.get())
        self.lista.append(self.txtc52.get())
        self.lista.append(self.txtc53.get())
        self.lista.append(self.txtc54.get())
        self.lista.append(self.txtc55.get())
        self.lista.append(self.txtc56.get())
        self.lista.append(self.txtc57.get())
        self.lista.append(self.txtc58.get())
        self.lista.append(self.txtc59_1.get())
        self.lista.append(self.txtc59_2.get())
        self.lista.append(self.txtc59_3.get())
        self.lista.append(self.txtc59_4.get())
        self.lista.append(self.txtc59_5.get())
        self.lista.append(self.txtc59_6.get())
        self.lista.append(self.txtc59_7.get())
        self.lista.append(self.txtc59_8.get())
        self.lista.append(self.txtc59_9.get())
        self.lista.append(self.txtc60_1.get())
        self.lista.append(self.txtc60_2.get())
        self.lista.append(self.txtc61.get())
        self.lista.append(self.txtc62.get())
        self.lista.append(self.txtc63_1_1.get())
        self.lista.append(self.txtc63_1_2.get())
        self.lista.append(self.txtc63_2.get())
        self.lista.append(self.txtc63_3.get())
        self.lista.append(self.txtc63_4.get())
        self.lista.append(self.txtc63_5_1.get())
        self.lista.append(self.txtc63_5_2.get())
        self.lista.append(self.txtc63_5_3.get())
        self.lista.append(self.txtc63_5_4.get())
        self.lista.append(self.txtc63_5_5.get())
        self.lista.append(self.txtc63_5_6.get())
        self.lista.append(self.txtc63_5_7.get())
        self.lista.append(self.txtc63_5_8.get())
        self.lista.append(self.txtc63_5_9.get())
        self.lista.append(self.txtc63_5_10.get())
        self.lista.append(self.txtc63_5_11.get())
        self.lista.append(self.txtc64_1.get())
        self.lista.append(self.txtc64_2.get())
        self.lista.append(self.txtc65.get())
        self.lista.append(self.txtc66.get())
        self.lista.append(self.txtc67.get())
        self.lista.append(self.txtc68.get())
        self.lista.append(self.txtc69.get())
        self.lista.append(self.txtc70.get())

        print(self.lista)
        print(len(self.lista))

        ficha.lista = self.lista

        self.lblmsg["text"] = ficha.insertFicha()


root = Tk()
root.title("Sivep Digital")
Application(root)
root.mainloop()
