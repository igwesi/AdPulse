from django.db import models
from django.contrib.auth.models import User

class Campaign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    impressions = models.IntegerField(default=0)
    clicks = models.IntegerField(default=0)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def ctr(self):
        return round((self.clicks / self.impressions) * 100, 2) if self.impressions else 0