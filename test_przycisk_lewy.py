import pytest
import serial
import threading
import time

@pytest.fixture(scope="module")
def ser():
    # Inicjalizacja połączenia szeregowego z Arduino
    ser = serial.Serial('COM3', 9600)
    time.sleep(2)  # Oczekiwanie na stabilizację połączenia
    yield ser
    ser.close()  # Zamknięcie połączenia po zakończeniu testów

def read_data(ser):
    while True:
        # Odczytaj dane z portu szeregowego
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print(data)
            if data == 'gasnie zielona':
                send_command(ser) 
            
            return data

def send_command(ser):
    command = "L"  
    ser.write(command.encode())

def test_game_results(ser):

    expected_data = "wygral gracz 1"
    received_data=''
    for _ in range(4):
        data = read_data(ser)
        received_data = received_data + data


    assert expected_data in received_data, "Blad - nie otrzymano oczekiwanych danych"