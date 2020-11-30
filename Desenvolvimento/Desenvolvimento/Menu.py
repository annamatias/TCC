from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMdiArea, QAction, QMdiSubWindow, QTableView, QTableWidget, QPushButton, QMessageBox
from PyQt5 import uic
import mysql.connector


banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "teste")

lista = []
lista2 = []


def chama_tela_Orcamento_Cliente():
    tela_orcamento_cliente.show()

def chama_login():
    primeira_tela.show()

def chama_tela_orcamento_editar():
    tela_OrcamentoEditar.show()

def limpa_tabela():
    tela_caixa.tableWidget.clear()

def limpa_lista():
    lista.clear()

def chama_tela_cadastro():
    tela_cadastro.show()

def chama_tela_editar():
    tela_editarEstoque.show()

def chama_tela_caixa():
    tela_caixa.show()

def chama_tela_estoque():
    tela_estoque.show()
    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  produtos"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    tela_estoque.tableWidget.setRowCount(len(dados))
    tela_estoque.tableWidget.setColumnCount(8)

    for i in range(0, len(dados)):
        for j in range(0, 8):
            tela_estoque.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))



def abre_tela_cadastro():
    tela_cadastro_usuario.show()

def chama_tela_excluirUsuario():
    tela_excluir_usuario.show()

def chama_tela_reset():
    tela_reset.show()
    

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
    comando_SQL = "INSERT INTO realizar_orcamento (Nome_Produto,Descrição_Produto,Unidade,Qtd,Desconto,Preco_uni,Preco_total,Frete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
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
    comando_SQL = "SELECT *FROM realizar_orcamento;"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    tela_orcamento_cliente.tableWidget_2.setRowCount(len(dados))
    tela_orcamento_cliente.tableWidget_2.setColumnCount(9)

    for i in range(0, len(dados)):
        for j in range(0, 9):
            tela_orcamento_cliente.tableWidget_2.setItem(i,j,QtWidgets.QTableWidgetItem(str(dados[i][j])))

def editar_orcamento():
    
    linha2 = tela_OrcamentoEditar.lineEdit_nome.text()
    linha3 = tela_OrcamentoEditar.lineEdit_DescProduto.text()
    linha4 = tela_OrcamentoEditar.lineEdit_Unidade.text()
    linha5 = tela_OrcamentoEditar.lineEdit_Qtd.text()
    linha6 = tela_OrcamentoEditar.lineEdit_Desconto.text()
    linha7 = tela_OrcamentoEditar.lineEdit_PrecoUnidade.text()
    linha8 = tela_OrcamentoEditar.lineEdit_Preco.text()
    linha9 = tela_OrcamentoEditar.lineEdit_Frete.text()


    cursor = banco.cursor()
    comando_SQL = "UPDATE realizar_orcamento SET Nome_Produto = (%s), Descricao_Produto = (%s), Unidade = (%s), Qtd = (%s), Desconto = (%s), Preco_uni = (%s), Preco_total = (%s), Frete = (%s) WHERE Codigo = (%s)"
    dados = (str(linha2), str(linha3), str(linha4), str(linha5), str(linha6), str(linha7),  str(linha8), str(linha9))
    cursor.executemany(comando_SQL, (dados))
    banco.commit()


    tela_OrcamentoEditar.lineEdit_Codigo.setText("")
    tela_OrcamentoEditar.lineEdit_nome.setText("")
    tela_OrcamentoEditar.lineEdit_DescProduto.setValue(0)
    tela_OrcamentoEditar.lineEdit_Unidade.setValue(0)
    tela_OrcamentoEditar.lineEdit_Qtd.setText("")
    tela_OrcamentoEditar.lineEdit_Desconto.setText("0%")
    tela_OrcamentoEditar.lineEdit_PrecoUnidade.setText(0)
    tela_OrcamentoEditar.lineEdit_Preco.setValue(0)
    tela_OrcamentoEditar.lineEdit_Frete.setText("")

    if cursor.executemany() == True:
        QMessageBox.about(tela_orcamento_cliente, "Aviso","Orçamento Editado!")
    else:
        QMessageBox.about(tela_orcamento_cliente, "Aviso","Campos vazios ou preenchidos incorretamente!")

