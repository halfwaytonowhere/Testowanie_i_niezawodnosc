import serial
import time
import pytest

@pytest.fixture(scope="module")
def arduino_serial():
    # Inicjalizacja połączenia szeregowego z Arduino
    ser = serial.Serial('COM3', 9600)
    time.sleep(2)  # Oczekiwanie na stabilizację połączenia
    yield ser
    ser.close()  # Zamknięcie połączenia po zakończeniu testów

def test_arduino(arduino_serial):
    # Wysłanie komunikatu "Zaswieca sie zielona" do Arduino
    arduino_serial.write(b"zaswieca sie zielona\n")

    # Oczekiwanie na odpowiedź od Arduino przez 7 sekund
    start_time = time.time()
    response = ""
    while time.time() - start_time <= 7:
        if arduino_serial.in_waiting > 0:
            response += arduino_serial.readline().decode().strip()
            if "gasnie zielona" in response:
                break

    # Sprawdzenie wyniku testu
    assert "gasnie zielona" in response, "Blad - nie otrzymano oczekiwanych danych"
