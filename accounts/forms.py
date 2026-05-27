from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


LOGIN_ERROR_MESSAGES = {
    "max_length": "تعداد کاراکتر وارد شده از حد مجاز بیشتر است.",
    "required": "این فیلد الزامی میباشد"
}
USER_DATA_ERROR_MESSAGES = {**LOGIN_ERROR_MESSAGES, "unique": "این %(field_label)s در سایت ذخیره شده است"}
PASSWORD_ERROR_MESSAGES = {"required": LOGIN_ERROR_MESSAGES['required']}

class UserLoginForm(forms.Form):

    login = forms.CharField(
        max_length=254,
        widget=forms.TextInput(attrs={"placeholder": "ایمیل یا یوزرنیم خود را وارد کنید", "autocomplete": "username"}),
        label="ایمیل یا یزورنیم",
        error_messages=LOGIN_ERROR_MESSAGES
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "رمز عبور", "autocomplete": "current-password"}),
        label="رمز عبور",
        error_messages=LOGIN_ERROR_MESSAGES
    )


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ["username", "email", "password1", "password2"]
        labels = {"username": "نام کاربری", "email": "ایمیل"}
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "نام کاربری", "autocomplete": "username"}),
            "email": forms.EmailInput(attrs={"placeholder": "ایمیل", "autocomplete": "email", "inputmode": "email"})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for x in self.fields.keys():
            if x != "password1":
                self.fields[x].help_text = None
            else:
                self.fields[x].help_text = [
                "۱. رمز عبور نباید ساده و یا یک کلمه رایج باشد",
                "۲. رمز عبور نمیتواند فقط از اعداد تشکیل شود",
                "۳. رمز عبور نباید به نام کاربری نزدیک باشد",
                "۴. حین وارد کردن رمز عبور زبان کیبورد را به انگلیسی تغییر دهید",
                "۵. رمز عبور باید ترکیبی از اعداد - حروف و نماد باشد"
            ]

        self.fields['password1'].label = "رمز عبور"
        self.fields['password2'].label = "تکرار رمز عبور"

        self.fields['password1'].widget.attrs['placeholder'] = "رمز عبور"
        self.fields['password2'].widget.attrs['placeholder'] = "تکرار رمز عبور"

        self.fields['username'].error_messages.update(USER_DATA_ERROR_MESSAGES)
        self.fields['email'].error_messages.update(USER_DATA_ERROR_MESSAGES)
        self.fields['password1'].error_messages.update(PASSWORD_ERROR_MESSAGES)
        self.fields['password2'].error_messages.update(PASSWORD_ERROR_MESSAGES)