def deletar_orcamento():
    try: 
        linha = tela_OrcamentoEditar.lineEdit_Codigo.text()
        if linha != "":
            cursor = banco.cursor()
            comando_SQL = "DELETE FROM realizar_orcamento WHERE Codigo = (%s);"
            dados = (str(linha))
            cursor.execute(comando_SQL, (dados,))
            banco.commit()

            tela_OrcamentoEditar.lineEdit_Codigo.setText("")
            tela_OrcamentoEditar.lineEdit_nome.setText("")
            tela_OrcamentoEditar.lineEdit_DescProduto.setText("")
            tela_OrcamentoEditar.lineEdit_Unidade.setText("")
            tela_OrcamentoEditar.lineEdit_Qtd.setText("")
            tela_OrcamentoEditar.lineEdit_Desconto.setText("")
            tela_OrcamentoEditar.lineEdit_PrecoUnidade.setText("")
            tela_OrcamentoEditar.lineEdit_Preco.setText("")
            tela_OrcamentoEditar.lineEdit_Frete.setText("")
            
            QMessageBox.about(tela_orcamento_cliente, "Aviso","Orçamento Apagado!")
        
        else:
            QMessageBox.about(tela_orcamento_cliente, "Aviso","Revise os campos!")

    except Exception:    
            QMessageBox.about(tela_orcamento_cliente, "Aviso","Ocorreu um erro, revise os campos e tente novamente!")


def pesquisar_orcamento():
    try:    
        linha = tela_OrcamentoEditar.lineEdit_Codigo.text()
    
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM realizar_orcamento WHERE Codigo = (%s);"
        dados = (str(linha))
        cursor.execute(comando_SQL, (dados,))
        dados1 = cursor.fetchall()

        tela_OrcamentoEditar.lineEdit_Codigo.setText(str(dados1[0][0]))
        tela_OrcamentoEditar.lineEdit_nome.setText(dados1[0][1])
        tela_OrcamentoEditar.lineEdit_DescProduto.setText(str(dados1[0][2]))
        tela_OrcamentoEditar.lineEdit_Unidade.setText(str(dados1[0][3]))
        tela_OrcamentoEditar.lineEdit_Qtd.setText(str(dados1[0][4]))
        tela_OrcamentoEditar.lineEdit_Desconto.setText(str(dados1[0][5]))
        tela_OrcamentoEditar.lineEdit_PrecoUnidade.setText(str(dados1[0][6]))
        tela_OrcamentoEditar.lineEdit_Preco.setText(str(dados1[0][7]))
        tela_OrcamentoEditar.lineEdit_Frete.setText(dados1[0][8])
    except IndexError:
        QMessageBox.about(tela_editarEstoque, "Aviso","Produto Não encontro!")




    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  produtos"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    tela_estoque.tableWidget.setRowCount(len(dados))
    tela_estoque.tableWidget.setColumnCount(8)

    for i in range(0, len(dados)):
        for j in range(0, 8):
            tela_estoque.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))


def cadastro():
    linha1 = tela_cadastro.lineEdit_NomeProduto.text()
    linha2 = tela_cadastro.lineEdit_Ean.text()
    linha3 = tela_cadastro.lineEdit_Estoque.text()
    linha4 = tela_cadastro.lineEdit_Preco.text()
    linha5 = tela_cadastro.lineEdit_Altura.text()
    linha6 = tela_cadastro.lineEdit_Largura.text()
    linha7 = tela_cadastro.lineEdit_Descricao.text()

    if linha1 == "" or linha2 == "" or linha3 == "":
        QMessageBox.about(tela_cadastro, "Aviso", "Campos Incorretos ou Vázios!")
    else:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO produtos (Nome,EAN,Estoque,Preco,Altura,Largura,Descricao) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6), str(linha7))
        cursor.execute(comando_SQL, dados)
        banco.commit()

        tela_cadastro.lineEdit_NomeProduto.setText("")
        tela_cadastro.lineEdit_Ean.setText("")
        tela_cadastro.lineEdit_Estoque.setText("")
        tela_cadastro.lineEdit_Preco.setText("")
        tela_cadastro.lineEdit_Altura.setText("")
        tela_cadastro.lineEdit_Largura.setText("")
        tela_cadastro.lineEdit_Descricao.setText("")

        QMessageBox.about(tela_cadastro, "Aviso", "Produto Cadastrado!")

