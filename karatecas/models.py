from django.db import models

# Create your models here.

GENRE = (
    ('MAS', 'Masculino'),
    ('FEM', 'Feminino')
)
GRADUATION = (
    ('7kyu', 'Faixa Branca'),
    ('6kyu', 'Faixa Amarela'),
    ('5kyu', 'Faixa Vermelha'),
    ('4kyu', 'Faixa Laranja'),
    ('3kyu', 'Faixa Verde'),
    ('2kyu', 'Faixa Roxa'),
    ('1kyu', 'Faixa Marrom'),
    ('1dan', '1º Dan Faixa Preta'),
    ('2dan', '2º Dan Preta'),
    ('3dan', '3º Dan Preta'),
    ('4dan', '4º Dan Preta'),
    ('5dan', '5º Dan Preta'),
    ('6dan', '6º Dan Preta'),
    ('7dan', '7º Dan Preta'),
    ('8dan', '8º Dan Preta'),
    ('9dan', '9º Dan Preta'),
    ('10dan', '10º Dan Preta'),
)

class Karateca(models.Model):
    register = models.IntegerField()
    name     = models.CharField(max_length=200)
    graduation = models.CharField(max_length=60, choices=GRADUATION, blank=True, null=True)
    age      = models.IntegerField()
    genre    = models.CharField(
        max_length=60,
        choices=GENRE,
        blank=True,
        null=True 
    )
    street     = models.CharField(max_length=150)
    number     = models.IntegerField()
    zipcode    = models.CharField(max_length=16, blank=True, null=True)
    complement = models.CharField(max_length=60, blank=True, null=True)
    district   = models.CharField(max_length=160, blank=True, null=True)
    city       = models.CharField(max_length=160, blank=True, null=True)
    state      = models.CharField(max_length=160, blank=True, null=True)
    country    = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
