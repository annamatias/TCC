from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTableView, QTableWidget, QPushButton
from PyQt5 import uic
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "realizar_orcamento"
    )

def chama_tela_orcamento_cliente():
    tela_orcamento_cliente.show()

def realizar_orcamento():
    linha1 = tela_orcamento_cliente.lineEdit_desc.text()
    linha2 = tela_orcamento_cliente.spinBox_uni.text()
    linha3 = tela_orcamento_cliente.spinBox_qtd.text()
    linha4 = tela_orcamento_cliente.lineEdit_lista.text()
    linha5 = tela_orcamento_cliente.spinBox_desconto.text()
    linha6 = tela_orcamento_cliente.lineEdit_unid.text()
    linha7 = tela_orcamento_cliente.lineEdit_total.text()
    linha8 = tela_orcamento_cliente.lineEdit_frete.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO realizar_orcamento (Descricao_Produto, Unidade, Qtd, Preco_lista, Desconto, Preco_uni, Preco_total, Frete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), int(linha2), int(linha3), float(linha4), int(linha5), float(linha6), float(linha7), float(linha8))
    cursor.execute(comando_SQL, dados)
    banco.commit()

def cadastro_Orcamento_Cliente():
    linha1 = tela_orcamento_cliente.lineEdit_NomeProduto.text()
    linha2 = tela_orcamento_cliente.spinBox_uni.value()
    linha3 = tela_orcamento_cliente.spinBox_qtd.value()
    linha4 = tela_orcamento_cliente.lineEdit_unid.text()
    linha5 = tela_orcamento_cliente.lineEdit_total.text()
    linha6 = tela_orcamento_cliente.lineEdit_frete.text()
    linha7 = tela_orcamento_cliente.spinBox_desconto.value()
    linha8 = tela_orcamento_cliente.lineEdit_desc.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO realizar_orcamento (Nome_Produto,Descrição_Produto,Unidade,Qtd,Desconto,Preco_uni,Preco_total,Frete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha1), str(linha8), str(linha2), str(linha3), str(linha7), str(linha4),  str(linha5), str(linha6))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    tela_orcamento_cliente.lineEdit_NomeProduto.setText("")
    tela_orcamento_cliente.spinBox_uni.setValue(0)
    tela_orcamento_cliente.spinBox_qtd.setValue(0)
    tela_orcamento_cliente.lineEdit_unid.setText("")
    tela_orcamento_cliente.lineEdit_total.setText("")
    tela_orcamento_cliente.lineEdit_frete.setText("")
    tela_orcamento_cliente.spinBox_desconto.setValue(0)
    tela_orcamento_cliente.lineEdit_desc.setText("")

    QMessageBox.about(tela_orcamento_cliente, "Aviso","Orçamento Cadastrado!")

def Orcamento_Cliente():
    tela_orcamento_cliente.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  realizar_orcamento"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    tela_orcamento_cliente.tableWidget_2.setRowCount(len(dados))
    tela_orcamento_cliente.tableWidget_2.setColumnCount(9)

    for i in range(0, len(dados)):
        for j in range(0, 9):
            tela_orcamento_cliente.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))



def visualizar_orcamentos():
    pass

app = QtWidgets([])
menu = uic.loadUi("Menu.ui")
menu.orcamento_cliente.triggered.connect(chama_tela_orcamento_cliente)

tela_orcamento_cliente = uic.loadUi("Realizar_Orcamento_Cliente_Empresa.ui")
tela_orcamento_cliente.show()
app.exec()

"""
Feito:

Interface da realização e visualização de orçamento.
Código fonte .py para execução das funcionalidades.
Criação da tabala no banco "realizar orçamento".
Integração com o banco "realizar orçamento".

Falta:

Condições para o botão de calcular orçamento e o botão criar orçamento.
Necessário da criação de função para visualização de orçamentos.
Necessário a criação de função para pesquisa na descrição do produto e a integração com a tabela de produtos.
"""

def editar():
    linha  = tela_OrcamentoEditar.lineEdit_Codigo.text()
    linha1 = tela_OrcamentoEditar.lineEdit_DescProduto.text()
    linha2 = tela_OrcamentoEditar.lineEdit_Unidade.text()
    linha3 = tela_OrcamentoEditar.lineEdit_Qtd.text()
    linha4 = tela_OrcamentoEditar.lineEdit_Preco.text()
    linha5 = tela_OrcamentoEditar.lineEdit_Desconto.text()
    linha6 = tela_OrcamentoEditar.lineEdit_PrecoUnidade.text()
    linha7 = tela_OrcamentoEditar.lineEdit_Frete.text()

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO realizar_orcamento (Codigo_Produto,Nome_Produto,Unidade,Qtd,Desconto,Preco_uni,Preco_total,Frete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    dados = (str(linha),str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6),  str(linha7), str(linha8))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    tela_orcamento_cliente.lineEdit_Codigo.setText("")
    tela_orcamento_cliente.lineEdit_NomeProduto.setText("")
    tela_orcamento_cliente.spinBox_uni.setValue(0)
    tela_orcamento_cliente.spinBox_qtd.setValue(0)
    tela_orcamento_cliente.lineEdit_unid.setText("")
    tela_orcamento_cliente.lineEdit_total.setText("")
    tela_orcamento_cliente.lineEdit_frete.setText("")
    tela_orcamento_cliente.spinBox_desconto.setValue(0)
    tela_orcamento_cliente.lineEdit_desc.setText("")

    if cursor.executemany() == True:
        QMessageBox.about(tela_orcamento_cliente, "Aviso","Orçamento Editado!")
    else:
        QMessageBox.about(tela_orcamento_cliente, "Aviso","Campos vazios ou preenchidos incorretamente!")


def deletar():
    try: 
        linha = tela_orcamento_cliente.lineEdit_Codigo.setText()
        if linha != "":
            cursor = banco.cursor()
            comando_SQL = "DELETE FROM realizar_orcamento WHERE Codigo = (%s)"
            dados = (str(linha))
            cursor.execute(comando_SQL, (dados,))
            banco.commit()

            
            tela_orcamento_cliente.lineEdit_Codigo.setText("")
            tela_orcamento_cliente.lineEdit_NomeProduto.setText("")
            tela_orcamento_cliente.spinBox_uni.setValue(0)
            tela_orcamento_cliente.spinBox_qtd.setValue(0)
            tela_orcamento_cliente.lineEdit_unid.setText("")
            tela_orcamento_cliente.lineEdit_total.setText("")
            tela_orcamento_cliente.lineEdit_frete.setText("")
            tela_orcamento_cliente.spinBox_desconto.setValue(0)
            tela_orcamento_cliente.lineEdit_desc.setText("")
            QMessageBox.about(tela_orcamento_cliente, "Aviso","Orçamento Apagado!")
        
        else:
            QMessageBox.about(tela_orcamento_cliente, "Aviso","Revise os campos!")

    except Exception:    
            QMessageBox.about(tela_orcamento_cliente, "Aviso","Ocorreu um erro, revise os campos e tente novamente!")