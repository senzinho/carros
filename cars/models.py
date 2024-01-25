from django.db import models

class Brand(models.Model):
    id = models.AutoField(primary_key=True)#autoincremento
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
        # AQUI definimos que retorne no painel admin o modelo  do carro
        #e não retorne object(1)...]


class Car(models.Model): #class model onde herda model
    id = models.AutoField(primary_key=True)#autoincremento
    model = models.CharField(max_length=200)#model -> modelo Charfield-> string blank -> deixar em branco se quiser
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand') #relação entre tabeleas
    factory_year = models.IntegerField(blank=True,null=True)#tipo inteiro  podendo deixar o banco em branco e nem nulo
    model_year = models.IntegerField(blank=True,null=True)#tipo inteiro  podendo deixar o banco em branco e nem nulo
    plate = models.CharField(max_length=10, blank=True, null=True)
    value = models.FloatField(blank=True,null=True)#numero flutuante  podendo deixar o banco em branco e nem nulo
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True) ## description

    def __str__(self):
        return self.model
        # AQUI definimos que retorne no painel admin o modelo  do carro
        #e não retorne object(1)...]

class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at'] #ordenação decrescente

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'