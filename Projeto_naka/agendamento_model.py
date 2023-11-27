class AgendamentoModel:
    def __init__(self, idAgendamento, idUsuario, agendamentoData, agendamentoHora, agendamentoTipoServico):
        self.idAgendamento = idAgendamento
        self.idUsuario = idUsuario
        self.agendamentoData = agendamentoData
        self.agendamentoHora = agendamentoHora
        self.agendamentoTipoServico = agendamentoTipoServico

    def getIdAgendamento(self):
        return self.idAgendamento

    def getIdUsuario(self):
        return self.idUsuario

    def getAgendamentoData(self):
        return self.agendamentoData

    def getAgendamentoHora(self):
        return self.agendamentoHora

    def getAgendamentoTipoServico(self):
        return self.agendamentoTipoServico
