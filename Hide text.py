from PIL import Image, ImageDraw
from random import randint

def stega_encrypt():
    text = input('text: ')
    keys = []
    img = Image.open(input("img:  "))
    draw = ImageDraw.Draw(img)
    width = img.size[0]
    height = img.size[1]
    pix = img.load()
    f = open('text.txt','w')

    for elem in ([ord(elem) for elem in text]):
        key = (randint(1,width-10),randint(1,height-10))
        r,g,b = pix[key][:3]
        draw.point(key, (r,elem , b))
        f.write(str(key)+'\n')


    img.save("supermemc.png", "PNG")
    f.close()

stega_encrypt()

    
