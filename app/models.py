from django.db import models


class Palestrante(models.Model):
    nome = models.CharField(max_length=50)
    bio = models.TextField()
    link = models.URLField()

    def __str__(self):
        return self.nome


class Palestra(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField()
    data = models.DateField()
    hora = models.TimeField()
    palestrante = models.ForeignKey(
        'Palestrante', related_name='palestras', on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
