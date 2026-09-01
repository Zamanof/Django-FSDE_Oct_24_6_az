from typing import Any

from django.http import HttpResponse, HttpRequest
from django.urls import reverse
from django.utils.html import escape

from . import data



def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Knowledge Hub Home Page")

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Knowledge Hub About Page")

def notes_list(request: HttpRequest) -> HttpResponse:
    raw_tag = request.GET.get('tag')
    raw_category = request.GET.get('category')
    items:list[str] = []
    notes:list[dict[str, Any]] = data.list_notes()
    if raw_tag:
        tag_filter = raw_tag.strip()
        notes = [n for n in notes if n['tag'] == tag_filter]
    if raw_category:
        category_filter = raw_category.strip()
        notes = [n for n in notes if n['category'] == category_filter]

    for note in notes:
        url = reverse('note_detail', kwargs={"note_id": note['id']})
        items.append(f"""
        <li>
            <a href="{escape(url)}">
                    {escape(note['title'])} ({escape(note['tag'])})
            </a>
        </li>
""")
    body = (
        f"""
        <h1>Knowledge Hub Notes</h1>
        <ul>
            {''.join(items)}
        </ul>
        <p><a href={escape(reverse('home'))}>Return to home page</a></p>
        """
    )
    return HttpResponse(body)


def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:
    note = data.get_note(note_id)
    if note is None:
        return HttpResponse(f"Note id={note_id} not found")

    body = (
        f"""
        <h1>{escape(note['title'])}</h1>
        <p>Text: {escape(note['body'])}</p>
        <p>Tag: {escape(note['tag'])}</p>
        <p>Category: {escape(note['category'])}</p>
        <p><a href={escape(reverse('notes_list'))}>Return to notes list</a></p>
        """
    )
    return HttpResponse(body)


# Query string

