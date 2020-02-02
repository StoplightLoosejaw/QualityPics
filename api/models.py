from django.db import models

# Create your models here.
class Pic(models.Model):
    category = models.CharField(max_length=255, default = 'OTHER' )
    url = models.CharField(max_length=255)
    available_flg = models.BooleanField(default = True)
    description = models.TextField(default = 'Пожалуй, лучшая картинка во всем интернете')

    
    def __str__(self):
        return self.name
