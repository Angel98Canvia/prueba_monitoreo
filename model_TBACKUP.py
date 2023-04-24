# coding: utf-8
from sqlalchemy import Boolean, CHAR, Column, Date, DateTime, ForeignKey, Integer, String, Table, text
from sqlalchemy.orm import relationship
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


t_POLI_TAREA = Table(
    'POLI_TAREA', metadata,
    Column('ID_POLI_TAREA', Integer),
    Column('ID_POLITICA', Integer),
    Column('ID_BKVERSION', Integer),
    Column('NOMBRE_TAREA', String(250, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('HORA_VINICIO', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('HORA_VFIN', String(20, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BKS_LUN', Integer),
    Column('BKS_MAR', Integer),
    Column('BKS_MIE', Integer),
    Column('BKS_JUEV', Integer),
    Column('BKS_VIE', Integer),
    Column('BKS_SAB', Integer),
    Column('BKS_DOM', Integer),
    Column('BKS_ELIMINAR_CONT', Integer),
    Column('TIPO_BACKUP', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FRECUENCIA', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CONTENIDO', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MODO', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('HERRAMIENTA', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PROTECCION', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('MEDIO', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('CELL_MANAGER', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BKS_DEPEND', Integer),
    Column('ACCION', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ACLARACION', String(250, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('PROCESO_ESTADO', String(200, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BKS_TAMDAT', String(10, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BKS_DETRES', String(200, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BKS_SERVER', String(collation='SQL_Latin1_General_CP1_CI_AS')),
    Column('TIPO_TAREA', String(80, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BK_LIB_ID', Integer),
    Column('BKLIB_DRIVE', String(30, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('DETALLE_DEPENDENCIA', String(250, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('HORA_ESTIMADO', Integer),
    Column('MINUTO_ESTIMADO', Integer),
    Column('BKP_TNAMEOLD', String(80, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('BKP_BD', String(100, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('COMENTARIO', String(700, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('ESTADO', CHAR(1, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('USUARIO_CREACION', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FECHA_CREACION', DateTime),
    Column('USUARIO_MODIFICACION', String(50, 'SQL_Latin1_General_CP1_CI_AS')),
    Column('FECHA_MODIFICACION', DateTime),
    schema='TBACKUP'
)


class SOLIHORATAREA(Base):
    __tablename__ = 'SOLI_HORA_TAREA'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_SOLI_HORA_TAREA = None
    ID_SOLI_TAREA = Column(Integer)
    DESCRIPCION = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    OBSERVACION = Column(String(300, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)


class SOLIRUTATAREA(Base):
    __tablename__ = 'SOLI_RUTA_TAREA'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_SOLI_RUTA_TAREA = None
    ID_SOLI_TAREA = Column(Integer)
    DESCRIPCION = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    EXCEPCION = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    ID_EQUIPO = Column(Integer)
    UNIDAD = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    PARAMETRO = Column(String(500, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)


class SOLITAREA(Base):
    __tablename__ = 'SOLI_TAREA'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_SOLI_TAREA = None
    ID_POLI_TAREA = Column(Integer)
    NOMBRE_TAREA = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    HORA_VINICIO = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    HORA_VFIN = Column(String(20, 'SQL_Latin1_General_CP1_CI_AS'))
    BKS_LUN = Column(Integer)
    BKS_MAR = Column(Integer)
    BKS_MIE = Column(Integer)
    BKS_JUEV = Column(Integer)
    BKS_VIE = Column(Integer)
    BKS_SAB = Column(Integer)
    BKS_DOM = Column(Integer)
    BKS_ELIMINAR_CONT = Column(Integer)
    TIPO_BACKUP = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    FRECUENCIA = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CONTENIDO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    MODO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    HERRAMIENTA = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    PROTECCION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    MEDIO = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    CELL_MANAGER = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    BKS_DEPEND = Column(Integer)
    ACCION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    ACLARACION = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    PROCESO_ESTADO = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ID_SOLICITUD = Column(Integer)
    BKS_TAMDAT = Column(String(10, 'SQL_Latin1_General_CP1_CI_AS'))
    BKS_DETRES = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    BKS_SERVER = Column(String(collation='SQL_Latin1_General_CP1_CI_AS'))
    TIPO_TAREA = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    BK_LIB_ID = Column(Integer)
    BKLIB_DRIVE = Column(String(30, 'SQL_Latin1_General_CP1_CI_AS'))
    DETALLE_DEPENDENCIA = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    HORA_ESTIMADO = Column(Integer)
    MINUTO_ESTIMADO = Column(Integer)
    BKP_TNAMEOLD = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    BKP_BD = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    COMENTARIO = Column(String(700, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)


class SOLITAREAAPROB(Base):
    __tablename__ = 'SOLI_TAREA_APROB'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_SOLI_TAREA_APROB = None
    ID_SOLI_TAREA = Column(Integer)
    NOMBRE_TAREA = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    APROBADOR = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO_APROB = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO_SOLICITUD = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ACCION = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    ROL_APROB = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(150, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)


class SOLITAREASERVER(Base):
    __tablename__ = 'SOLI_TAREA_SERVER'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_SOLI_TAREA = Column(Integer, nullable=False)
    ID_EQUIPO = Column(Integer)
    ESTADO = Column(CHAR(1, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(50, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)
    ID_SOLI_TAREA_SERVER = None


class VERSION(Base):
    __tablename__ = 'VERSION'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_BKVERSION = Column(Integer, primary_key=True, nullable=False)
    ID_POLITICA = Column(Integer, primary_key=True, nullable=False)
    FECHA_VERSION = Column(DateTime)
    ID_SOLICITUD = Column(Integer)
    MOTIVO = Column(String(400, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_MODIFICACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))


class GRUPO(Base):
    __tablename__ = 'GRUPO'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_GRUPO = None
    DESCRIPCION = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ID_PROYECTO = Column(ForeignKey('MANAGEMENT.PROYECTO.ID_PROYECTO'))
    ESTADO = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)

    PROYECTO = relationship('PROYECTO')


class POLITICA(Base):
    __tablename__ = 'POLITICA'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_POLITICA = None
    ID_GRUPO = Column(ForeignKey('TBACKUP.GRUPO.ID_GRUPO'))
    FECHA_VERSION = Column(DateTime)
    ID_BKVERSION = Column(Integer)
    ID_SOLICITUD = Column(Integer)
    MOTIVO = Column(String(400, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)

    GRUPO = relationship('GRUPO')


class SOLICITUD(Base):
    __tablename__ = 'SOLICITUD'
    __table_args__ = {'schema': 'TBACKUP'}

    ID_SOLICITUD = None
    FECHA_REGISTRO = Column(DateTime)
    FECHA_ACTUALIZACION = Column(DateTime)
    SOLICITANTE = Column(String(100, 'SQL_Latin1_General_CP1_CI_AS'))
    ETAPA = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    TIPO_SOL = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    MOTIVO = Column(String(400, 'SQL_Latin1_General_CP1_CI_AS'))
    ACTOR_ACTUAL = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ACTOR_SIGUIENTE = Column(String(200, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO_ACTUAL = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    ESTADO_SIGUIENTE = Column(String(250, 'SQL_Latin1_General_CP1_CI_AS'))
    USUARIO_CREACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_CREACION = Column(DateTime)
    USUARIO_MODIFICACION = Column(String(80, 'SQL_Latin1_General_CP1_CI_AS'))
    FECHA_MODIFICACION = Column(DateTime)
    ID_GRUPO = Column(ForeignKey('TBACKUP.GRUPO.ID_GRUPO'))

    GRUPO = relationship('GRUPO')