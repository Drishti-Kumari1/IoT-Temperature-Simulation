import random
import time

print("IoT Temperature Sensor Simulation")
for i in range(5):
    temp = round(random.uniform(25.0, 35.0), 2)
    print(f"Temperature reading {i+1}: {temp} °C")
    time.sleep(1)
