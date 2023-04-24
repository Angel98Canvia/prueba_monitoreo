# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, LargeBinary, SmallInteger, String, text
from sqlalchemy.dialects.mssql import TINYINT
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


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


class HORARIO(Base):
    __tablename__ = 'HORARIO'
    __table_args__ = {'schema': 'ROBOTDIALER'}

    IDHORARIO = None
    HORARIO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("(NULL)"))
    HORA = Column(String(25, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    DIA = Column(String(62, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    MES = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    DIASEMANA = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'))
    IDUSERREG = Column(Integer)
    IDUSERLAST = Column(Integer)
    STATUS = Column(Boolean, server_default=text("((1))"))
    SYSLASTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    SYSSTARTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))


class QUEUE(Base):
    __tablename__ = 'QUEUE'
    __table_args__ = {'schema': 'ROBOTDIALER'}

    IDQUEUE = None
    CLIENTE = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IDMONITOR = Column(Integer)
    DISPOSITIVO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPOMONITOREO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    NOMBRE = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    CORREO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    TELEFONO = Column(String(15, 'SQL_Latin1_General_CP1_CI_AS'))
    ROL = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    AREA = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPOESCALABILIDAD = Column(TINYINT)
    ORDENROL = Column(SmallInteger, server_default=text("((0))"))
    ORDENESCALABILIDAD = Column(SmallInteger, server_default=text("((0))"))
    IDUSERREG = Column(Integer)
    IDUSERLAST = Column(Integer)
    STATUS = Column(Boolean, server_default=text("((1))"))
    SYSLASTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    SYSSTARTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    CANALES = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IDESCALABILIDAD = Column(Integer, server_default=text("((0))"))


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


class RESULTADO(Base):
    __tablename__ = 'RESULTADOS'
    __table_args__ = {'schema': 'ROBOTDIALER'}

    IDRESULTADO = None
    IDQUEUE = Column(ForeignKey('ROBOTDIALER.QUEUE.IDQUEUE'))
    CANAL = Column(String(120, 'SQL_Latin1_General_CP1_CI_AS'))
    SID = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ORIGEN = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    DESTINO = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    DIGITOS = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    SYSDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))

    QUEUE = relationship('QUEUE')


class HORARIOUSUARIO(Base):
    __tablename__ = 'HORARIO_USUARIO'
    __table_args__ = {'schema': 'ROBOTDIALER'}

    IDHORARIOUSUARIO = None
    IDHORARIO = Column(ForeignKey('ROBOTDIALER.HORARIO.IDHORARIO'))
    IDUSUARIO = Column(ForeignKey('MONITOR.USUARIOS.IDUSUARIO'))
    IDROL = Column(ForeignKey('MONITOR.OPCIONES.IDOPCION'))
    IDAREA = Column(ForeignKey('MONITOR.OPCIONES.IDOPCION'))
    ORDEN = Column(SmallInteger, server_default=text("((0))"))
    IDUSERREG = Column(Integer)
    IDUSERLAST = Column(Integer)
    STATUS = Column(Boolean, server_default=text("((1))"))
    SYSLASTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    SYSSTARTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    CANALES = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))

    OPCIONE = relationship('OPCIONE', primaryjoin='HORARIOUSUARIO.IDAREA == OPCIONE.IDOPCION')
    HORARIO = relationship('HORARIO')
    OPCIONE1 = relationship('OPCIONE', primaryjoin='HORARIOUSUARIO.IDROL == OPCIONE.IDOPCION')
    USUARIO = relationship('USUARIO')


class ESCALABILIDAD(Base):
    __tablename__ = 'ESCALABILIDAD'
    __table_args__ = {'schema': 'ROBOTDIALER'}

    IDESCALABILIDAD = None
    PROYECTO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    ALP = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'), server_default=text("('')"))
    IDROL_AREA = Column(ForeignKey('ROBOTDIALER.HORARIO_USUARIO.IDHORARIOUSUARIO'))
    TIPOESCALABILIDAD = Column(TINYINT)
    ORDEN = Column(SmallInteger, server_default=text("((0))"))
    IDUSERREG = Column(Integer)
    IDUSERLAST = Column(Integer)
    STATUS = Column(Boolean, server_default=text("((1))"))
    SYSLASTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    SYSSTARTDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))
    IDPERFIL = Column(Integer)

    HORARIO_USUARIO = relationship('HORARIOUSUARIO')