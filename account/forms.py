from django import forms


class UserLoginForm(forms.Form):

    ERROR_MESSAGES = {"required": "این فیلد الزامی میباشد.", "max_length": "تعداد کاراکتر وارد شده از حد مجاز بیشتر است."}

    login =  forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={"placeholder": "ایمیل یا یوزرنیم خود را وارد کنید", "autocomplete": "username"}),
        label="ایمیل یا یزورنیم",
        error_messages=ERROR_MESSAGES
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور", "autocomplete": "current-password"}),
        label="رمز عبور",
        error_messages=ERROR_MESSAGES
    )
