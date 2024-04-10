from sqlalchemy import Column, Integer, String, DateTime,Float
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class BRTRaw(Base):
    __tablename__ = "tb_brt_api"
    __table_args__ = {'schema': 'sc_silver'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    codigo = Column(String,nullable=True),
    placa = Column(String,nullable=True),
    linha = Column(String,nullable=True),
    latitude = Column(Float,nullable=True),
    longitude = Column(Float,nullable=True),
    dataHora = Column(Integer,nullable=True),
    velocidade = Column(Float,nullable=True),
    id_migracao_trajeto = Column(String,nullable=True),
    sentido = Column(String,nullable=True),
    trajeto = Column(String,nullable=True),
    hodometro = Column(Float,nullable=True),
    direcao = Column(Integer,nullable=True),
    dh_extraction=Column(DateTime)

# class BRTGold(Base):
#     __tablename__ = "tb_brt_api"
#     __table_args__ = {'schema': 'sc_gold'}

#     codigo = Column(String),
#     latitude = Column(float),
#     longitude = Column(float),
#     velocidade = Column(float)
