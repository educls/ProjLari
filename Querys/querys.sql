
1°
SELECT * FROM agendamentos WHERE agendamentoData = '15/10/2023';

2°
SELECT * FROM agendamentos WHERE agendamentoTipoServico = 'Apenas Lavagem';

3°
SELECT 
    agendamentos.idAgendamento,
    agendamentos.agendamentoData,
    agendamentos.agendamentoHora,
    agendamentos.agendamentoTipoServico,
    usuarios.nomeUsuario,
    usuarios.contaTipo
FROM agendamentos
JOIN usuarios ON agendamentos.idUsuario = usuarios.idUsuario
WHERE agendamentos.agendamentoTipoServico = 'Apenas Lavagem'
    AND usuarios.contaTipo = 'administrador';

4°
SELECT 
    agendamentos.idAgendamento,
    agendamentos.agendamentoData,
    agendamentos.agendamentoHora,
    agendamentos.agendamentoTipoServico,
    usuarios.nomeUsuario,
    usuarios.contaTipo
FROM agendamentos
JOIN usuarios ON agendamentos.idUsuario = usuarios.idUsuario
WHERE usuarios.nomeUsuario = 'Maria Oliveira';
