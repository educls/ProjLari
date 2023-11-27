from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from agendamentoControl import AgendamentoControl


class CadastroAgendamento(QtWidgets.QMainWindow):
    def __init__(self):
        super(CadastroAgendamento, self).__init__()
        self.agendamentoControle = AgendamentoControl()
        self.telaAgend = uic.loadUi("TelaProjAgendamento.ui")
        self.telaAgend.pbLogar.clicked.connect(self.consultarLogin)
        self.telaAgend.pbAgendar.clicked.connect(self.cadastrarAgendamento)
        self.telaAgend.pbLogar.clicked.connect(self.consultarLogin)
        self.telaAgend.show()


    def consultarLogin(self):
        dados=self.agendamentoControle.consultar(self.telaAgend.leUsuario.text())

        if dados==None:
            return True
        self.telaAgend.leUsuario.setEnabled(False)
        self.telaAgend.leSenha.setEnabled(False)

        self.telaAgend.lbStatusLogin.setText("Login realizado")
        return dados

    def cadastrarAgendamento(self):

        dados = self.consultarLogin()
        print(dados)

        if self.telaAgend.rbCheckLavagem.isChecked():
            rbCheckLavagem = "Apenas Lavagem"
        else:
            rbCheckLavagem = "Apenas Secagem"

        if self.agendamentoControle.cadastrar(" ", dados[0], self.telaAgend.deData.text(),
                                    self.telaAgend.teHora.text(),
                                    rbCheckLavagem):
            print("Agendamento Realizado!")
        self.limpar()


    def limpar(self):

        self.telaAgend.leUsuario.setEnabled(True)
        self.telaAgend.leSenha.setEnabled(True)
