from django.forms  import ModelForm, widgets
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
          model = Project
          #fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
          fields = "__all__"
          widgets = { "tags": forms.CheckboxSelectMultiple(), }
          
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        #self.fields['title'].widget.attrs.update({'class':'input'})
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input', 'placeholder':field.label})
   
