from django.contrib import admin

from notes.models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at', 'updated_at')
    list_filter = ('created_at', 'category')
    search_fields = ('title', 'content', 'author__username')
    autocomplete_fields = ('author', 'category')
    filter_horizontal = ('tags',)
    readonly_fields = ("created_at", "updated_at")



# ============================================================
# Django Admin - ModelAdmin əsas ayarları
# ============================================================

# list_display
# Admin siyahısında göstəriləcək sütunları təyin edir.
# list_display = ("id", "title", "author", "created_at")


# list_display_links
# Siyahıda hansı sütunların obyektin edit səhifəsinə link olacağını təyin edir.
# list_display_links = ("id", "title")


# list_filter
# Sağ tərəfdə filter paneli yaradır.
# list_filter = ("category", "created_at")


# search_fields
# Admin panelə axtarış imkanı əlavə edir.
# search_fields = ("title", "content", "author__username")


# ordering
# Obyektlərin hansı ardıcıllıqla göstəriləcəyini təyin edir.
# "-" azalan sıra deməkdir.
# ordering = ("-created_at",)


# readonly_fields
# Göstərilən, amma dəyişdirilməsi mümkün olmayan field-ləri təyin edir.
# readonly_fields = ("created_at", "updated_at")


# fields
# Create/Edit səhifəsində hansı field-lərin və hansı ardıcıllıqla
# göstəriləcəyini təyin edir.
# fields = ("title", "content", "category", "tags")


# exclude
# Create/Edit səhifəsində göstərilməyəcək field-ləri təyin edir.
# exclude = ("author",)


# fieldsets
# Field-ləri qruplara/bölmələrə ayırmağa imkan verir.


# filter_horizontal
# ManyToManyField üçün rahat horizontal seçim interfeysi yaradır.
# filter_horizontal = ("tags",)


# filter_vertical
# ManyToManyField üçün vertical seçim interfeysi yaradır.
# filter_vertical = ("tags",)


# prepopulated_fields
# Bir field-in dəyərini digər field əsasında avtomatik yaradır.
# Əsasən slug yaratmaq üçün istifadə olunur.
# prepopulated_fields = {"slug": ("name",)}


# autocomplete_fields
# ForeignKey və ManyToManyField üçün autocomplete axtarışı əlavə edir.
# autocomplete_fields = ("author", "tags")


# raw_id_fields
# ForeignKey / ManyToManyField seçimlərini ID əsasında göstərir.
# Böyük həcmli məlumatlarda faydalıdır.
# raw_id_fields = ("author",)


# date_hierarchy
# Tarix field-i əsasında yuxarı hissədə tarix naviqasiyası yaradır.
# date_hierarchy = "created_at"


# list_per_page
# Admin siyahısında bir səhifədə neçə obyekt göstəriləcəyini təyin edir.
# list_per_page = 20


# list_editable
# Obyektləri ayrıca açmadan birbaşa siyahıdan dəyişməyə imkan verir.
# list_editable = ("is_published",)


# empty_value_display
# Boş (None) dəyərlərin admin paneldə necə göstəriləcəyini təyin edir.
# empty_value_display = "—"


# save_on_top
# Save düymələrini edit səhifəsinin yuxarı hissəsində də göstərir.
# save_on_top = True