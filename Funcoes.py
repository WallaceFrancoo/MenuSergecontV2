# Aqui estará nossas funções -> Ao clicar em cada botão estará aqui o que cada um vai fazer!

import socket

maquina = socket.gethostname()


def botao1():
    print(f"Olá aqui será a calculadora!\n{maquina}")
def REINF():
    print("Aqui será o progama da REINF")

def clicado(event):
    event.widget.config(width=16,height=5, bg='#B22222')

# Função chamada quando o botão é liberado
def soltou(event):
    event.widget.config(width=15,height=4)