def pesquisar():
    try:
        linha = tela_editarEstoque.lineEdit_Ean.text()

        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM  produtos WHERE EAN = (%s)"
        dados = (str(linha))
        cursor.execute(comando_SQL, (dados,))
        dados1 = cursor.fetchall()

        tela_editarEstoque.lineEdit_NomeProduto.setText(dados1[0][1])
        tela_editarEstoque.lineEdit_Estoque.setText(dados1[0][3])
        tela_editarEstoque.lineEdit_Preco.setText(str(dados1[0][4]))
        tela_editarEstoque.lineEdit_Altura.setText(dados1[0][5])
        tela_editarEstoque.lineEdit_Largura.setText(dados1[0][6])
        tela_editarEstoque.lineEdit_Descricao.setText(dados1[0][7])
    except IndexError:
        QMessageBox.about(tela_editarEstoque, "Aviso", "Produto Não encontrado!")


def editar():
    linha1 = tela_editarEstoque.lineEdit_NomeProduto.text()
    linha2 = tela_editarEstoque.lineEdit_Estoque.text()
    linha3 = tela_editarEstoque.lineEdit_Preco.text()
    linha4 = tela_editarEstoque.lineEdit_Altura.text()
    linha5 = tela_editarEstoque.lineEdit_Largura.text()
    linha6 = tela_editarEstoque.lineEdit_Descricao.text()
    linha7 = tela_editarEstoque.lineEdit_Ean.text()
    try:
        cursor = banco.cursor()
        comando_SQL = "UPDATE produtos SET Nome = (%s), Estoque = (%s), Preco = (%s), Altura = (%s), Largura = (%s), Descricao = (%s) WHERE EAN = (%s)"
        dados = (str(linha1), str(linha2), str(linha3), str(linha4), str(linha5), str(linha6), str(linha7))
        cursor.executemany(comando_SQL, (dados,))
        banco.commit()

        tela_editarEstoque.lineEdit_NomeProduto.setText("")
        tela_editarEstoque.lineEdit_Ean.setText("")
        tela_editarEstoque.lineEdit_Estoque.setText("")
        tela_editarEstoque.lineEdit_Preco.setText("")
        tela_editarEstoque.lineEdit_Altura.setText("")
        tela_editarEstoque.lineEdit_Largura.setText("")
        tela_editarEstoque.lineEdit_Descricao.setText("")
        QMessageBox.about(tela_editarEstoque, "Aviso", "Produto Editado!")
    except Exception:
        QMessageBox.about(tela_editarEstoque, "Aviso", "Campos vazios ou preenchidos incorretamente!")


def deletar():
    try:
        linha = tela_editarEstoque.lineEdit_Ean.text()
        if linha != "":
            cursor = banco.cursor()
            comando_SQL = "DELETE FROM produtos WHERE EAN = (%s)"
            dados = (str(linha))
            cursor.execute(comando_SQL, (dados,))
            banco.commit()

            tela_editarEstoque.lineEdit_Ean.setText("")
            tela_editarEstoque.lineEdit_NomeProduto.setText("")
            tela_editarEstoque.lineEdit_Estoque.setText("")
            tela_editarEstoque.lineEdit_Preco.setText("")
            tela_editarEstoque.lineEdit_Altura.setText("")
            tela_editarEstoque.lineEdit_Largura.setText("")
            tela_editarEstoque.lineEdit_Descricao.setText("")
            QMessageBox.about(tela_editarEstoque, "Aviso", "Produto Apagado!")

        else:
            QMessageBox.about(tela_editarEstoque, "Aviso", "Revise os campos!")

    except Exception:
        QMessageBox.about(tela_editarEstoque, "Aviso", "Ocorreu um erro, revise os campos e tente novamente!")


