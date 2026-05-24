from django import forms


class UserLoginForm(forms.Form):
    login =  forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={"placeholder": "ایمیل یا یوزرنیم خود را وارد کنید", "autocomplete": "username"}),
        label="ایمیل یا یزورنیم"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور", "autocomplete": "current-password"}),
        label="رمز عبور"
    )
