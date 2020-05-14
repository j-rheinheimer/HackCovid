# Programa principal, onde fica a programação da interface do aplicativo

from Usuarios import *
from tkinter import *


class Application:

# Mateus Corradini

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

        self.lblc1 = Label(self.container2, text="1 - Data de preenchimento: ", font=self.fonte)
        self.lblc1.pack(side=LEFT)

        self.txtc1 = Entry(self.container2)
        self.txtc1["font"] = self.fonte
        self.txtc1["width"] = 10
        self.txtc1.pack(side=LEFT)

        self.lblc2 = Label(self.container2, text="2 - Data dos primeiros sintomas: ", font=self.fonte)
        self.lblc2.pack(side=LEFT)

        self.txtc2 = Entry(self.container2)
        self.txtc2["font"] = self.fonte
        self.txtc2["width"] = 10
        self.txtc2.pack(side=LEFT)

        self.lblc3 = Label(self.container2, text="3 - UF: ", font=self.fonte)
        self.lblc3.pack(side=LEFT)

        self.txtc3 = Entry(self.container2)
        self.txtc3["font"] = self.fonte
        self.txtc3["width"] = 2
        self.txtc3.pack(side=LEFT)

        self.lblc4 = Label(self.container2, text="4 - Município: ", font=self.fonte)
        self.lblc4.pack(side=LEFT)

        self.txtc4 = Entry(self.container2)
        self.txtc4["font"] = self.fonte
        self.txtc4["width"] = 20
        self.txtc4.pack(side=LEFT)

        self.lblc5 = Label(self.container2, text=" Código(IBGE): ", font=self.fonte)
        self.lblc5.pack(side=LEFT)

        self.txtc5 = Entry(self.container2)
        self.txtc5["font"] = self.fonte
        self.txtc5["width"] = 13
        self.txtc5.pack(side=LEFT)

        self.lblc6 = Label(self.container2, text="5 - Unidade de Saúde: ", font=self.fonte)
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

        self.lblCPF = Label(self.container4, text="6 - CPF: ", font=self.fonte)
        self.lblCPF.pack(side=LEFT)

        self.txtCPF = Entry(self.container4)
        self.txtCPF["font"] = self.fonte
        self.txtCPF["width"] = 20
        self.txtCPF.pack(side=LEFT)

        self.lblc8 = Label(self.container4, text="7 - Nome: ", font=self.fonte)
        self.lblc8.pack(side=LEFT)

        self.txtc8 = Entry(self.container4)
        self.txtc8["font"] = self.fonte
        self.txtc8["width"] = 25
        self.txtc8.pack(side=LEFT)

        self.lblc9 = Label(self.container4, text="8 - Sexo(1-M/2-F/9-Ignorar): ", font=self.fonte)
        self.lblc9.pack(side=LEFT)

        self.txtc9 = Entry(self.container4)
        self.txtc9["font"] = self.fonte
        self.txtc9["width"] = 3
        self.txtc9.pack(side=LEFT)

        self.lblc10 = Label(self.container4, text="9 -  Data de Nascimento: ", font=self.fonte)
        self.lblc10.pack(side=LEFT)

        self.txtc10 = Entry(self.container4)
        self.txtc10["font"] = self.fonte
        self.txtc10["width"] = 10
        self.txtc10.pack(side=LEFT)

        self.lblIdade_1 = Label(self.container4, text="10 - (ou)Idade ", font=self.fonte)
        self.lblIdade_1.pack(side=LEFT)

        self.txtIdade_1 = Entry(self.container4)
        self.txtIdade_1["font"] = self.fonte
        self.txtIdade_1["width"] = 3
        self.txtIdade_1.pack(side=LEFT)

        self.lblIdade_2 = Label(self.container4, text="1 - Dia, 2- Mês, 3- Ano ", font=self.fonte)
        self.lblIdade_2.pack(side=LEFT)

        self.txtIdade_2 = Entry(self.container4)
        self.txtIdade_2["font"] = self.fonte
        self.txtIdade_2["width"] = 2
        self.txtIdade_2.pack(side=LEFT)

        self.lblc11 = Label(self.container4, text="11 - Gestante(1 - 1ºTrimerstre, 2-2ºTrimestre, 3-3ºTrimestre "
                                                  "\n 4-Idade gestacional ignorada), 5-Não \n6-Não se aplica, "
                                                  "9-Ignorado: ", font=self.fonte)
        self.lblc11.pack(side=LEFT)

        self.txtc11 = Entry(self.container4)
        self.txtc11["font"] = self.fonte
        self.txtc11["width"] = 2
        self.txtc11.pack(side=LEFT)

        self.lblc12 = Label(self.container5, text="12 - Raça/Cor (1-Branca, 2-Preta, 3-Amarela\n"
                                                  "4-Parda, 5-Indígena, 9-Ignorado): ", font=self.fonte)
        self.lblc12.pack(side=LEFT)

        self.txtc12 = Entry(self.container5)
        self.txtc12["font"] = self.fonte
        self.txtc12["width"] = 10
        self.txtc12.pack(side=LEFT)

        self.lblc13 = Label(self.container5, text="13 - Se indígena, etnia: ", font=self.fonte)
        self.lblc13.pack(side=LEFT)

        self.txtc13 = Entry(self.container5)
        self.txtc13["font"] = self.fonte
        self.txtc13["width"] = 20
        self.txtc13.pack(side=LEFT)

        self.lblc14 = Label(self.container5, text="14 - Escolaridade (0-Sem Escolaridade/Analfabeto\n"
                                                  "1-Fundamental I, 2-Fundamental II, 3-Médio,\n"
                                                  "4-Superior, 5-Não se Aplica, 9-Ignorado): ", font=self.fonte)
        self.lblc14.pack(side=LEFT)

        self.txtc14 = Entry(self.container5)
        self.txtc14["font"] = self.fonte
        self.txtc14["width"] = 2
        self.txtc14.pack(side=LEFT)

        self.lblc15 = Label(self.container5, text="15 - Ocupação: ", font=self.fonte)
        self.lblc15.pack(side=LEFT)

        self.txtc15 = Entry(self.container5)
        self.txtc15["font"] = self.fonte
        self.txtc15["width"] = 20
        self.txtc15.pack(side=LEFT)

        self.lblc16 = Label(self.container5, text="16 - Nome da mãe: ", font=self.fonte)
        self.lblc16.pack(side=LEFT)

        self.txtc16 = Entry(self.container5)
        self.txtc16["font"] = self.fonte
        self.txtc16["width"] = 20
        self.txtc16.pack(side=LEFT)

        self.dados_residencia = Label(self.container6, text="Dados de Residência", font=("Calibri", "12", "bold"))
        self.dados_residencia.pack()

        self.lblc17 = Label(self.container7, text="17 - CEP: ", font=self.fonte)
        self.lblc17.pack(side=LEFT)

        self.txtc17 = Entry(self.container7)
        self.txtc17["font"] = self.fonte
        self.txtc17["width"] = 15
        self.txtc17.pack(side=LEFT)

        self.lblc18 = Label(self.container7, text="18 - UF: ", font=self.fonte)
        self.lblc18.pack(side=LEFT)

        self.txtc18 = Entry(self.container7)
        self.txtc18["font"] = self.fonte
        self.txtc18["width"] = 2
        self.txtc18.pack(side=LEFT)

        self.lblc19 = Label(self.container7, text="19 - Município: ", font=self.fonte)
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

        self.lblc21 = Label(self.container7, text="20 - Bairro: ", font=self.fonte)
        self.lblc21.pack(side=LEFT)

        self.txtc21 = Entry(self.container7)
        self.txtc21["font"] = self.fonte
        self.txtc21["width"] = 20
        self.txtc21.pack(side=LEFT)

        self.lblc22 = Label(self.container7, text="21 - Logradouro: ", font=self.fonte)
        self.lblc22.pack(side=LEFT)

        self.txtc22 = Entry(self.container7)
        self.txtc22["font"] = self.fonte
        self.txtc22["width"] = 20
        self.txtc22.pack(side=LEFT)

        self.lblc23 = Label(self.container7, text="22 - Nº: ", font=self.fonte)
        self.lblc23.pack(side=LEFT)

        self.txtc23 = Entry(self.container7)
        self.txtc23["font"] = self.fonte
        self.txtc23["width"] = 4
        self.txtc23.pack(side=LEFT)

        self.lblc24 = Label(self.container7, text="23 - Complemento: ", font=self.fonte)
        self.lblc24.pack(side=LEFT)

        self.txtc24 = Entry(self.container7)
        self.txtc24["font"] = self.fonte
        self.txtc24["width"] = 15
        self.txtc24.pack(side=LEFT)

        self.lblc25 = Label(self.container8, text="24 - Telefone(DDD): ", font=self.fonte)
        self.lblc25.pack(side=LEFT)

        self.txtc25 = Entry(self.container8)
        self.txtc25["font"] = self.fonte
        self.txtc25["width"] = 15
        self.txtc25.pack(side=LEFT)

        self.lblc26 = Label(self.container8, text="25 - Zona(1-Urbana, 2-Rural\n"
                                                  "3-Periurbana, 9-Ignorado): ", font=self.fonte)
        self.lblc26.pack(side=LEFT)

        self.txtc26 = Entry(self.container8)
        self.txtc26["font"] = self.fonte
        self.txtc26["width"] = 2
        self.txtc26.pack(side=LEFT)

        self.lblc27 = Label(self.container8, text="26 - País(se residente fora do Brasil): ", font=self.fonte)
        self.lblc27.pack(side=LEFT)

        self.txtc27 = Entry(self.container8)
        self.txtc27["font"] = self.fonte
        self.txtc27["width"] = 20
        self.txtc27.pack(side=LEFT)

