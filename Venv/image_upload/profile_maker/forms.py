from django import forms
from .models import User_Profile
#DataFlair #File_Upload
class Profile_Form(forms.ModelForm):
    class Meta:
        model = User_Profile
        fields = [
        'Faculty_Name',
        'Lecture_Name',
        'Upload_Picture'
        ]
