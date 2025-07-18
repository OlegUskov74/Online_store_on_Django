from django import forms
from django.core.exceptions import ValidationError

from blog.models import Blog
from config.settings import ALLOWED_EXTENSIONS


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ["name", "description", "photo", "sign_publication"]

    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.allowed_extensions = ALLOWED_EXTENSIONS

        self.fields["name"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите имя'}
        )
        self.fields["description"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': 'Введите описание',
             'rows': 3}
        )
        self.fields["photo"].widget.attrs.update(
            {'class': 'form-control',
             'placeholder': ''}
        )
        self.fields["sign_publication"].widget.attrs.update(
            {'class': 'form-check-input',
             'placeholder': ''}
        )

    def clean_photo(self):
        """ Проверка размера и типа изображения. """
        photo = self.cleaned_data.get('photo')
        max_size = 5 * 1024 * 1024

        if photo:
            photo_name = photo.name.lower()
            if not any(photo_name.endswith(ext) for ext in self.allowed_extensions):
                raise ValidationError('Не допустимый формат! Доступные типы файла  .jpeg , .jpg , .png')

            if photo.size > max_size:
                raise ValidationError('Превышен размер файла! Доступные размер файла 5 Мб ')
            return photo