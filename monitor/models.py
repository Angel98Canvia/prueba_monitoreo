from django.db import models

class BaseModel(models.Model):
    """
    For future abstraction.
    """
    class Meta:
        abstract=True # specify this model as an Abstract Model
        app_label = 'MONITOR'

class CONFREMEDY(BaseModel):

    IDCONFREMEDY = models.AutoField(primary_key=True)
    IDATRIBUTO = models.CharField(max_length=255)
    ATRIBUTO = models.CharField(max_length=255)
    DEPENDENCIA1 = models.CharField(max_length=255)
    DEPENDENCIA2 = models.CharField(max_length=255)
    TIPO = models.CharField(max_length=50)
    IDUSERREG = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=True)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField(null=True, blank=True)
    SYSDATELAST = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'CONF_REMEDY'

class CONTROLITSM(BaseModel):
    IDCONTROLITSM = models.AutoField(primary_key=True)
    IDCENTRALIZADOR = models.IntegerField()
    URL = models.CharField(max_length=300)
    HEAD = models.CharField(max_length=2000)
    BODY = models.CharField(max_length=8000)
    TIPO = models.CharField(max_length=50)
    IDUSERREG = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=True)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField(null=True, blank=True)
    SYSDATELAST = models.DateTimeField(auto_now=True)
    PRIORIDAD = models.SmallIntegerField()
    TICKETID = models.CharField(max_length=20)
    class Meta:
        db_table = 'CONTROL_ITSM'

class MATRIZPRIORIDAD(BaseModel):
    IDMATRIZ = models.AutoField(primary_key=True)
    IMPACTO = models.SmallIntegerField(default=0)
    URGENCIA = models.SmallIntegerField(default=0)
    PRIORIDAD = models.SmallIntegerField(default=0)
    TIPO = models.CharField(max_length=20)
    OWNERGROUP = models.CharField(max_length=300)
    OWNERGROUPID = models.CharField(max_length=300)
    ESTADO = models.IntegerField(default=1)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField(null=True, blank=True)
    SYSDATELAST = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'MATRIZ_PRIORIDAD'

class MONITOR(BaseModel):
    IDMONITOR = models.AutoField(primary_key=True)
    CLIENT = models.CharField(max_length=100, null=True, blank=True)
    ALERTID = models.CharField(max_length=255, null=True, blank=True)
    ALERTSTATE = models.CharField(max_length=50, null=True, blank=True)
    TICKETID = models.CharField(max_length=50, null=True, blank=True)
    TICKETSTATE = models.CharField(max_length=50, null=True, blank=True)
    OWNERGROUP = models.CharField(max_length=255, null=True, blank=True)
    PRIORITY = models.CharField(max_length=255, null=True, blank=True)
    SYSLASTDATE = models.DateTimeField(auto_now=True)
    SYSSTARTDATE = models.DateTimeField(auto_now_add=True)
    URLTICKET = models.CharField(max_length=255, null=True, blank=True)
    DISPOSITIVO = models.CharField(max_length=255, null=True, blank=True)
    STATUS = models.BooleanField(default=True)
    ESTADO = models.CharField(max_length=30, default='PENDIENTE')
    class Meta:
        db_table = 'MONITOR'

class OPCIONE(BaseModel):
    IDOPCION = models.AutoField(primary_key=True)
    ATRIBUTO = models.CharField(max_length=512)
    VALOR = models.CharField(max_length=512)
    ICON = models.CharField(max_length=255)
    URI = models.CharField(max_length=300)
    PRIORIDAD = models.IntegerField()
    PARENTID = models.IntegerField()
    TIPOATRIBUTO = models.CharField(max_length=255)
    IDUSERREG = models.IntegerField()
    ESTADO = models.IntegerField(default=1)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField()
    SYSDATELAST = models.DateTimeField(auto_now=True)
    VALOR1 = models.CharField(max_length=512)
    VALOR2 = models.CharField(max_length=255, default='')
    VALOR3 = models.CharField(max_length=255, default='')
    ENTERO1 = models.IntegerField(default=0)
    ENTERO2 = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'OPCIONES'


