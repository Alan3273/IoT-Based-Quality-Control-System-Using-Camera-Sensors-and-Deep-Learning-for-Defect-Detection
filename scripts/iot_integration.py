# iot_integration.py
# IoT Integration Simulation Script for Defect Detection
# (Demo - not actual cloud send)

import time
import random

def get_defect_status():
    return random.choice(["No Defect", "Minor Defect", "Major Defect"])

while True:
    status = get_defect_status()
    print(f"📡 Sending defect status: {status}")
    # Here you could send to ThingSpeak / MQTT in real setup
    time.sleep(3)

