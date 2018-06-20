from django.db import models


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


class Agent(models.Model):
    nom = models.CharField(max_length=100)
    date = models.DateField(blank=True, auto_now_add=True)
    heure = models.TimeField(blank=False, null=False)
    nom_etablissement = models.CharField(max_length=400)
    type_etablissement = models.CharField(max_length=400)
    adresse = models.CharField(max_length=500)
    type_compte = models.CharField(max_length=8, choices=TYPE_CHOICES)
    type_client = models.CharField(max_length=8, choices=CLIENT_CHOICES)
    nom_client = models.CharField(max_length=200)
    numero = models.IntegerField()
    email = models.EmailField(blank=True, null=True)
    sexe = models.CharField(max_length=8, choices=SEXE_CHOICES)
    depot = models.CharField(max_length=30)

    def __str__(self):
        return self.nom
