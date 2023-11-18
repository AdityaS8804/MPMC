from django.db import models

# Create your models here.
class PlasticModel(models.Model):
    type=models.CharField(max_length=15)
    count=models.IntegerField(default=0)
    def __str__(self) -> str:
        #super().__str__()
        return f"{self.type} : {self.count}"
