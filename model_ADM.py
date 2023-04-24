# coding: utf-8
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, LargeBinary, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class SESIONE(Base):
    __tablename__ = 'SESIONES'
    __table_args__ = {'schema': 'ADM'}

    IDSESION = None
    USUARIO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    JWT = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHAINI = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHAFIN = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    RESULT = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'))
    STATUS = Column(Boolean, server_default=text("((1))"))
    SYSDATE = Column(DateTime, server_default=text("(dateadd(hour,(-5),getdate()))"))


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


class AUDITORIA(Base):
    __tablename__ = 'AUDITORIA'
    __table_args__ = {'schema': 'ADM'}

    IDAUDITORIA = None
    USUARIO = Column(ForeignKey('MONITOR.USUARIOS.IDUSUARIO'))
    SO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    URL = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    BROWSER = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    HOSTNAME = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    IP = Column(String(40, 'SQL_Latin1_General_CP1_CI_AS'))
    OPERACION = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    RESULTADO = Column(String(255, 'SQL_Latin1_General_CP1_CI_AS'))
    SYSDATE = Column(DateTime, server_default=text("(getdate())"))

    USUARIO1 = relationship('USUARIO')