# Mateus Corradini

# João Victor
    def dadosClinicos(self):
        dados_clinicos = Toplevel(root)
        dados_clinicos.title('Formulário')

        self.fontePadrao = ("Arial", "10")
        self.fonteTitulo = ("Arial", "15", "bold")
        self.containerTitulo = Frame(dados_clinicos)
        self.containerTitulo["padx"] = 10
        self.containerTitulo.pack()
  
        self.container27 = Frame(dados_clinicos)
        self.container27["pady"] = 10
        self.container27["width"] = 160
        self.container27.pack()
  
        self.container2829 = Frame(dados_clinicos)
        self.container2829["pady"] = 10
        self.container2829["width"] = 160
        self.container2829.pack()

        self.container3031 = Frame(dados_clinicos)
        self.container3031["pady"] = 10
        self.container3031["width"] = 160
        self.container3031.pack()

        self.container32 = Frame(dados_clinicos)
        self.container32["pady"] = 10
        self.container32["width"] = 160
        self.container32.pack()

        self.container33 = Frame(dados_clinicos)
        self.container33["pady"] = 5
        self.container33["width"] = 160
        self.container33.pack()

        self.container34 = Frame(dados_clinicos)
        self.container34["pady"] = 5
        self.container34["width"] = 160
        self.container34.pack()

        self.container35 = Frame(dados_clinicos)
        self.container35["pady"] = 10
        self.container35["width"] = 160
        self.container35.pack()

        self.container35row1 = Frame(dados_clinicos)
        self.container35row1["pady"] = 5
        self.container35row1["width"] = 160
        self.container35row1.pack()

        self.container36row0 = Frame(dados_clinicos)
        self.container36row0["pady"] = 5
        self.container36row0["width"] = 160
        self.container36row0.pack()

        self.container36row1 = Frame(dados_clinicos)
        self.container36row1["pady"] = 5
        self.container36row1["width"] = 160
        self.container36row1.pack()

        self.container36row2 = Frame(dados_clinicos)
        self.container36row2["pady"] = 5
        self.container36row2["width"] = 160
        self.container36row2.pack()

        self.container36row3 = Frame(dados_clinicos)
        self.container36row3["pady"] = 10
        self.container36row3["width"] = 160
        self.container36row3.pack()

        self.container3738 = Frame(dados_clinicos)
        self.container3738["pady"] = 5
        self.container3738["width"] = 160
        self.container3738.pack()

        self.containerExtrarow0 = Frame(dados_clinicos)
        self.containerExtrarow0["pady"] = 5
        self.containerExtrarow0["width"] = 160
        self.containerExtrarow0.pack()

        self.containerExtrarow1 = Frame(dados_clinicos)
        self.containerExtrarow1["pady"] = 5
        self.containerExtrarow1["width"] = 160
        self.containerExtrarow1.pack()

        self.containerExtrarow2 = Frame(dados_clinicos)
        self.containerExtrarow2["pady"] = 5
        self.containerExtrarow2["width"] = 160
        self.containerExtrarow2.pack()

        self.containerExtrarow3 = Frame(dados_clinicos)
        self.containerExtrarow3["pady"] = 5
        self.containerExtrarow3["width"] = 160
        self.containerExtrarow3.pack()

        self.containerExtrarow4 = Frame(dados_clinicos)
        self.containerExtrarow4["pady"] = 5
        self.containerExtrarow4["width"] = 160
        self.containerExtrarow4.pack()

        self.containerExtrarow5 = Frame(dados_clinicos)
        self.containerExtrarow5["pady"] = 5
        self.containerExtrarow5["width"] = 160
        self.containerExtrarow5.pack()

        self.tituloDadosClinicos = Label(self.containerTitulo, text="Dados clínicos e epidemiológicos")
        self.tituloDadosClinicos["font"] = self.fonteTitulo
        self.tituloDadosClinicos.pack()
  
        self.historicoViagemLabel = Label(self.container27,text="27 - Paciente tem histórico de viagem internacional até 14 dias antes do início dos sintomas?(1-Sim 2-Não 9-Ignorado)", font=self.fontePadrao)
        self.historicoViagemLabel.pack(side=LEFT)
  
        self.historicoViagem = Entry(self.container27)
        self.historicoViagem["width"] = 20
        self.historicoViagem["font"] = self.fontePadrao
        self.historicoViagem.pack(side=LEFT)
 
        self.confirmPaisLabel = Label(self.container2829,text="28 - Se sim: Qual País?",font=self.fontePadrao)
        self.confirmPaisLabel["width"] = 20
        self.confirmPaisLabel.pack(side=LEFT)

        self.confirmPais = Entry(self.container2829)
        self.confirmPais["width"] = 40
        self.confirmPais["font"] = self.fontePadrao
        self.confirmPais.pack(side=LEFT)

        self.confirmLocalLabel = Label(self.container2829,text="29 - Em qual local?",font=self.fontePadrao)
        self.confirmLocalLabel["width"] = 20
        self.confirmLocalLabel.pack(side=LEFT)

        self.confirmLocal = Entry(self.container2829)
        self.confirmLocal["width"] = 40
        self.confirmLocal["font"] = self.fontePadrao
        self.confirmLocal.pack(side=LEFT)

        self.dataViagemLabel = Label(self.container3031,text="30 - Data de viagem:",font=self.fontePadrao)
        self.dataViagemLabel["width"] = 20
        self.dataViagemLabel.pack(side=LEFT)

        self.dataViagem = Entry(self.container3031)
        self.dataViagem["width"] = 40
        self.dataViagem["font"] = self.fontePadrao
        self.dataViagem.pack(side=LEFT)

        self.dataRetornoLabel = Label(self.container3031,text="31 - Data de retorno:",font=self.fontePadrao)
        self.dataRetornoLabel["width"] = 20
        self.dataRetornoLabel.pack(side=LEFT)

        self.dataRetorno = Entry(self.container3031)
        self.dataRetorno["width"] = 40
        self.dataRetorno["font"] = self.fontePadrao
        self.dataRetorno.pack(side=LEFT)
	
        self.provemLabel = Label(self.container32)
        self.provemLabel["text"] = "32 - É caso proveniente de surto de SG que evoluiu para SRAG?(1-Sim 2-Não 9-Ignorado)"
        self.provemLabel["font"] = self.fontePadrao
        self.provemLabel.pack(side=LEFT)
        
        self.provem = Entry(self.container32)
        self.provem["width"] = 30
        self.provem["font"] = self.fontePadrao
        self.provem.pack(side=LEFT)

        self.adqHospitalLabel = Label(self.container33)
        self.adqHospitalLabel["text"] = "33 - Trata-se de caso nosocomial (infecção adquirida no hospital)?(1-Sim 2-Não 9-Ignorado)"
        self.adqHospitalLabel["font"] = self.fontePadrao
        self.adqHospitalLabel.pack(side=LEFT)

        self.adqHospital = Entry(self.container33)
        self.adqHospital["width"] = 30
        self.adqHospital["font"] = self.fontePadrao
        self.adqHospital.pack(side=LEFT)

        self.contatoAnimaisLabel = Label(self.container34)
        self.contatoAnimaisLabel["text"] = "34 - Paciente trabalha ou tem contato direto com aves ou suínos?(1-Sim 2-Não 9-Ignorado)"
        self.contatoAnimaisLabel["font"] = self.fontePadrao
        self.contatoAnimaisLabel.pack(side=LEFT)

        self.contatoAnimaisLabel = Entry(self.container34)
        self.contatoAnimaisLabel["width"] = 30
        self.contatoAnimaisLabel["font"] = self.fontePadrao
        self.contatoAnimaisLabel.pack(side=LEFT)

        self.sintomasLabel = Label(self.container35)
        self.sintomasLabel["text"] = "35 - Sinais e Sintomas:(1-Sim 2-Não 9-Ignorado):"
        self.sintomasLabel["font"] = self.fontePadrao
        self.sintomasLabel.pack(side=LEFT)

        self.sintomaFebreLabel = Label(self.container35)
        self.sintomaFebreLabel["text"] = "  Febre"
        self.sintomaFebreLabel["font"] = self.fontePadrao  
        self.sintomaFebreLabel.pack(side=LEFT)

        self.sintomaFebre = Entry(self.container35)
        self.sintomaFebre["width"] = 5
        self.sintomaFebre["font"] = self.fontePadrao
        self.sintomaFebre.pack(side=LEFT)

        self.sintomaTosseLabel = Label(self.container35)
        self.sintomaTosseLabel["text"] = "  Tosse"
        self.sintomaTosseLabel["font"] = self.fontePadrao  
        self.sintomaTosseLabel.pack(side=LEFT)

        self.sintomaTosse = Entry(self.container35)
        self.sintomaTosse["width"] = 5
        self.sintomaTosse["font"] = self.fontePadrao
        self.sintomaTosse.pack(side=LEFT)

        self.sintomaGargantaLabel = Label(self.container35)
        self.sintomaGargantaLabel["text"] = "  Dor de garganta"
        self.sintomaGargantaLabel["font"] = self.fontePadrao  
        self.sintomaGargantaLabel.pack(side=LEFT)

        self.sintomaGarganta = Entry(self.container35)
        self.sintomaGarganta["width"] = 5
        self.sintomaGarganta["font"] = self.fontePadrao
        self.sintomaGarganta.pack(side=LEFT)

        self.sintomaDispneiaLabel = Label(self.container35)
        self.sintomaDispneiaLabel["text"] = "  Dispnéia"
        self.sintomaDispneiaLabel["font"] = self.fontePadrao  
        self.sintomaDispneiaLabel.pack(side=LEFT)

        self.sintomaDispneia = Entry(self.container35)
        self.sintomaDispneia["width"] = 5
        self.sintomaDispneia["font"] = self.fontePadrao
        self.sintomaDispneia.pack(side=LEFT)

        self.sintomaDesconfortoLabel = Label(self.container35row1)
        self.sintomaDesconfortoLabel["text"] = "  Desconforto Respiratório"
        self.sintomaDesconfortoLabel["font"] = self.fontePadrao  
        self.sintomaDesconfortoLabel.pack(side=LEFT)

        self.sintomaDesconforto = Entry(self.container35row1)
        self.sintomaDesconforto["width"] = 5
        self.sintomaDesconforto["font"] = self.fontePadrao
        self.sintomaDesconforto.pack(side=LEFT)

        self.sintomaSaturaLabel = Label(self.container35row1)
        self.sintomaSaturaLabel["text"] = "  Saturação de O2<95%"
        self.sintomaSaturaLabel["font"] = self.fontePadrao  
        self.sintomaSaturaLabel.pack(side=LEFT)

        self.sintomaSatura = Entry(self.container35row1)
        self.sintomaSatura["width"] = 10
        self.sintomaSatura["font"] = self.fontePadrao
        self.sintomaSatura.pack(side=LEFT)

        self.sintomaDiarrLabel = Label(self.container35row1)
        self.sintomaDiarrLabel["text"] = "  Diarreia"
        self.sintomaDiarrLabel["font"] = self.fontePadrao  
        self.sintomaDiarrLabel.pack(side=LEFT)

        self.sintomaDiarr = Entry(self.container35row1)
        self.sintomaDiarr["width"] = 5
        self.sintomaDiarr["font"] = self.fontePadrao
        self.sintomaDiarr.pack(side=LEFT)

        self.sintomaVomitoLabel = Label(self.container35row1)
        self.sintomaVomitoLabel["text"] = "  Vômito"
        self.sintomaVomitoLabel["font"] = self.fontePadrao  
        self.sintomaVomitoLabel.pack(side=LEFT)

        self.sintomaVomito = Entry(self.container35row1)
        self.sintomaVomito["width"] = 5
        self.sintomaVomito["font"] = self.fontePadrao
        self.sintomaVomito.pack(side=LEFT)

        self.sintomaOutrosLabel = Label(self.container35row1)
        self.sintomaOutrosLabel["text"] = " Outro(s)"
        self.sintomaOutrosLabel["font"] = self.fontePadrao  
        self.sintomaOutrosLabel.pack(side=LEFT)

        self.sintomaOutros = Entry(self.container35row1)
        self.sintomaOutros["width"] = 20
        self.sintomaOutros["font"] = self.fontePadrao
        self.sintomaOutros.pack(side=LEFT)

        self.fatoresRiscoLabel = Label(self.container36row0)
        self.fatoresRiscoLabel["text"] = "36 - Possui fatores de risco/comorbidades?(1-Sim 2-Não 9-Ignorado)"
        self.fatoresRiscoLabel["font"] = self.fontePadrao  
        self.fatoresRiscoLabel.pack(side=LEFT)

        self.fatoresRisco = Entry(self.container36row0)
        self.fatoresRisco["width"] = 30
        self.fatoresRisco["font"] = self.fontePadrao
        self.fatoresRisco.pack(side=LEFT)

        self.qualLabel = Label(self.container36row1)
        self.qualLabel["text"] = "Se sim, qual(is)?(marcar x):     "
        self.qualLabel["font"] = self.fontePadrao  
        self.qualLabel.pack(side=LEFT)

        self.puerperaLabel = Label(self.container36row1)
        self.puerperaLabel["text"] = "Puérpera(até 45 dias do parto)"
        self.puerperaLabel["font"] = self.fontePadrao  
        self.puerperaLabel.pack(side=LEFT)

        self.puerpera = Entry(self.container36row1)
        self.puerpera["width"] = 2
        self.puerpera["font"] = self.fontePadrao
        self.puerpera.pack(side=LEFT)

        self.cardCronicaLabel = Label(self.container36row1)
        self.cardCronicaLabel["text"] = "  Doença Cardiovascular Crônica"
        self.cardCronicaLabel["font"] = self.fontePadrao  
        self.cardCronicaLabel.pack(side=LEFT)

        self.cardCronica = Entry(self.container36row1)
        self.cardCronica["width"] = 2
        self.cardCronica["font"] = self.fontePadrao
        self.cardCronica.pack(side=LEFT) 

        self.hermCronicaLabel = Label(self.container36row1)
        self.hermCronicaLabel["text"] = "  Doença Hematológica Crônica"
        self.hermCronicaLabel["font"] = self.fontePadrao  
        self.hermCronicaLabel.pack(side=LEFT)

        self.hermCronica = Entry(self.container36row1)
        self.hermCronica["width"] = 2
        self.hermCronica["font"] = self.fontePadrao
        self.hermCronica.pack(side=LEFT)  

        self.sindrDownLabel = Label(self.container36row2)
        self.sindrDownLabel["text"] = "  Síndrome de Down"
        self.sindrDownLabel["font"] = self.fontePadrao  
        self.sindrDownLabel.pack(side=LEFT)

        self.sindrDown = Entry(self.container36row2)
        self.sindrDown["width"] = 2
        self.sindrDown["font"] = self.fontePadrao
        self.sindrDown.pack(side=LEFT) 

        self.hepCronicaLabel = Label(self.container36row2)
        self.hepCronicaLabel["text"] = "  Doença Hepática Crônica"
        self.hepCronicaLabel["font"] = self.fontePadrao  
        self.hepCronicaLabel.pack(side=LEFT)

        self.hepCronica = Entry(self.container36row2)
        self.hepCronica["width"] = 2
        self.hepCronica["font"] = self.fontePadrao
        self.hepCronica.pack(side=LEFT) 

        self.asmaLabel = Label(self.container36row2)
        self.asmaLabel["text"] = "  Asma"
        self.asmaLabel["font"] = self.fontePadrao  
        self.asmaLabel.pack(side=LEFT)

        self.asma = Entry(self.container36row2)
        self.asma["width"] = 2
        self.asma["font"] = self.fontePadrao
        self.asma.pack(side=LEFT) 

        self.diabetisLabel = Label(self.container36row2)
        self.diabetisLabel["text"] = "   Diabetes mellitus"
        self.diabetisLabel["font"] = self.fontePadrao  
        self.diabetisLabel.pack(side=LEFT)

        self.diabetis = Entry(self.container36row2)
        self.diabetis["width"] = 2
        self.diabetis["font"] = self.fontePadrao
        self.diabetis.pack(side=LEFT) 

        self.neuroCronLabel = Label(self.container36row2)
        self.neuroCronLabel["text"] = "   Doença Neurológica Crônica"
        self.neuroCronLabel["font"] = self.fontePadrao  
        self.neuroCronLabel.pack(side=LEFT)

        self.neuroCron = Entry(self.container36row2)
        self.neuroCron["width"] = 2
        self.neuroCron["font"] = self.fontePadrao
        self.neuroCron.pack(side=LEFT) 

        self.outraPneumopatiaLabel = Label(self.container36row2)
        self.outraPneumopatiaLabel["text"] = "   Outra Pneumopatia Crônica"
        self.outraPneumopatiaLabel["font"] = self.fontePadrao  
        self.outraPneumopatiaLabel.pack(side=LEFT)

        self.outraPneumopatia = Entry(self.container36row2)
        self.outraPneumopatia["width"] = 2
        self.outraPneumopatia["font"] = self.fontePadrao
        self.outraPneumopatia.pack(side=LEFT) 

        self.imunodefLabel = Label(self.container36row3)
        self.imunodefLabel["text"] = "   Imunodefiência/Imunodepressão"
        self.imunodefLabel["font"] = self.fontePadrao  
        self.imunodefLabel.pack(side=LEFT)

        self.imunodef = Entry(self.container36row3)
        self.imunodef["width"] = 2
        self.imunodef["font"] = self.fontePadrao
        self.imunodef.pack(side=LEFT)

        self.renalCronicLabel = Label(self.container36row3)
        self.renalCronicLabel["text"] = "   Doença Renal Crônica"
        self.renalCronicLabel["font"] = self.fontePadrao  
        self.renalCronicLabel.pack(side=LEFT)

        self.renalCronic = Entry(self.container36row3)
        self.renalCronic["width"] = 2
        self.renalCronic["font"] = self.fontePadrao
        self.renalCronic.pack(side=LEFT)

        self.obesidLabel = Label(self.container36row3)
        self.obesidLabel["text"] = "   Obesidade"
        self.obesidLabel["font"] = self.fontePadrao  
        self.obesidLabel.pack(side=LEFT)

        self.obesid = Entry(self.container36row3)
        self.obesid["width"] = 2
        self.obesid["font"] = self.fontePadrao
        self.obesid.pack(side=LEFT)  

        self.imcLabel = Label(self.container36row3)
        self.imcLabel["text"] = "IMC"
        self.imcLabel["font"] = self.fontePadrao  
        self.imcLabel.pack(side=LEFT)

        self.imc = Entry(self.container36row3)
        self.imc["width"] = 2
        self.imc["font"] = self.fontePadrao
        self.imc.pack(side=LEFT)  

        self.outrosFatoresLabel = Label(self.container36row3)
        self.outrosFatoresLabel["text"] = "   Outros"
        self.outrosFatoresLabel["font"] = self.fontePadrao  
        self.outrosFatoresLabel.pack(side=LEFT)

        self.outrosFatores = Entry(self.container36row3)
        self.outrosFatores["width"] = 15
        self.outrosFatores["font"] = self.fontePadrao
        self.outrosFatores.pack(side=LEFT)

        self.ultimaCampanhaLabel = Label(self.container3738)
        self.ultimaCampanhaLabel["text"] = "37 - Recebeu vacina contra Gripe na última campanha?(1-Sim 2-Não 9-Ignorado)"
        self.ultimaCampanhaLabel["font"] = self.fontePadrao
        self.ultimaCampanhaLabel.pack(side=LEFT)

        self.ultimaCampanha = Entry(self.container3738)
        self.ultimaCampanha["width"] = 15
        self.ultimaCampanha["font"] = self.fontePadrao
        self.ultimaCampanha.pack(side=LEFT)

        self.dataVacinacaoLabel = Label(self.container3738)
        self.dataVacinacaoLabel["text"] = "  38 - Data da Vacinação"
        self.dataVacinacaoLabel["font"] = self.fontePadrao
        self.dataVacinacaoLabel.pack(side=LEFT)

        self.dataVacinacao = Entry(self.container3738)
        self.dataVacinacao["width"] = 15
        self.dataVacinacao["font"] = self.fontePadrao
        self.dataVacinacao.pack(side=LEFT)

        self.maeVacinaLabel = Label(self.containerExtrarow0)
        self.maeVacinaLabel["text"]= "Se < 6 meses: A mãe recebeu vacina?(1-Sim 2-Não 9-Ignorado)"
        self.maeVacinaLabel["font"] = self.fontePadrao
        self.maeVacinaLabel.pack(side=LEFT)

        self.maeVacina = Entry(self.containerExtrarow0)
        self.maeVacina["width"] = 15
        self.maeVacina["font"] = self.fontePadrao
        self.maeVacina.pack(side=LEFT)
        
        self.maeVacinaDataLabel = Label(self.containerExtrarow0)
        self.maeVacinaDataLabel["text"]= "   Se sim, data:"
        self.maeVacinaDataLabel["font"] = self.fontePadrao
        self.maeVacinaDataLabel.pack(side=LEFT)

        self.maeVacinaData = Entry(self.containerExtrarow0)
        self.maeVacinaData["width"] = 15
        self.maeVacinaData["font"] = self.fontePadrao
        self.maeVacinaData.pack(side=LEFT)

        self.amamentacaoLabel = Label(self.containerExtrarow1)
        self.amamentacaoLabel["text"]= "    A mãe amamentava a criança?(1-Sim 2-Não 9-Ignorado)"
        self.amamentacaoLabel["font"] = self.fontePadrao
        self.amamentacaoLabel.pack(side=LEFT)

        self.amamentacao = Entry(self.containerExtrarow1)
        self.amamentacao["width"] = 15
        self.amamentacao["font"] = self.fontePadrao
        self.amamentacao.pack(side=LEFT)

        self.textoCondicao = Label(self.containerExtrarow2)
        self.textoCondicao["text"]= "Se >= 6 meses e <= 8 anos:"
        self.textoCondicao["font"] = self.fontePadrao
        self.textoCondicao.pack(side=LEFT)

        self.dataDoseUnicaLabel = Label(self.containerExtrarow3)
        self.dataDoseUnicaLabel["text"]= "Data da dose única 1/1:"
        self.dataDoseUnicaLabel["font"] = self.fontePadrao
        self.dataDoseUnicaLabel.pack(side=LEFT)

        self.dataDoseUnica = Entry(self.containerExtrarow3)
        self.dataDoseUnica["width"] = 15
        self.dataDoseUnica["font"] = self.fontePadrao
        self.dataDoseUnica.pack(side=LEFT)

        self.textoInformativo1 = Label(self.containerExtrarow3)
        self.textoInformativo1["text"]= "   (dose única para crianças vacinadas em campanhas de anos anteriores)"
        self.textoInformativo1["font"] = self.fontePadrao
        self.textoInformativo1.pack(side=LEFT)

        self.dataPrimDoseLabel = Label(self.containerExtrarow4)
        self.dataPrimDoseLabel["text"]= "Data da primeira dose:"
        self.dataPrimDoseLabel["font"] = self.fontePadrao
        self.dataPrimDoseLabel.pack(side=LEFT)

        self.dataPrimDose = Entry(self.containerExtrarow4)
        self.dataPrimDose["width"] = 15
        self.dataPrimDose["font"] = self.fontePadrao
        self.dataPrimDose.pack(side=LEFT)

        self.textoInformativo2 = Label(self.containerExtrarow4)
        self.textoInformativo2["text"]= "   (1ª dose para crianças vacinadas pela primeira vez)"
        self.textoInformativo2["font"] = self.fontePadrao
        self.textoInformativo2.pack(side=LEFT)

        self.dataSegDoseLabel = Label(self.containerExtrarow5)
        self.dataSegDoseLabel["text"]= "Data da segunda dose:"
        self.dataSegDoseLabel["font"] = self.fontePadrao
        self.dataSegDoseLabel.pack(side=LEFT)

        self.dataSegDose = Entry(self.containerExtrarow5)
        self.dataSegDose["width"] = 15
        self.dataSegDose["font"] = self.fontePadrao
        self.dataSegDose.pack(side=LEFT)

        self.textoInformativo2 = Label(self.containerExtrarow5)
        self.textoInformativo2["text"]= "   (2ª dose para crianças vacinadas pela primeira vez)"
        self.textoInformativo2["font"] = self.fontePadrao
        self.textoInformativo2.pack(side=LEFT)

    def dadosAtendimento(self):
        dados_atendimento = Toplevel(root)
        dados_atendimento.title('Formulário')

        self.fontePadrao = ("Arial", "10")
        self.fonteTitulo = ("Arial", "15", "bold")
        self.containerTituloSecAtendimento = Frame(dados_atendimento)
        self.containerTituloSecAtendimento["pady"] = 5
        self.containerTituloSecAtendimento["width"] = 160
        self.containerTituloSecAtendimento.pack()     
        
        self.container3941 = Frame(dados_atendimento)
        self.container3941["pady"] = 5
        self.container3941["width"] = 160
        self.container3941.pack()

        self.container4244 = Frame(dados_atendimento)
        self.container4244["pady"] = 5
        self.container4244["width"] = 160
        self.container4244.pack()

        self.container45 = Frame(dados_atendimento)
        self.container45["pady"] = 5
        self.container45["width"] = 160
        self.container45.pack()

        self.container46 = Frame(dados_atendimento)
        self.container46["pady"] = 5
        self.container46["width"] = 160
        self.container46.pack()

        self.container4749 = Frame(dados_atendimento)
        self.container4749["pady"] = 5
        self.container4749["width"] = 160
        self.container4749.pack()

        self.container50 = Frame(dados_atendimento)
        self.container50["pady"] = 5
        self.container50["width"] = 160
        self.container50.pack()

        self.container5152 = Frame(dados_atendimento)
        self.container5152["pady"] = 5
        self.container5152["width"] = 160
        self.container5152.pack()

        self.container5354 = Frame(dados_atendimento)
        self.container5354["pady"] = 5
        self.container5354["width"] = 160
        self.container5354.pack()

        self.container55 = Frame(dados_atendimento)
        self.container55["pady"] = 5
        self.container55["width"] = 160
        self.container55.pack()

        self.tituloSecAtendimento = Label(self.containerTituloSecAtendimento, text="Dados de Atendimento")
        self.tituloSecAtendimento["font"] = self.fonteTitulo
        self.tituloSecAtendimento.pack()

        self.antiviralLabel = Label(self.container3941,text="39 - Usou antiviral para gripe?(1-Sim 2-Não 9-Ignorado)", font=self.fontePadrao)
        self.antiviralLabel.pack(side=LEFT)
  
        self.antiviral = Entry(self.container3941)
        self.antiviral["width"] = 8
        self.antiviral["font"] = self.fontePadrao
        self.antiviral.pack(side=LEFT)

        self.antiviralDetailLabel = Label(self.container3941,text="40 - Qual antiviral?(1-Oseltamivir 2-Zanamivir 3-Outro, especifique)", font=self.fontePadrao)
        self.antiviralDetailLabel.pack(side=LEFT)
  
        self.antiviralDetail = Entry(self.container3941)
        self.antiviralDetail["width"] = 16
        self.antiviralDetail["font"] = self.fontePadrao
        self.antiviralDetail.pack(side=LEFT)

        self.dataInicioTratamLabel = Label(self.container3941,text="41 - Data inicio do tratamento", font=self.fontePadrao)
        self.dataInicioTratamLabel.pack(side=LEFT)
  
        self.dataInicioTratam = Entry(self.container3941)
        self.dataInicioTratam["width"] = 12
        self.dataInicioTratam["font"] = self.fontePadrao
        self.dataInicioTratam.pack(side=LEFT)

        self.internaLabel = Label(self.container4244,text="   42 - Houve interneção?(1-Sim 2-Não 9-Ignorado)", font=self.fontePadrao)
        self.internaLabel.pack(side=LEFT)
  
        self.interna = Entry(self.container4244)
        self.interna["width"] = 12
        self.interna["font"] = self.fontePadrao
        self.interna.pack(side=LEFT)

        self.dataInternaLabel = Label(self.container4244,text="   43 - Data da internação por SRAG:", font=self.fontePadrao)
        self.dataInternaLabel.pack(side=LEFT)
  
        self.dataInterna = Entry(self.container4244)
        self.dataInterna["width"] = 12
        self.dataInterna["font"] = self.fontePadrao
        self.dataInterna.pack(side=LEFT)

        self.ufInternaLabel = Label(self.container4244,text="   44 - UF de internação:", font=self.fontePadrao)
        self.ufInternaLabel.pack(side=LEFT)
  
        self.ufInterna = Entry(self.container4244)
        self.ufInterna["width"] = 12
        self.ufInterna["font"] = self.fontePadrao
        self.ufInterna.pack(side=LEFT)

        self.municipioInternaLabel = Label(self.container45,text="45 - Município de internação:", font=self.fontePadrao)
        self.municipioInternaLabel.pack(side=LEFT)
  
        self.municipioInterna = Entry(self.container45)
        self.municipioInterna["width"] = 12
        self.municipioInterna["font"] = self.fontePadrao
        self.municipioInterna.pack(side=LEFT)

        self.codigoIBGELabel = Label(self.container45,text="          Código(IBGE):", font=self.fontePadrao)
        self.codigoIBGELabel.pack(side=LEFT)
  
        self.codigoIBGE = Entry(self.container45)
        self.codigoIBGE["width"] = 12
        self.codigoIBGE["font"] = self.fontePadrao
        self.codigoIBGE.pack(side=LEFT)

        self.unidInternaLabel = Label(self.container46,text="46 - Unidade de saúde de internação:", font=self.fontePadrao)
        self.unidInternaLabel.pack(side=LEFT)
  
        self.unidInterna = Entry(self.container46)
        self.unidInterna["width"] = 12
        self.unidInterna["font"] = self.fontePadrao
        self.unidInterna.pack(side=LEFT)

        self.codigoCNESLabel = Label(self.container46,text="          Código(CNES):", font=self.fontePadrao)
        self.codigoCNESLabel.pack(side=LEFT)
  
        self.codigoCNES = Entry(self.container46)
        self.codigoCNES["width"] = 12
        self.codigoCNES["font"] = self.fontePadrao
        self.codigoCNES.pack(side=LEFT)

        self.internadoUTILabel = Label(self.container4749,text="   47 - Internado em UTI?(1-Sim 2-Não 9-Ignorado)", font=self.fontePadrao)
        self.internadoUTILabel.pack(side=LEFT)
  
        self.internadoUTI = Entry(self.container4749)
        self.internadoUTI["width"] = 12
        self.internadoUTI["font"] = self.fontePadrao
        self.internadoUTI.pack(side=LEFT)

        self.dataEntradaUTILabel = Label(self.container4749,text="   48 - Data de entrada na UTI:", font=self.fontePadrao)
        self.dataEntradaUTILabel.pack(side=LEFT)
  
        self.dataEntradaUTI = Entry(self.container4749)
        self.dataEntradaUTI["width"] = 12
        self.dataEntradaUTI["font"] = self.fontePadrao
        self.dataEntradaUTI.pack(side=LEFT)

        self.dataSaidaUTILabel = Label(self.container4749,text="   49 - Data de saida na UTI:", font=self.fontePadrao)
        self.dataSaidaUTILabel.pack(side=LEFT)
  
        self.dataSaidaUTI = Entry(self.container4749)
        self.dataSaidaUTI["width"] = 12
        self.dataSaidaUTI["font"] = self.fontePadrao
        self.dataSaidaUTI.pack(side=LEFT)

        self.suporteVentilatorioLabel = Label(self.container50,text="50 - Uso de suporte ventilarório:", font=self.fontePadrao)
        self.suporteVentilatorioLabel.pack(side=LEFT)
  
        self.suporteVentilatorio = Entry(self.container50)
        self.suporteVentilatorio["width"] = 12
        self.suporteVentilatorio["font"] = self.fontePadrao
        self.suporteVentilatorio.pack(side=LEFT)

        self.suporteVentilatorioInfoLabel = Label(self.container50,text=" (1-Sim, invasico 2-Sim, não invasivo 3-Não 9-Ignorado)", font=self.fontePadrao)
        self.suporteVentilatorioInfoLabel.pack(side=LEFT)

        self.raioXLabel = Label(self.container5152,text="51 - Raio X de toráx:", font=self.fontePadrao)
        self.raioXLabel.pack(side=LEFT)
  
        self.raioX = Entry(self.container5152)
        self.raioX["width"] = 12
        self.raioX["font"] = self.fontePadrao
        self.raioX.pack(side=LEFT)

        self.raioXinfo = Label(self.container5152,text=" (1-Normal 2-Infiltrado intersticial 3-Consolidação 4-Misto 5-Outro 6-Não realizado 9-Ignorado)", font=self.fontePadrao)
        self.raioXinfo.pack(side=LEFT)

        self.dataRaioXLabel = Label(self.container5152,text="   52 - Data do raio X:", font=self.fontePadrao)
        self.dataRaioXLabel.pack(side=LEFT)
  
        self.dataRaioX = Entry(self.container5152)
        self.dataRaioX["width"] = 12
        self.dataRaioX["font"] = self.fontePadrao
        self.dataRaioX.pack(side=LEFT)

        self.coletAmostraLabel = Label(self.container5354,text="53 - Coletou amostra?(1-Sim 2-Não 9-Ignorado):", font=self.fontePadrao)
        self.coletAmostraLabel.pack(side=LEFT)
  
        self.coletAmostra = Entry(self.container5354)
        self.coletAmostra["width"] = 12
        self.coletAmostra["font"] = self.fontePadrao
        self.coletAmostra.pack(side=LEFT)

        self.dataColetAmostraLabel = Label(self.container5354,text="   54 - Data da coleta:", font=self.fontePadrao)
        self.dataColetAmostraLabel.pack(side=LEFT)
  
        self.dataColetAmostra = Entry(self.container5354)
        self.dataColetAmostra["width"] = 12
        self.dataColetAmostra["font"] = self.fontePadrao
        self.dataColetAmostra.pack(side=LEFT)

        self.tipoAmostraLabel = Label(self.container55,text="55 - Tipo de amostra:", font=self.fontePadrao)
        self.tipoAmostraLabel.pack(side=LEFT)
  
        self.tipoAmostra = Entry(self.container55)
        self.tipoAmostra["width"] = 12
        self.tipoAmostra["font"] = self.fontePadrao
        self.tipoAmostra.pack(side=LEFT)

        self.tipoAmostraInfoLabel = Label(self.container55,text="(1-Secreção de Naso-orofaringe 2-Lavado Broco-alveolar 3-Tecido Post-mortem 4-Outra 9-Ignorado)", font=self.fontePadrao)
        self.tipoAmostraInfoLabel.pack(side=LEFT)

        self.outrAmostraLabel = Label(self.container55,text="  Se outra, qual?", font=self.fontePadrao)
        self.outrAmostraLabel.pack(side=LEFT)
  
        self.outrAmostra = Entry(self.container55)
        self.outrAmostra["width"] = 12
        self.outrAmostra["font"] = self.fontePadrao
        self.outrAmostra.pack(side=LEFT)

