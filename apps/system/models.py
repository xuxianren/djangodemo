from django.db import models

# Create your models here.
class System(models.Model):
    cnname = models.CharField("系统中文名称", max_length=256)
    enname = models.CharField("系统英文名称", max_length=256)
    desc   = models.CharField("系统描述", max_length=256)
