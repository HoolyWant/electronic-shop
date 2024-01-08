from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return f'{self.email}, {self.username}'
