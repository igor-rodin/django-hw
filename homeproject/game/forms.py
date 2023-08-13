from django import forms


class GameForm(forms.Form):
    game = forms.ChoiceField(
        choices=[("C", "Coin"), ("D", "Dice"), ("RN", "RandomNumber")],
        label="Игра",
    )
    n_attempts = forms.IntegerField(min_value=1, label="Количество попыток")
