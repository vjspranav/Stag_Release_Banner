from PIL import Image, ImageDraw, ImageFont

device_name = "OnePlus Nord"
device_codename = "avicii"
maintainer_name = "Manikantaravi"

font_style = "ProductSans-Thin.ttf"
im=Image.open("avicii.jpeg")
draw=ImageDraw.Draw(im)
image_width, image_heigth=im.size
font=ImageFont.truetype(font=font_style,size=85)

char_width,char_heigth=font.getsize('A')

print(char_heigth, char_width)
# print(charPerLine)
line="Stag OS"
y=200
lineWidth, lineheigth = font.getsize(line)
x=60

draw.text((x,y),line,fill='white',font=font,stroke_width=1)
y+=lineheigth+12

colour_white = "#C8C8C8"
font=ImageFont.truetype(font=font_style,size=40)
line="For " + device_name
draw.text((x,y),line,fill=colour_white,font=font,stroke_width=1)

y+=50
line="(" + device_codename + ")"
draw.text((x,y),line,fill='#4E7AAF',font=font,stroke_width=1)

y+=lineheigth+8
line="Maintained by"
draw.text((x,y),line,fill=colour_white,font=font,stroke_width=1)

y+=50
line=maintainer_name
draw.text((x,y),line,fill='#4E7AAF',font=font,stroke_width=1)

im.save('kamesmeme.jpg')
