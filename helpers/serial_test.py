from time import sleep
import serial


def do_stuff():
    counter = 32 # Below 32 everything in ASCII is gibberish
    ser = serial.Serial('/dev/tty.usbserial-DN03FRQP', 9600) # Establish the connection on a specific port
    while True:
         counter +=1
         ser.write(str(chr(counter)))  # Convert the decimal number to ASCII then send it to the Arduino
         print(ser.readline())  # Read the newest output from the Arduino
         sleep(.1)  # Delay for one tenth of a second
         if counter == 255:
            counter = 32
    return