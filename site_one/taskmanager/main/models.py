from django.db import models

class Task(models.Model):
    title = models.CharField('Номер', max_length=50)
    task = models.TextField('Описание')
    status = models.CharField('Статус', max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
