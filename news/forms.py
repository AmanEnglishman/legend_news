from django import forms

from .models import Comments

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

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'content')
        widgets = {
            'name' : forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите ваше имя'
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Введите ваш комментарий'
                }
            )
        }

