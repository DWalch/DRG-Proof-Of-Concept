import time
import serial
import RPi.GPIO as GPIO
import Emailer as emailer
import csv

#create the serial object on the pi
ser = serial.Serial(
    port = '/dev/serial0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout = 1
    )

#Create the variables used to assign email destination, subject and the content
sendTo = "walchD@protonmail.com"
emailSubject = "Temperature Data"
emailContent = "This is a test of sending an attached csv file to an email"
#Naive way to track number of loops and data inputs
#Loop currently works by reading from serial every 10 seconds, writing that to a file
#After 5 minutes it emails the file and deletes it
count = 0

#Function, takes 3 parameters, time, objectTemp, and airTemp.
#Creates the file tempData if it does not exist, if it does opens it in append mode and writes a row of the passed data
def writeFile(time, objectTemp, airTemp):
    with open('tempData.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([time, airTemp, objectTemp])

#Primary loop
#Checks if anything is waiting in the serial input
#Decodes and strips the data recieved
#Captures local time and converts it to month/day/hour/minute/seconds
#Writes the data to the file and then sleeps for 10 seconds
#Finally after approximately 5 minutes have passed calls our emailer object and sends the email to our destination
while 1:
    if ser.in_waiting > 0:
        tempLine = ser.readline().decode('utf-8').strip().split(',')
        t = time.localtime()
        currentTime = time.strftime("%b-%d-%y %H:%M:%S", t)
        print(tempLine)
        writeFile(currentTime, tempLine[1], tempLine[0])
    time.sleep(10)
    count += 1
    if count % 30 == 0:
        emailer.sendmail(sendTo, emailSubject, emailContent)
