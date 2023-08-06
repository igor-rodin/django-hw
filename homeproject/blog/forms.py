from django import forms
from .models import Author


class AuthorForm(forms.Form):
    name = forms.CharField(max_length=100, label="Имя")
    surname = forms.CharField(max_length=100, label="Фамилия")
    email = forms.EmailField(label="Email")
    biography = forms.CharField(
        label="Биография", widget=forms.Textarea(attrs={"class": "form-control"})
    )
    birthday = forms.DateField(label="Дата рождения")


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=200, label="Заголовок")
    content = forms.CharField(
        label="Текст статьи", widget=forms.Textarea(attrs={"class": "form-control"})
    )
    category = forms.CharField(
        label="Категория",
        max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label="Выберите автора",
        label="Автор",
    )


class CommentForm(forms.Form):
    comment = forms.CharField(
        label="Комментарий", widget=forms.Textarea(attrs={"class": "form-control"})
    )
    author = forms.ModelChoiceField(
        queryset=Author.objects.all(),
        empty_label="Выберите автора",
        label="Автор",
    )
