from django import forms
from .models import BugTable
from django.forms import widgets


class BugTableForm(forms.ModelForm):
    class Meta:
        model = BugTable
        fields = ('bug_name', 'bug_description', 'bug_solution')
        widgets = {'bug_solution': forms.HiddenInput()}
