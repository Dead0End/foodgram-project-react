from django.contrib.auth.models import AbstractUser
from django.db import models

MAX_FIELD_LENGTH = 150


class FoodgramUser(AbstractUser):
    """Переопределение стандартного пользователя."""

    first_name = models.CharField('Имя', max_length=MAX_FIELD_LENGTH)
    last_name = models.CharField('Фамилия', max_length=MAX_FIELD_LENGTH)

    email = models.EmailField('Почта', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)


class Follow(models.Model):
    """Модель фоловеров."""

    user = models.ForeignKey(
        FoodgramUser, on_delete=models.CASCADE, related_name='subscriber',
        verbose_name='Подписчик')
    following = models.ForeignKey(
        FoodgramUser, on_delete=models.CASCADE, related_name='following',
        verbose_name='Подписан на')

    class Meta:
        verbose_name = 'подписчик'
        verbose_name_plural = 'Подписчики'
        constraints = [
            models.UniqueConstraint(
                fields=('user', 'following'),
                name='unique_user_following'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F('following')),
                name='can_not_follow_youself'
            )
        ]
        default_related_name = 'follows'

    def __str__(self):
        return self.user.username
