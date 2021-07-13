
# coding: utf-8

# In[1]:

from PIL import Image, ImageChops
import os

lista1 = os.listdir("Imagens")
os.mkdir("Imagens/Cropped")


# In[1]:
def trim(im,nome):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    box = diff.getbbox()
    if box:
        imagem = im.crop(box)
        imagem.save("Imagens/Cropped/%s"%nome, quality = 1)


# In[69]:

for imagem in lista1:
    im = Image.open("Imagens/%s"%imagem)
    im = trim(im,imagem)
