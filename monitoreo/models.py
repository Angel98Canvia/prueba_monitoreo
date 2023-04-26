from django.db import models
from inventario.models import EQUIPO


class MONITOREOSOLICITUD(models.Model):
    #EQUIPO = models.OneToOneField(EQUIPO, on_delete=models.CASCADE)
    NOMBRE = models.CharField(max_length=100)
    MOTIVO = models.CharField(max_length=100)
    ESTADO = models.CharField(max_length=100)

    class Meta:
        db_table = 'MONITOREO_SOLICITUD'

class MONITOREOPOLITICA(models.Model):
    SOLICITUD = models.OneToOneField(MONITOREOSOLICITUD, on_delete=models.CASCADE)
    NOMBRE = models.CharField(max_length=100)
    ESTADO = models.CharField(max_length=100)
    VERSION = models.CharField(max_length=100)
    class Meta:
        db_table = 'MONITOREO_POLITICA'



class MONITOREOINVENTARIO(models.Model):
    POLITICA = models.ForeignKey(MONITOREOPOLITICA, on_delete=models.CASCADE)
    EQUIPO = models.ForeignKey(EQUIPO, on_delete=models.CASCADE)
    MONITOREADO = models.CharField(max_length=100)
    METODO_MONITOREO = models.CharField(max_length=100)
    VERSION_AGENTE = models.CharField(max_length=100)
    VERSION = models.CharField(max_length=100)

    class Meta:
        db_table = 'MONITOREO_INVENTARIO'

class CPUMEMORIA(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    MFU_UMBRAL_WARNING = models.CharField(max_length=100)
    MFU_UMBRAL_CRITICAL = models.CharField(max_length=100)
    MFU_UMBRAL_FATAL = models.CharField(max_length=100)
    MFU_INTEVALO_CAPTURA = models.CharField(max_length=100)
    MFU_NOMBRE_UMBRAL = models.CharField(max_length=100)
    SU_UMBRAL_WARNING = models.CharField(max_length=100)
    SU_UMBRAL_CRITICAL = models.CharField(max_length=100)
    SU_UMBRAL_FATAL = models.CharField(max_length=100)
    SU_INTEVALO_CAPTURA = models.CharField(max_length=100)
    SU_NOMBRE_UMBRAL = models.CharField(max_length=100)
    CU_UMBRAL_WARNING = models.CharField(max_length=100)
    CU_UMBRAL_CRITICAL = models.CharField(max_length=100)
    CU_INTEVALO_CAPTURA = models.CharField(max_length=100)
    CU_NOMBRE_UMBRAL = models.CharField(max_length=100)

    class Meta:
        db_table = 'CPU_MEMORIA'

class FILESYSTEM(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    METRICA_DISCO = models.CharField(max_length=100)
    UMBRAL_WANING = models.CharField(max_length=100)
    UMBRAL_CRITICAL = models.CharField(max_length=100)
    UMBRAL_FATAL = models.CharField(max_length=100)
    INTERVALO_CAPTURA = models.CharField(max_length=100)
    NOMBRE_UMBRAL = models.CharField(max_length=100)

    class Meta:
        db_table = 'FILE_SYSTEM'


class NETWORK(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    PROTOCOLO = models.CharField(max_length=100)
    PORT = models.CharField(max_length=100)
    INTERVALO = models.CharField(max_length=100)

    class Meta:
        db_table = 'NETWORK'

class SERVICIOS(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    SERVICIO_ASOCIADO = models.CharField(max_length=100)
    COMMAND = models.CharField(max_length=100)
    INTERVALO = models.CharField(max_length=100)

    class Meta:
        db_table = 'SERVICIOS'

class APLICACIONES(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    TIPO_MONITOREO = models.CharField(max_length=100)
    NOMBRE_MODULO = models.CharField(max_length=100)
    PATH = models.CharField(max_length=100)
    DATA = models.CharField(max_length=100)
    ALERTAS = models.CharField(max_length=100)
    SEVERIDAD = models.CharField(max_length=100)
    UMBRAL = models.CharField(max_length=100)
    OWNER = models.CharField(max_length=100)
    INTERVALO = models.CharField(max_length=100)
    class Meta:
        db_table = 'APLICACIONES'


class REDES(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    INTERFACES = models.CharField(max_length=100)
    DESCRIPCION = models.CharField(max_length=100)
    OBSERVACION = models.CharField(max_length=100)

    class Meta:
        db_table = 'REDES'


class WEBS(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    OBSERVACION = models.CharField(max_length=100)
    TIPO = models.CharField(max_length=100)
    MONITOREADO_DESDE = models.CharField(max_length=100)
    INTERVALO = models.CharField(max_length=100)

    class Meta:
        db_table = 'WEBS'

class INATIVIDADPROGRAMADA(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    LUNES = models.CharField(max_length=100)
    MARTES = models.CharField(max_length=100)
    MIERCOLES = models.CharField(max_length=100)
    JUEVES = models.CharField(max_length=100)
    VIERNES = models.CharField(max_length=100)
    SABADO = models.CharField(max_length=100)
    DOMINGO = models.CharField(max_length=100)

    class Meta:
        db_table = 'INATIVIDAD_PROGRAMADA'

class CAMBIOS(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    OBSERVACION = models.CharField(max_length=100)
    TIPO = models.CharField(max_length=100)
    MONITOREADO_DESDE = models.CharField(max_length=100)
    INTERVALO = models.CharField(max_length=100)

    class Meta:
        db_table = 'CAMBIOS'

class ALERTAS(models.Model):
    MONITOREO_INVENTARIO = models.ForeignKey(MONITOREOINVENTARIO, on_delete=models.CASCADE)
    OBSERVACION = models.CharField(max_length=100)
    TIPO = models.CharField(max_length=100)
    MONITOREADO_DESDE = models.CharField(max_length=100)
    INTERVALO = models.CharField(max_length=100)

    class Meta:
        db_table = 'ALERTAS'
