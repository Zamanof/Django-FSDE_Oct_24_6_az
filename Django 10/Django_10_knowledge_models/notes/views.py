from django.contrib import messages
from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render

from . import data
from .forms import NoteForm
from .models import Note


def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'notes/home.html')


def about(request: HttpRequest) -> HttpResponse:
    context = {
        'project_name':'Knowledge Hub',
        'author':'Nadir Zamanov',
    }
    return render(request, 'notes/about.html', context)


def notes_list(request: HttpRequest) -> HttpResponse:
    notes = Note.objects.select_related('category', 'author').prefetch_related('tags').all()
    return render(request, 'notes/notes_list.html', {'notes': notes})


def note_detail(
    request: HttpRequest,
    note_id: int
) -> HttpResponse:

    note = data.get_note(note_id)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form.save_m2m()
            messages.success(request, 'Qeyd uğurla yarandı')
            return redirect('notes:note_detail', note_id=note.pk)
    else:
        form = NoteForm()

    return render(request, 'notes/note_create.html', {
        'form': form,
        'mode': 'create',
    })


def note_edit(request: HttpRequest, note_id:int) -> HttpResponse:
    note = data.get_note(note_id)
    if request.method == 'POST':
        title = request.POST.get('title', "")
        content = request.POST.get('content', "")
        category = request.POST.get('category', "")
        tags = request.POST.get('tag')
        data.update_note(
            note_id=note_id,
            title=title.strip(),
            content=content.strip(),
            category=category.strip(),
            tags= tags.split() or None
        )
        return redirect('notes_list')

    return render(request, 'notes/note_edit.html', {'note': note})

def note_delete(request: HttpRequest, note_id:int) -> HttpResponse:
    note = data.get_note(note_id)
    if request.method == 'POST':
        data.delete_note(note_id)
        return redirect('notes_list')
    return render(request, 'notes/note_delete.html', {'note': note})