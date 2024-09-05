import os

from django.utils.text import slugify
from django.db import models


def character_image_path(instance, filename):
    # Создаем путь, используя имя и фамилию персонажа
    first_name_slug = slugify(instance.first_name)
    last_name_slug = slugify(instance.last_name)

    # Путь будет выглядеть как 'character_images/first_name_last_name/filename'
    return os.path.join('character_images', f'{first_name_slug}_{last_name_slug}', filename)


class Character(models.Model):
    is_published = models.BooleanField(
        default=True,
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.'
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=256,
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=256,
        blank=True
    )
    gender = models.CharField(
        verbose_name='Пол',
        max_length=256,
        blank=True
    )
    age = models.PositiveSmallIntegerField(
        verbose_name='Возраст',
        null=True,
        blank=True,
    )
    birth_date = models.DateField(
        verbose_name='День рождения',
        null=True,
        blank=True,
    )
    height = models.PositiveSmallIntegerField(
        verbose_name='Рост',
        null=True,
        blank=True,
    )
    orientation = models.CharField(
        verbose_name='Предпочтение',
        max_length=256,
        null=True,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )
    background = models.TextField(
        verbose_name='Предыстория',
        null=True,
        blank=True,
    )
    history_now = models.TextField(
        verbose_name='История на данный момент',
        null=True,
        blank=True,
    )
    ethnicity = models.CharField(
        verbose_name='Этническая принадлежность',
        max_length=256,
        null=True,
        blank=True,
    )
    likes = models.JSONField(
        verbose_name='Нравится',
        default=list,
        blank=True,
        null=True
    )
    unlikes = models.JSONField(
        verbose_name='НЕ нравится',
        default=list,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to=character_image_path,
        verbose_name='Фото',
        blank=True
    )

    class Meta:
        verbose_name = 'персонаж'
        verbose_name_plural = 'Персонажи'
        ordering = ('first_name', 'last_name',)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
