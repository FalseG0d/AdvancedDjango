from .models import Name
from django.forms import ModelForm

class NameForm(ModelForm):
    class Meta:
        model=Name
        fields='__all__'