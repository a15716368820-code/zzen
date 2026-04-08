from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["nickname", "email", "content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4})
        }
