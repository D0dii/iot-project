import time
import RPi.GPIO as GPIO
import board
import neopixel
from mfrc522 import MFRC522
from config import *
from datetime import datetime

# import sys
# sys.path.append("/home/pi/.local/lib/python3.9/site-packages")
# import paho.mqtt.client as mqtt 


# terminal_id = "T0"
# broker = "localhost" 

# WS2812 LED
LED_COUNT = 8 
LED_PIN = board.D18 
pixels = neopixel.NeoPixel(LED_PIN, LED_COUNT, brightness=0.5, auto_write=False)

# Czytnik RFID
reader = MFRC522()

# client = mqtt.Client()

# --- Zmienne globalne ---
last_card_id = None 
last_detection_time = 0 
DETECTION_INTERVAL = 2
card_present = False 

def log_card(card_uid):
    curr_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f"Karta UID: {card_uid} przyłożona o {curr_time}")
    

def buzz(duration=0.2):
    GPIO.output(buzzerPin, False)
    time.sleep(duration)
    GPIO.output(buzzerPin, True)

def indicate_success():
    for i in range(LED_COUNT):
        pixels[i] = (0, 255, 0) 
        pixels.show()
    time.sleep(1)
    pixels.fill((0, 0, 0)) 
    pixels.show()

# def call_worker(worker_id, dt):
#     client.publish("worker/card", str(worker_id) + "-" + str(dt))

# def connect_to_broker():
#     client.connect(broker)
#     call_worker("Client connected", datetime.now())

# def disconnect_from_broker():
#     call_worker("Client disconnected", datetime.now())
#     client.disconnect()

# --- Główna pętla ---
def main():
    id_to_return = 0
    try:
        # connect_to_broker()
        print("Program rozpoczęty. Przyłóż kartę.")
        running = True
        while running:
            status, _ = reader.MFRC522_Request(reader.PICC_REQIDL)
            #card_id, _ = reader.read() 
            
            if status == reader.MI_OK:
                status, uid = reader.MFRC522_Anticoll()
                if status == reader.MI_OK:
                    current_time = time.time()
                    num = 0
                    for i in range(0, len(uid)):
                        num += uid[i] << (i*8)
                    log_card(num)
                        # call_worker(num, datetime.now())
                    buzz()
                    indicate_success()
                    id_to_return = num
                    running = False
                    

            time.sleep(0.1) 
    except KeyboardInterrupt:
        print("Program zatrzymany przez użytkownika.")
    finally:
        # GPIO.cleanup()
        pixels.fill((0, 0, 0))
        pixels.show()
        return id_to_return
        # disconnect_from_broker()

if __name__ == "__main__":
    main()