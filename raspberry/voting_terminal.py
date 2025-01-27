from email import message
import lib.oled.SSD1331 as SSD1331
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
from time import sleep
import rfid_handler 
import sys
sys.path.append("/home/pi/.local/lib/python3.9/site-packages")
import paho.mqtt.client as mqtt 

# def setup():
# Konfiguracja pinów
PIN_GREEN = 6 # Pin dla zielonego przycisku (zmiana opcji)
PIN_RED = 5 # Pin dla czerwonego przycisku (zatwierdzenie)

vote_number = 0

MQTT_BROKER = "10.108.33.125"
MQTT_PORT = 1883
MQTT_TOPIC = "vote"

client = mqtt.Client()

# Konfiguracja GPIO
GPIO.setmode(GPIO.BCM)
print("konfiguruje...")
GPIO.setup(PIN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Inicjalizacja wyświetlacza OLED
display = SSD1331.SSD1331()
display.Init()

image2 = Image.new("RGB", (display.width, display.height), "BLACK")
draw2 = ImageDraw.Draw(image2)
fontLarge = ImageFont.truetype('./lib/oled/Font.ttf', 10)
fontSmall = ImageFont.truetype('./lib/oled/Font.ttf', 8)

def on_message(client, userdata, msg):
    global vote_number
    message = msg.payload.decode()
    vote_number = int(message)
    print(f"Received message: {message}")

def connect_to_broker():
    client.connect(MQTT_BROKER)
    client.subscribe("backend")

def disconnect_from_broker():
    client.disconnect()

def call_voter(uid, vote):
    client.publish(MQTT_TOPIC, str(uid) + "-" + str(vote))

def show_start_screen():
    display.clear()
    image = Image.new("RGB", (display.width, display.height), "BLACK")
    draw = ImageDraw.Draw(image)
    draw.text((0, 30), "Prosze przyłóż kartę rfid", font=fontLarge, fill="WHITE")
    display.ShowImage(image, 0, 0)

# Funkcje pomocnicze
def show_voting_screen(vote_number, current_option):
    image1 = Image.new("RGB", (display.width, display.height), "BLACK")
    draw = ImageDraw.Draw(image1)
    #display.clear()
    draw.text((0, 0), f"Głosowanie nr {vote_number}", font=fontLarge, fill="WHITE")
    draw.text((0, 15), current_option, font=fontLarge, fill="WHITE")
    draw.rectangle([(20, 30), (30, 40)], fill="GREEN")
    draw.text((10, 50), "Zmień", font=fontSmall, fill="WHITE")
    draw.rectangle([(60, 30), (70, 40)] , fill="RED")
    draw.text((60, 50), "Zatwierdź", font=fontSmall, fill="WHITE")
    display.ShowImage(image1, 0, 0)

def show_confirmation_screen(selected_option):
    display.clear()
    draw2.text((0, 0), f"Oddany głos:", font=fontLarge, fill="WHITE")
    draw2.text((0, 20), f"{selected_option}", font=fontLarge, fill="WHITE")
    draw2.text((0, 40), "Oczekiwanie...", font=fontLarge, fill="WHITE")
    display.ShowImage(image2, 0, 0)



# Główna funkcja
def main():
    global vote_number
    show_start_screen()
    uid = rfid_handler.main()
    print(uid)
    if uid:

        options = ["Za", "Przeciw", "Wstrzymuję się"]
        current_index = 0

        show_voting_screen(vote_number, options[current_index])

        while True:
            if GPIO.input(PIN_GREEN) == GPIO.LOW:
                current_index = (current_index + 1) % len(options)
                show_voting_screen(vote_number, options[current_index])
                sleep(0.2) # Debouncing

            if GPIO.input(PIN_RED) == GPIO.LOW:
                selected_option = options[current_index]
                show_confirmation_screen(selected_option)
                break

            sleep(0.1)

        # Czekanie na zapisanie głosu
        call_voter(uid, options[current_index])
        while vote_number != -1:
            pass
        print("wszystko git smiga dobrze")
        display.clear()
        display.reset()

# Uruchomienie programu
if __name__ == "__main__":
    connect_to_broker()
    client.on_message = on_message
    client.loop_start()

    while True:
        vote_number = 0
        while vote_number == 0:
            pass
        if vote_number == -2:
            break
        else:
            main()

    disconnect_from_broker()
    # Czyszczenie GPIO
    GPIO.cleanup()