def Caixa():
    quantidade = 0
    tela_caixa.comboBox.clear()

    try:
        linha = tela_caixa.lineEdit.text()
        cursor = banco.cursor()
        comando_SQL = "SELECT Nome, Estoque, Preco, EAN FROM  produtos WHERE EAN = (%s)"
        dados = (str(linha))
        cursor.execute(comando_SQL, (dados,))
        dados1 = cursor.fetchall()
        quantidade = (dados1[0][1])
        quantidade1 = int(quantidade)

        for i in range(0, quantidade1 + 1):
            tela_caixa.comboBox.addItem(str(i))



    except IndexError:
        QMessageBox.about(tela_editarEstoque, "Aviso", "Produto Não encontrado!")


def Caixa_Adicionar():
    global total2
    soma2 = []
    linha = tela_caixa.lineEdit.text()
    cursor = banco.cursor()
    comando_SQL = "SELECT Nome, Estoque, Preco, EAN FROM  produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados1 = cursor.fetchall()

    lista.append([dados1[0][0], tela_caixa.comboBox.currentText(), dados1[0][2], dados1[0][3]])

    data_compra = tela_caixa.calendarWidget.selectedDate()

    tela_caixa.pushButton_Limpar.clicked.connect(limpa_tabela)
    tela_caixa.tableWidget.setRowCount(len(lista))
    tela_caixa.tableWidget.setColumnCount(4)

    for list in lista:
        soma2.append((list[2]) * float(list[1]))
        total2 = sum(soma2)
        tela_caixa.label_valor.setText(str(float("%.3f" % total2)))
        for i in range(0, len(lista)):
            for j in range(0, 4):
                tela_caixa.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))


def finalizar_compra():
    total = 0
    frm_pagamento = ""
    data_compra = ""
    soma = []
    lista_final = []
    linha = tela_caixa.lineEdit.text()
    cursor = banco.cursor()

    comando_SQL = "SELECT Nome, Estoque, Preco, EAN FROM  produtos WHERE EAN = (%s)"
    dados = (str(linha))
    cursor.execute(comando_SQL, (dados,))
    dados1 = cursor.fetchall()

    if tela_caixa.radioButton_1.isChecked() == True:
        frm_pagamento = tela_caixa.radioButton_1.text()


    elif tela_caixa.radioButton_2.isChecked() == True:
        frm_pagamento = tela_caixa.radioButton_2.text()

    elif tela_caixa.radioButton_3.isChecked() == True:
        frm_pagamento = tela_caixa.radioButton_3.text()

    data_compra = tela_caixa.calendarWidget.selectedDate()
    print(data_compra)

    for list in lista:
        soma.append((list[2]) * float(list[1]))
        total = sum(soma)
        tela_caixa.label_valor.setText(str(float("%.3f" % total)))
        lista_final.append([list[0], list[3], list[2], list[1], frm_pagamento, data_compra])
        print(lista_final)

    for list in lista_final:
        cursor = banco.cursor()
        comando_SQL = "INSERT INTO compra (nome, ean, preco, qtd, forma_pg, data_compra) VALUES (%s,%s,%s,%s,%s,%s)"
        dados = (str(list[0]), str(list[1]), str(list[2]), str(list[3]), str(list[4]), str(list[5]))
        cursor.execute(comando_SQL, dados)
        banco.commit()
    QMessageBox.about(tela_caixa, "Aviso", "Compra Finalizada")
    limpa_lista()
    limpa_tabela()


def troco():
    try:
        resultado = 0
        troco = tela_caixa.lineEdit_2.text()
        print(total2)
        resultado = float(troco) - total2
        tela_caixa.label_10.setText(str(float("%.3f" % resultado)))
    except NameError:
        QMessageBox.about(tela_caixa, "Aviso", "Valor de compra não encontrado!")


def relatorio_compras():
    tela_RCompras.show()

    cursor = banco.cursor()
    comando_SQL = "SELECT *FROM  compra"
    cursor.execute(comando_SQL)
    dados = cursor.fetchall()

    tela_RCompras.tableWidget.setRowCount(len(dados))
    tela_RCompras.tableWidget.setColumnCount(7)

    for i in range(0, len(dados)):
        for j in range(0, 7):
            tela_RCompras.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))


