from django.shortcuts import render
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.http import HttpResponse
from django.template import loader
from django.forms import modelformset_factory

from rest_framework.parsers import JSONParser
import importlib

from . import serializers
from . import models
from . import forms

# Create your views here.
#######################################################################################################################
# Form-based interface: server-side only
#######################################################################################################################

def node_form(request):
    # NodeFormset=modelformset_factory(models.Node, form=forms.NodeForm)
    NodeFormset = modelformset_factory(models.Node, form=forms.NodeForm, can_delete=True)
    if request.method == 'POST':
        formset = NodeFormset(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = NodeFormset()
    return render(request, 'nodes.html', {'formset': formset, "capabilities": models.GenericCapabilityEntry.get_capabilities()})


def capability_form(request, node_id, capability):
    # get model class
    if capability in models.capabilities:
        # cap = models.capabilities[capability]
        # print(cap["name"])
        model = models.GenericCapabilityEntry.get_model(capability)
        form = models.GenericCapabilityEntry.get_form(capability)
        print("model is " + str(model))
        print("form is " + str(form))
    else:
        raise Http404('Capability not found')
    CapabilityFormset = modelformset_factory(model, form=form, can_delete=True)
    if request.method == 'POST':
        formset = CapabilityFormset(request.POST, queryset=model.objects.filter(node__exact=node_id))
        if formset.is_valid():
            formset.save()
    else:
        formset = CapabilityFormset(queryset=model.objects.filter(node__exact=node_id))
    return render(request, 'capabilities.html', {'formset': formset})


#######################################################################################################################
