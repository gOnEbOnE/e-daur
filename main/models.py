import uuid  # tambahkan baris ini di paling atas
from django.db import models

class MaterialEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    nama = models.CharField(max_length=255)
    time = models.DateField(auto_now_add=True)
    harga = models.IntegerField()
    deskripsi = models.TextField()
    image = models.ImageField()

# Create your models here.