class CENTRALIZADOR(BaseModel):
    IDCENTRALIZADOR = models.AutoField(primary_key=True)
    CENTRALIZADOR = models.CharField(max_length=255)
    IDCLIENTE = models.ForeignKey(OPCIONE, on_delete=models.CASCADE)
    PARENTID = models.IntegerField(default=0)
    IDUSERREG = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=True)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField(default=0)
    SYSDATELAST = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'CENTRALIZADOR'

class INVENTARIO(BaseModel):
    IDINVENTARIO = models.AutoField(primary_key=True)
    CLIENT = models.CharField(max_length=255)
    HOSTNAME = models.CharField(max_length=255)
    IP = models.CharField(max_length=50)
    ENTORNO = models.CharField(max_length=50)
    ROL = models.CharField(max_length=50)
    IDCONFREMEDY = models.ForeignKey('CONFREMEDY', on_delete=models.CASCADE)
    CRITICIDAD = models.CharField(max_length=20)
    IDUSERREG = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=True)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField()
    SYSDATELAST = models.DateTimeField(auto_now=True)
    ALP = models.CharField(max_length=20)
    IDLOGINITSM = models.CharField(max_length=20)
    PROYECTO = models.CharField(max_length=255)
    CAT1 = models.CharField(max_length=255)
    CAT2 = models.CharField(max_length=255)
    CAT3 = models.CharField(max_length=255)
    class Meta:
        db_table = 'INVENTARIO'

class USUARIO(BaseModel):
    IDUSUARIO = models.AutoField(primary_key=True)
    USUARIO = models.CharField(max_length=50)
    PWD = models.BinaryField(max_length=8000)
    NOMBRE = models.CharField(max_length=255)
    APELLIDO = models.CharField(max_length=255)
    CORREO = models.CharField(max_length=255)
    TOKEN = models.CharField(max_length=255)
    IDPERFIL_EMPLEADO = models.ForeignKey('OPCIONE', on_delete=models.CASCADE, related_name='perfil_empleado')
    IDUSERREG = models.IntegerField()
    ESTADO = models.IntegerField(default=1)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField()
    SYSDATELAST = models.DateTimeField(auto_now=True)
    TELEFONO = models.CharField(max_length=20, default='')
    IDAREA = models.ForeignKey('OPCIONE', on_delete=models.CASCADE, related_name='area')
    class Meta:
        db_table = 'USUARIOS'

class CENTRALIZADORPERFIL(BaseModel):
    IDCENTRALIZADORPERFIL = models.AutoField(primary_key=True)
    PERFIL = models.CharField(max_length=255)
    IDCENTRALIZADOR = models.ForeignKey('CENTRALIZADOR', on_delete=models.CASCADE)
    IDTOOL = models.ForeignKey('OPCIONE', on_delete=models.CASCADE)
    PARENTID = models.IntegerField(default=0)
    IDUSERREG = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=True)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField(default=0)
    SYSDATELAST = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'CENTRALIZADOR_PERFIL'

class CENTRALIZADORDETALLE(BaseModel):
    IDCENTRALIZADORDETALLE = models.AutoField(primary_key=True)
    IDCENTRALIZADORPERFIL = models.ForeignKey('CENTRALIZADORPERFIL', on_delete=models.CASCADE)
    AVANZADO = models.BooleanField(default=True)
    URL = models.CharField(max_length=255)
    HEAD = models.CharField(max_length=2000)
    CONTENT = models.CharField(max_length=8000)
    COMENTARIO = models.CharField(max_length=255)
    TIPO = models.CharField(max_length=50)
    IDUSERREG = models.IntegerField(default=0)
    ESTADO = models.BooleanField(default=True)
    SYSDATEREG = models.DateTimeField(auto_now_add=True)
    IDUSERLAST = models.IntegerField(default=0)
    SYSDATELAST = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'CENTRALIZADOR_DETALLE'