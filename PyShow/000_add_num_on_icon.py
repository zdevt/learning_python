from PIL import Image, ImageFont, ImageDraw


def add_num( img ):
    im = Image.open( img )
    w, h = im.size
    font = ImageFont.truetype( "/Library/Fonts/Times New Roman Italic.ttf" )
    fillcolor = "#ff0000"
    draw = ImageDraw.Draw( im )
    draw.text( (w - 20, 0), '1', font = font, fill = fillcolor )
    im.save( "a.jpg", 'jpeg' )


if __name__ == '__main__':
    add_num("000_sven.jpg" )
