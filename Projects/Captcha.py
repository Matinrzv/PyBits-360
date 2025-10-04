from captcha.image import ImageCaptcha
from PIL import Image
import string
import random

def Generate_Captcha_text(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def Generate_and_save_Captcha(image_width=300, image_height=100,captcha_length=6, save_path="assets\Captcha.png"):
    image =ImageCaptcha(width=image_width, height=image_height)
    Captcha_txt = Generate_Captcha_text(captcha_length)
    data = image.generate(Captcha_txt)
    image.write(Captcha_txt, save_path)
    return Captcha_txt

if __name__ == "__main__":
    Captcha_txt = Generate_and_save_Captcha()
    print(f"CAPTCHA text: {Captcha_txt}")

Image.open("assets\Captcha.png")