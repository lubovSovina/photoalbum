from django.db import models
from ..user.models import User


class Photo(models.Model):
    name = models.CharField('Название', max_length=50)
    date = models.DateTimeField('Дата создания', auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField('Фотография', upload_to='image/', default=None)

    def __str__(self):
        return self.name
