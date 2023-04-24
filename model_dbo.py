# coding: utf-8
from sqlalchemy import Column, DateTime, Float, Integer, LargeBinary, SmallInteger, String, Table, Unicode, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ANSIBLECONTROL(Base):
    __tablename__ = 'ANSIBLE_CONTROL'
    __table_args__ = {'schema': 'dbo'}

    IDANSIBLE = None
    IDJOB = Column(Integer)
    NOMBRE = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    HOST = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    URI = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADOJOB = Column(String(25, 'SQL_Latin1_General_CP1_CI_AS'))
    CONTENT = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERSTART = Column(Integer)
    SYSDATESTART = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))


class CONTADORE(Base):
    __tablename__ = 'CONTADORES'
    __table_args__ = {'schema': 'dbo'}

    ID = None
    Des_Tabla = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), nullable=False)
    NUM_ID = Column(Integer, nullable=False)


t_Datamigrar = Table(
    'Datamigrar', metadata,
    Column('PROY_ALP', Float(53)),
    Column('ITEM_HOSTNAME', Unicode(255)),
    Column('descripcion', Unicode(255)),
    Column('detalle_administracion', Unicode(255)),
    Column('confidencialidad', Unicode(255)),
    Column('integridad', Unicode(255)),
    Column('disponibilidad', Unicode(255)),
    Column('ITEM_SERIE', Unicode(255)),
    Column('PROP_DETALLE', Unicode(255)),
    Column('ITEM_FECINST', Unicode(255)),
    Column('ITEM_FECBAJA', Unicode(255)),
    Column('BahiaDesde', Unicode(255)),
    Column('BahiaHasta', Unicode(255)),
    Column('ITEM_RUNRO', Unicode(255)),
    Column('CID', Unicode(255)),
    Column('RUDesde', Unicode(255)),
    Column('RUHasta', Unicode(255)),
    Column('ITEM_VMNAME', Unicode(255)),
    Column('esVirtual', Float(53)),
    Column('ITEM_CORE', Float(53)),
    Column('ITEM_CPU', Float(53)),
    Column('ITEM_CPUDESC', Unicode(255)),
    Column('ITEM_DISKAPROV', Float(53)),
    Column('ITEM_DISK', Float(53)),
    Column('ITEM_RAM', Float(53)),
    Column('eci_id', Float(53)),
    Column('ITEM_PARTNUM', Unicode(255)),
    Column('EC_LINEABASE', Unicode(255)),
    Column('estado', Float(53)),
    Column('software', Unicode(255)),
    Column('MO_MODELO', Unicode(255)),
    Column('ROL_USODESC', Unicode(255)),
    Column('VC_NOMBRE', Unicode(255)),
    Column('PROP_DESC', Unicode(255)),
    Column('FAM_DESC', Unicode(255)),
    Column('CLASE_DESC', Unicode(255)),
    Column('AdminDesc', Unicode(255)),
    Column('EST_DESC', Unicode(255)),
    Column('CRITICAL_DESC', Unicode(255)),
    Column('UBIC_DESC', Unicode(255)),
    Column('AMB_DESC', Unicode(255)),
    schema='dbo'
)


class OPCIONE(Base):
    __tablename__ = 'OPCIONES'
    __table_args__ = {'schema': 'dbo'}

    IDOPCION = None
    ATRIBUTO = Column(String(512, 'SQL_Latin1_General_CP1_CI_AS'))
    VALOR = Column(String(512, 'SQL_Latin1_General_CP1_CI_AS'))
    ICON = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    PRIORIDAD = Column(Integer)
    PARENTID = Column(Integer)
    TIPOATRIBUTO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERREG = Column(Integer)
    ESTADO = Column(Integer, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    URI = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))


class Sysdiagram(Base):
    __tablename__ = 'sysdiagrams'
    __table_args__ = {'schema': 'dbo'}

    name = Column(Unicode(128), nullable=False)
    principal_id = Column(Integer, nullable=False)
    diagram_id = None
    version = Column(Integer)
    definition = Column(LargeBinary)