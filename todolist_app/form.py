from asyncio import Task
from dataclasses import field
from django import forms
from todolist_app.models import DoList


class TaskForm(forms.ModelForm):
    class Meta:
        model = DoList
        fields = ['task', 'do']
        