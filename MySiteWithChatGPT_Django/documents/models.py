from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=100)  # Название документа
    content = models.TextField()  # Содержание документа
    folder = models.ForeignKey('Folder', related_name='documents', on_delete=models.CASCADE)  # Ссылка на папку

    def __str__(self):
        return self.title


class Folder(models.Model):
    name = models.CharField(max_length=100)  # Название папки

    def __str__(self):
        return self.name
