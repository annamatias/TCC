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

def salvar():
    dado_salvo = [Orcamento_Papelaria.lineEdit_4.text(), Orcamento_Papelaria.lineEdit_7.text(), Orcamento_Papelaria.comboBox.currentText(), Orcamento_Papelaria.lineEdit_10.text(), Orcamento_Papelaria.lineEdit_6.text(), Orcamento_Papelaria.lineEdit.text()]

    cursor = banco.cursor()
    comando_SQL = "INSERT INTO Formulario (DescricaoConta, Valor, Situacao, Data, Observacao, ValTotal) VALUES (%s,%s,%s,%s,%s,%s)"
    dados = (str(dado_salvo[0]), int(dado_salvo[1]), str(dado_salvo[2]), date(dado_salvo[3]), str(dado_salvo[4]), int(dado_salvo[5]))
    cursor.execute(comando_SQL, dados)
    banco.commit()

    Orcamento_Papelaria.lineEdit_4.setText("")
    Orcamento_Papelaria.lineEdit_7.setText("")
    Orcamento_Papelaria.lineEdit_10.setText("")
    Orcamento_Papelaria.lineEdit_6.setText("")
    Orcamento_Papelaria.lineEdit.setText("")

def apagar():

    pass


def editar():

    pass


app = QtWidgets.QApplication([])
Orcamento_Papelaria = uic.loadUi("Orcamento_Papelaria.ui")
Orcamento_Papelaria.pushButton.clicked.connect(salvar)
Orcamento_Papelaria.comboBox.addItem("Pendente")
Orcamento_Papelaria.comboBox.addItem("Pago")
Orcamento_Papelaria.comboBox.addItem("Pago com atraso")


Orcamento_Papelaria.show()
app.exec()