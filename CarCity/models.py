from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings
fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class Ad(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    pic = models.ImageField(null=True, blank=True)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    contact_info = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"
