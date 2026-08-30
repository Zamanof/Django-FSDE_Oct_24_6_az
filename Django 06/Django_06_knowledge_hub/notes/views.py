from django.http import HttpResponse, HttpRequest

from . import data
def home(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Knowledge Hub Home Page")

def about(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Knowledge Hub About Page")

def notes_list(request: HttpRequest) -> HttpResponse:
    notes = data.list_notes()
    content = "<ul>"
    for note in notes:
        content += f"""
        <a href="#">
        <li>
        <p>Title: {note['title']}</p>
        </li>
</a>"""
    content += "</ul>"

    return HttpResponse(content)


def note_detail(request: HttpRequest, note_id: int) -> HttpResponse:

    return HttpResponse("Knowledge Hub Note Detail")




