import os
import glob
import time
import serial

# Thresholds
TEMP_HIGH = 30
TEMP_LOW = 10

# Phone numbers
TARGET_PHONE_NUMBER = "+98****"

# Setup serial for SIM800C
sim = serial.Serial("/dev/serial0", baudrate=9600, timeout=1)

# AT command function
def send_at(cmd, delay=1):
    sim.write((cmd + '\r\n').encode())
    time.sleep(delay)
    return sim.read(sim.in_waiting).decode()

# Send SMS
def send_sms(message, phone_number=TARGET_PHONE_NUMBER):
    print(f"Sending SMS: {message}")
    send_at("AT")
    send_at("AT+CMGF=1")
    send_at(f'AT+CMGS="{phone_number}"')
    sim.write((message + "\x1A").encode())
    time.sleep(3)
    print("SMS sent.")

# Read temperature
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
    last_status = None
    last_normal_time = 0

    while True:
        temp = read_temp()
        print(f"Current Temp: {temp:.2f}°C")

        current_time = time.time()

        if temp > TEMP_HIGH:
            if last_status != "high":
                send_sms(f"Alert! Temperature too high: {temp:.1f}°C")
                last_status = "high"

        elif temp < TEMP_LOW:
            if last_status != "low":
                send_sms(f"Alert! Temperature too low: {temp:.1f}°C")
                last_status = "low"

        else:
            if last_status == "high":
                send_sms(f"Info: Temperature back to normal from high. Current: {temp:.1f}°C")
            elif last_status == "low":
                send_sms(f"Info: Temperature back to normal from low. Current: {temp:.1f}°C")
            elif (current_time - last_normal_time) >= 900:
                send_sms(f"Temperature is normal: {temp:.1f}°C")

            last_status = "normal"
            last_normal_time = current_time

        time.sleep(5)  # Check temperature every 5 seconds

except KeyboardInterrupt:
    print("Exiting...")
    sim.close()
