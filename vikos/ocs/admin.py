from django.contrib import admin
from django.utils.html import mark_safe

from .models import Character


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'is_published',
        'first_name',
        'last_name',
        'gender',
        'age',
        'display_image'
    )
    list_editable = (
        'is_published',
    )
    list_display_links = ('first_name', )

    @admin.display(description='Фото')
    def display_image(self, character):
        if character.image:
            return mark_safe(f'<img src={character.image.url}'
                             ' width="80" height="60">')

        return 'Без фото'
