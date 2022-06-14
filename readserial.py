#!/usr/bin/env python3
import serial
import requests
def upload_data(distance):
    data = {
        'device': 'Gahamanyi-Pauline-Elissa',
        'distance': distance
    }
    try:
        res = requests.post('http://insecure.benax.rw/iot/', json=data)
        res.raise_for_status()
        print('Success!')
        if res is not None:
            print(res.json())
    except requests.exceptions.HTTPError as err:
        print(f"Error {res.status_code}: {res.json()}, for {res.request}: {res.url}")
    except Exception as err:
        print(f"Error {err}")


ser = serial.Serial(
 port='/dev/ttyUSB0',
 baudrate=9600,
 parity=serial.PARITY_NONE,
 stopbits=serial.STOPBITS_ONE,
 bytesize=serial.EIGHTBITS,
 timeout=1
)
ser.flush()
if __name__ == '__main__':
 while True:
     if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').rstrip()
        upload_data(line)
        f=open("data.txt","a")
        f.write(line)
        f.write("\n")
        f.close()
        print(line)