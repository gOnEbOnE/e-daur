from django.forms import ModelForm
from main.models import MaterialEntry
from django.utils.html import strip_tags

class MaterialEntryForm(ModelForm):
    class Meta:
        model = MaterialEntry
        fields = ["nama", "harga", "deskripsi", "rating",]

    def clean_nama(self):
        nama = self.cleaned_data["nama"]
        return strip_tags(nama)

    def clean_deskripsi(self):
        deskripsi = self.cleaned_data["deskripsi"]
        return strip_tags(deskripsi)