def deletar_compras():
    try:
        linha = tela_RCompras.lineEdit.text()
        if linha != "":
            cursor = banco.cursor()
            comando_SQL = "DELETE  FROM compra WHERE id = (%s)"
            dados = (str(linha))
            cursor.execute(comando_SQL, (dados,))
            banco.commit()

            QMessageBox.about(tela_RCompras, "Aviso", "Registro Apagado!")

        else:
            QMessageBox.about(tela_RCompras, "Aviso", "Revise os campos!")

    except Exception:
        QMessageBox.about(tela_RCompras, "Aviso", "Ocorreu um erro, revise os campos e tente novamente!")


def chama_segunda_tela():
    primeira_tela.label_5.setText("")
    nome_usuario = primeira_tela.lineEdit_2.text()
    senha = primeira_tela.lineEdit.text()
    try:
        cursor = banco.cursor()
        comando_SQL = "select * from usuarios where usuario = (%s) and senha = (%s);"
        dados = (str(nome_usuario), str(senha))
        cursor = banco.cursor(buffered=True)
        cursor.execute(comando_SQL, (dados))
        banco.commit()
        dados1 = cursor.fetchall()
        print (dados1)
        if nome_usuario == dados1[0][2] and senha == dados1[0][3]:    
            if dados1[0][4] == "Funcionário":
                menu.actionLogout.triggered.connect(logout)
                menu.actionEditar_e_Excluir_Or_amento_Cliente_Empresa.setEnabled(False)
                menu.actionProduto.triggered.connect(chama_tela_cadastro)
                menu.actionEstoque.triggered.connect(chama_tela_estoque)
                menu.actionCaixa.triggered.connect(chama_tela_caixa)
                menu.actionEditar_Estoque.triggered.connect(chama_tela_editar)
                menu.actionOr_amento_Cliente_Empresa.setEnabled(False)
                menu.actionUsu_rio.setEnabled(False)
                menu.actionReset_de_Senha.setEnabled(False)
                menu.actionExcluir_usu_rio.setEnabled(False)
                
                primeira_tela.close()
                menu.show()

            elif dados1[0][4] == "Administrador":
                menu.actionLogout.triggered.connect(logout)
                menu.actionEditar_e_Excluir_Or_amento_Cliente_Empresa.setEnabled(True)
                menu.actionProduto.triggered.connect(chama_tela_cadastro)
                menu.actionEstoque.triggered.connect(chama_tela_estoque)
                menu.actionCaixa.triggered.connect(chama_tela_caixa)
                menu.actionEditar_Estoque.triggered.connect(chama_tela_editar)
                menu.actionOr_amento_Cliente_Empresa.setEnabled(True)
                menu.actionUsu_rio.setEnabled(True)
                menu.actionReset_de_Senha.setEnabled(True)
                menu.actionExcluir_usu_rio.setEnabled(True)
                primeira_tela.close()
                menu.show()
        else:
            QMessageBox.about(primeira_tela, "Aviso","Dados de login incorretos ou Campos Não Preenchidos!")

    except IndexError:
        QMessageBox.about(primeira_tela, "Aviso","Dados de login incorretos ou Campos Não Preenchidos!")




