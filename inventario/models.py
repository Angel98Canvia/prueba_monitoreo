from django.db import models

class BaseModel(models.Model):
    """
    For future abstraction.
    """
    class Meta:
        abstract=True # specify this model as an Abstract Model
        app_label = 'INVENTORY'

class PROYECTO(BaseModel):
    NOMBRE = models.CharField(max_length=255)
    ALP = models.CharField(max_length=100)
    FECHA_INICIO = models.DateField()
    FECHA_FIN = models.DateField()
    ESTADO = models.BooleanField()
    USUARIO_CREACION = models.CharField(max_length=255)
    FECHA_CREACION = models.DateTimeField()
    USUARIO_MODIFICACION = models.CharField(max_length=255)
    FECHA_MODIFICACION = models.DateTimeField()
    CLIENTE = models.CharField(max_length=250)
    PROYECTO_TIPO = models.CharField(max_length=300)
    PROYECTO_ESTADO = models.CharField(max_length=250)

    class Meta:
        db_table = 'PROYECTO'

class EQUIPO(BaseModel):
    ID_PROYECTO = models.ForeignKey('PROYECTO', on_delete=models.CASCADE)
    NOMBRE = models.CharField(max_length=255)
    DETALLE_ADMINISTRACION = models.CharField(max_length=255)
    DESCRIPCION = models.CharField(max_length=255)
    CONFIDENCIALIDAD = models.CharField(max_length=255)
    INTEGRIDAD = models.CharField(max_length=255)
    DISPONIBILIDAD = models.CharField(max_length=255)
    CRQ_ALTA = models.CharField(max_length=100)
    NRO_SERIE = models.CharField(max_length=100)
    DETALLE_PROPIEDAD = models.CharField(max_length=255)
    FECHA_ALTA = models.DateField()
    FECHA_BAJA = models.DateField()
    BAHIA_DESDE = models.CharField(max_length=155)
    BAHIA_HASTA = models.CharField(max_length=155)
    CANTIDAD_RU = models.CharField(max_length=255)
    NRO_CID = models.CharField(max_length=155)
    NRO_RANURAS = models.CharField(max_length=155)
    RANGO_RU_DESDE = models.CharField(max_length=100)
    RANGO_RU_HASTA = models.CharField(max_length=100)
    NOMBRE_VIRTUAL = models.CharField(max_length=255)
    TIPO_EQUIPO = models.CharField(max_length=150)
    NRO_CORE = models.CharField(max_length=100)
    NRO_CPU = models.CharField(max_length=100)
    CPU_DESCRIPCION = models.CharField(max_length=100)
    DISK_APROVISIONADO = models.CharField(max_length=100)
    DISK_ASIGNADO = models.CharField(max_length=100)
    RAM_ASIGNADO = models.CharField(max_length=100)
    ENERGIA_KW = models.CharField(max_length=100)
    ENERGIA_USO = models.CharField(max_length=100)
    ID_GENESYS = models.IntegerField()
    PART_NUMBER = models.CharField(max_length=150)
    FABRICANTE = models.CharField(max_length=255)
    PROVEEDOR = models.CharField(max_length=255)
    REFERENCIA_EXTERNA = models.CharField(max_length=255)
    LINEA_BASE = models.CharField(max_length=200)
    MONITOREO = models.CharField(max_length=200)
    ESTADO = models.BooleanField()
    USUARIO_CREACION = models.CharField(max_length=255)
    FECHA_CREACION = models.DateTimeField()
    USUARIO_MODIFICACION = models.CharField(max_length=255)
    FECHA_MODIFICACION = models.DateTimeField()
    TOKEN_ID = models.CharField(max_length=500)
    VERSION_SW = models.CharField(max_length=250)
    MODELO = models.CharField(max_length=250)
    ROL_USO = models.CharField(max_length=250)
    VCENTER = models.CharField(max_length=250)
    PROPIEDAD = models.CharField(max_length=250)
    FAMILIA = models.CharField(max_length=250)
    CLASE = models.CharField(max_length=250)
    ADMINISTRADOR = models.CharField(max_length=250)
    EQUIPO_ESTADO = models.CharField(max_length=250)
    PRIORIDAD = models.CharField(max_length=250)
    TIPO_SERVICIO = models.CharField(max_length=250)
    UBICACION = models.CharField(max_length=250)
    AMBIENTE = models.CharField(max_length=250)
    MARCA = models.CharField(max_length=250)
    SISTEMA_OPERATIVO = models.CharField(max_length=250)
    BACKUPS_CLOUD = models.CharField(max_length=200)
    MONITOREO_CLOUD = models.CharField(max_length=200)
    BACKUPS = models.CharField(max_length=200)
    NOMBRE_CI = models.CharField(max_length=300)
    TIPO_ALCANCE = models.CharField(max_length=300)
    ADMINISTRADOPOR = models.CharField(max_length=200)

    #PROYECTO = models.ForeignKey('PROYECTO', on_delete=models.CASCADE)

    class Meta:
        db_table = 'EQUIPO'


class EQUIPOIP(BaseModel):
    ID_EQUIPO = models.OneToOneField('EQUIPO', on_delete=models.CASCADE, primary_key=True)
    NRO_IP = models.CharField(max_length=200)
    MASCARA = models.CharField(max_length=200)
    COMENTARIO = models.CharField(max_length=200)
    ESTADO = models.BooleanField()
    USUARIO_CREACION = models.CharField(max_length=255)
    FECHA_CREACION = models.DateTimeField()
    USUARIO_MODIFICACION = models.CharField(max_length=255)
    FECHA_MODIFICACION = models.DateTimeField()
    TIPO_IP = models.CharField(max_length=200)

    #EQUIPO = models.ForeignKey('EQUIPO', on_delete=models.CASCADE)

    class Meta:
        db_table = 'EQUIPO_IP'