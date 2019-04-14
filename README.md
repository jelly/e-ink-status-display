# 7.5" E-ink home status display

Work in progress e-ink home status display, showing news, weather information
and hopefully soon much more. Updates in ~ 45 seconds with network requests on
a Raspberry Pi Zero W.

# Dependencies

* python3
* python3-pillow
* python3-rpi.gpio

For the display functionality:

* fonts-roboto
* python3-requests
* python3-feedparser

SPI has to be enabled on the Raspberry Pi, follows the
[steps](https://www.raspberrypi.org/documentation/hardware/raspberrypi/spi/README.md)
on the raspberrypi.org website.

Vendored font in the repo is [weather-icons](https://erikflowers.github.io/weather-icons/).

# Running

This depends on a newer spi-dev then is available in Debian, to compile and run follow the following steps:

```
apt install python3-dev
git clone https://github.com/doceme/py-spidev.git
cd py-spidev
make PYTHON=python3
PYTHONPATH=/home/pi/py-spidev/lib/ python3 bench.py
```

# Case

![e-ink ribba ikea](https://pbs.twimg.com/media/D3gJUvkXkAUaTWx.jpg)
