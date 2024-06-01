from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import *
from .models import SocieteAviation, TrajetVoyage
from .forms import VoyageForm


def societe_aviation(request):
    societes = SocieteAviation.objects.all().order_by('id')
    template_name = 'other/societe_voyage.html'
    context = {
        'societes': societes
    }
    return render(request, template_name, context)

def detail_societe_aviation(request, slug):
    societe = get_object_or_404(SocieteAviation, slug=slug)
    trajets = TrajetVoyage.objects.filter(societe=societe)
    template_name = 'other/trajet_voyage.html'
    context = {
        'societe': societe,
        'trajets': trajets,
    }
    return render(request, template_name, context)

########## Voyage Management ##########
class Societes_aviation(View, LoginRequiredMixin):
    template_name = 'back/voyage.html'
    def get(self, request, *args, **kwargs):
        voyage = SocieteAviation.objects.all()
        context = {
            'voyage': voyage,
        }
        return render(request, self.template_name, context)

class AddVoyage(CreateView, LoginRequiredMixin):
    model = SocieteAviation
    form_class = VoyageForm
    template_name = 'back/add-voyage.html'
    success_url = '/back/voyage'

class Updatesociete_aviation(UpdateView, LoginRequiredMixin):
    model = societe_aviation
    template_name = 'back/update-societe_aviation.html'
    success_url = '/back/societe_aviations'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["secteurs"] = Secteur.objects.all()
    #     return context

@login_required
def Deletesociete_aviation(request, pk):
    template_name = 'back/delete-societe_aviation.html'
    societe_aviation = societe_aviation.objects.get(pk=pk)
    if request.method == "POST":
        societe_aviation.delete()
        return HttpResponseRedirect('/back/societe_aviations')
    context = {
        'societe_aviation': societe_aviation,
    }
    return render(request, template_name, context)



def livraison(request):
    template_name = 'other/livraison.html'
    context = {}
    return render(request, template_name, context)


def immobilier(request):
    template_name = 'other/immobilier.html'
    context = {}
    return render(request, template_name, context)


def decoration(request):
    template_name = 'other/decoration.html'
    context = {}
    return render(request, template_name, context)


def assurance(request):
    template_name = 'other/assurance.html'
    context = {}
    return render(request, template_name, context)


def evenement(request):
    template_name = 'other/evenement.html'
    context = {}
    return render(request, template_name, context)


def mecanique(request):
    template_name = 'other/mecanique.html'
    context = {}
    return render(request, template_name, context)


def formation(request):
    template_name = 'other/formation.html'
    context = {}
    return render(request, template_name, context)


def contact(request):
    template_name = 'other/contact.html'
    context = {}
    return render(request, template_name, context)
