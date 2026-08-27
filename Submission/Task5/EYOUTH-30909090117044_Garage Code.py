# Future Mall Smart Garage for Wokwi
# Project ID: EYOUTH-30909090117044
# Copy of the portfolio garage program for Wokwi's main.py file.

from machine import Pin
from time import sleep

entry_button = Pin(12, Pin.IN, Pin.PULL_UP)
exit_button = Pin(13, Pin.IN, Pin.PULL_UP)

green_led = Pin(25, Pin.OUT)
red_led = Pin(26, Pin.OUT)
yellow_led = Pin(27, Pin.OUT)
blue_led = Pin(14, Pin.OUT)

car_count = 0
MAX_CARS = 15


def show_garage_status():
    if car_count < MAX_CARS:
        green_led.on()
        red_led.off()
    else:
        green_led.off()
        red_led.on()


def blink(led):
    for number in range(3):
        led.on()
        sleep(0.3)
        led.off()
        sleep(0.3)


show_garage_status()

while True:
    if entry_button.value() == 0:
        if car_count < MAX_CARS:
            car_count = car_count + 1
            print("Car entered. Cars in garage:", car_count)
            blink(yellow_led)
        else:
            print("Garage is full")
        show_garage_status()
        while entry_button.value() == 0:
            sleep(0.1)

    if exit_button.value() == 0:
        if car_count > 0:
            car_count = car_count - 1
            print("Car exited. Cars in garage:", car_count)
            blink(blue_led)
        else:
            print("Garage is empty")
        show_garage_status()
        while exit_button.value() == 0:
            sleep(0.1)

    sleep(0.1)
