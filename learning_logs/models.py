from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    """Тема, которую изучает пользователь"""

    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Возвращает строковое представление модели."""
        return self.text


class Entry(models.Model):
    """Информация по темам изученная пользователем"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Возврат строкогого представления модели"""
        return self.text[:50] if len(self.text) < 50 else self.text[:50] + '...'
