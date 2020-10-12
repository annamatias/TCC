from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTableView, QTableWidget, QPushButton
from PyQt5 import uic
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "teste"

)



def chama_tela_cadastro():
    tela_cadastro.show()

def chama_tela_editar():
    tela_editarEstoque.show()

def chama_tela_estoque():
    tela_estoque.show()
    

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  produtos"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()
    print(dados)

    tela_estoque.tableWidget.setRowCount(len(dados))
    tela_estoque.tableWidget.setColumnCount(8)

    for i in range(0, len(dados)):
        for j in range(0, 8):
            tela_estoque.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))
            

def cadastro():
    linha1 = tela_cadastro.lineEdit_NomeProduto.text()
    linha2 = tela_cadastro.lineEdit_Ean.text()
    linha3 = tela_cadastro.lineEdit_Estoque.text()
    linha4 = tela_cadastro.lineEdit_Preco.text()
    linha5 = tela_cadastro.lineEdit_Altura.text()
    linha6 = tela_cadastro.lineEdit_Largura.text()
    linha7 = tela_cadastro.lineEdit_Descricao.text()


    cursor = banco.cursor()
    comando_SQL = "INSERT INTO Produtos (Nome,EAN,Estoque,Preço,Altura,Largura,Descrição) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6),  str(linha7))
    cursor.execute(comando_SQL, dados)
    banco.commit()


    tela_cadastro.lineEdit_NomeProduto.setText("")
    tela_cadastro.lineEdit_Ean.setText("")
    tela_cadastro.lineEdit_Estoque.setText("")
    tela_cadastro.lineEdit_Preco.setText("")
    tela_cadastro.lineEdit_Altura.setText("")
    tela_cadastro.lineEdit_Largura.setText("")
    tela_cadastro.lineEdit_Descricao.setText("")

def pesquisar():

   
    linha = tela_editarEstoque.lineEdit_Ean.text()
   

    cursor = banco.cursor()
    comando_SQL = "SELECT * FROM  produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados1 = cursor.fetchall()
    print(dados1)

    tela_editarEstoque.lineEdit_NomeProduto.setText(dados1[0][1])
    tela_editarEstoque.lineEdit_Estoque.setText(dados1[0][3])
    tela_editarEstoque.lineEdit_Preco.setText(str(dados1[0][4]))
    tela_editarEstoque.lineEdit_Altura.setText(dados1[0][5])
    tela_editarEstoque.lineEdit_Largura.setText(dados1[0][6])
    tela_editarEstoque.lineEdit_Descricao.setText(dados1[0][7])


def editar():
    linha1 = tela_editarEstoque.lineEdit_NomeProduto.text()
    linha2 = tela_editarEstoque.lineEdit_Estoque.text()
    linha3 = tela_editarEstoque.lineEdit_Preco.text()
    linha4 = tela_editarEstoque.lineEdit_Altura.text()
    linha5 = tela_editarEstoque.lineEdit_Largura.text()
    linha6 = tela_editarEstoque.lineEdit_Descricao.text()
    linha7 = tela_editarEstoque.lineEdit_Ean.text()

    cursor = banco.cursor()
    comando_SQL = "UPDATE produtos SET Nome = (%s), Estoque = (%s), Preço = (%s), Altura = (%s), Largura = (%s), Descrição = (%s) WHERE EAN = (%s)"
    dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6),  str(linha7))
    cursor.executemany(comando_SQL, (dados,))
    banco.commit()

    tela_editarEstoque.lineEdit_NomeProduto.setText("")
    tela_editarEstoque.lineEdit_Ean.setText("")
    tela_editarEstoque.lineEdit_Estoque.setText("")
    tela_editarEstoque.lineEdit_Preco.setText("")
    tela_editarEstoque.lineEdit_Altura.setText("")
    tela_editarEstoque.lineEdit_Largura.setText("")
    tela_editarEstoque.lineEdit_Descricao.setText("")


def deletar():
    linha = tela_editarEstoque.lineEdit_Ean.text()

    cursor = banco.cursor()
    comando_SQL = "DELETE FROM produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    banco.commit()

    print("Produto Deletado:", linha)

    tela_editarEstoque.lineEdit_Ean.setText("")
    tela_editarEstoque.lineEdit_NomeProduto.setText("")
    tela_editarEstoque.lineEdit_Estoque.setText("")
    tela_editarEstoque.lineEdit_Preco.setText("")
    tela_editarEstoque.lineEdit_Altura.setText("")
    tela_editarEstoque.lineEdit_Largura.setText("")
    tela_editarEstoque.lineEdit_Descricao.setText("")

def Caixa():
    tela_caixa.show()

    linha = tela_caixa.lineEdit.text()

    cursor = banco.cursor()
    comando_SQL = "SELECT Nome, EAN, Preço FROM produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados = cursor.fetchall()
    

    print(dados)
    

    tela_caixa.tableWidget.setRowCount(len(dados))
    tela_caixa.tableWidget.setColumnCount(3)

    for i in range(0, len(dados)):
        for j in range(0, 3):
            tela_caixa.tableWidget.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))
            


app = QtWidgets.QApplication([])
menu = uic.loadUi("Menu.ui")
tela_caixa = uic.loadUi("Caixa.ui")
tela_cadastro = uic.loadUi("Cadastro_Produto.ui")
tela_estoque = uic.loadUi("Estoque.ui")
tela_deletarProduto = uic.loadUi("Deletar_Produto.ui")
tela_editarEstoque = uic.loadUi("Estoque_Editar.ui")

tela_cadastro.pushButton.clicked.connect(cadastro)
tela_editarEstoque.pushButton_deletar.clicked.connect(deletar)
tela_caixa.pushButton.clicked.connect(Caixa)
tela_editarEstoque.pushButton_pesquisar.clicked.connect(pesquisar)
tela_editarEstoque.pushButton_editar.clicked.connect(editar)

menu.actionProduto.triggered.connect(chama_tela_cadastro)
menu.actionEstoque.triggered.connect(chama_tela_estoque)
menu.actionCaixa.triggered.connect(Caixa)
menu.actionEditar_Estoque.triggered.connect(chama_tela_editar)


menu.show()
app.exec()