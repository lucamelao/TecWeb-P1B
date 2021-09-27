from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        # TAG
        return f"{self.name}"

# Nesse código cria-se um modelo chamado Note que possui um atributo title, que será 
# mapeado no banco de dados em uma coluna cujos valores são strings de no máximo 200 caracteres.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tag = models.ForeignKey(Tag, null = True, on_delete = models.SET_NULL)

    def __str__(self):
        # ID. TITULO
        return f"{self.id}. {self.title}"