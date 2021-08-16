from django.db import models
import importlib

# Create your models here.

class Node(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.name)


class GenericCapabilityEntry(models.Model):
    name = models.CharField(max_length=40)
    node = models.ForeignKey(Node, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    capability = "generic"

    def get_topic(self):
        return "home/" + self.node.name + "/" + self.capability + "/" + self.name


    @classmethod
    def get_model(cls, name):
        return getattr(importlib.import_module(__name__), name.capitalize()+'CapabilityEntry')


    @classmethod
    def get_serializer(cls, name):
        serializer_module=__name__.replace('model', 'seralizers')
        return getattr(importlib.import_module(serializer_module), name.capitalize()+'CapabilitySerializer')


    @classmethod
    def get_form(cls, name):
        form_module=__name__.replace('model', 'forms')
        return getattr(importlib.import_module(form_module), name.capitalize()+'CapabilityForm')

    @classmethod
    def get_capabilities(cls):
        return ['tapparelle', 'temperatura']


class TapparelleCapabilityEntry(GenericCapabilityEntry):
    capability = "tapparelle"
    timeout = models.IntegerField()
    pinUp = models.CharField(max_length=10)
    pinDown = models.CharField(max_length=10)


class TemperaturaCapabilityEntry(GenericCapabilityEntry):
    capability = "temperatura"
    update = models.IntegerField()
    pin = models.CharField(max_length=10)
    sensor = models.CharField(max_length=10)


class SwitchCapabilityEntry(GenericCapabilityEntry):
    capability = "switch"
    # Longer pin field because we can have multiple pins for a single switch
    pin = models.CharField(max_length=255)

    def __str__(self):
        return str(self.descrizione)


class ButtonCapabilityEntry(GenericCapabilityEntry):
    capability = "button"
    pin = models.CharField(max_length=10)
    # Multiple topic can be supported
    topic = models.ForeignKey(SwitchCapabilityEntry, on_delete=models.CASCADE)