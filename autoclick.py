import pyautogui
import time
import random
import keyboard

min_interval = 0.2
max_interval = 0.4

interval_count = 0
interval_sum = 0 
clicking = False  

def autoclick():
    global clicking
    clicking = not clicking
    if clicking:
        print("Autoclicker turned ON.")
    else:
        print("Autoclicker turned OFF.")

keyboard.add_hotkey('j', autoclick)

try:
    while True:
        if clicking:
            pyautogui.click()

            interval = random.uniform(min_interval, max_interval)
            interval_count += 1
            interval_sum += interval

            print(f"click - {interval:.3f}s")
            time.sleep(interval)
        else:
            time.sleep(0.1)

except KeyboardInterrupt:
    print("Autoclicker stopped.")
    if interval_count > 0:
        print(f"Average interval was {(interval_sum / interval_count):.3f}s!")
    else:
        print("No clicks were made.")
