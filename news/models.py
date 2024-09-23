from django.db import models

class articles(models.Model):
    title = models.CharField('Название', max_length = 50)
    text = models.TextField('Новость', max_length = 1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'