from django import forms


class AuthorForms(forms.Form):
    name = forms.CharField(max_length=100)
    surname = forms.CharField(max_length=100)
    email = forms.EmailField()
    biography = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))
    birthday = forms.DateField()
