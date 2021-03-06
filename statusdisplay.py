import configparser
import time

from datetime import datetime

import feedparser

from PIL import Image, ImageDraw, ImageFont

from driver import epd7in5

# Data sources
from datasources.wordclock import time_str
from datasources.ovinfo import get_departures
from datasources.weather import (get_weather, BUIENRADAR_ICONS, WIND_SCALE, WIND_DIRECTION, WeatherData)

config = configparser.ConfigParser()
config.read('statusdisplay.cfg')


font_small = ImageFont.truetype('Roboto-Bold.ttf', 16)
font = ImageFont.truetype('Roboto-Bold.ttf', 20)
font_big = ImageFont.truetype('Roboto-Bold.ttf', 36)
weather_font = ImageFont.truetype("./weathericons-regular-webfont.ttf", 24)
weather_font_big = ImageFont.truetype("./weathericons-regular-webfont.ttf", 36)

epd = epd7in5.EPD()
epd.init()

Himage = Image.new('1', (epd7in5.EPD_WIDTH, epd7in5.EPD_HEIGHT), 255)  # 255: clear the frame
draw = ImageDraw.Draw(Himage)

days = get_weather(config.get('weather', 'code'))

i = 0
today = days[0]

weather = WeatherData(config.get('weather', 'code'))

# Wind, sunset/sunrise.
sunicon, suntime = weather.sundata()
draw.text((0, i), weather.winddirection(), font=weather_font, fill=0)
draw.text((25, i), weather.windspeed(), font=weather_font, fill=0)
draw.text((60, i), sunicon, font=weather_font, fill=0)
draw.text((95, i+4), suntime.strftime('%H:%M'), font=font, fill=0)

now = datetime.now()
timestr = time_str(now.hour, now.minute)
# Calculate text width and add margin
time_length = draw.textsize(timestr, font_big)[0] + 5
draw.text((epd7in5.EPD_WIDTH-time_length, i), timestr, font=font_big, fill=0)

i += 35
old_i = i + 18

# Current temp
iconcode, current_temp = weather.currenttemp()
draw.text((0, i), iconcode, font=weather_font_big, fill=0)
draw.text((60, i), current_temp, font=font_big, fill=0)
draw.text((110, i), "\uf03c", font=weather_font_big, fill=0)

# Min/max
mintemp, maxtemp = weather.minmax_today()
draw.text((140, i+5), maxtemp, font=font_small, fill=0)
draw.text((140, i+draw.textsize(maxtemp, font_small)[0]+5), mintemp  ,font=font_small, fill=0)

i += 45

draw.line((0, i, 140, i), fill=0)

draw.text((300, old_i), "OV vertrektijden", font=font)
old_i += 25
draw.line((300, old_i, 455, old_i), fill=0)

# OV info
for d in get_departures(config.get('ov', 'id')):
    draw.text((300, old_i), d, font=font)
    old_i += 20

i += 6

for day in weather.forecast():
    draw.text((0, i), day['txt'], font=font)
    draw.text((50, i), day['icon'], font=weather_font, fill=0)
    draw.text((90, i), day['temp'], font=font)
    i += 25


i += 60
draw.text((0, i), "Nieuws", font=font)
i += 25
draw.line((0, i, 70, i), fill=0)
i += 2
news_data = feedparser.parse(config.get('news', 'url'))
for index, entry in enumerate(news_data['items']):
    if index == 5:
        break

    draw.text((0, i), "- " + entry['title'], font=font_small, fill=0)
    i += 20


# Get buffer, clear and render display
buf = epd.getbuffer(Himage)
epd.clear()
epd.display(buf)
time.sleep(2)
epd.sleep()
