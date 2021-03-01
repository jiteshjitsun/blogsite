from django import forms
from django.forms import fields, widgets
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for i in choices:
    choice_list.append(i)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','category', 'writer','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'input your article title here'}),
            'category': forms.Select(choices=choice_list,attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'writer': forms.TextInput(attrs={'class': 'form-control','value': '', 'id':'userid', 'type':'hidden'}),
            # 'writer': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','title_tag','body')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'input your article title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }