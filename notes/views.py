from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        tag = request.POST.get('tag')
        # filtra dentre as tags, a tag com o nome
        filtered_tags = Tag.objects.filter(name = tag)

        # Cada anotação pode ter no máximo uma tag (pode não ter nenhuma)
        
        # para o caso de não ter nenhuma
        if len(filtered_tags) == 0:
            new_tag = Tag(name = tag)
            new_tag.save()
        else:
            # caso já tenha
            new_tag = filtered_tags[0]

        # Criando um novo Note (objeto) no banco de dados
        new_note = Note(title = title, content = content, tag = new_tag)
        # Salva o objeto no db
        new_note.save()
        return redirect('index')
    else:
    # o modelo Note é importado e são carregadas todas as entradas dessa tabela 
    # Carregando os dados do banco de dados, tem todas as notas contidas nele
        notes = Note.objects.all()
        tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': notes, 'tags': tags})

def remove_note(request):
    if request.method == 'POST':
        # pega o ID da note que será removida
        id = request.POST.get('id')
        tag_name = request.POST.get('tag')
        # filtra pelo ID pego na linha anterior e deleta do db
        Note.objects.filter(id=id).delete()

        tag = Tag.objects.filter(name = tag_name)[0]
        if tag is not None:
            notes_with_tag = Note.objects.filter(tag = tag)
            # se não houver notes com a tag em questão
            if len(notes_with_tag) == 0:
                Tag.objects.filter(name = tag).delete()
                
        return redirect('index')
    else:
        notes = Note.objects.all()
        tags = Tag.objects.all()
        return render(request, 'notes/index.html', {'notes': notes}, {'tags': tags})
    
def update_note(request):
    if request.method == 'POST':
        # pega as informações da note editada
        id = request.POST.get('id')
        title = request.POST.get('title')
        content = request.POST.get('content')
        # Atualiza a note no db
        Note.objects.filter(id=id).update(title = title, content = content)
        return redirect('index')
    else:
    # o modelo Note é importado e são carregadas todas as entradas dessa tabela 
    # Carregando os dados do banco de dados, tem todas as notas contidas nele
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def group_per_tag(request):
    tag_name = request.POST.get('tag')
    # filtra notas com a tag desejada para agrupar
    group = Note.objects.filter(tag__name = tag_name)
    return render(request, 'notes/tagNotes.html', {'notes': group, 'tag': tag_name})
    
def list_tags(request):
    list = Tag.objects.all()
    return render(request, 'notes/tagsList.html', {'tags': list})
