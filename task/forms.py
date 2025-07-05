from django import forms
from .models import TaskModel,TaskCategory
class Task(forms.ModelForm):
    class Meta:
        model=TaskModel
        fields='__all__'
        widgets = {
            'taskAssignDate': forms.DateInput(attrs={
                'type': 'date',   # This shows a calendar picker in HTML5-supported browsers
                'class': 'form-control'  # Optional: for Bootstrap styling
            }),
        }

class Category(forms.ModelForm):
    class Meta:
        model=TaskCategory
        fields='__all__'
