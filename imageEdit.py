from PIL import Image, ImageDraw, ImageFont
import sys

from zmq import device


[ _, device_name, device_codename, maintainer_name, device_type ] = sys.argv

im=Image.open("templates/" + device_type+".png")

font_style = "nevis.ttf"
draw=ImageDraw.Draw(im)
image_width, image_heigth=im.size
font=ImageFont.truetype(font=font_style,size=95)

char_width,char_heigth=font.getsize('A')
colour_white = "white"

# print(char_heigth, char_width)
# print(charPerLine)

line=device_name
y=1320
lineWidth, lineheigth = font.getsize(line)
x=600
draw.text((x,y),line,fill=colour_white,font=font,stroke_width=1)

y=1475
x=775

line=maintainer_name
draw.text((x,y),line,fill=colour_white,font=font,stroke_width=1)

# y+=50
# line="(" + device_codename + ")"
# draw.text((x,y),line,fill='#4E7AAF',font=font,stroke_width=1)

# y+=lineheigth+8
# line="Maintained by"
# draw.text((x,y),line,fill=colour_white,font=font,stroke_width=1)

# y+=50
# line=maintainer_name
# draw.text((x,y),line,fill='#4E7AAF',font=font,stroke_width=1)

im.save(device_codename+".png")
