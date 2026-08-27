# Future Mall Smart Garage for ESP32 MicroPython
# Project ID: EYOUTH-30909090117044
# Entry and exit buttons use INPUT_PULLUP, so a pressed button reads 0.

from machine import Pin
from time import sleep

entry_button = Pin(12, Pin.IN, Pin.PULL_UP)
exit_button = Pin(13, Pin.IN, Pin.PULL_UP)

green_led = Pin(25, Pin.OUT)   # Spaces available
red_led = Pin(26, Pin.OUT)     # Garage full
yellow_led = Pin(27, Pin.OUT)  # Car entered
blue_led = Pin(14, Pin.OUT)    # Car exited

car_count = 0
MAX_CARS = 15


def show_garage_status():
    """Show whether the garage has a free space."""
    if car_count < MAX_CARS:
        green_led.on()
        red_led.off()
    else:
        green_led.off()
        red_led.on()


def blink(led):
    """Blink one LED once to show a car movement."""
    led.on()
    sleep(0.3)
    led.off()


show_garage_status()

while True:
    if entry_button.value() == 0:
        # Do not let the count become more than 15.
        if car_count < MAX_CARS:
            car_count = car_count + 1
            print("Car entered. Cars in garage:", car_count)
            blink(yellow_led)
        else:
            print("Garage is full")

        show_garage_status()
        # Wait for the button to be released, so one press adds one car.
        while entry_button.value() == 0:
            sleep(0.1)

    if exit_button.value() == 0:
        # Do not let the count become less than 0.
        if car_count > 0:
            car_count = car_count - 1
            print("Car exited. Cars in garage:", car_count)
            blink(blue_led)
        else:
            print("Garage is empty")

        show_garage_status()
        # Wait for the button to be released, so one press removes one car.
        while exit_button.value() == 0:
            sleep(0.1)

    sleep(0.1)
