import os
import glob
import time
import serial

# Thresholds
TEMP_HIGH = 30  # High temperature threshold (°C)
TEMP_LOW = 10   # Low temperature threshold (°C)

# Phone numbers
RPI_NUMBER = "+989112548017"          # Raspberry Pi SIM number (not used directly)
TARGET_PHONE_NUMBER = "+989376818413"  # Recipient phone number

# Setup serial for SIM800C
sim = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# Function to send AT commands
def send_at(cmd, delay=1):
    sim.write((cmd + '\r\n').encode())
    time.sleep(delay)
    return sim.read(sim.in_waiting).decode()

# Function to send SMS
def send_sms(message, phone_number=TARGET_PHONE_NUMBER):
    print("Sending SMS...")
    send_at("AT")
    send_at("AT+CMGF=1")  # Set SMS mode to text
    send_at(f'AT+CMGS="{phone_number}"')
    sim.write((message + "\x1A").encode())  # Ctrl+Z to send SMS
    time.sleep(3)
    print("SMS sent.")

# Function to read temperature from DS18B20
def read_temp():
    base_dir = '/sys/bus/w1/devices/'
    device_folder = glob.glob(base_dir + '28*')[0]
    device_file = device_folder + '/w1_slave'

    with open(device_file, 'r') as f:
        lines = f.readlines()

    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        with open(device_file, 'r') as f:
            lines = f.readlines()

    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

# Main loop
try:
    while True:
        temp = read_temp()
        print(f"Current Temp: {temp:.2f}°C")

        if temp > TEMP_HIGH:
            send_sms(f"Alert! Temperature too high: {temp:.1f}°C")
        elif temp < TEMP_LOW:
            send_sms(f"Alert! Temperature too low: {temp:.1f}°C")
        else:
            send_sms(f"Temperature is normal: {temp:.1f}°C")

        time.sleep(900)  # Wait 15 minutes (900 seconds)

except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting cleanly.")
    sim.close()
