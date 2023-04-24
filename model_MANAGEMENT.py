# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, Integer, String, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class PROYECTO(Base):
    __tablename__ = 'PROYECTO'
    __table_args__ = {'schema': 'MANAGEMENT'}

    ID_PROYECTO = None
    NOMBRE = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    ALP = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_INICIO = Column(Date)
    FECHA_FIN = Column(Date)
    ESTADO = Column(Boolean)
    USUARIO_CREACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)
    CLIENTE = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    PROYECTO_TIPO = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    PROYECTO_ESTADO = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))