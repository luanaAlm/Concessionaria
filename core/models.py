from django.db import models


class Cliente(models.Model):
    ID_Cliente = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    mensagem = models.TextField()

    def __str__(self):
        template = '{0.nome} {0.email} {0.telefone} {0.mensagem}'
        return template.format(self)


class Banner1(models.Model):
    banner = models.URLField(max_length=400)
    titulo = models.CharField(max_length=40)

    def __str__(self):
        template = '{0.titulo}'
        return template.format(self)


class Banner2(models.Model):
    banner = models.URLField(max_length=400)
    titulo = models.CharField(max_length=40)

    def __str__(self):
        template = '{0.titulo}'
        return template.format(self)


class Carros(models.Model):
    CATERGORIA_CARRO_CHOICE = (
        ('Destaques', 'Destaques'),
        ('Seminovos', 'Seminovos'),
    )
    ID_Carro = models.AutoField(primary_key=True)
    categoria = models.CharField(
        max_length=100, choices=CATERGORIA_CARRO_CHOICE)

    # imagens
    imagem1 = models.URLField(max_length=300)
    imagem2 = models.URLField(max_length=300)
    imagem3 = models.URLField(max_length=300)
    imagem4 = models.URLField(max_length=300)
    imagem5 = models.URLField(max_length=300)

    marca = models.CharField(max_length=100)
    Modelo = models.CharField(max_length=100)
    AnoInicial = models.IntegerField()
    AnoFinal = models.IntegerField()
    versao = models.CharField(max_length=300)
    cambio = models.CharField(max_length=100)
    porta = models.IntegerField()
    combustivel = models.CharField(max_length=100)
    km = models.DecimalField(max_digits=19, decimal_places=3)
    obsAdicionais = models.TextField()
    finalPlaca = models.IntegerField()
    cor = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        template = '{0.ID_Carro} - {0.marca} - {0.Modelo}'
        return template.format(self)


class Depoimento (models.Model):
    ID_Depoimentos = models.AutoField(primary_key=True)
    imageDep = models.URLField(max_length=300)
    nome = models.CharField(max_length=100, blank=False, null=False)
    comentario = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        template = '{0.ID_Depoimentos} - {0.nome} '
        return template.format(self)
