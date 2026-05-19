from django import forms


class UserLoginForm(forms.Form):
    login =  forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={"placeholder": "آدرس ایمیل یا نام کاربری", "autocomplete": "username"}),
        label=False
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور", "autocomplete": "current-password"}),
        label=False
    )
