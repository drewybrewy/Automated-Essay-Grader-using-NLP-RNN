from django import forms
from app.models import Students, Teachers

class StudentsForm(forms.ModelForm):

    class Meta:
        model =  Students
        fields = "__all__"

class TeachersForm(forms.ModelForm):

    class Meta:
        model =  Teachers
        fields = "__all__"
