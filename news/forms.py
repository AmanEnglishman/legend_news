from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        label='Ваше имя',
        widget=forms.TextInput(
            attrs={'placeholder':'Ваше имя'}
        )
    )
    email = forms.EmailField(
        label='email',
        widget=forms.TextInput(
            attrs={'placeholder':'email'}
        )
    )
    message = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(
            attrs={'placeholder':'Ваше сообщение'}
        )
    )