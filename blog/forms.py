from django import forms

from blog_system.error_messages import GLOBAL_ERROR_MESSAGES
from .models import Blog


class BlogCreateForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "body", "cover"]
        labels = {"title": "موضوع", "body": "متن", "cover": "تصویر"}
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "عنوان بلاگ", "autocomplete": "off"}),
            "body": forms.Textarea(attrs={"placeholder": "متن بلاگ"})
        }
        error_messages = {
            "title": {**GLOBAL_ERROR_MESSAGES, "max_length": "تعداد کاراکتر وارد شده از حد مجاز بیشتر است."},
            "body": GLOBAL_ERROR_MESSAGES,
            "cover": {**GLOBAL_ERROR_MESSAGES, "invalid_image": "تصویر انتخاب شده معتبر نمیباشد . مججد بارگذاری کنید"}
        }
        
