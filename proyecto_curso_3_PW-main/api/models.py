from django.db import models


class boleteria(models.Model):
    concierto = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha_concierto = models.DateTimeField(auto_created=True)
    precio= models.BigIntegerField()
    
    
    
