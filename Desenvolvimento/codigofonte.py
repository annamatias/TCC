from PyQt5 import uic, QtWidgets

def funcao_principal():
    #linha1 = cadastro_produto.lineEdit.text()
    print("teste")
    #print("código", linha1)

app = QtWidgets.QApplication([])
cadastro_produto = uic.loadUi("Cadastro_Produtos.ui")
#cadastro_produto.botao_salvar.clicked.connect(funcao_principal)

cadastro_produto.show()
app.exec()

'''
aplicacao = QApplication(sys.argv)
j = Janela()
sys.exit(aplicacao.exec())
'''