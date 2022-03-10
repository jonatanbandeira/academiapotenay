from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Date, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

NOME_BANCO = "academia"

engine = create_engine(f"sqlite:///./{NOME_BANCO}.db", echo=True)
Base = declarative_base()

# Declaracao das classes


class Modalidade(Base):

    __tablename__ = "modalidade"

    cdModalidade = Column(Integer, primary_key=True)
    nomeModalidade = Column(String, nullable=False)

    def __repr__(self):
        return f"Modalidade {self.nome}"


class Turno(Base):
    __tablename__ = "turno"

    cdTurno = Column(Integer, primary_key=True)
    nomeTurno = Column(String, nullable=False)

    def __repr__(self) -> str:
        return f"Turno {self.nome}"


class Cidade(Base):
    __tablename__ = "cidade"
    cdCidade = Column(Integer, primary_key=True)
    nomeCidade = Column(String, nullable=False)

    def __repr__(self):
        return f"Cidade {self.nome}"


class Instrutor(Base):
    __tablename__ = "instrutor"
    cdInstrutor = Column(Integer, primary_key=True)
    nomeInstrutor = Column(String, nullable=False)

    def __repr__(self):
        return f"Instrutor {self.nome}"


class Cliente(Base):

    __tablename__ = "cliente"

    cdCliente = Column(Integer, primary_key=True)
    nomeCliente = Column(String, nullable=False)
    telefone = Column(String, nullable=False)
    email = Column(String, nullable=False)
    cidade_cdCidade = Column(Integer, ForeignKey("cidade.cdCidade"))
    modalidade_cdModalidade = Column(
        Integer, ForeignKey("modalidade.cdModalidade"))
    turno_cdTurno = Column(Integer, ForeignKey("turno.cdTurno"))
    instrutor_cdInstrutor = Column(
        Integer, ForeignKey("instrutor.cdInstrutor"))


# fim da declaracao

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
