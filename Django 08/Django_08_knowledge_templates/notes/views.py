from typing import Any

from django.http import HttpResponse, HttpRequest
from django.shortcuts import redirect, render
from django.template.defaultfilters import title
from django.urls import reverse
from django.utils.html import escape
from django.middleware.csrf import get_token

from . import data

def home(request: HttpRequest) -> HttpResponse:
    return render(request, 'notes/home.html')


def about(request: HttpRequest) -> HttpResponse:
    context = {
        'project_name':'Knowledge Hub',
        'author':'Nadir Zamanov',
    }
    return render(request, 'notes/about.html', context)


def notes_list(request: HttpRequest) -> HttpResponse:
    notes = data.list_notes()
    return render(request, 'notes/notes_list.html', {'notes': notes})


def note_detail(
    request: HttpRequest,
    note_id: int
) -> HttpResponse:

    note = data.get_note(note_id)
    return render(request, 'notes/note_detail.html', {'note': note})


def note_create(request: HttpRequest) -> HttpResponse:
    error = ''
    title = ''
    content = ''
    tags = ''
    category = ''
    if request.method == 'POST':
        title = request.POST.get('title', "")
        content = request.POST.get('body', "")
        category = request.POST.get('category', "")
        tags = request.POST.get('tag')

        if not title.strip():
            error = 'Title is required'
        else:
            data.create_note(
                title=title.strip(),
                content=content.strip(),
                category=category.strip() or "qarışıq",
                tags= tags.split() or None
            )

        return redirect('notes_list')
    context = {
        'error': error,
        'title': title,
        'content': content,
        'category': category,
        'tags': tags,
    }

    return render(request, 'notes/note_create.html', context)


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