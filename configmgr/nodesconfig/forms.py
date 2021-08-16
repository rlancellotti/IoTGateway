from django.forms import ModelForm
from django.forms import HiddenInput
from . import models


class NodeForm(ModelForm):
    class Meta:
        model = models.Node
        fields = ['id', 'name']


class TapparelleCapabilityForm(ModelForm):
    class Meta:
        model = models.TapparelleCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pinUp', 'pinDown', 'timeout']


class TemperaturaCapabilityForm(ModelForm):
    class Meta:
        model = models.TemperaturaCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pin', 'sensor', 'update']


class SwitchCapabilityForm(ModelForm):
    class Meta:
        model = models.SwitchCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pin']


class ButtonCapabilityForm(ModelForm):
    class Meta:
        model = models.ButtonCapabilityEntry
        fields = ['id', 'name', 'description', 'node', 'pin', 'topic']