from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import Agent
from .forms import FormulaireModel


def index(request):
    form_list = Agent.objects.order_by('id')

    # form = FormulaireForm()
    formulaire_model = FormulaireModel

    context = {'form_list': form_list, 'form': formulaire_model}

    return render(request, 'pages/index.html', context)


@require_POST
def addForm(request):
    # form = FormulaireForm(request.POST)
    formulaire_model = FormulaireModel(request.POST)

    if formulaire_model.is_valid():

        new_todo = formulaire_model.save()

    return redirect('index')
