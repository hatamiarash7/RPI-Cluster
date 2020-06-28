FROM python:3.7.3-slim

RUN apt-get update && apt install python3-dev python3-pip libfreetype6-dev libjpeg-dev build-essential -y

RUN apt install libsdl-dev libportmidi-dev libsdl-ttf2.0-dev libsdl-mixer1.2-dev libsdl-image1.2-dev -y

ADD test.py /
ADD demo_opts.py /

RUN pip3 install luma.core>=1.8.0 luma.emulator>=1.0.2 luma.oled>=3.4.0 luma.lcd>=1.0.3 luma.led_matrix>=1.0.7 argcomplete

CMD python ./test.py -d sh1106 -i spi --width 128 --height 64
