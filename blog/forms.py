from django import forms
from comments.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["nickname", "email", "content"]
        widgets = {
            "content": forms.Textarea(attrs={"rows": 4, "maxlength": 1000})
        }

    def clean_nickname(self):
        nickname = self.cleaned_data["nickname"].strip()
        if len(nickname) < 2:
            raise forms.ValidationError("昵称至少需要2个字符")
        return nickname

    def clean_content(self):
        content = self.cleaned_data["content"].strip()
        if len(content) < 5:
            raise forms.ValidationError("评论内容太短")
        if len(content) > 1000:
            raise forms.ValidationError("评论内容不能超过1000字")
        return content