def cadastrar_usuario():
    cpf = tela_cadastro_usuario.lineEdit.text()
    nome = tela_cadastro_usuario.lineEdit_2.text()
    usuario = tela_cadastro_usuario.lineEdit_3.text()
    senha = tela_cadastro_usuario.lineEdit_4.text()
    c_senha = tela_cadastro_usuario.lineEdit_5.text()
    tipo = ""
    
    if senha == c_senha:
        try:
            if tela_cadastro_usuario.radioButton.isChecked() == True:
                tipo = tela_cadastro_usuario.radioButton.text()
                cursor = banco.cursor()
                comando_SQL = "INSERT INTO usuarios (cpf, nome, usuario, senha, tipo) VALUES (%s,%s,%s,%s,%s)"
                dados = (str(cpf), str(nome), str(usuario), str(senha), str(tipo))
                cursor.execute(comando_SQL, dados)
                banco.commit()
                QMessageBox.about(tela_cadastro_usuario, "Aviso", "Usuário Cadastrado")
        except Exception:
            QMessageBox.about(tela_editarEstoque, "Aviso", "Ocorreu um erro, revise os campos e tente novamente!")

        try:
            if tela_cadastro_usuario.radioButton_2.isChecked() == True:
                tipo = tela_cadastro_usuario.radioButton_2.text()
                cursor = banco.cursor()
                comando_SQL = "INSERT INTO usuarios (cpf, nome, usuario, senha, tipo) VALUES (%s,%s,%s,%s,%s)"
                dados = (str(cpf), str(nome), str(usuario), str(senha), str(tipo))
                cursor.execute(comando_SQL, dados)
                banco.commit()
                QMessageBox.about(tela_cadastro_usuario, "Aviso", "Usuário Cadastrado")
        except Exception:
            QMessageBox.about(tela_editarEstoque, "Aviso", "Ocorreu um erro, revise os campos e tente novamente!")
    
    else:
        QMessageBox.about(tela_cadastro_usuario, "Aviso", "As senhas digitadas não são iguais")

    cpf = tela_cadastro_usuario.lineEdit.setText()
    nome = tela_cadastro_usuario.lineEdit_2.setText()
    usuario = tela_cadastro_usuario.lineEdit_3.setText()
    senha = tela_cadastro_usuario.lineEdit_4.setText()
    c_senha = tela_cadastro_usuario.lineEdit_5.setText()


def logout():
    app.closeAllWindows()
    chama_login()
    
   
    
def excluir_usuario_pesquisar():
    
    try:
        cpf = tela_excluir_usuario.lineEdit_cpf.text()
        cursor = banco.cursor()
        comando_SQL = "SELECT * FROM  usuarios WHERE cpf = (%s)"
        dados = (str(cpf))
        cursor.execute(comando_SQL, (dados,))
        dados1 = cursor.fetchall()

        tela_excluir_usuario.lineEdit_nome.setText(dados1[0][2])
        tela_excluir_usuario.lineEdit_tipo.setText(dados1[0][4])
        
    except IndexError:
        QMessageBox.about(tela_editarEstoque, "Aviso", "Usuario Não encontrado!")

def excluir_usuario():
    try:
        linha = tela_excluir_usuario.lineEdit_cpf.text()
        if linha != "":
            cursor = banco.cursor()
            comando_SQL = "DELETE FROM usuarios WHERE cpf = (%s)"
            dados = (str(linha))
            cursor.execute(comando_SQL, (dados,))
            banco.commit()

            tela_excluir_usuario.lineEdit_nome.setText("")
            tela_excluir_usuario.lineEdit_tipo.setText("")
            tela_excluir_usuario.lineEdit_cpf.setText("")
            QMessageBox.about(tela_excluir_usuario, "Aviso", "Usuário Apagado!")

        else:
            QMessageBox.about(tela_excluir_usuario, "Aviso", "Revise os campos!")

    except Exception:
        QMessageBox.about(tela_excluir_usuario, "Aviso", "Ocorreu um erro, revise os campos e tente novamente!")

def reset_senha():
    linha1 = tela_reset.lineEdit_cpf.text()
    linha2 = tela_reset.lineEdit_senha.text()
    linha3 = tela_reset.lineEdit_csenha.text()
    
    if linha2 == linha3:

        cursor = banco.cursor()
        comando_SQL = "UPDATE usuarios SET senha = (%s) WHERE cpf = (%s)"
        dados = (str(linha2), str(linha1))
        cursor.executemany(comando_SQL, (dados,))
        banco.commit()

        tela_reset.lineEdit_cpf.setText("")
        tela_reset.lineEdit_senha.setText("")
        tela_reset.lineEdit_csenha.setText("")
        QMessageBox.about(tela_reset, "Aviso", "Senha Alterada!")
    else:
        QMessageBox.about(tela_reset, "Aviso", "As senhas digitadas não são as mesmas!")


