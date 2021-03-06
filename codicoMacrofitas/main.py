# -*- coding: utf-8 -*-
import Worker as wk
from OperacoesArquivo import Reader
from tkinter import (Tk, Button, Frame, filedialog, Label, Listbox, Checkbutton, IntVar)
import threading
import openpyxl

class Mensagem:

    def __init__(self, master=None, mensagem='Erro'):
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text=mensagem)
        self.msg["font"] = ("Calibri", "13", "bold")
        self.msg.pack ()

        self.sair = Button(self.widget1)
        self.sair["text"] = "OK"
        self.sair["font"] = ("Calibri", "13")
        self.sair["width"] = 10
        self.sair['command'] = self.widget1.quit
        self.sair.pack()

# TELA PRINCIPAL
class Menu:

    def __init__(self, master=None):
        self.master = master

        self.nomeArquivo = None

        # criando os conteiners
        self.conteinerFile = Frame(master)
        self.conteiner1 = Frame(master)
        self.conteiner2 = Frame(master)
        self.conteiner3 = Frame(master)
        self.conteiner4 = Frame(master)
        self.conteiner5 = Frame(master)
        self.conteiner0 = Frame(master)
        self.conteinerCB = Frame(master)    # container checkbox

        self.conteinerFile.pack()
        self.conteiner1.pack()
        self.conteiner2.pack()
        self.conteiner3.pack()
        self.conteiner4.pack()
        self.conteiner5.pack()
        self.conteiner0.pack()
        self.conteinerCB.pack()

        self.botaoFile = self.criaBotao(self.conteinerFile, 'Escolha um arquivo', self.getFile)
        self.botao1 = self.criaBotao(self.conteiner1, 'Validar nomes', self.release1)
        self.botao2 = self.criaBotao(self.conteiner2, 'Gerar lista de sinônimos', self.release2)
        self.botao3 = self.criaBotao(self.conteiner3, 'Gerar informações', self.release3)
        self.botao4 = self.criaBotao(self.conteiner4, 'Gerar coordenadas geográficas', self.release4)
        self.botao5 = self.criaBotao(self.conteiner5, 'Todas as operações.', self.todasReleases)
        self.botao0 = self.criaBotao(self.conteiner0, 'Sair', None)
        self.botao0['command'] = self.conteiner0.quit

        # distanciando verticalmente
        self.botaoFile.grid(row=0, column=0, pady=(3, 10))
        self.botao1.grid(row=1, column=0, pady=(3, 10))
        self.botao2.grid(row=2, column=0, pady=(3, 10))
        self.botao3.grid(row=3, column=0, pady=(3, 10))
        self.botao4.grid(row=4, column=0, pady=(3, 10))
        self.botao5.grid(row=5, column=0, pady=(3, 10))
        self.botao0.grid(row=6, column=0, pady=(3, 10))

        # finalizando a configuração dos botões
        self.botaoFile.pack()
        self.botao1.pack()
        self.botao2.pack()
        self.botao3.pack()
        self.botao4.pack()
        self.botao5.pack()
        self.botao0.pack()

        # cria a lista mas não deixa visivel
        # 37 - quantidade de linhas
        self.lista = Listbox(self.master, height=37, width=120, bd=10, font=("Times", 16))
        #self.lista.pack()

        # quando for realizar todas as operações, não voltar os botões depois de cada uma
        self.naoVoltar = False

        # checkbox para escolher o auto-confirma
        autoconfirm = IntVar()
        c = Checkbutton(self.conteinerCB, text="AUTO-CONFIRMA após executar", variable=autoconfirm)
        c.grid(row=7, column=0, pady=(3, 10))
        c.bind('<Button-1>', self.cb)
        c.pack()

        self.AutoConfirma = False

    def criaBotao(self, conteiner, texto, funcao):
        botao = Button(conteiner, width=40, pady=10) # criando os botões
        botao['text'] = texto               # atribuindo nome
        botao.bind('<Button-1>', funcao)    # adicionando evento
        botao["font"] = ("Calibri", "13")   # fonte
        botao.pack()                        # salvando o botão

        return botao

    def cb(self, event):
        self.AutoConfirma = not self.AutoConfirma

    def escondeBotoes(self):
        self.conteinerFile.pack_forget()
        self.conteiner1.pack_forget()
        self.conteiner2.pack_forget()
        self.conteiner3.pack_forget()
        self.conteiner4.pack_forget()
        self.conteiner5.pack_forget()
        self.conteiner0.pack_forget()
        self.conteinerCB.pack_forget()

        self.lista.pack()

    def voltaBotoes(self):
        if self.naoVoltar:
            return

        self.conteinerFile.pack()
        self.conteiner1.pack()
        self.conteiner2.pack()
        self.conteiner3.pack()
        self.conteiner4.pack()
        self.conteiner5.pack()
        self.conteiner0.pack()
        self.conteinerCB.pack()

        self.lista.pack_forget()

    def getFile(self, event):
        self.nomeArquivo = filedialog.askopenfilename(initialdir = ".",title = "Selecione o arquivo",filetypes = (("Planilha","*.xlsx"),("Todos arquivos","*.*")))

        if self.nomeArquivo.__eq__(''):
            return

        try:
            wk.Reader(self.nomeArquivo)
        except openpyxl.utils.exceptions.InvalidFileException:
            threading.Thread(target=self.mensagemErro, args=('Arquivo não suportado.\nSelecione um arquivo \'.xlsx\'',)).start()

    def mensagemErro(self, msg='Selecione um arquivo usando o primeiro botão.'):
        # se não for marcado para auto confirmar, executa normal
        # em ambas as situações, vai pra função voltaBotoes
        if not self.AutoConfirma:
            mensagem = Tk()
            Mensagem(mensagem, msg)
            mensagem.title('Aviso')
            mensagem.mainloop()

        self.voltaBotoes()

    def release1(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            self.escondeBotoes()
            parametros = {'arquivoEntrada': self.nomeArquivo,
                          'funcaoRetorno': self.mensagemErro,
                          'msgRetorno': 'Arquivo de saída:.\n{0}',
                          'lista': self.lista,
                          'arquivoSaida': ''}
            threading.Thread(target=wk.release1, args=(parametros,)).start()

    def release2(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            self.escondeBotoes()
            parametros = {'arquivoEntrada': self.nomeArquivo,
                'funcaoRetorno': self.mensagemErro,
                'msgRetorno': 'Arquivo de saída:.\n{0}',
                'lista': self.lista,
                'arquivoSaida': ''}

            threading.Thread(target=wk.release2, args=(parametros,)).start()

    def release3(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            self.escondeBotoes()
            parametros = {
                'arquivoEntrada': self.nomeArquivo,
                'funcaoRetorno': self.mensagemErro,
                'msgRetorno': 'Arquivo de saída:.\n{0}',
                'lista': self.lista,
                'arquivoSaida': ''
                }

            threading.Thread(target=wk.release3, args=(parametros,)).start()
 
    def release4(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            self.escondeBotoes()
            parametros = {
                'arquivoEntrada': self.nomeArquivo,
                'funcaoRetorno': self.mensagemErro,
                'msgRetorno': 'Arquivo de saída:.\n{0}',
                'lista': self.lista,
                'arquivoSaida': ''}

            threading.Thread(target=wk.release4, args=(parametros,)).start()

    def todas(self, parametros):
        wk.release1(parametros)
        parametros['arquivoEntrada'] = parametros['arquivoSaida']   # pega o nome do novo arquivo

        wk.release2(parametros)
        # não precisa alterar o arquivo de entrada, pois vai ser o arquivo VALIDADO mesmo

        wk.release3(parametros)

        self.naoVoltar = False

        wk.release4(parametros)

    def todasReleases(self, event):
        if self.nomeArquivo.__eq__(''):
            threading.Thread(target=self.mensagemErro).start()
        else:
            self.escondeBotoes()
            self.naoVoltar = True   # não volta os botões depois de cada operação

            parametros = {'arquivoEntrada': self.nomeArquivo,
                'funcaoRetorno': self.mensagemErro,
                'msgRetorno': 'Arquivo de saída:.\n{0}',
                'lista': self.lista,
                'arquivoSaida': ''}

            threading.Thread(target=self.todas, args=(parametros,)).start()
            # tem que criar uma thread senão a interface trava do mesmo modo


root = Tk()
root.title('Macrofitas Mining')
root.geometry("800x600")
root.resizable(0, 0)
Menu(root)
root.mainloop()
