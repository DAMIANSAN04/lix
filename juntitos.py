import network
import socket
from machine import Pin, PWM
import time

# WiFi credentials
ssid = 'DAMIAN'
password = 'Migo3006'

# Servomotor pins
servo_right = PWM(Pin(8))
servo_left = PWM(Pin(9))

# Gearmotor pins
motor_A_forward = Pin(18, Pin.OUT)
motor_A_backward = Pin(19, Pin.OUT)
motor_B_forward = Pin(20, Pin.OUT)
motor_B_backward = Pin(21, Pin.OUT)

# Servomotor functions
def servo_configuration(servo, duty_cycle):
    servo.freq(50)
    servo.duty_u16(duty_cycle)

def move_servo_right_forward():
    servo_configuration(servo_right, 6000)

def move_servo_right_backward():
    servo_configuration(servo_right, 3000)

def move_servo_left_forward():
    servo_configuration(servo_left, 3000)

def move_servo_left_backward():
    servo_configuration(servo_left, 6000)

# Gearmotor functions
def move_forward():
    motor_A_forward.value(1)
    motor_B_forward.value(1)
    motor_A_backward.value(0)
    motor_B_backward.value(0)

def move_backward():
    motor_A_forward.value(0)
    motor_B_forward.value(0)
    motor_A_backward.value(1)
    motor_B_backward.value(1)

def stop():
    motor_A_forward.value(0)
    motor_B_forward.value(0)
    motor_A_backward.value(0)
    motor_B_backward.value(0)

def turn_left():
    motor_A_forward.value(1)
    motor_B_forward.value(0)
    motor_A_backward.value(0)
    motor_B_backward.value(1)

def turn_right():
    motor_A_forward.value(0)
    motor_B_forward.value(1)
    motor_A_backward.value(1)
    motor_B_backward.value(0)

# Connect to WiFi
def connect():
    net = network.WLAN(network.STA_IF)
    net.active(True)
    net.connect(ssid, password)
    while not net.isconnected():
        print('Connecting to Wi-Fi...')
        time.sleep(1)
    print('Connected to Wi-Fi:', net.ifconfig())

# Open server socket
def open_socket():
    address = ('0.0.0.0', 80)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(address)
    server_socket.listen(5)
    return server_socket

# Serve requests
def serve():
    while True:
        client_socket, client_address = server_socket.accept()
        request = client_socket.recv(1024)
        request = str(request)
        print('Request:', request)
        if '/move_servo_right_forward' in request:
            move_servo_right_forward()
        elif '/move_servo_right_backward' in request:
            move_servo_right_backward()
        elif '/move_servo_left_forward' in request:
            move_servo_left_forward()
        elif '/move_servo_left_backward' in request:
            move_servo_left_backward()
        elif '/move_forward' in request:
            move_forward()
        elif '/move_backward' in request:
            move_backward()
        elif '/turn_left' in request:
            turn_left()
        elif '/turn_right' in request:
            turn_right()
        elif '/stop' in request:
            stop()
        response = 'HTTP/1.1 200 OK\r\nContent-Type: text/html\r\nConnection: close\r\n\r\n' + html
        client_socket.send(response)
        client_socket.close()

# HTML interface
html = """
<!DOCTYPE html>
<html>
<head>
    <title>Robot Control</title>
</head>
<body>
    <h1>Robot Control</h1>
    <h2>Servomotors:</h2>
    <form action="/move_servo_right_forward" method="post">
        <button type="submit">Move Right Forward</button>
    </form>
    <form action="/move_servo_right_backward" method="post">
        <button type="submit">Move Right Backward</button>
    </form>
    <form action="/move_servo_left_forward" method="post">
        <button type="submit">Move Left Forward</button>
    </form>
    <form action="/move_servo_left_backward" method="post">
        <button type="submit">Move Left Backward</button>
    </form>
    <h2>Gearmotors:</h2>
    <form action="/move_forward" method="post">
        <button type="submit">Forward</button>
    </form>
    <form action="/move_backward" method="post">
        <button type="submit">Backward</button>
    </form>
    <form action="/turn_left" method="post">
        <button type="submit">Turn Left</button>
    </form>
    <form action="/turn_right" method="post">
        <button type="submit">Turn Right</button>
    </form>
    <form action="/stop" method="post">
        <button type="submit">Stop</button>
    </form>
</body>
</html>
"""

# Main execution
connect()
server_socket = open_socket()
serve()
