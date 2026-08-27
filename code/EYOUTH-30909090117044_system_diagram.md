# Future Mall System Diagram

**Project ID:** EYOUTH-30909090117044

```mermaid
flowchart TD
    Customer[Customer] --> Website[Future Mall Website\nHTML + CSS]
    Customer --> Cashier[Cashier Program\nPython]
    EntryButton[Entry button\nGPIO 12] --> ESP32[ESP32 Smart Garage\nMicroPython]
    ExitButton[Exit button\nGPIO 13] --> ESP32
    ESP32 --> Green[Green LED GPIO 25\nSpaces available]
    ESP32 --> Red[Red LED GPIO 26\nGarage full]
    ESP32 --> Yellow[Yellow LED GPIO 27\nCar entered]
    ESP32 --> Blue[Blue LED GPIO 14\nCar exited]
```

The website introduces the mall, the cashier program calculates a shopping total, and the ESP32 program controls the garage indicator lights.
