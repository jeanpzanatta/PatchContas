from PyQt5 import QtCore, QtGui, QtWidgets


class WidgetInicial(QtWidgets.QWidget):
    """Primeiro Widget que deve aparecer na tela inicial,
    foi gerado automaticamente, e por possui esse atributo form,
    lembrar de usar self.form quando for chamar essa tela"""
    def __init__(self, form):
        super(WidgetInicial, self).__init__()
        self.Form = form
        self.Form.setObjectName("TelaInicial")
        self.Form.resize(640, 480)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 91))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_cadastrar_nova = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_cadastrar_nova.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_cadastrar_nova.setObjectName("lbl_cadastrar_nova")
        self.verticalLayout.addWidget(self.lbl_cadastrar_nova)
        self.btn_nova_compra = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_nova_compra.setObjectName("btn_nova_compra")
        self.verticalLayout.addWidget(self.btn_nova_compra)
        self.btn_nova_venda = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_nova_venda.setObjectName("btn_nova_venda")
        self.verticalLayout.addWidget(self.btn_nova_venda)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(self.spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_verificar_passada = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.lbl_verificar_passada.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_verificar_passada.setObjectName("lbl_verificar_passada")
        self.verticalLayout_2.addWidget(self.lbl_verificar_passada)
        self.btn_compra_passada = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_compra_passada.setObjectName("btn_compra_passada")
        self.verticalLayout_2.addWidget(self.btn_compra_passada)
        self.btn_venda_passada = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.btn_venda_passada.setObjectName("btn_venda_passada")
        self.verticalLayout_2.addWidget(self.btn_venda_passada)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.Form)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 120, 621, 341))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_infos_importantes = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.lbl_infos_importantes.setObjectName("lbl_infos_importantes")
        self.verticalLayout_3.addWidget(self.lbl_infos_importantes)
        self.calendarWidget = QtWidgets.QCalendarWidget(self.verticalLayoutWidget_3)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_3.addWidget(self.calendarWidget)

        self.Form.show()

        self.retranslate_ui(self.Form)
        QtCore.QMetaObject.connectSlotsByName(self.Form)

    def retranslate_ui(self, form):
        self.Form = form
        _translate = QtCore.QCoreApplication.translate
        self.Form.setWindowTitle(_translate("Form", "TelaInicial"))
        self.lbl_cadastrar_nova.setText(_translate("Form", "Cadastrar:"))
        self.btn_nova_compra.setText(_translate("Form", "Nova Compra"))
        self.btn_nova_venda.setText(_translate("Form", "Nova Venda"))
        self.lbl_verificar_passada.setText(_translate("Form", "Verificar:"))
        self.btn_compra_passada.setText(_translate("Form", "Compra Passada"))
        self.btn_venda_passada.setText(_translate("Form", "Venda Passada"))
        self.lbl_infos_importantes.setText(_translate("Form", "Aqui serão exibidas informações importantes,"
                                                              " mas por enquanto, fique com esse calendário:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    form = QtWidgets.QWidget()
    ui = WidgetInicial(form)
    sys.exit(app.exec_())
