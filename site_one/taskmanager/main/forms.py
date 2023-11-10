from .models import Task
from django.forms import ModelForm, TextInput, Textarea, Select


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task", "status"]
        widgets = {
            "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер'
        }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите описание'
            }),
            "status": Select(attrs={
                'class': 'form-control',
            }, choices=[('Новое', 'Новое'),
                        ('Подтверждено', 'Подтверждено'),
                        ('Отклонено', 'Отклонено')]),
        }
