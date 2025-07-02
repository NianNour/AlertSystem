🌡️ Raspberry Pi Temperature Monitoring & SMS Alert System

This is a real-time temperature monitoring system built using a DS18B20 temperature sensor and a SIM800C GSM module, powered by a Raspberry Pi. The system continuously reads the ambient temperature and sends SMS alerts when the temperature goes outside a safe range, or sends periodic status updates when it’s normal.

🚀 Features

📡 Sends SMS alerts via AT commands over UART to the SIM800C GSM module

🌡️ Monitors ambient temperature using a DS18B20 digital sensor

📈 Sends status updates every 15 minutes when temperature is in normal range

⚠️ Sends immediate alerts for high (> 30°C) or low (< 10°C) temperature

✅ Notifies when temperature returns to normal after a warning

🧰 Hardware Requirements

Raspberry Pi 4 (or compatible model with UART and GPIO)

DS18B20 Digital Temperature Sensor

SIM800C GSM Module (or compatible GSM module)

Breadboard and jumper wires

SIM card with active SMS service

4.7V–5V power supply for SIM800C

4.7kΩ pull-up resistor between DS18B20 data and VCC

🖥️ Software Requirements

Raspberry Pi OS (Lite or Desktop)

Python 3

Enable required interfaces:

sudo raspi-config

Interfacing Options → 1-Wire → Enable

Interface Options → Serial →

Login shell: NO

Serial interface: YES

🔌 Wiring and Connections

DS18B20 Temperature Sensor:

Connect the Data pin of the DS18B20 to GPIO4 on the Raspberry Pi (Physical Pin 7).

Connect the VCC pin to 3.3V on the Raspberry Pi (Physical Pin 1).

Connect the GND pin to any Ground (GND) pin on the Raspberry Pi (Physical Pin 6).

Place a 4.7kΩ pull-up resistor between the DS18B20 Data pin and the 3.3V line.

SIM800C GSM Module:

Connect the TX pin of SIM800C to the Raspberry Pi’s RX pin (GPIO15, Physical Pin 10).

Connect the RX pin of SIM800C to the Raspberry Pi’s TX pin (GPIO14, Physical Pin 8).

Connect GND of SIM800C to GND on the Raspberry Pi.

Power the SIM800C module using a separate 4.7V–5V power supply (DO NOT power SIM800C directly from Raspberry Pi 5V pin to avoid damage).

🧠 What You’ll Learn

Interfacing digital sensors (1-Wire protocol) with Raspberry Pi

Communicating with GSM modules via UART and AT commands

Reading and parsing raw temperature data in Python

Automating condition-based alerts using time and logic

Building lightweight, headless monitoring systems with Raspberry Pi
