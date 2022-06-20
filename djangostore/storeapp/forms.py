from django.forms import ModelForm
from .models import Call

class CallForm(ModelForm):
    class Meta:
        model=Call
        fields=('name', 'number')