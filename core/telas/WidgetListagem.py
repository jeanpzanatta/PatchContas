from PyQt5 import QtCore, QtGui, QtWidgets


class WidgetListagem(QtWidgets.QWidget):
    def __init__(self, form):
        super(WidgetListagem, self).__init__()

        self.Form = form

        self.Form.setObjectName("Listagem")
        self.Form.resize(640, 480)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 621, 431))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_listagem = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.lbl_listagem.setObjectName("lbl_listagem")
        self.verticalLayout.addWidget(self.lbl_listagem)
        self.treeView = QtWidgets.QTreeView(self.verticalLayoutWidget)
        self.treeView.setObjectName("treeView")
        self.verticalLayout.addWidget(self.treeView)
        self.btn_voltar = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.btn_voltar.setObjectName("btn_cancel_compra")
        self.verticalLayout.addWidget(self.btn_voltar)

        self.Form.show()

        self.retranslate_ui(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

        self.numero_colunas = range(5)
        self.NOME, self.DESCRICAO, self.VALOR, self.DATA, self.PARCELAS = self.numero_colunas
        self.model = QtGui.QStandardItemModel(0, 5)

        self.treeView.setModel(self.model)
        self.model.setHeaderData(self.NOME, QtCore.Qt.Horizontal, "Nome")
        self.model.setHeaderData(self.DESCRICAO, QtCore.Qt.Horizontal, "Descrição")
        self.model.setHeaderData(self.VALOR, QtCore.Qt.Horizontal, "Valor")
        self.model.setHeaderData(self.DATA, QtCore.Qt.Horizontal, "Data")
        self.model.setHeaderData(self.PARCELAS, QtCore.Qt.Horizontal, "Nº de Parcelas")

    def ajutar_tamanho(self):
        for colunas in self.numero_colunas:
            if colunas != 1:
                self.treeView.resizeColumnToContents(colunas)

    def retranslate_ui(self, form):
        self.Form = form
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "Listagem"))
        self.lbl_listagem.setText(_translate("Form", "Lista:"))
        self.btn_voltar.setText(_translate("Form", "Voltar"))

    def add_item(self, nome, descricao, valor, data, parcelas):
        model = self.model
        model.insertRow(0)
        model.setData(self.model.index(0, self.NOME), nome)
        model.setData(self.model.index(0, self.DESCRICAO), descricao)
        model.setData(self.model.index(0, self.VALOR), valor)
        model.setData(self.model.index(0, self.DATA), data)
        model.setData(self.model.index(0, self.PARCELAS), parcelas)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = WidgetListagem(Form)
    sys.exit(app.exec_())
