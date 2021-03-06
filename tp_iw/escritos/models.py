from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone


#este es el modelo de los escritos 
class Escrito(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    created_date = models.DateTimeField(
        default=timezone.now)
    date = models.DateTimeField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='post_escritos', blank=True)

    def total_likes(self):
        return self.likes.count()


    def publish(self): #cambia el datetime de publicacion cuando se clickea en publicar 
        self.date = timezone.now()
        self.save()    
    
    def get_detail_url(self): #devuelve url en home
        url = 'escrito_detail'
        return url

    def __str__(self):
        return self.title + ' | ' + str(self.author)




