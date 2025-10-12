from django.db import models
from django.contrib.auth.models import User

class GeneratedCopy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    audience = models.TextField()
    tone = models.CharField(max_length=50)
    output = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
