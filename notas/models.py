from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Nota(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    nome_nota = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)
