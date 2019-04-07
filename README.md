# 7.5" E-ink home status display

Work in progress e-ink home status display, showing news, weather information
and hopefully soon much more. Currently heavy work in progress and unstable,
but also awfully slow on an rpi zero W for still unknown reasons so it
takes ~ 1 minute to update the screen. 26 seconds for clearing the screen and
further drawing and setup 30 seconds.

# Running

This depends on a newer spi-dev then is available in Debian, to compile and run follow the following steps:

* apt install python3-dev
* git clone https://github.com/doceme/py-spidev.git
* cd py-spidev
* make PYTHON=python3
* PYTHONPATH=/home/pi/py-spidev/lib/ python3 bench.py

# Case

![e-ink ribba ikea](https://pbs.twimg.com/media/D3gJUvkXkAUaTWx.jpg)
