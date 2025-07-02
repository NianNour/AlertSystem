# 🌡️ Raspberry Pi Temperature Monitoring & SMS Alert System

This is a real-time temperature monitoring system built using a **DS18B20 temperature sensor** and a **SIM800C GSM module**, powered by a Raspberry Pi. The system continuously reads the ambient temperature and sends SMS alerts when the temperature goes outside a safe range, or sends periodic status updates when it’s normal.

---

## 🚀 Features

- 📡 Sends SMS alerts via AT commands over UART to the SIM800C GSM module  
- 🌡️ Monitors ambient temperature using a DS18B20 digital sensor  
- 📈 Sends status updates every 15 minutes (and in the begining) when temperature is in normal range  
- ⚠️ Sends immediate alerts for high (> 30°C) or low (< 10°C) temperature  
- ✅ Notifies when temperature returns to normal after a warning  

---

## 🧰 Hardware Requirements

- Raspberry Pi 4 (or compatible model with UART and GPIO)  
- DS18B20 Digital Temperature Sensor  
- SIM800C GSM Module (or compatible GSM module)  
- Breadboard and jumper wires  
- SIM card with active SMS service  
- 4.7V–5V power supply for SIM800C  
- 4.7kΩ pull-up resistor between DS18B20 data and VCC  

---

## 🖥️ Software Requirements

- Raspberry Pi OS (Lite or Desktop)  
- Python 3  

Enable required interfaces using:

```bash
sudo raspi-config
```

Then:

1. Interfacing Options → 1-Wire → Enable  
2. Interface Options → Serial →  
   - Login shell: **NO**  
   - Serial interface: **YES**  

---

## 🔌 Wiring and Connections

### DS18B20 Temperature Sensor

- Connect **Data** pin to **GPIO4** (Physical Pin 7)  
- Connect **VCC** to **3.3V** (Physical Pin 1)  
- Connect **GND** to **Ground** (Physical Pin 6)  
- Place a **4.7kΩ pull-up resistor** between Data pin and 3.3V  

### SIM800C GSM Module

- Connect **TX** pin to Raspberry Pi **RX** (GPIO15, Pin 10)  
- Connect **RX** pin to Raspberry Pi **TX** (GPIO14, Pin 8)  
- Connect **GND** to Raspberry Pi **GND**  
- Power SIM800C with a **separate 4.7V–5V supply** (do **NOT** use Pi 5V pin)  

---

## 🧠 What You’ll Learn

- Interfacing digital sensors (1-Wire protocol) with Raspberry Pi  
- Communicating with GSM modules via UART and AT commands  
- Reading and parsing raw temperature data in Python  
- Automating condition-based alerts using time and logic  
- Building lightweight, headless monitoring systems with Raspberry Pi  
