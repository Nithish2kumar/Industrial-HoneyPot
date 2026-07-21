import random
import time
import threading

TEMP_REG = 0
PRESSURE_REG = 1
LEVEL_REG = 2
PUMP_REG = 3

reg = [85, 550, 45, 1]

def updateRegister():
    while True:

        if reg[PUMP_REG]:
            reg[TEMP_REG] += random.randint(0, 1)
        else:
            reg[TEMP_REG] -= random.randint(0, 1)
        reg[TEMP_REG] = max(70, min(120, reg[TEMP_REG]))

        if reg[PUMP_REG]:
            reg[PRESSURE_REG] += random.randint(0, 2)
        else:
            reg[PRESSURE_REG] -= random.randint(0, 2)
        reg[PRESSURE_REG] = max(450, min(900, reg[PRESSURE_REG]))

        if reg[PUMP_REG]:
            reg[LEVEL_REG] += random.randint(0, 2)
        else:
            reg[LEVEL_REG] -= random.randint(0, 2)
        reg[LEVEL_REG] = max(0, min(100, reg[LEVEL_REG]))

        if random.random() < 0.1:
            reg[PUMP_REG] ^= 1

        print(
            f"Temp: {reg[TEMP_REG]}°C | "
            f"Pressure: {reg[PRESSURE_REG]} PSI | "
            f"Level: {reg[LEVEL_REG]}% | "
            f"Pump: {'ON' if reg[PUMP_REG] else 'OFF'}"
        )

        time.sleep(1)


def startSimulator():
    thread = threading.Thread(target=updateRegister, daemon=True)
    thread.start()