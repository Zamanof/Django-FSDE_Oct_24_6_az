from copy import deepcopy
from datetime import datetime
from typing import Any


_NOTES: list[dict[str, Any]] = [
    {
        'id': 1,
        'title': "Django Views",
        'content': 'View request qəbul edir və response qaytarır.',
        'tags': ['django', 'python', 'views'],
        'category': 'backend',
        'created_at': datetime(2026, 8, 15, 10, 30),
    },
    {
        'id': 2,
        'title': "Django Models",
        'content': 'Models məlumat bazası ilə işləmək üçün istifadə olunur.',
        'tags': ['django', 'python', 'models', 'database', 'orm'],
        'category': 'database',
        'created_at': datetime(2026, 8, 18, 14, 45),
    },
    {
        'id': 3,
        'title': "Django Templates",
        'content': 'Templates HTML səhifələrinin yaradılması üçün istifadə olunur.',
        'tags': ['django', 'html', 'templates', 'frontend'],
        'category': 'frontend',
        'created_at': datetime(2026, 8, 21, 9, 15),
    },
    {
        'id': 4,
        'title': "Django URLs",
        'content': 'URLs sorğuları uyğun view funksiyalarına yönləndirir.',
        'tags': ['django', 'urls'],
        'category': 'backend',
        'created_at': datetime(2026, 8, 25, 16, 20),
    },
    {
        'id': 5,
        'title': "Python Functions",
        'content': 'Functions kodu təkrar istifadə etmək üçün qruplaşdırmağa imkan verir.',
        'tags': ['python', 'functions', 'programming', 'backend', 'code', 'development'],
        'category': 'programming',
        'created_at': datetime(2026, 8, 29, 11, 50),
    }
]

_next_id = 6

def list_notes()-> list[dict[str, Any]]:
    return deepcopy(_NOTES)


def get_note(note_id: int) -> dict[str, Any]|None:
    for note in _NOTES:
        if note['id'] == note_id:
            return deepcopy(note)
    return None


def create_note(*, title: str, content: str, tags: list[str], category: str) -> dict[str, Any]:
    global _next_id
    note = {
        'id': _next_id,
        'title': title.strip(),
        'content': content.strip(),
        'tags': tags,
        'category': category.strip(),
        'created_at': datetime.now(),

    }
    _NOTES.append(note)
    _next_id += 1
    return deepcopy(note)


def update_note(
        note_id:int,
        *,
        title: str,
        content: str,
        tags:list[str],
        category: str,
) -> dict[str, Any]|None:
    for note in _NOTES:
        if note['id'] == note_id:
            note['title'] = title.strip()
            note['content'] = content.strip()
            note['tags'] = tags
            note['category'] = category.strip()
            return deepcopy(note)
    return None

def delete_note(note_id: int) -> bool:
    global _NOTES
    before = len(_NOTES)
    _NOTES = [n for n in _NOTES if n['id'] != note_id]
    return before != len(_NOTES)

