import uuid  # tambahkan baris ini di paling atas
from django.db import models
from django.contrib.auth.models import User


class MaterialEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nama = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    image = models.ImageField()
    rating = models.IntegerField()

# Create your models here.
