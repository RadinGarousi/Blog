from django.core.exceptions import ValidationError
from PIL import Image


# User Model
def validate_avatar(image):
    img = Image.open(image)

    if img.width < 200 or img.height < 200:
        raise ValidationError("تصویر پروفایل باید حداقل ۲۰۰×۲۰۰باشد")

    elif img.width > 512 or img.height > 512:
        raise ValidationError("تصویر پروفایل نهایتا میتواند ۵۱۲×۵۱۲ باشد")
    

def validate_poster(image):
    img = Image.open(image)

    if img.width < 1280 or img.height < 720:
        raise ValidationError("تصویر پوستر باید حداقل ۷۲۰×۱۲۸۰باشد")
    
    elif img.width > 2560 or img.height > 1440:
        raise ValidationError("تصویر پوستر میتواد نهایتا ۲۵۶۰×۱۴۴۰ باشد")
