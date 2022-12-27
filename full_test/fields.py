from django.forms import ValidationError
from django.db import models

class CustomFileField(models.FileField):

    def __init__(self, *args, **kwargs):
        self.max_size=kwargs.pop('max_size', [])
        self.content_types=kwargs.pop('content_types', [])
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data=super().clean(*args, **kwargs)
        file=data.file

        if file.content_type in self.content_types:
            if file.size > self.max_size:
                raise ValidationError(
                    f'The file size should keep under {self.max_size}!!'
                )
        else:
            raise ValidationError(
                f'{file.content_type} is not supported!'
            )
        return data

