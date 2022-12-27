from django.db import models
from django.core.exceptions import ValidationError

class CustomImageField(models.ImageField):

    default='default_avatar.png'

    def __init__(self,*args, **kwargs):
        self.content_types=kwargs.pop('content_types', [])
        self.max_size=kwargs.pop('max_size', [])
        super().__init__(*args, **kwargs)

    def clean(self, *args, **kwargs):
        data=super().clean(*args, **kwargs)
        file=data.file

        if not hasattr(file, 'content_type'):
            file.content_type = 'image/png'

        if file.content_type in self.content_types:
            if file.size > self.max_size:
                raise ValidationError(
                    f'The avatar size is too big!'
                )
        else:
            raise ValidationError(
                f'The content_type is not supported.Sorry!'
            )

        return data