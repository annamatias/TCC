import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QToolTip

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.topo = 100
        self.esquerda = 100
        self.largura = 800
        self.altura = 600
        self.titulo = "Menu"

        #botões
        botao_produtos = QPushButton("Produtos", self)
        botao_produtos.move(50,50) #espaço esquerda base, topo
        botao_produtos.resize(200,100) #base,altura
        botao_produtos.setStyleSheet('QPushButton {font:bold;font-size:20px}')
        #botao_produtos.setStyleSheet('QPushButton {background-color:#78849D;font:bold;font-size:20px}')
        botao_produtos.clicked.connect(self.botao_produtosjanela)

        self.CarregarJanela()

    def CarregarJanela(self):
        self.setGeometry(self.esquerda, self.topo, self.largura, self.altura)
        self.setWindowTitle(self.titulo)
        #self.setWindowIcon(self.QWidget, QIcon="menu_home.jpn")
        self.show()

    def botao_produtosjanela(self):
        print("botão funcionando")

        #criação de janela de produtos com suas funções.



aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec())
