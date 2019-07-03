from django import forms
from .models import Post, Comment


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'post_text',)


class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)