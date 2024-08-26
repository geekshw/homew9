from django.db import models

# Create your models here.
class Settings(models.Model):
    title = models.CharField(
        max_length=155,
        verbose_name='Заголовка'
    )
    full_name = models.CharField(
        max_length=155,
        verbose_name='ФИО'
    )
    image = models.ImageField(
        upload_to='base',
        verbose_name='Фото'
    )
    image_main = models.ImageField(
        upload_to='base/',
        verbose_name='Фото- 2'
    )
    job = models.CharField(
        max_length=155,
        verbose_name='Позиция'
    )
    title_about = models.CharField(
        max_length=155,
        verbose_name='Заголовка о нас'
    )
    descriptions_about = models.TextField(
        verbose_name='Описание О нас'
    )
    image_abot = models.ImageField(
        upload_to='image/',
        verbose_name='Фото о нас'
    )
    title_team =  models.CharField(
        max_length=155,
        verbose_name='Заголовка Команды'
    )
    descriptions_team = models.TextField(
        verbose_name='Описание Команды'
    )

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural = 'Настройка главной'


class Image(models.Model):
    image = models.ImageField(
        upload_to='image/',
        verbose_name='Фото'
    )

    class Meta:
        verbose_name_plural = 'Фотография'

class About(models.Model):
    title = models.CharField(
        max_length=155,
    )
    image = models.ImageField(
        upload_to='image'
    )
    title2 = models.CharField(
        max_length=155
    )
    descriptions = models.TextField()
    video = models.CharField(
        max_length=155
    )
    image2 = models.ImageField(upload_to='video/')
     
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name_plural ='О нас'