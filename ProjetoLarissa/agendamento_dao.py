import mysql.connector

from agendamento_model import AgendamentoModel
from user_model import UserModel

class AgendamentoDAO:
    def conectar(self):
        self.con = mysql.connector.connect(host="localhost",
                                           database="projnaka",
                                           user="root",
                                           password="")
        if self.con.is_connected():
            self.cursor = self.con.cursor()
            return True
        return False

    def disconnect(self):
        try:
            if self.con.is_connected():
                self.con.close()
                print("Conexão fechada com sucesso.")
        except Exception as e:
            print(f"Erro ao fechar a conexão: {e}")


    def insert(self, agendamento):
        sql = 'insert into agendamentos values (%s, %s, %s, %s, %s)'
        values = (agendamento.getIdAgendamento(), agendamento.getIdUsuario(), agendamento.getAgendamentoData(),
                  agendamento.getAgendamentoHora(), agendamento.getAgendamentoTipoServico())
        if self.conectar():
            self.cursor.execute(sql, values)
            if self.cursor.rowcount > 0:
                self.con.commit()
                self.disconnect()
                return True
            self.disconnect()
        return False

    def delete(self, idAgendamento):
        sql = 'delete from agendamentos where idAgendamento= %s'
        if self.conectar():
            self.cursor.execute(sql, (idAgendamento, ))
            if self.cursor.rowcount > 0:
                self.con.commit()
                self.disconnect()
                return True
            self.disconnect()
        return False

    def selectUsuario(self, nomeUsuario):
        sql = 'select * from usuarios where nomeUsuario= %s'
        if self.conectar():
            self.cursor.execute(sql, (nomeUsuario, ))
            dados = self.cursor.fetchone()
            self.disconnect()
            if dados is not None:
                user = UserModel(dados[0], dados[1], dados[2], dados[3])
                return user
            self.disconnect()
        return None
