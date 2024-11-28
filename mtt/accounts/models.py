from django.db import models
from django.contrib.auth.models import AbstractUser


class Accounts(AbstractUser):
    phone = models.CharField(max_length=150, null=True)

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Accounts'
        verbose_name_plural = 'Пользователи'
        ordering = ('id', )
