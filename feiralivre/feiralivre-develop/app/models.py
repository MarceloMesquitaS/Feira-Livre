from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco_por_kg = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        abstract = True


class Verduras(Produto):
    estoque_verdura = models.IntegerField()

class Frutas(Produto):
    estoque_fruta = models.IntegerField()

class Entrega(models.Model):
    nome_cliente = models.CharField(max_length=255)
    endereco_entrega = models.TextField()
    data_entrega = models.DateTimeField()
    pagamento = models.OneToOneField('Pagamento', on_delete=models.CASCADE, related_name='entrega')

class Pagamento(models.Model):
    metodo_pagamento = models.CharField(max_length=50)
    valor_total = models.DecimalField(max_digits=8, decimal_places=2)

class Item(models.Model):
    entrega = models.ForeignKey(Entrega, on_delete=models.CASCADE, related_name="itens")
    nome_item = models.CharField(max_length=100)
    estoque_item = models.IntegerField()
    preco_item_uni = models.DecimalField(max_digits=6, decimal_places=2)

