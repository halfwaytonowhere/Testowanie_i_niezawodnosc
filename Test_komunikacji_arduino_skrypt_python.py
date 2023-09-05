import serial
import threading

port = 'COM3'  # Zmień na właściwą nazwę portu
baudrate = 9600

ser = serial.Serial(port, baudrate)

def read_data():
    while True:
        # Odczytaj dane z portu szeregowego
        if ser.in_waiting > 0:
            data = ser.readline().decode().strip()
            print('Odczytano dane:', data)

def send_command():
    while True:
        command = input("")  # Pusta wiadomość

        if command == 'q':
            break  # Zakończ pętlę, jeśli użytkownik wprowadził 'q'

        # Wysyłaj dane do Arduino tylko gdy użytkownik wprowadzi L lub R
        if command in ['L', 'R']:
            ser.write(command.encode())

# Uruchom wątek odczytu danych
read_thread = threading.Thread(target=read_data)
read_thread.start()

# Uruchom wątek wysyłania komend
send_thread = threading.Thread(target=send_command)
send_thread.start()

# Oczekuj na zakończenie programu
send_thread.join()

# Zakończ wątek odczytu danych
ser.close()