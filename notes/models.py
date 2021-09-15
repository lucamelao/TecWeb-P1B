from django.db import models

# Create your models here.

# Nesse código cria-se um modelo chamado Note que possui um atributo title, que será 
# mapeado no banco de dados em uma coluna cujos valores são strings de no máximo 200 caracteres.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        # ID. TITULO
        return f"{self.id}. {self.title}"