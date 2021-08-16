from rest_framework.serializers import ModelSerializer, SerializerMethodField
from . import models

class NodeSerializer(ModelSerializer):
    capabilities = SerializerMethodField()

    def get_capabilities(self, foo):
        cap=[]
        for c in models.capabilities:
            cap.append(c)
        return cap

    class Meta:
        model = models.Node
        fields = ['id', 'name', 'capabilities']


class TapparelleCapabilitySerializer(ModelSerializer):
    class Meta:
        model = models.TapparelleCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pinUp', 'pinDown', 'timeout']


class TemperaturaCapabilitySerializer(ModelSerializer):
    class Meta:
        model = models.TemperaturaCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pin', 'sensor', 'update']


class SwitchCapabilitySerializer(ModelSerializer):
    class Meta:
        model = models.SwitchCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pin']


class ButtonCapabilitySerializer(ModelSerializer):
    class Meta:
        model = models.ButtonCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pin', 'topic']