from django import forms
#from tinymce import TinyMCE
from tinymce.widgets import TinyMCE
from .models import Post,Comment
from ckeditor.widgets import CKEditorWidget


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    # overview = forms.CharField(
    #     widget=TinyMCEWidget(
    #         attrs={'required': True, 'cols': 30, 'rows': 10}
    #     )
    # )
    # content = forms.CharField(
    #     widget=TinyMCEWidget(
    #         attrs={'required': True, 'cols': 30, 'rows': 10}
    #     )
    # )
    overview= forms.CharField(widget=CKEditorWidget())
    content = forms.CharField(widget=CKEditorWidget())


    class Meta:
        model = Post
        fields = ('title','overview','content','thumbnail','categories','featured','previous_post','next_post')

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget= forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder' : 'Type your Comments',
        'id' : 'usercomment',
        'rows':'4'
    }))
    class Meta:
        model = Comment
        fields = ('content',)
