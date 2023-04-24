# coding: utf-8
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_TEST = Table(
    'TEST', metadata,
    Column('ID', Integer),
    Column('NOMBRE', String(255, 'SQL_Latin1_General_CP1_CI_AS')),
    schema='INVENTORY'
)


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


class EQUIPO(Base):
    __tablename__ = 'EQUIPO'
    __table_args__ = {'schema': 'INVENTORY'}

    ID_EQUIPO = None
    ID_PROYECTO = Column(ForeignKey('MANAGEMENT.PROYECTO.ID_PROYECTO'), nullable=False)
    NOMBRE = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DETALLE_ADMINISTRACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DESCRIPCION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    CONFIDENCIALIDAD = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    INTEGRIDAD = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DISPONIBILIDAD = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    CRQ_ALTA = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    NRO_SERIE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    DETALLE_PROPIEDAD = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_ALTA = Column(Date)
    FECHA_BAJA = Column(Date)
    BAHIA_DESDE = Column(String(155, 'SQL_Latin1_General_CP1_CI_AS'))
    BAHIA_HASTA = Column(String(155, 'SQL_Latin1_General_CP1_CI_AS'))
    CANTIDAD_RU = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    NRO_CID = Column(String(155, 'SQL_Latin1_General_CP1_CI_AS'))
    NRO_RANURAS = Column(String(155, 'SQL_Latin1_General_CP1_CI_AS'))
    RANGO_RU_DESDE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    RANGO_RU_HASTA = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    NOMBRE_VIRTUAL = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO_EQUIPO = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    NRO_CORE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    NRO_CPU = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    CPU_DESCRIPCION = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    DISK_APROVISIONADO = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    DISK_ASIGNADO = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    RAM_ASIGNADO = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ENERGIA_KW = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ENERGIA_USO = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ID_GENESYS = Column(Integer)
    PART_NUMBER = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    FABRICANTE = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    PROVEEDOR = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    REFERENCIA_EXTERNA = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    LINEA_BASE = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    MONITOREO = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(Boolean)
    USUARIO_CREACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)
    TOKEN_ID = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    VERSION_SW = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    MODELO = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    ROL_USO = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    VCENTER = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    PROPIEDAD = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    FAMILIA = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    CLASE = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    ADMINISTRADOR = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    EQUIPO_ESTADO = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    PRIORIDAD = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO_SERVICIO = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    UBICACION = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    AMBIENTE = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    MARCA = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    SISTEMA_OPERATIVO = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    BACKUPS_CLOUD = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    MONITOREO_CLOUD = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    BACKUPS = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    NOMBRE_CI = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO_ALCANCE = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    ADMINISTRADOPOR = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))

    PROYECTO = relationship('PROYECTO')


class EQUIPOIP(Base):
    __tablename__ = 'EQUIPO_IP'
    __table_args__ = {'schema': 'INVENTORY'}

    ID_EQUIPO_IP = None
    ID_EQUIPO = Column(ForeignKey('INVENTORY.EQUIPO.ID_EQUIPO'), primary_key=True, nullable=False)
    NRO_IP = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    MASCARA = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    COMENTARIO = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(Boolean)
    USUARIO_CREACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)
    TIPO_IP = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))

    EQUIPO = relationship('EQUIPO')