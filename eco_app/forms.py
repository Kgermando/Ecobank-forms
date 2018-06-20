from django import forms
from .models import Agent
from datetime import date

TYPE_CHOICES = (
    ('EPARGNE', 'Epargne'),
    ('COURANT', 'Courant'),
)
CLIENT_CHOICES = (
    ('INDIVIDU', 'Individu'),
    ('AGENT', 'Agent'),
    ('MARCHANT', 'Marchant'),
)
SEXE_CHOICES = (
    ('MAXCULIN', 'Masculin'),
    ('FEMININ', 'Feminin'),
)


class FormulaireForm(forms.Form):
    nom = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Mettez votre Nom et Prénom"}))
    date = forms.DateField(required=True, widget=forms.SelectDateWidget)
    heure = forms.TimeField(required=True)
    nom_etablissement = forms.CharField(max_length=400, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Mettez le Nom de l'établissement"}))
    type_etablissement = forms.CharField(max_length=400, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Mettez le type de l'établissement"}))
    adresse = forms.CharField(max_length=500, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Mettez C/ Q/ Av/ N/"}))

    type_client = forms.CharField(max_length=8, widget=forms.Select(choices=TYPE_CHOICES))
    type_compte = forms.CharField(max_length=8, widget=forms.Select(choices=CLIENT_CHOICES))
    nom_client = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Mettez le Nom du client'}))
    numero = forms.IntegerField()
    email = forms.EmailField(required=True)
    sexe = forms.CharField(max_length=8, widget=forms.Select(choices=SEXE_CHOICES))
    depot = forms.CharField(max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Dépot en USD ou CDF"}))


class FormulaireModel(forms.ModelForm):
    class Meta:
        model = Agent
        fields = ['nom', 'heure', 'nom_etablissement', 'type_etablissement', 'adresse', 'type_compte', 'type_client', 'nom_client', 'numero', 'email', 'sexe', 'depot']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mettez votre Nom et Prénom"}),
            'nom_etablissement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mettez le Nom de l'établissement"}),
            'type_etablissement': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mettez le type de l'établissement"}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Mettez  Numéro°/ Avenue/ Quartier/ Commune/ Ville/"}),
            'nom_client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mettez le Nom du client'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Mettez l'adresse mail du client ex: example@xxx.com"}),
            'depot': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Dépot en USD ou CDF"}),
        }
