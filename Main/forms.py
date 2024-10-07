from django import forms
from .models import MyCV

class PDFUploadForm(forms.ModelForm):
    class Meta:
        model = MyCV
        fields = ['title', 'pdf_file']