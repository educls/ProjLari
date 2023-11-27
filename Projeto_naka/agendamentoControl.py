from agendamento_model import AgendamentoModel
from user_model import UserModel

from agendamento_dao import AgendamentoDAO


class AgendamentoControl:
    agendamento = None
    agendamentoDAO = AgendamentoDAO()

    def cadastrar(self, idAgendamento, idUsuario, agendamentoData, agendamentoHora, agendamentoTipoServico):
        self.agendamento = AgendamentoModel(idAgendamento, idUsuario, agendamentoData, agendamentoHora, agendamentoTipoServico)
        return self.agendamentoDAO.insert(self.agendamento)

    def consultar(self, idUsuario):
        self.user = self.agendamentoDAO.selectUsuario(idUsuario)
        if self.user == None:
            return None
        dados = (str(self.user.getIdUsuario()),
                 self.user.getNomeUsuario(),
                 str(self.user.getSenha()),
                 str(self.user.getTipoConta()))
        return dados

    def excluir(self, idAgendamento):
        if self.agendamento != None and self.agendamento.getIdAgendamento() == int(idAgendamento):
            self.agendamento = None
            return self.agendamentoDAO.delete(int(idAgendamento))