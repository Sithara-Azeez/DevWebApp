from django.forms import ModelForm
from .models import Project, Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'demo_link', 'source_link', 'tags',]
        widgets = {
            'tags': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for label, field in self.fields.items():
            field.widget.attrs.update({
                'class':'input'
            },)
        #self.fields['title'].widget.attrs.update({
           # 'class':'input'
        #},)

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'body':'Add the comments here..',
            'value':'Add your vote for the comment'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for label, field in self.fields.items():
            field.widget.attrs.update({
                'class':'input input--text','placeholder':'Enter Value'
            },)