import time
import pytest
from serial import Serial

@pytest.fixture
def arduino_serial():
    # Inicjalizacja połączenia szeregowego z Arduino
    serial = Serial(port='COM3', baudrate=9600, timeout=2)
    yield serial
    serial.close()

def test_arduino(arduino_serial):
    # Wysłanie komunikatu "Zaswieca sie zielona" do Arduino
    arduino_serial.write(b"zaswieca sie zielona\n")

    # Oczekiwanie na odpowiedź od Arduino przez 2 sekundy
    start_time = time.time()
    response = ""
    while time.time() - start_time < 2:
        if arduino_serial.in_waiting > 0:
            response += arduino_serial.readline().decode().strip()

    # Sprawdzenie wyniku testu
    assert "gasnie zielona" not in response, "Blad - otrzymano informacje o gasnieciu zielonej"
