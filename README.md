# 🌡️ Raspberry Pi Temperature Monitoring and SMS Alert System

This project is a real-time temperature monitoring system using a **DS18B20** temperature sensor and **SIM800C GSM module**, powered by a **Raspberry Pi**. It reads the ambient temperature every 15 minutes and sends an SMS alert via GSM if the temperature goes out of a safe range—or simply reports that it’s normal.

## 🚀 Features

- 📡 Sends SMS alerts using AT commands over UART via SIM800C
- 🌡️ Monitors ambient temperature using a DS18B20 sensor
- 📈 Sends updates every 15 minutes
- ⚠️ Alerts for high (>30°C) or low (<10°C) temperature conditions
- ✅ Reports when temperature is within the normal range (Optional)

---

## 🧰 Hardware Requirements

- Raspberry Pi 4 (or compatible)
- DS18B20 Digital Temperature Sensor
- SIM800C GSM module (or compatible)
- Breadboard and jumper wires
- SIM card with SMS service
- 4.7V–5V power supply for SIM800C
- 4.7kΩ pull-up resistor for DS18B20 (between data and VCC)

---
## 🖥️ Software Requirements

- Raspberry Pi OS (Lite or Desktop)
- Python 3
- Enable 1-Wire interface:
  ```bash
  sudo raspi-config
  # Interfacing Options → 1-Wire → Enable
  sudo raspi-config
# Interface Options → Serial → Login shell NO, Serial interface YES

🧠 What You Learn

Interfacing with sensors (1-Wire)

Serial communication with GSM modules

AT command protocol

Reading and parsing raw sensor data in Python

Automating time-based tasks with embedded Linux systems

🛠️ Future Improvements

Add email or Telegram alerts

Web dashboard with live temperature graph

Data logging to file or database

Battery backup and low-voltage detection
