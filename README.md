# ProjLari

Script SQL para a criação do Banco

```mysql
CREATE DATABASE IF NOT EXISTS projnaka;

USE projnaka;

CREATE TABLE usuarios(
  idUsuario INT NOT NULL AUTO_INCREMENT,
  nomeUsuario VARCHAR(45) NOT NULL,
  senha VARCHAR(45) NOT NULL,
  contaTipo VARCHAR(45) NOT NULL,
  PRIMARY KEY (idUsuario)
);

CREATE TABLE agendamentos (
    idAgendamento INT AUTO_INCREMENT PRIMARY KEY,
    idUsuario INT,
    agendamentoData VARCHAR(255),
    agendamentoHora VARCHAR(255),
    agendamentoTipoServico VARCHAR(255),
    FOREIGN KEY (idUsuario) REFERENCES usuarios(idUsuario),
    CONSTRAINT check_tipo_servico 
        CHECK (agendamentoTipoServico IN ('Apenas Lavagem', 'Apenas Secagem'))
);

```

# Dependencias do Projeto

## Mysql Connector
```bash
$ pip install mysql-connector-python
```


## PyQt5
```bash
$ pip install PyQt5
```


## PyQt5 Tools
```bash
$ pip install PyQt5-Tools
```


## PyQt5 Designer
```bash
$ pip install PyQt5Designer
```


