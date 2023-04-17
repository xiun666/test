import pytesseract
from PIL import Image
# 打开图片实例化图片对象
img = Image.open('11.png')
text = pytesseract.image_to_string(img,lang='chi_sim')
print(text)