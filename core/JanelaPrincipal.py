from PyQt5 import QtCore, QtGui, QtWidgets
from telas import WidgetInicial, WidgetNovaCompra, WidgetNovaVenda, WidgetListagem, Grafico
from BancoDeDados import Banco1


class JanelaPrincipal(QtWidgets.QMainWindow):
    """Janela principal do programa, gerada automaticamente pelo arquivo .ui,
    precisa passar por mais refatoração para corrigir problemas da geração automatica."""
    def __init__(self, main_window):
        super().__init__()

        self.banco = Banco1.BancoDeDados()
        self.banco.conecta()
        self.banco.criar_tabelas()
        self.banco.desconecta()

        self.MainWindow = main_window
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.setFixedSize(650, 495)

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 631, 421))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 638, 23))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.actionObter_Ajuda = QtWidgets.QAction(self.MainWindow)
        self.actionObter_Ajuda.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionObter_Ajuda.setObjectName("actionObter_Ajuda")
        self.actionObter_Ajuda.setShortcut('F1')
        self.action_Sair = QtWidgets.QAction(self.MainWindow)
        self.action_Sair.setObjectName("action_Sair")
        self.action_Sair.setShortcut('Ctrl+Q')
        self.action_Inicio = QtWidgets.QAction(self.MainWindow)
        self.action_Inicio.setObjectName('Action_Inicio')
        self.action_Inicio.setShortcut('Ctrl+I')
        self.menuArquivo.addAction(self.action_Sair)
        self.menuArquivo.addAction(self.action_Inicio)
        self.menuAjuda.addAction(self.actionObter_Ajuda)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.action_Sair.triggered.connect(QtWidgets.qApp.quit)
        self.actionObter_Ajuda.triggered.connect(self.ajuda)
        self.action_Inicio.triggered.connect(self.mudar_tela_inicial)

        self.widget_atual = WidgetInicial.WidgetInicial(QtWidgets.QWidget())
        self.MainWindow.setCentralWidget(self.widget_atual.Form)

        self.MainWindow.show()

        self.retranslate_ui(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

        self.verificar_botoes()

    def verificar_botoes(self):
        """Serve para atualizar os botoes que aparecem na tela inicial, dependendo do Widget q está sendo exibido."""
        if self.widget_atual.Form.windowTitle() == 'TelaInicial':
            self.widget_atual.btn_nova_compra.clicked.connect(self.mudar_tela_nova_compra)
            self.widget_atual.btn_nova_venda.clicked.connect(self.mudar_tela_nova_venda)
            self.widget_atual.btn_compra_passada.clicked.connect(self.mudar_tela_listagem)
            self.widget_atual.btn_venda_passada.clicked.connect(self.mudar_tela_listagem)

        elif self.widget_atual.Form.windowTitle() == 'NovaVenda':
            self.widget_atual.btn_cancel.clicked.connect(self.mudar_tela_inicial)
            self.widget_atual.btn_concluir.clicked.connect(self.salvar_dados_venda)

        elif self.widget_atual.Form.windowTitle() == 'NovaCompra':
            self.widget_atual.btn_cancel.clicked.connect(self.mudar_tela_inicial)
            self.widget_atual.btn_concluir.clicked.connect(self.salvar_dados_compra)

        elif self.widget_atual.Form.windowTitle() == 'Listagem':
            self.widget_atual.btn_voltar.clicked.connect(self.mudar_tela_inicial)

    def retranslate_ui(self, main_window):
        self.MainWindow = main_window
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", "PatchContas"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.actionObter_Ajuda.setText(_translate("MainWindow", "Obter &Ajuda"))
        self.action_Sair.setText(_translate("MainWindow", "&Sair"))
        self.action_Inicio.setText(_translate('MainWindow', '&Inicio'))

    def ajuda(self):
        mensagem = 'Para obter ajuda procure por:\nJean Pedro Zanatta\nemail: jeanpedrozanatta@gmail.com'
        titulo = 'Ajuda'
        QtWidgets.QMessageBox.about(self, titulo, mensagem)

    def salvar_dados_venda(self):
        """Ordem dos dados: 'Nome do cliente, Descrição da venda, Valor, data, numero parcelas"""
        self.banco.conecta()
        try:
            if self.widget_atual.txt_cliente.text() == '' or self.widget_atual.txt_desc_venda.toPlainText() == '':
                raise ValueError
            self.banco.inserir_venda(
                self.widget_atual.txt_cliente.text(),
                self.widget_atual.txt_desc_venda.toPlainText(),
                self.widget_atual.spin_valor.value(),
                self.widget_atual.data_primeira_parcela.text(),
                self.widget_atual.box_n_parcelas.value()
            )
            self.mudar_tela_inicial()
        except ValueError:
            QtWidgets.QMessageBox.about(self, 'Erro', 'Verifique todos os campos e tente novamente.')
        finally:
            self.banco.desconecta()

    def salvar_dados_compra(self):
        """Ordem dos dados: 'Nome do fornecedor, Descrição da compra, Valor, data, numero parcelas"""
        self.banco.conecta()
        try:
            if self.widget_atual.txt_fornecedor.text() == '' or self.widget_atual.txt_desc_compra.toPlainText() == '':
                raise ValueError
            self.banco.inserir_compra(
                self.widget_atual.txt_fornecedor.text(),
                self.widget_atual.txt_desc_compra.toPlainText(),
                self.widget_atual.spin_valor.value(),
                self.widget_atual.data_primeira_parcela.text(),
                self.widget_atual.box_n_parcelas.value()
            )
            self.mudar_tela_inicial()
        except ValueError:
            QtWidgets.QMessageBox.about(self, 'Erro', 'Verifique todos os campos e tente novamente.')
        finally:
            self.banco.desconecta()

    def mudar_tela_inicial(self):
        tela_inicial = WidgetInicial.WidgetInicial(QtWidgets.QWidget())
        self.widget_atual = tela_inicial
        self.MainWindow.setCentralWidget(self.widget_atual.Form)
        self.verificar_botoes()

    def mudar_tela_nova_compra(self):
        nova_compra = WidgetNovaCompra.WidgetNovaCompra(QtWidgets.QWidget())
        self.widget_atual = nova_compra
        self.MainWindow.setCentralWidget(self.widget_atual.Form)
        self.verificar_botoes()

    def mudar_tela_nova_venda(self):
        nova_venda = WidgetNovaVenda.WidgetNovaVenda(QtWidgets.QWidget())
        self.widget_atual = nova_venda
        self.MainWindow.setCentralWidget(self.widget_atual.Form)
        self.verificar_botoes()

    def mudar_tela_listagem(self):
        self.banco.conecta()
        listagem = WidgetListagem.WidgetListagem(QtWidgets.QWidget())
        self.widget_atual = listagem
        self.MainWindow.setCentralWidget(self.widget_atual.Form)
        if self.sender().text() == 'Compra Passada':
            lido = self.banco.buscar_compras()
        else:
            lido = self.banco.buscar_vendas()
        for tupla in lido:
            listagem.add_item(tupla[0], tupla[1], tupla[2], tupla[3], tupla[4])
        self.verificar_botoes()
        self.banco.desconecta()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = JanelaPrincipal(MainWindow)
    sys.exit(app.exec_())