app = QtWidgets.QApplication([])


tela_cadastro = uic.loadUi("Cadastro_Produto.ui")
tela_caixa = uic.loadUi("Caixa.ui")
tela_estoque = uic.loadUi("Estoque.ui")
tela_orcamento_cliente = uic.loadUi("Realizar_Orcamento_Cliente_Empresa.ui")
tela_OrcamentoEditar = uic.loadUi("Orcamento_Editar.ui")
tela_editarEstoque = uic.loadUi("Estoque_Editar.ui")
tela_RCompras = uic.loadUi("Relatorio_Compras.ui")
primeira_tela= uic.loadUi("login.ui")
menu = uic.loadUi("Menu.ui")
tela_cadastro_usuario = uic.loadUi("cadastrar_usuario.ui")

tela_excluir_usuario = uic.loadUi("Deletar_usuario.ui")
tela_reset = uic.loadUi("Reset_senha.ui")


primeira_tela.pushButton.clicked.connect(chama_segunda_tela)
primeira_tela.lineEdit.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro_usuario.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro_usuario.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Password)
tela_cadastro_usuario.pushButton.clicked.connect(cadastrar_usuario)
tela_editarEstoque.pushButton_deletar.clicked.connect(deletar)
tela_caixa.pushButton_pesquisa.clicked.connect(Caixa)
tela_caixa.pushButton.clicked.connect(Caixa_Adicionar)
tela_caixa.pushButton_Limpar.clicked.connect(limpa_tabela)
tela_caixa.pushButton_Limpar.clicked.connect(limpa_lista)
tela_editarEstoque.pushButton_pesquisar.clicked.connect(pesquisar)
tela_editarEstoque.pushButton_editar.clicked.connect(editar)
tela_estoque.pushButton.clicked.connect(chama_tela_estoque)
tela_caixa.pushButton_2.clicked.connect(finalizar_compra)
tela_caixa.pushButton_calc.clicked.connect(troco)
tela_RCompras.pushButton_2.clicked.connect(deletar_compras)
tela_RCompras.pushButton_atualizar.clicked.connect(relatorio_compras)
tela_orcamento_cliente.pushButton_criar.clicked.connect(cadastro_Orcamento_Cliente)
tela_orcamento_cliente.pushButton_atualizar.clicked.connect(Orcamento_Cliente)
tela_OrcamentoEditar.pushButton_pesquisar.clicked.connect(pesquisar_orcamento)
tela_OrcamentoEditar.pushButton_editar.clicked.connect(editar_orcamento)
tela_OrcamentoEditar.pushButton_deletar.clicked.connect(deletar_orcamento)
tela_excluir_usuario.pushButton_pesquisar.clicked.connect(excluir_usuario_pesquisar)
tela_excluir_usuario.pushButton_deletar.clicked.connect(excluir_usuario)
tela_reset.pushButton_reset.clicked.connect(reset_senha)
tela_cadastro.pushButton.clicked.connect(cadastro)
primeira_tela.pushButton_2.clicked.connect(chama_tela_reset)

menu.actionExcluir_usu_rio.triggered.connect(chama_tela_excluirUsuario)
menu.actionLogout.triggered.connect(logout)
menu.actionEditar_e_Excluir_Or_amento_Cliente_Empresa.triggered.connect(chama_tela_orcamento_editar)
menu.actionProduto.triggered.connect(chama_tela_cadastro)
menu.actionEstoque.triggered.connect(chama_tela_estoque)
menu.actionCaixa.triggered.connect(chama_tela_caixa)
menu.actionEditar_Estoque.triggered.connect(chama_tela_editar)
menu.actionOr_amento_Cliente_Empresa.triggered.connect(chama_tela_Orcamento_Cliente)
menu.actionRelat_rio_Compras.triggered.connect(relatorio_compras)
menu.actionUsu_rio.triggered.connect(abre_tela_cadastro)
menu.actionReset_de_Senha.triggered.connect(chama_tela_reset)
primeira_tela.show()
app.exec()