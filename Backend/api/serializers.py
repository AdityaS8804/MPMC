from rest_framework.serializers import ModelSerializer
from .models import PlasticModel
class PlasticSerializer(ModelSerializer):
    class Meta:
        model=PlasticModel
        fields='__all__'