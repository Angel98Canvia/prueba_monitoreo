# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, LargeBinary, String, Table, text
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


t_ALERTAS_INCIDENTES = Table(
    'ALERTAS_INCIDENTES', metadata,
    Column('CLIENT', String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('ALERTID', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('ALERTSTATE', String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('ALERTSEVERITY', String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('ALERTGROUP', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('REASON', String(512, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('DESCRIPTION', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('THRESHOLD', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('TAGS', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('HOSTIP', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('RULENAME', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('RULESPACE', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('TIMESTAMP', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('VALUE', String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('INCIDENT_URL', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('RULETYPE', String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('TOOL', String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)")),
    Column('SYSDATE', DateTime, server_default=text("(dateadd(hour,(-5),getdate()))")),
    Column('PARENT_CLIENT', String(155, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO_ALERT', String(155, 'SQL_Latin1_General_CP1_CI_AS')),
    schema='MONITOR'
)


class CONFREMEDY(Base):
    __tablename__ = 'CONF_REMEDY'
    __table_args__ = {'schema': 'MONITOR'}

    IDCONFREMEDY = None
    IDATRIBUTO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    ATRIBUTO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DEPENDENCIA1 = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    DEPENDENCIA2 = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERREG = Column(Integer, server_default=text("((0))"))
    ESTADO = Column(Boolean, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))


class CONTROLITSM(Base):
    __tablename__ = 'CONTROL_ITSM'
    __table_args__ = {'schema': 'MONITOR'}

    IDCONTROLITSM = None
    IDCENTRALIZADOR = Column(Integer)
    URL = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    HEAD = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'))
    BODY = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERREG = Column(Integer, server_default=text("((0))"))
    ESTADO = Column(Boolean, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    PRIORIDAD = Column(TINYINT)
    TICKETID = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))


class MATRIZPRIORIDAD(Base):
    __tablename__ = 'MATRIZ_PRIORIDAD'
    __table_args__ = {'schema': 'MONITOR'}

    IDMATRIZ = None
    IMPACTO = Column(TINYINT, server_default=text("((0))"))
    URGENCIA = Column(TINYINT, server_default=text("((0))"))
    PRIORIDAD = Column(TINYINT, server_default=text("((0))"))
    TIPO = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    OWNERGROUP = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    OWNERGROUPID = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(Integer, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))


class MONITOR(Base):
    __tablename__ = 'MONITOR'
    __table_args__ = {'schema': 'MONITOR'}

    IDMONITOR = None
    CLIENT = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    ALERTID = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    ALERTSTATE = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    TICKETID = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    TICKETSTATE = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    OWNERGROUP = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    PRIORITY = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    SYSLASTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    SYSSTARTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    URLTICKET = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    DISPOSITIVO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    STATUS = Column(Boolean, server_default=text("((1))"))
    ESTADO = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('PENDIENTE')"))


class OPCIONE(Base):
    __tablename__ = 'OPCIONES'
    __table_args__ = {'schema': 'MONITOR'}

    IDOPCION = None
    ATRIBUTO = Column(String(512, 'SQL_Latin1_General_CP1_CI_AS'))
    VALOR = Column(String(512, 'SQL_Latin1_General_CP1_CI_AS'))
    ICON = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    URI = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    PRIORIDAD = Column(Integer)
    PARENTID = Column(Integer)
    TIPOATRIBUTO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERREG = Column(Integer)
    ESTADO = Column(Integer, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    VALOR1 = Column(String(512, 'SQL_Latin1_General_CP1_CI_AS'))
    VALOR2 = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    VALOR3 = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    ENTERO1 = Column(Integer, server_default=text("((0))"))
    ENTERO2 = Column(Integer, server_default=text("((0))"))


class CENTRALIZADOR(Base):
    __tablename__ = 'CENTRALIZADOR'
    __table_args__ = {'schema': 'MONITOR'}

    IDCENTRALIZADOR = None
    CENTRALIZADOR = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IDCLIENTE = Column(ForeignKey('MONITOR.OPCIONES.IDOPCION'))
    PARENTID = Column(Integer, nullable=False, server_default=text("((0))"))
    IDUSERREG = Column(Integer, server_default=text("((0))"))
    ESTADO = Column(Boolean, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer, server_default=text("((0))"))
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))

    OPCIONE = relationship('OPCIONE')


class INVENTARIO(Base):
    __tablename__ = 'INVENTARIO'
    __table_args__ = {'schema': 'MONITOR'}

    IDINVENTARIO = None
    CLIENT = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    HOSTNAME = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IP = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ENTORNO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ROL = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    IDCONFREMEDY = Column(ForeignKey('MONITOR.CONF_REMEDY.IDCONFREMEDY'))
    CRITICIDAD = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERREG = Column(Integer, server_default=text("((0))"))
    ESTADO = Column(Boolean, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    ALP = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    IDLOGINITSM = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    PROYECTO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    CAT1 = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    CAT2 = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    CAT3 = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))

    CONF_REMEDY = relationship('CONFREMEDY')


class USUARIO(Base):
    __tablename__ = 'USUARIOS'
    __table_args__ = {'schema': 'MONITOR'}

    IDUSUARIO = None
    USUARIO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    PWD = Column(LargeBinary(8000))
    NOMBRE = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    APELLIDO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    CORREO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    TOKEN = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IDPERFIL_EMPLEADO = Column(ForeignKey('MONITOR.OPCIONES.IDOPCION'))
    IDUSERREG = Column(Integer)
    ESTADO = Column(Integer, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    TELEFONO = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    IDAREA = Column(ForeignKey('MONITOR.OPCIONES.IDOPCION'))

    OPCIONE = relationship('OPCIONE', primaryjoin='USUARIO.IDAREA == OPCIONE.IDOPCION')
    OPCIONE1 = relationship('OPCIONE', primaryjoin='USUARIO.IDPERFIL_EMPLEADO == OPCIONE.IDOPCION')


class CENTRALIZADORPERFIL(Base):
    __tablename__ = 'CENTRALIZADOR_PERFIL'
    __table_args__ = {'schema': 'MONITOR'}

    IDCENTRALIZADORPERFIL = None
    PERFIL = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IDCENTRALIZADOR = Column(ForeignKey('MONITOR.CENTRALIZADOR.IDCENTRALIZADOR'), nullable=False)
    IDTOOL = Column(ForeignKey('MONITOR.OPCIONES.IDOPCION'))
    PARENTID = Column(Integer, server_default=text("((0))"))
    IDUSERREG = Column(Integer, server_default=text("((0))"))
    ESTADO = Column(Boolean, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))

    CENTRALIZADOR = relationship('CENTRALIZADOR')
    OPCIONE = relationship('OPCIONE')


class CENTRALIZADORDETALLE(Base):
    __tablename__ = 'CENTRALIZADOR_DETALLE'
    __table_args__ = {'schema': 'MONITOR'}

    IDCENTRALIZADORDETALLE = None
    IDCENTRALIZADORPERFIL = Column(ForeignKey('MONITOR.CENTRALIZADOR_PERFIL.IDCENTRALIZADORPERFIL'))
    AVANZADO = Column(Boolean, server_default=text("((1))"))
    URL = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    HEAD = Column(String(2000, 'SQL_Latin1_General_CP1_CI_AS'))
    CONTENT = Column(String(8000, 'SQL_Latin1_General_CP1_CI_AS'))
    COMENTARIO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERREG = Column(Integer, server_default=text("((0))"))
    ESTADO = Column(Boolean, server_default=text("((1))"))
    SYSDATEREG = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDUSERLAST = Column(Integer)
    SYSDATELAST = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))

    CENTRALIZADOR_PERFIL = relationship('CENTRALIZADORPERFIL')