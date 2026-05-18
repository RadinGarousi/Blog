from django.core.exceptions import ValidationError
from PIL import Image


# User Model
def validate_avatar(image): 
    
    img = Image.open(image)
    if img.width != img.height:
            raise ValidationError("تصویر پروفایل باید مربع باشد")
    if img.width < 200 or img.height < 200:
        raise ValidationError("تصویر پروفایل باید حداقل ۲۰۰×۲۰۰باشد")
    if img.width > 400 or img.height > 400:
        raise ValidationError("تصویر پروفایل نهایتا میتواند ۴۰۰×۴۰۰ باشد")
    

def validate_poster(image):
    
    img = Image.open(image)
    if img.width < 1280 or img.height < 720:
        raise ValidationError("تصویر پوستر باید حداقل ۷۲۰×۱۲۸۰باشد")
    if img.width > 1920 or img.height > 1080:
        raise ValidationError("تصویر پوستر میتواد نهایتا ۱۰۸۰×۱۹۲۰ باشد")
