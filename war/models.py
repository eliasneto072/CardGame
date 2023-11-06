from django.db import models

from django.db import models

class Tipo(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Custo(models.Model):
    custo = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return str(self.custo)  # Convertendo o inteiro para string

class Feitico(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    img = models.ImageField(upload_to='feiticos')
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, related_name='feitiços', null=True, blank=True)
    
    def __str__(self):
        return self.nome

class Carta(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)
    ataque = models.IntegerField(null=True, blank=True)
    vida = models.IntegerField(null=True, blank=True)
    data_lancamento = models.DateTimeField(auto_created=True, blank=True)
    img = models.ImageField(upload_to='campeoes', null=True, blank=True)
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-data_lancamento']
        
    def __str__(self):
        return self.nome


class Habilidade(models.Model):
    carta = models.ForeignKey(Carta, on_delete=models.CASCADE, related_name='habilidades', null=True, blank=True)
    nome = models.CharField(max_length=100, null=True, blank=True)
    descricao = models.TextField(null=True, blank=True)
    custo = models.ForeignKey(Custo, on_delete=models.CASCADE, null=True, blank=True)
    img = models.ImageField(upload_to='habilidades', null=True, blank=True)
    
    def __str__(self):
        return f'{self.nome} : {self.carta.nome}'

    
    


    


