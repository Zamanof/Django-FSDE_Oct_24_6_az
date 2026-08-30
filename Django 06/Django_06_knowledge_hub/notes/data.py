from copy import deepcopy
from typing import Any

from unicodedata import category

_NOTES:list[dict[str:Any]] = [
    {
        'id': 1,
        'title': "Django Views",
        'body': 'View request qəbul edir və response qaytarır.',
        'tag': 'django',
        'category': 'backend'
    },
    {
        'id': 2,
        'title': "Django Models",
        'body': 'Models məlumat bazası ilə işləmək üçün istifadə olunur.',
        'tag': 'django',
        'category': 'database'
    },
    {
        'id': 3,
        'title': "Django Templates",
        'body': 'Templates HTML səhifələrinin yaradılması üçün istifadə olunur.',
        'tag': 'html',
        'category': 'frontend'
    },
    {
        'id': 4,
        'title': "Django URLs",
        'body': 'URLs sorğuları uyğun view funksiyalarına yönləndirir.',
        'tag': 'django',
        'category': 'backend'
    },
    {
        'id': 5,
        'title': "Python Functions",
        'body': 'Functions kodu təkrar istifadə etmək üçün qruplaşdırmağa imkan verir.',
        'tag': 'python',
        'category': 'programming'
    }
]

def list_notes()-> list[dict[str, Any]]:
    return deepcopy(_NOTES)

def get_note(note_id: int) -> dict[str, Any]|None:
    for note in _NOTES:
        if note['id'] == note_id:
            return deepcopy(note)
    return None