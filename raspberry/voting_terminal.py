import lib.oled.SSD1331 as SSD1331
from PIL import Image, ImageDraw, ImageFont
import RPi.GPIO as GPIO
from time import sleep

# Konfiguracja pinów
PIN_GREEN = 6 # Pin dla zielonego przycisku (zmiana opcji)
PIN_RED = 5 # Pin dla czerwonego przycisku (zatwierdzenie)

# Konfiguracja GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_GREEN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_RED, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Inicjalizacja wyświetlacza OLED
display = SSD1331.SSD1331()
display.Init()

image2 = Image.new("RGB", (display.width, display.height), "BLACK")
draw2 = ImageDraw.Draw(image2)
fontLarge = ImageFont.truetype('./lib/oled/Font.ttf', 10)
fontSmall = ImageFont.truetype('./lib/oled/Font.ttf', 8)

def show_start_screen():
    image = Image.new("RGB", (display.width, display.height), "BLACK")
    draw = ImageDraw.Draw(image)

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
def main(vote_number):
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
    sleep(2)
    display.clear()
    display.reset()

# Uruchomienie programu
if __name__ == "__main__":
    main(vote_number=1) # Przykładowe uruchomienie dla głosowania nr 1

    # Czyszczenie GPIO
    GPIO.cleanup()
