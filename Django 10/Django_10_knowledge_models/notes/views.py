from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest, HttpResponseForbidden
from django.shortcuts import redirect, render, get_object_or_404

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


@login_required
def notes_list(request: HttpRequest) -> HttpResponse:
    if request.user.is_superuser:
        notes = Note.objects.select_related('author', 'category').prefetch_related('tags')
    else:
        notes = (
            Note.objects.filter(author=request.user)
            .select_related('author', 'category')
            .prefetch_related('tags')
            .order_by('-created_at')
        )
    return render(request, 'notes/notes_list.html', {'notes': notes})


@login_required
def note_detail(
    request: HttpRequest,
    note_id: int
) -> HttpResponse:

    note =  get_object_or_404(
        Note.objects.select_related('author', 'category').prefetch_related('tags'),
        pk=note_id
    )
    if note.author != request.user and not request.user.is_superuser:
        return  HttpResponseForbidden("Siz ancaq öz qeydlərinizi görə bilərsiniz")
    return render(request, 'notes/note_detail.html', {'note': note})


@login_required
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


@login_required
def note_edit(request: HttpRequest, note_id:int) -> HttpResponse:
    note = get_object_or_404(Note, pk=note_id)
    if request.user != note.author and not request.user.is_superuser:
        return HttpResponseForbidden("Siz ancaq öz qeydlərinizi dəyişə bilərsiniz")
    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('notes:note_detail', note_id=note.pk)
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_edit.html', {'note': note, 'form': form, 'mode': 'edit'})


@login_required
def note_delete(request: HttpRequest, note_id:int) -> HttpResponse:
    note = get_object_or_404(
        Note, pk=note_id
    )

    if request.user != note.author and not request.user.is_superuser:
        return HttpResponseForbidden("Siz ancaq öz qeydlərinizi silə bilərsiniz")

    if request.method == 'POST':
        note.delete()
        messages.success(request, "")
        return redirect('notes:notes_list')
    return render(request, 'notes/note_delete.html', {'note': note})