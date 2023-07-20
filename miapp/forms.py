from django import forms
from django.core import validators


class FormArticle(forms.Form):
    title= forms.CharField(
        label="Titulo",
        max_length=20,
        required=True,
        widget=forms.TextInput(
        attrs={
        'placeholder':'Introduce titulo aqui...',
        'class':'titulo_form_article'
        }),
        validators=[
            validators.MinLengthValidator(4,'El titulo es demasiado corto'),
            validators.RegexValidator('^[a-zA-Z0-9ñ ]*$','El titulo esta mal formado','invalid_title')
        ]
        )
    
    content= forms.CharField(
    label="Contenido",
    widget=forms.Textarea,
    validators=[
        validators.MaxLengthValidator(50,'Te has pasado, has puesto mucho texto')]
    )
    public_options =[
        (1,'Si'),
        (0,'No')
    ]
    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_options
    )
