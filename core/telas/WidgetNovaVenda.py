from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date


class WidgetNovaVenda(QtWidgets.QWidget):
    def __init__(self, form):
        super(WidgetNovaVenda, self).__init__()

        self.hoje = str(date.today()).split('-')
        self.dia_hoje = int(self.hoje[0])
        self.mes_hoje = int(self.hoje[1])
        self.ano_hoje = int(self.hoje[2])

        self.Form = form
        self.Form.setObjectName("NovaVenda")
        self.Form.resize(640, 460)
        self.formLayoutWidget = QtWidgets.QWidget(self.Form)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 441))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(4)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.lbl_cliente = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_cliente.setObjectName("lbl_cliente")
        self.horizontalLayout_10.addWidget(self.lbl_cliente)
        self.txt_cliente = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.txt_cliente.setObjectName("txt_cliente")
        self.horizontalLayout_10.addWidget(self.txt_cliente)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_7)
        self.lbl_desc_venda = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_desc_venda.setObjectName("lbl_desc_venda")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lbl_desc_venda)
        self.txt_desc_venda = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.txt_desc_venda.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.txt_desc_venda.setObjectName("txt_desc_venda")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_desc_venda)
        self.spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, self.spacerItem)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lbl_valor_venda = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_valor_venda.setObjectName("lbl_valor_venda")
        self.horizontalLayout_9.addWidget(self.lbl_valor_venda)
        self.spin_valor = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.spin_valor.setAccelerated(True)
        self.spin_valor.setProperty("showGroupSeparator", True)
        self.spin_valor.setMinimum(0.01)
        self.spin_valor.setMaximum(999999.99)
        self.spin_valor.setSingleStep(0.01)
        self.spin_valor.setObjectName("spin_valor")
        self.horizontalLayout_9.addWidget(self.spin_valor)
        self.lbl_reais = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_reais.setObjectName("lbl_reais")
        self.horizontalLayout_9.addWidget(self.lbl_reais)
        self.spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(self.spacerItem1)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.lbl_primeira_parcela = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_primeira_parcela.setObjectName("lbl_primeira_parcela")
        self.horizontalLayout_11.addWidget(self.lbl_primeira_parcela)
        self.data_primeira_parcela = QtWidgets.QDateEdit(self.formLayoutWidget)
        self.data_primeira_parcela.setWrapping(False)
        self.data_primeira_parcela.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.data_primeira_parcela.setCalendarPopup(True)
        self.data_primeira_parcela.setDate(QtCore.QDate(self.dia_hoje, self.mes_hoje, self.ano_hoje))
        self.data_primeira_parcela.setObjectName("data_primeira_parcela")
        self.horizontalLayout_11.addWidget(self.data_primeira_parcela)
        self.verticalLayout_8.addLayout(self.horizontalLayout_11)
        self.verticalLayout_6.addLayout(self.verticalLayout_8)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_6)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.lbl_n_parcelas = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_n_parcelas.setObjectName("lbl_n_parcelas")
        self.horizontalLayout_6.addWidget(self.lbl_n_parcelas)
        self.box_n_parcelas = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.box_n_parcelas.setMaximum(6)
        self.box_n_parcelas.setObjectName("box_n_parcelas")
        self.horizontalLayout_6.addWidget(self.box_n_parcelas)
        self.lbl_aviso_pgmt = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_aviso_pgmt.setObjectName("lbl_aviso_pgmt")
        self.horizontalLayout_6.addWidget(self.lbl_aviso_pgmt)
        self.spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(self.spacerItem2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_5)
        self.spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.FieldRole, self.spacerItem3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.btn_cancel = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_cancel.setObjectName("btn_cancel_venda")
        self.horizontalLayout_5.addWidget(self.btn_cancel)
        self.btn_concluir = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_concluir.setObjectName("btn_concluir_venda")
        self.horizontalLayout_5.addWidget(self.btn_concluir)
        self.formLayout.setLayout(8, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)

        self.retranslate_ui(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

        self.Form.show()

    def retranslate_ui(self, form):
        _translate = QtCore.QCoreApplication.translate
        self.Form = form
        self.Form.setWindowTitle(_translate("Form", "NovaVenda"))
        self.lbl_cliente.setText(_translate("Form", "Nome do Cliente: "))
        self.lbl_desc_venda.setText(_translate("Form", "Descrição da venda:"))
        self.lbl_valor_venda.setText(_translate("Form", "Valor da Venda: "))
        self.lbl_reais.setText(_translate("Form", "Reais"))
        self.lbl_primeira_parcela.setText(_translate("Form", "Data da primeira parcela (ou da compra para pagamento a vista): "))
        self.lbl_n_parcelas.setText(_translate("Form", "Nº de Parcelas: "))
        self.lbl_aviso_pgmt.setText(_translate("Form", "Selecione 0 para Débito/Dinheiro, ou 1 para no credito sem parcelas."))
        self.btn_cancel.setText(_translate("Form", "Cancelar"))
        self.btn_concluir.setText(_translate("Form", "Concluir"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = WidgetNovaVenda(Form)
    sys.exit(app.exec_())