# João Victor

# João Pedro

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

        self.lbl_56 = Label(self.container2)
        self.lbl_56['text'] = '56 - Nº Requisição do GAL'
        self.lbl_56.pack(side=LEFT)

        self.txt_56 = Entry(self.container2)
        self.txt_56['width'] = 100
        self.txt_56.pack(side=LEFT) 

        self.container3 = Frame(dados_laboratoriais)
        self.container3['padx'] = 10
        self.container3['pady'] = 8
        self.container3.pack()

        self.lbl_57 = Label(self.container3)
        self.lbl_57['text'] = '57 - Resultado da IF/outro método que não seja biologia molecular:'
        self.lbl_57.pack(side=LEFT)

        self.lbl_57_opcoes = Label(self.container3)
        self.lbl_57_opcoes['text'] = '(1 - Positivo, 2 - Negativo, 3 - Inconclusivo, 4 - Não realizado, 5 - Aguardando resultado, 9 - Ignorado):'
        self.lbl_57_opcoes.pack(side=LEFT)

        self.txt_57 = Entry(self.container3)
        self.txt_57['width'] = 2
        self.txt_57.pack(side=LEFT)

        self.container4 = Frame(dados_laboratoriais)
        self.container4['padx'] = 10
        self.container4['pady'] = 8
        self.container4.pack()

        self.lbl_58 = Label(self.container4)
        self.lbl_58['text'] = '58 - Data do resultado da IF/outro método que não seja Biologia Molecular:'
        self.lbl_58.pack(side=LEFT)

        self.txt_58 = Entry(self.container4)
        self.txt_58['width'] = 15
        self.txt_58.pack(side=LEFT)

        self.container5 = Frame(dados_laboratoriais)
        self.container5['padx'] = 10
        self.container5['pady'] = 8
        self.container5.pack()

        self.lbl_59_title = Label(self.container5)
        self.lbl_59_title['text'] = '59 - Agente Etiológico - IF/outro método que não seja Biologia Molecular:'
        self.lbl_59_title.pack(side=LEFT)

        self.lbl_59_1 = Label(self.container5)
        self.lbl_59_1['text'] = 'Positivo para influenza? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lbl_59_1.pack(side=LEFT)

        self.txt_59_1 = Entry(self.container5)
        self.txt_59_1['width'] = 2
        self.txt_59_1.pack(side=LEFT)

        self.lbl_59_2 = Label(self.container5)
        self.lbl_59_2['text'] = 'Positivo para outro vírus? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lbl_59_2.pack(side=LEFT)

        self.txt_59_2 = Entry(self.container5)
        self.txt_59_2['width'] = 2
        self.txt_59_2.pack(side=LEFT)

        self.container6 = Frame(dados_laboratoriais)
        self.container6['padx'] = 10
        self.container6['pady'] = 8
        self.container6.pack()

        self.lbl_59_3 = Label(self.container6)
        self.lbl_59_3['text'] = 'Se outro vírus respiratórios qual(is)? (Marcar X): '
        self.lbl_59_3.pack(side=LEFT)

        self.lbl_59_sinicial = Label(self.container6)
        self.lbl_59_sinicial['text'] = 'Virus Sincicial Respiratório:'
        self.lbl_59_sinicial.pack(side=LEFT)

        self.txt_59_sinicial = Entry(self.container6)
        self.txt_59_sinicial['width'] = 2
        self.txt_59_sinicial.pack(side=LEFT)

        self.lbl_59_parainfluenza_1 = Label(self.container6)
        self.lbl_59_parainfluenza_1['text'] = 'Parainfluenza 1:'
        self.lbl_59_parainfluenza_1.pack(side=LEFT)

        self.txt_59_parainfluenza_1 = Entry(self.container6)
        self.txt_59_parainfluenza_1['width'] = 2
        self.txt_59_parainfluenza_1.pack(side=LEFT)

        self.lbl_59_parainfluenza_2 = Label(self.container6)
        self.lbl_59_parainfluenza_2['text'] = 'Parainfluenza 2:'
        self.lbl_59_parainfluenza_2.pack(side=LEFT)

        self.txt_59_parainfluenza_2 = Entry(self.container6)
        self.txt_59_parainfluenza_2['width'] = 2
        self.txt_59_parainfluenza_2.pack(side=LEFT)

        self.lbl_59_parainfluenza_3 = Label(self.container6)
        self.lbl_59_parainfluenza_3['text'] = 'Parainfluenza 3:'
        self.lbl_59_parainfluenza_3.pack(side=LEFT)

        self.txt_59_parainfluenza_3 = Entry(self.container6)
        self.txt_59_parainfluenza_3['width'] = 2
        self.txt_59_parainfluenza_3.pack(side=LEFT)

        self.lbl_59_adenovirus = Label(self.container6)
        self.lbl_59_adenovirus['text'] = 'Adenovírus:'
        self.lbl_59_adenovirus.pack(side=LEFT)

        self.txt_59_adenovirus = Entry(self.container6)
        self.txt_59_adenovirus['width'] = 2
        self.txt_59_adenovirus.pack(side=LEFT)

        self.lbl_59_outro = Label(self.container6)
        self.lbl_59_outro['text'] = 'Outro vírus respiratório, especifique:'
        self.lbl_59_outro.pack(side=LEFT)

        self.txt_59_outro = Entry(self.container6)
        self.txt_59_outro['width'] = 15
        self.txt_59_outro.pack(side=LEFT)

        self.container7 = Frame(dados_laboratoriais)
        self.container7['padx'] = 10
        self.container7['pady'] = 8
        self.container7.pack()

        self.lbl_60_1 = Label(self.container7)
        self.lbl_60_1['text'] = '60 - Laboratório que realizou IF/outro método que não seja biologia molecular:'
        self.lbl_60_1.pack(side=LEFT)

        self.txt_60_1 = Entry(self.container7)
        self.txt_60_1['width'] = 15
        self.txt_60_1.pack(side=LEFT)

        self.lbl_60_2 = Label(self.container7)
        self.lbl_60_2['text'] = 'Código (CNES):'
        self.lbl_60_2.pack(side=LEFT)

        self.txt_60_2 = Entry(self.container7)
        self.txt_60_2['width'] = 10
        self.txt_60_2.pack(side=LEFT)

        self.container8 = Frame(dados_laboratoriais)
        self.container8['padx'] = 10
        self.container8['pady'] = 8
        self.container8.pack()

        self.lbl_61 = Label(self.container8)
        self.lbl_61['text'] = '61 - Resultado da RT-PCR/outro método por Biologia Molecular: (1 - Detectável, 2 - Não detectável, 3 - Inconclusivo, 4 - Não realizado, 5 - Aguardando resultado, 9 - Ignorado)'
        self.lbl_61.pack(side=LEFT)

        self.txt_61 = Entry(self.container8)
        self.txt_61['width'] = 2
        self.txt_61.pack(side=LEFT)

        self.container9 = Frame(dados_laboratoriais)
        self.container9['padx'] = 10
        self.container9['pady'] = 8
        self.container9.pack()

        self.lbl_62 = Label(self.container9)
        self.lbl_62['text'] = '62 - Data do resultado RT-PCR/Outro métdodo por Biologia Molecular:'
        self.lbl_62.pack(side=LEFT)

        self.txt_62 = Entry(self.container9)
        self.txt_62['width'] = 15
        self.txt_62.pack(side=LEFT)

        self.container10 = Frame(dados_laboratoriais)
        self.container10['padx'] = 10
        self.container10['pady'] = 8
        self.container10.pack()

        self.lbl_63_1 = Label(self.container10)
        self.lbl_63_1['text'] = ('63 - Agente Etiológico - RT-PCR/outro método por Biologia Molecular '+
            '(1 - Sim, 2 - Não, 9 - Ignorado): ')
        self.lbl_63_1.pack(side=LEFT)

        self.txt_63_1 = Entry(self.container10)
        self.txt_63_1['width'] = 2
        self.txt_63_1.pack(side=LEFT)

        self.lbl_63_2 = Label(self.container10)
        self.lbl_63_2['text'] = 'Se sim, qual influenza? (1 - Influenza A, 2 - Influenza B):'
        self.lbl_63_2.pack(side=LEFT)

        self.txt_63_2 = Entry(self.container10)
        self.txt_63_2['width'] = 2
        self.txt_63_2.pack(side=LEFT)

        self.container11 = Frame(dados_laboratoriais)
        self.container11['padx'] = 10
        self.container11['pady'] = 8
        self.container11.pack()   

        self.lbl_63_3 = Label(self.container11)
        self.lbl_63_3['text'] = ('Influenza A, qual subtipo? '+
            '(1 - Influenza A(H1N1)pdm09, 2 - Influenza A/H3N2, '+
            '3 - Influenza A não subtipado, 4 - Influenza A não subtipável, '+
            '5 - Inconclusivo, 6 - Outro, especifique):')
        self.lbl_63_3.pack(side=LEFT)

        self.txt_63_3 = Entry(self.container11)
        self.txt_63_3['width'] = 10
        self.txt_63_3.pack(side=LEFT)

        self.container12 = Frame(dados_laboratoriais)
        self.container12['padx'] = 10
        self.container12['pady'] = 8
        self.container12.pack()

        self.lbl_63_4 = Label(self.container12)
        self.lbl_63_4['text'] = ('Influenza B, qual subtipo? '+
            '(1 - Victoria, 2 - Yamagatha, 3 - Não realizado, 4 - Inconclusivo, 5 - Outro, especifique):'
        )
        self.lbl_63_4.pack(side=LEFT)

        self.txt_63_4 = Entry(self.container12)
        self.txt_63_4['width'] = 10
        self.txt_63_4.pack(side=LEFT)

        self.lbl_63_5 = Label(self.container12)
        self.lbl_63_5['text'] = 'Positivo para outro vírus? (1 - Sim, 2 - Não, 9 - Ignorado):'
        self.lbl_63_5.pack(side=LEFT)

        self.txt_63_5 = Entry(self.container12)
        self.txt_63_5['width'] = 2
        self.txt_63_5.pack(side=LEFT)

        self.container13 = Frame(dados_laboratoriais)
        self.container13['padx'] = 10
        self.container13['pady'] = 8
        self.container13.pack()

        self.lbl_63_6_titulo = Label(self.container13)
        self.lbl_63_6_titulo['text'] = ('Se outros vírus respiratórios, qual (is)? (Marcar X): ')

        self.lbl_63_6_sarscov2 = Label(self.container13)
        self.lbl_63_6_sarscov2['text'] = 'SARS-CoV-2:'
        self.lbl_63_6_sarscov2.pack(side=LEFT)

        self.txt_63_6_sarscov2 = Entry(self.container13)
        self.txt_63_6_sarscov2['width'] = 2
        self.txt_63_6_sarscov2.pack(side=LEFT)

        self.lbl_63_6_sinicial = Label(self.container13)
        self.lbl_63_6_sinicial['text'] = 'Vírus Sincicial Respiratório: '
        self.lbl_63_6_sinicial.pack(side=LEFT)

        self.txt_63_6_sinicial = Entry(self.container13)
        self.txt_63_6_sinicial['width'] = 2
        self.txt_63_6_sinicial.pack(side=LEFT)

        self.lbl_63_6_parainfluenza_1 = Label(self.container13)
        self.lbl_63_6_parainfluenza_1['text'] = 'Parainfluenza 1: '
        self.lbl_63_6_parainfluenza_1.pack(side=LEFT)

        self.txt_63_6_parainfluenza_1 = Entry(self.container13)
        self.txt_63_6_parainfluenza_1['width'] = 2
        self.txt_63_6_parainfluenza_1.pack(side=LEFT)

        self.lbl_63_6_parainfluenza_2 = Label(self.container13)
        self.lbl_63_6_parainfluenza_2['text'] = 'Parainfluenza 2: '
        self.lbl_63_6_parainfluenza_2.pack(side=LEFT)

        self.txt_63_6_parainfluenza_2 = Entry(self.container13)
        self.txt_63_6_parainfluenza_2['width'] = 2
        self.txt_63_6_parainfluenza_2.pack(side=LEFT)

        self.lbl_63_6_parainfluenza_3 = Label(self.container13)
        self.lbl_63_6_parainfluenza_3['text'] = 'Parainfluenza 3: '
        self.lbl_63_6_parainfluenza_3.pack(side=LEFT)

        self.txt_63_6_parainfluenza_3 = Entry(self.container13)
        self.txt_63_6_parainfluenza_3['width'] = 2
        self.txt_63_6_parainfluenza_3.pack(side=LEFT)

        self.lbl_63_6_parainfluenza_4 = Label(self.container13)
        self.lbl_63_6_parainfluenza_4['text'] = 'Parainfluenza 4: '
        self.lbl_63_6_parainfluenza_4.pack(side=LEFT)

        self.txt_63_6_parainfluenza_4 = Entry(self.container13)
        self.txt_63_6_parainfluenza_4['width'] = 2
        self.txt_63_6_parainfluenza_4.pack(side=LEFT)

        self.lbl_63_6_adenovirus = Label(self.container13)
        self.lbl_63_6_adenovirus['text'] = 'Adenovírus: '
        self.lbl_63_6_adenovirus.pack(side=LEFT)

        self.txt_63_6_adenovirus = Entry(self.container13)
        self.txt_63_6_adenovirus['width'] = 2
        self.txt_63_6_adenovirus.pack(side=LEFT)

        self.lbl_63_6_metapneumovirus = Label(self.container13)
        self.lbl_63_6_metapneumovirus['text'] = 'Metapneumovírus: '
        self.lbl_63_6_metapneumovirus.pack(side=LEFT)

        self.txt_63_6_metapneumovirus = Entry(self.container13)
        self.txt_63_6_metapneumovirus['width'] = 2
        self.txt_63_6_metapneumovirus.pack(side=LEFT)

        self.lbl_63_6_bocavirus = Label(self.container13)
        self.lbl_63_6_bocavirus['text'] = 'Bocavírus: '
        self.lbl_63_6_bocavirus.pack(side=LEFT)

        self.txt_63_6_bocavirus = Entry(self.container13)
        self.txt_63_6_bocavirus['width'] = 2
        self.txt_63_6_bocavirus.pack(side=LEFT)

        self.lbl_63_6_rinovirus = Label(self.container13)
        self.lbl_63_6_rinovirus['text'] = 'Rinovírus: '
        self.lbl_63_6_rinovirus.pack(side=LEFT)

        self.txt_63_6_rinovirus = Entry(self.container13)
        self.txt_63_6_rinovirus['width'] = 2
        self.txt_63_6_rinovirus.pack(side=LEFT)

        self.lbl_63_6_outro = Label(self.container13)
        self.lbl_63_6_outro['text'] = 'Outro vírus respiratório, especifique: '
        self.lbl_63_6_outro.pack(side=LEFT)

        self.txt_63_6_outro = Entry(self.container13)
        self.txt_63_6_outro['width'] = 10
        self.txt_63_6_outro.pack(side=LEFT)

        self.container14 = Frame(dados_laboratoriais)
        self.container14['padx'] = 10
        self.container14['pady'] = 8
        self.container14.pack()

        self.lbl_64_1 = Label(self.container14)
        self.lbl_64_1['text'] = '64 - Laboratório que realizou RT-PCR/outro método por biologia molecular: '
        self.lbl_64_1.pack(side=LEFT)

        self.txt_64_1 = Entry(self.container14)
        self.txt_64_1['width'] = 25
        self.txt_64_1.pack(side=LEFT)

        self.lbl_64_2 = Label(self.container14)
        self.lbl_64_2['text'] = 'Código (CNES): '
        self.lbl_64_2.pack(side=LEFT)

        self.txt_64_2 = Entry(self.container14)
        self.txt_64_2['width'] = 15
        self.txt_64_2.pack(side=LEFT)

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

        self.lbl_65_1 = Label(self.container2)
        self.lbl_65_1['text'] = ('65 - Classificação final do caso) '+
            '(1 - SRAG por influenza, 2 - SRAG por vírus respiratório, '+
            '3 - SRAG por outro agente etiológico (especifique), '+
            '4 - SRAG não especificado, 5 - COVID-19): ')
        self.lbl_65_1.pack(side=LEFT)

        self.txt_65_1 = Entry(self.container2)
        self.txt_65_1['width'] = 15
        self.txt_65_1.pack(side=LEFT)

        self.container3 = Frame(conclusao_final)
        self.container3['padx'] = 10
        self.container3['pady'] = 8
        self.container3.pack()

        self.lbl_66 = Label(self.container3)
        self.lbl_66['text'] = ('66 - Critério de Encerramento: '+
            '(1 - Laboratorial, 2 - Vínculo-Epidemiológico, 3 - Clínico): ')
        self.lbl_66.pack(side=LEFT)

        self.txt_66 = Entry(self.container3)
        self.txt_66['width'] = 2
        self.txt_66.pack(side=LEFT)

        self.lbl_67 = Label(self.container3)
        self.lbl_67['text'] = '67 - Evolução do caso: (1 - Cura, 2 - Óbito, 3 - Ignorado): '
        self.lbl_67.pack(side=LEFT)

        self.txt_67 = Entry(self.container3)
        self.txt_67['width'] = 2
        self.txt_67.pack(side=LEFT)

        self.container4 = Frame(conclusao_final)
        self.container4['padx'] = 10
        self.container4['pady'] = 8
        self.container4.pack()

        self.lbl_68 = Label(self.container4)
        self.lbl_68['text'] = 'Data de alta ou óbito'
        self.lbl_68.pack(side=LEFT)

        self.txt_68 = Entry(self.container4)
        self.txt_68['width'] = 8
        self.txt_68.pack(side=LEFT)

        self.lbl_69 = Label(self.container4)
        self.lbl_69['text'] = 'Data do encerramento'
        self.lbl_69.pack(side=LEFT)
        
        self.txt_69 = Entry(self.container4)
        self.txt_69['width'] = 8
        self.txt_69.pack(side=LEFT)

        self.container5 = Frame(conclusao_final)
        self.container5['padx'] = 10
        self.container5['pady'] = 8
        self.container5.pack()

        self.lbl_70 = Label(self.container5)
        self.lbl_70['text'] = 'Observações'
        self.lbl_70.pack(side=LEFT)

        self.txt_70 = Entry(self.container5)
        self.txt_70.pack(side=LEFT)

# João Pedro

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
