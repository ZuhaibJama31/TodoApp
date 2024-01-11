from django import forms
from .models import MakeList

class MakeListForm(forms.ModelForm):
   class Meta:
      model = MakeList
      fields = ['Title','Description','Status','Date']