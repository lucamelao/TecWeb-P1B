from django.shortcuts import render, redirect
from .models import Note


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        # Criando um novo Note (objeto) no banco de dados
        new_note = Note(title = title, content = content)
        # Salva o objeto no db
        new_note.save()
        return redirect('index')
    else:
    # o modelo Note é importado e são carregadas todas as entradas dessa tabela 
    # Carregando os dados do banco de dados, tem todas as notas contidas nele
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})