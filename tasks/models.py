from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    objects = None
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(
        max_length=50,
        choices=[
            ('urgent_important', 'Acil ve Önemli'),
            ('not_urgent_important', 'Acil Değil ama Önemli'),
            ('urgent_not_important', 'Acil ama Önemsiz'),
            ('not_urgent_not_important', 'Acil Değil ve Önemsiz'),
        ]
    )
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
