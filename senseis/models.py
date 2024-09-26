from django.db import models


# Create your models here.
FAIXA =(
    ('1Dan', '1º Dan - Faixa preta'),
    ('2Dan', '2º Dan - Faixa preta'),
    ('3Dan', '3º Dan - Faixa preta'),
    ('4Dan', '4º Dan - Faixa preta'),
    ('5Dan', '5º Dan - Faixa preta'),
    ('6Dan', '6º Dan - Faixa preta'),
    ('7Dan', '7º Dan - Faixa preta'),
    ('8Dan', '8º Dan - Faixa preta'),
    ('9Dan', '9º Dan - Faixa preta'),
    ('10Dan', '10º Dan - Faixa preta'),
)

class Sensei(models.Model):
    name       = models.CharField(max_length=200)
    cpf        = models.CharField(max_length=15)
    graduation = models.CharField(max_length=60, choices=FAIXA,blank=True, null=True)
    email      = models.CharField(max_length=150, blank=True, null=True)
    celPhone   = models.CharField(max_length=60)

    def __str__(self):
        return self.name