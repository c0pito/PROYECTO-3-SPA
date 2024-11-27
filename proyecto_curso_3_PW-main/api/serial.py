from rest_framework import serializers

from.models import boleteria

class boleteriaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=boleteria
        fields= ['id','concierto','autor','fecha_concierto','precio']