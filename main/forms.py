from django.forms import ModelForm
from main.models import MaterialEntry

class MaterialEntryForm(ModelForm):
    class Meta:
        model = MaterialEntry
        fields = ["material", "item", "material_quantity","item_quantity", "notes"]