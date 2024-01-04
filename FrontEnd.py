import tkinter as tk
from tkinter import Button,Tk,Canvas
import Funcoes
import BancoDeDados
import socket

maquina = socket.gethostname()

janela = tk.Tk()
janela.title("Sergecont Contabilidade")
janela.geometry(f"385x265")
# Criando um frame para os dois primeiros botões
linha1 = tk.Frame(janela)
linha1.pack(pady=(15, 0), padx=(10, 10), anchor='nw')
# Criando um frame para os dois últimos botões
linha2 = tk.Frame(janela)
linha2.pack(pady=(15, 0), padx=(10, 10), anchor='nw')
#
linha3 = tk.Frame(janela)
linha3.pack(pady=(15, 0), padx=(10, 10), anchor='nw')

# Configurando o botão "Calculadora" dentro do frame_topo
botao1 = Button(linha1, text=BancoDeDados.NomeDesejado(maquina), command=Funcoes.botao1, width=15, height=4,bg=BancoDeDados.CorDesejada(maquina))
botao1.pack(side='left')
botao1.bind('<Button-1>', Funcoes.clicado)
botao1.bind('<ButtonRelease-1>', Funcoes.soltou)
# Configurando o botão "REINF" dentro do frame_topo
botao2 = Button(linha1, text="2", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao2.pack(side='left', padx=(10, 0))
botao2.bind('<Button-1>', Funcoes.clicado)
botao2.bind('<ButtonRelease-1>', Funcoes.soltou)
#
botao3 = Button(linha1, text="3", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao3.pack(side='left', padx=(10, 0))
botao3.bind('<Button-1>', Funcoes.clicado)
botao3.bind('<ButtonRelease-1>', Funcoes.soltou)
#
botao4 = Button(linha2, text="4", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao4.pack(side='left')
botao4.bind('<Button-1>', Funcoes.clicado)
botao4.bind('<ButtonRelease-1>', Funcoes.soltou)
#
botao5 = Button(linha2, text="5", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao5.pack(side='left', padx=(10, 0))
botao5.bind('<Button-1>', Funcoes.clicado)
botao5.bind('<ButtonRelease-1>', Funcoes.soltou)
#
botao6 = Button(linha2, text="6", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao6.pack(side='left', padx=(10, 0))
botao6.bind('<Button-1>', Funcoes.clicado)
botao6.bind('<ButtonRelease-1>', Funcoes.soltou)
#
botao7 = Button(linha3, text="7", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao7.pack(side='left')
botao7.bind('<Button-1>', Funcoes.clicado)
botao7.bind('<ButtonRelease-1>', Funcoes.soltou)
#
botao8 = Button(linha3, text="8", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao8.pack(side='left', padx=(10, 0))
botao8.bind('<Button-1>', Funcoes.clicado)
botao8.bind('<ButtonRelease-1>', Funcoes.soltou)
#
botao9 = Button(linha3, text="9", command=Funcoes.REINF, width=15, height=4,bg='#B22222')
botao9.pack(side='left', padx=(10, 0))
botao9.bind('<Button-1>', Funcoes.clicado)
botao9.bind('<ButtonRelease-1>', Funcoes.soltou)
#
janela.mainloop()