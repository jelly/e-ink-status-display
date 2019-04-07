from PIL import Image, ImageDraw, ImageFont, ImageFilter

import time
import epd7in5

font = ImageFont.truetype('Roboto-Bold.ttf', 20)
Himage = Image.new('1', (epd7in5.EPD_WIDTH, epd7in5.EPD_HEIGHT), 255)  # 255: clear the frame    
draw = ImageDraw.Draw(Himage)
draw.text((20, 20), "testing", font=font, fill=0)

epd = epd7in5.EPD()
buf = epd.getbuffer(Himage)

print(time.ctime())
epd.init()
print("Clear...")
epd.Clear()

epd.display(buf)
epd.sleep()
print(time.ctime())
