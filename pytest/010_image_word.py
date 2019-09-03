# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rdChar():
    return chr(random.randint(65, 90))


def rdColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rdColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('/Library/Fonts/AppleGothic.ttf', 36)
draw = ImageDraw.Draw(image)

for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rdColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rdChar(), font=font, fill=rdColor2())

image = image.filter(ImageFilter.BLUR)
image.save('010.jpg', 'jpeg')

print(rdChar())
print(rdColor())
